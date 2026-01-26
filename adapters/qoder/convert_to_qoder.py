#!/usr/bin/env python3
"""
Convert Agent Skills to Qoder Agent format

This script converts Agent Skills to Qoder agent module format.
Qoder is an agentic coding platform that supports agent-based automation.

Usage:
    python convert_to_qoder.py <skill_path> [output_path]
    
Example:
    python convert_to_qoder.py ../../skills/course-designer qoder-agents/
"""

import sys
import json
import re
import shutil
from pathlib import Path

try:
    import yaml
    HAS_YAML = True
except ImportError:
    HAS_YAML = False


def parse_yaml_simple(text):
    """Simple YAML parser for frontmatter (handles basic key: value pairs)"""
    result = {}
    for line in text.split('\n'):
        line = line.strip()
        if ':' in line and not line.startswith('#'):
            key, value = line.split(':', 1)
            key = key.strip()
            value = value.strip().strip('"').strip("'")
            result[key] = value
    return result


def extract_frontmatter(content):
    """Extract YAML frontmatter from SKILL.md"""
    frontmatter_pattern = r'^---\n(.*?)\n---\n'
    match = re.match(frontmatter_pattern, content, re.DOTALL)
    
    if match:
        frontmatter_text = match.group(1)
        if HAS_YAML:
            frontmatter = yaml.safe_load(frontmatter_text)
        else:
            frontmatter = parse_yaml_simple(frontmatter_text)
        body_start = match.end()
        body = content[body_start:].strip()
        return frontmatter, body
    return {}, content.strip()


def rewrite_markdown_links(content, skill_name, resource_dirs):
    """
    Rewrite markdown links to point to assets directory
    
    Args:
        content: Markdown content
        skill_name: Name of the skill
        resource_dirs: List of resource directories that were copied
    
    Returns:
        Updated content
    """
    def replace_link(match):
        text = match.group(1)
        url = match.group(2)
        
        # Skip absolute links, anchors, or existing asset links
        if url.startswith(('http://', 'https://', '#', '/')):
            return match.group(0)
            
        # Check if link points to a resource directory
        for res_dir in resource_dirs:
            if url.startswith(res_dir + '/') or url == res_dir:
                return f"[{text}](assets/{skill_name}/{url})"
                
        return match.group(0)
    
    # Replace [text](url) links
    content = re.sub(r'\[([^\]]+)\]\(([^\)]+)\)', replace_link, content)
    
    # Replace `path` references (common in our skills)
    def replace_code_path(match):
        path = match.group(1)
        # Check if path points to a resource directory
        for res_dir in resource_dirs:
            if path.startswith(res_dir + '/') or path == res_dir:
                return f"`assets/{skill_name}/{path}`"
        return match.group(0)

    content = re.sub(r'`([^`\n]+)`', replace_code_path, content)
    
    return content


def extract_workflow_steps(body):
    """Extract workflow steps from skill body"""
    steps = []
    # Look for numbered lists or workflow sections
    lines = body.split('\n')
    current_step = None
    
    for line in lines:
        # Match numbered list items
        match = re.match(r'^(\d+)\.\s+(.+)$', line.strip())
        if match:
            step_num = match.group(1)
            step_desc = match.group(2)
            steps.append({
                "step": f"step-{step_num}",
                "description": step_desc
            })
        # Match ## sections as workflow steps
        elif line.startswith('## ') and '流程' in line or 'workflow' in line.lower():
            current_step = line.replace('##', '').strip()
    
    return steps if steps else [
        {"step": "analyze", "description": "Analyze requirements"},
        {"step": "execute", "description": "Execute skill task"},
        {"step": "output", "description": "Generate output"}
    ]


