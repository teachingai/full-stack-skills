# Installation

## 在 UniAppX 项目中安装 uView Pro

uView Pro 是专为 UniAppX 设计的 UI 组件库，需要正确集成到 UniAppX 项目中。

### 方式一：通过 DCloud 插件市场安装（推荐）

1. 访问 DCloud 插件市场：https://ext.dcloud.net.cn/plugin?id=24633
2. 在 HBuilderX 中：
   - 打开 UniAppX 项目
   - 点击"工具" → "插件安装"
   - 搜索 "uView Pro" 或直接输入插件 ID: 24633
   - 点击"导入插件"
3. 插件会自动导入到 `uni_modules/uview-pro` 目录

### 方式二：通过 npm 安装

```bash
npm install uview-pro
```

安装后，uView Pro 位于 `node_modules/uview-pro` 目录。

### 方式三：手动下载安装

1. 从官方仓库下载 uView Pro
2. 将下载的文件解压到项目的 `uni_modules/uview-pro` 目录

## UniAppX 项目配置

### 1. 在 main.uts 中引入

```typescript
// main.uts
import { createSSRApp } from 'vue'
import App from './App.vue'
import uViewPro from 'uview-pro'

export function createApp() {
  const app = createSSRApp(App)
  app.use(uViewPro)
  return {
    app
  }
}
```

### 2. 在 App.vue 中引入样式

```vue
<!-- App.vue -->
<style lang="scss">
/* 引入 uView Pro 基础样式 */
@import "uview-pro/index.scss";
</style>
```

### 3. 在 uni.scss 中引入主题变量（可选）

```scss
/* uni.scss */
@import "uview-pro/theme.scss";
```

### 4. 配置 easycom（重要）

在 `pages.json` 中配置 easycom，实现组件自动引入：

```json
{
  "easycom": {
    "autoscan": true,
    "custom": {
      "^u-(.*)": "uview-pro/components/u-$1/u-$1.vue"
    }
  },
  "pages": [
    // ... 页面配置
  ]
}
```

### 5. 验证安装

创建测试页面 `pages/index/index.vue`：

```vue
<template>
  <view class="container">
    <u-button type="primary">uView Pro 按钮</u-button>
  </view>
</template>

<script setup lang="ts">
// UniAppX 使用 setup 语法
</script>

<style lang="scss" scoped>
.container {
  padding: 20rpx;
}
</style>
```

如果按钮正常显示，说明安装成功。

## 目录结构

安装后的 UniAppX 项目结构：

```
uniappx-project/
├── uni_modules/
│   └── uview-pro/          # uView Pro 插件
│       ├── components/    # 组件目录
│       ├── index.scss     # 基础样式
│       └── theme.scss     # 主题变量
├── pages/                 # 页面目录
├── static/                # 静态资源
├── App.vue                # 应用入口
├── main.uts               # 主入口文件（UniAppX 使用 .uts）
├── pages.json             # 页面配置
├── manifest.json          # 应用配置
└── uni.scss               # 全局样式变量
```

## UniAppX 特性

### TypeScript 支持

UniAppX 使用 TypeScript，需要类型定义：

```typescript
// main.uts
import { createSSRApp } from 'vue'
import App from './App.vue'
import uViewPro from 'uview-pro'

export function createApp() {
  const app = createSSRApp(App)
  app.use(uViewPro)
  return {
    app
  }
}
```

### Setup 语法

UniAppX 推荐使用 Composition API 和 setup 语法：

```vue
<template>
  <view>
    <u-button type="primary" @click="handleClick">按钮</u-button>
  </view>
</template>

<script setup lang="ts">
const handleClick = () => {
  console.log('按钮被点击')
}
</script>
```

## 注意事项

1. **TypeScript 支持**：UniAppX 使用 TypeScript，确保类型正确
2. **Setup 语法**：推荐使用 Composition API 和 setup 语法
3. **SCSS 支持**：确保项目支持 SCSS
4. **easycom 配置**：必须配置 easycom，否则需要手动引入每个组件
5. **路径问题**：如果使用 npm 安装，注意路径可能需要调整
6. **版本兼容**：确保 uView Pro 版本与 UniAppX 版本兼容

## 常见问题

### 组件找不到

- 检查 easycom 配置是否正确
- 检查组件名称是否正确（u-button, u-input 等）
- 检查是否在 main.uts 中注册了 uView Pro

### 样式不生效

- 检查是否在 App.vue 中引入了 `uview-pro/index.scss`
- 检查 style 标签是否设置了 `lang="scss"`
- 检查项目是否支持 SCSS

### TypeScript 类型错误

- 检查是否正确引入了 uView Pro
- 检查类型定义是否正确
- 检查 UniAppX 版本是否支持
