---
name: uniapp-cloud-guide
description: A comprehensive skill for uniCloud cloud development. Use this skill whenever the user wants to use uniCloud services, work with cloud databases, create cloud functions, use cloud storage, implement datacom components, or integrate backend services with uni-app. This skill provides complete documentation, examples, and best practices based on the official uniCloud documentation.
license: Complete terms in LICENSE.txt
---

## When to use this skill

Use this skill whenever the user wants to:
- Use uniCloud cloud development services
- Work with cloud databases (add, query, update, delete data)
- Create and deploy cloud functions
- Use cloud storage for file uploads and management
- Implement datacom components for data binding
- Integrate backend services with uni-app
- Set up uniCloud project and configuration
- Handle cloud database permissions and security

## How to use this skill

To use uniCloud in your project:

1. **Identify the cloud service** from the user's request:
   - Cloud database → Use database examples
   - Cloud functions → Use functions examples
   - Cloud storage → Use storage examples
   - Datacom components → Use datacom examples

2. **Load the appropriate example file** from the `examples/` directory:
   - `examples/guide/` - Cloud development guide and setup
   - `examples/database/` - Database operations examples
   - `examples/functions/` - Cloud functions examples
   - `examples/storage/` - Cloud storage examples

3. **Load the appropriate API reference** from the `api/` directory:
   - `api/cloud-api.md` - Complete uniCloud API reference

4. **Follow the specific instructions** in those files for implementation

## Examples and Templates

### Examples

Located in `examples/`:

- **guide/** - Cloud development guide, project setup, configuration
- **database/** - Database operations (CRUD, queries, permissions)
- **functions/** - Cloud functions development and deployment
- **storage/** - Cloud storage operations (upload, download, delete)

### API Reference

Located in `api/`:

- **cloud-api.md** - Complete uniCloud API reference

## Best Practices

1. **Security**: Always set proper database permissions
2. **Performance**: Use indexes for frequently queried fields
3. **Cost**: Optimize cloud function execution time
4. **Error handling**: Implement proper error handling for all cloud operations
5. **Data validation**: Validate data before saving to database

## Resources

- **Official Documentation**: https://doc.dcloud.net.cn/uniCloud/
- **Cloud Database**: https://doc.dcloud.net.cn/uniCloud/database.html
- **Cloud Functions**: https://doc.dcloud.net.cn/uniCloud/cf-functions.html
- **Cloud Storage**: https://doc.dcloud.net.cn/uniCloud/storage.html

## Keywords

unicloud, uniCloud, cloud development, cloud database, cloud functions, cloud storage, datacom, 云开发, 云数据库, 云函数, 云存储