def convert_to_qoder_agent(skill_path, output_dir=None):
    """
    Convert Agent Skill to Qoder agent format
    
    Args:
        skill_path: Path to skill directory containing SKILL.md
        output_dir: Output directory for agent (optional)
    """
    skill_path = Path(skill_path)
    skill_file = skill_path / "SKILL.md"
    
    if not skill_file.exists():
        print(f"Error: SKILL.md not found in {skill_path}")
        return None
    
    # Read skill file
    with open(skill_file, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Extract frontmatter and body
    frontmatter, body = extract_frontmatter(content)
    
    if not frontmatter:
        print(f"Warning: No frontmatter found in {skill_file}")
        frontmatter = {"name": skill_path.name, "description": ""}
    
    # Extract workflow steps
    workflow_steps = extract_workflow_steps(body)
    
    # Extract capabilities from description
    capabilities = []
    description = frontmatter.get("description", "")
    if "课程设计" in description or "course" in description.lower():
        capabilities.append("course-design")
    if "代码" in description or "code" in description.lower():
        capabilities.append("code-generation")
    if "测试" in description or "test" in description.lower():
        capabilities.append("testing")
    if not capabilities:
        capabilities = [frontmatter.get("name", skill_path.name)]
    
    # Create Qoder agent configuration
    agent_config = {
        "name": f"{frontmatter.get('name', skill_path.name)}-agent",
        "description": frontmatter.get("description", ""),
        "version": "1.0.0",
        "type": "skill-agent",
        "capabilities": capabilities,
        "workflow": workflow_steps,
        "instructions": "SKILL.md",
        "metadata": {
            "source": "teachingai-skills",
            "original_skill": frontmatter.get("name", skill_path.name),
            "repo": "https://github.com/teachingai/agent-skills-cli"
        }
    }
    
    # Write output
    if output_dir:
        output_dir = Path(output_dir)
        output_dir.mkdir(parents=True, exist_ok=True)
        
        # Create agent directory
        agent_dir = output_dir / agent_config["name"]
        agent_dir.mkdir(parents=True, exist_ok=True)
        
        # Write agent config
        config_file = agent_dir / "qoder-agent-config.json"
        with open(config_file, "w", encoding="utf-8") as f:
            json.dump(agent_config, f, indent=2, ensure_ascii=False)
        
        # Copy SKILL.md
        shutil.copy2(skill_file, agent_dir / "SKILL.md")
        
        # Copy resources to agent dir
        resource_dirs = ["scripts", "references", "assets", "api", "templates", "examples"]
        for res_dir in resource_dirs:
            src_dir = skill_path / res_dir
            if src_dir.exists() and src_dir.is_dir():
                dest_dir = agent_dir / res_dir
                if dest_dir.exists():
                    shutil.rmtree(dest_dir)
                shutil.copytree(src_dir, dest_dir)
        
        # Create Python agent module
        python_module = agent_dir / f"{frontmatter.get('name', skill_path.name).replace('-', '_')}_agent.py"
        create_python_agent_module(frontmatter, body, python_module)

        # Create Qoder rules directory if requested
        # Qoder supports project-specific rules in .qoder/rules/
        # We force creation of this directory to ensure rules are generated
        rules_dir = output_dir.parent / ".qoder" / "rules"
        rules_dir.mkdir(parents=True, exist_ok=True)
        
        # Copy resources to rules assets dir
        rule_assets_dir = rules_dir / "assets" / frontmatter.get('name', skill_path.name)
        copied_rule_resources = []
        for res_dir in resource_dirs:
            src_dir = skill_path / res_dir
            if src_dir.exists() and src_dir.is_dir():
                dest_dir = rule_assets_dir / res_dir
                if dest_dir.exists():
                    shutil.rmtree(dest_dir)
                shutil.copytree(src_dir, dest_dir)
                copied_rule_resources.append(res_dir)
        
        # Prepare rule content with rewritten links
        rule_body = body
        if copied_rule_resources:
            rule_body = rewrite_markdown_links(body, frontmatter.get('name', skill_path.name), copied_rule_resources)
        
        # Create rule file in .qoder/rules/
        rule_content = f"""# {frontmatter.get('name', skill_path.name)}

{frontmatter.get('description', '')}

## Instructions
{rule_body}
"""
        rule_file = rules_dir / f"{frontmatter.get('name', skill_path.name)}.md"
        with open(rule_file, "w", encoding="utf-8") as f:
            f.write(rule_content)
        
        # Also create a local rule file in the agent directory for reference/usage
        # For the local agent copy, we use the original body since resources are local
        local_rule_content = f"""# {frontmatter.get('name', skill_path.name)}

{frontmatter.get('description', '')}

## Instructions
{body}
"""
        local_rule_file = agent_dir / f"{frontmatter.get('name', skill_path.name)}.md"
        with open(local_rule_file, "w", encoding="utf-8") as f:
            f.write(local_rule_content)
        
        log_msg = f"✅ Converted to Qoder agent: {agent_dir}"
        if copied_rule_resources:
            log_msg += f" (Resources copied to rules: {', '.join(copied_rule_resources)})"
        print(log_msg)
        return agent_dir
    else:
        return agent_config


def create_python_agent_module(frontmatter, body, output_file):
    """Create Python agent module for Qoder"""
    skill_name = frontmatter.get("name", "skill")
    class_name = "".join(word.capitalize() for word in skill_name.split("-")) + "Agent"
    
    module_content = f'''"""
{frontmatter.get('description', 'Agent module')} for Qoder

This agent module was automatically generated from Agent Skill.
"""


class {class_name}:
    """
    Agent for {frontmatter.get('description', 'executing tasks')}
    """
    
    def __init__(self):
        self.name = "{skill_name}"
        self.description = "{frontmatter.get('description', '')}"
    
    def execute(self, task, context=None):
        """
        Execute the agent task
        
        Args:
            task: Task description or parameters
            context: Optional context information
            
        Returns:
            Task execution result
        """
        # Read instructions from SKILL.md
        # Execute skill workflow
        # Return result
        pass
    
    def get_capabilities(self):
        """Get agent capabilities"""
        return {{
            "name": self.name,
            "description": self.description,
            "capabilities": ["task-execution"]
        }}
'''
    
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(module_content)


def convert_all_skills(skills_dir, output_dir):
    """Convert all skills in a directory"""
    skills_dir = Path(skills_dir)
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    
    converted = []
    for skill_dir in skills_dir.iterdir():
        if skill_dir.is_dir() and (skill_dir / "SKILL.md").exists():
            try:
                result = convert_to_qoder_agent(skill_dir, output_dir)
                if result:
                    converted.append(skill_dir.name)
            except Exception as e:
                print(f"Error converting {skill_dir.name}: {e}")
    
    print(f"\n✅ Converted {len(converted)} skills: {', '.join(converted)}")
    return converted


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python convert_to_qoder.py <skill_path> [output_path]")
        print("   or: python convert_to_qoder.py --all <skills_dir> <output_dir>")
        sys.exit(1)
    
    if sys.argv[1] == "--all":
        if len(sys.argv) < 4:
            print("Usage: python convert_to_qoder.py --all <skills_dir> <output_dir>")
            sys.exit(1)
        convert_all_skills(sys.argv[2], sys.argv[3])
    else:
        skill_path = sys.argv[1]
        output_path = sys.argv[2] if len(sys.argv) > 2 else None
        convert_to_qoder_agent(skill_path, output_path)
