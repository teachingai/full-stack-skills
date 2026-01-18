---
name: uniapp-develop-skills
description: Comprehensive UniApp development skill integrating all uni-app components and APIs. Use when developing uni-app applications, creating Vue components for uni-app, working with uni-app APIs (network, storage, device, location, media, etc.), building cross-platform apps (H5, 小程序, App), or needing references for uni-app component properties, events, and API usage patterns. This skill provides complete documentation for all built-in components (view, text, image, button, form components, media components, navigation, etc.) and all uni-app APIs (uni.request, uni.getStorage, uni.getSystemInfo, uni.navigateTo, etc.) with platform compatibility information, usage examples, and best practices.
license: Complete terms in LICENSE.txt
---

# UniApp 开发技能

## 概述

本技能提供 uni-app 框架的完整开发支持，包括所有内置组件和 API 的详细文档、使用示例和最佳实践。适用于使用 uni-app 开发跨平台应用（H5、小程序、App）的场景。

## 核心能力

1. **组件支持**：提供所有 uni-app 内置组件的完整文档，包括属性、事件、插槽、平台兼容性
2. **API 支持**：提供所有 uni-app API 的完整文档，包括参数、返回值、平台兼容性、使用示例
3. **平台兼容性**：明确标注每个组件和 API 在不同平台（H5、微信小程序、支付宝小程序、App 等）的支持情况
4. **最佳实践**：提供常见场景的代码示例和开发建议

## 使用指南

### 组件查询

uni-app 组件分为两大类：**内置组件**和**扩展组件（uni-ui）**。

#### 1. 内置组件（Built-in Components）

uni-app 提供的基础组件，无需安装即可使用。包括：

- **视图容器**：view、scroll-view、swiper、match-media、movable-area、movable-view、cover-view、cover-image
- **基础内容**：icon、text、rich-text、progress
- **表单组件**：button、checkbox、editor、form、input、label、picker、picker-view、radio、slider、switch、textarea
- **导航组件**：navigator
- **媒体组件**：audio、camera、image、video、live-player、live-pusher
- **其他组件**：map、canvas、web-view、ad、ad-draw、custom-tab-bar、navigation-bar、page-meta、unicloud-db

**官方文档**：https://uniapp.dcloud.net.cn/component/

**参考文档**：`references/components/built-in/` 目录下提供内置组件的详细文档（属性、事件、平台兼容性、使用示例）

#### 2. 扩展组件（uni-ui）

uni-ui 是 DCloud 官方提供的跨端 UI 库，包含 40+ 个常用组件，需要从插件市场安装。

**官方文档**：https://uniapp.dcloud.net.cn/component/uniui/uni-ui.html

**插件市场**：https://ext.dcloud.net.cn/plugin?id=55

**组件列表**：
- **基础组件**：uni-badge、uni-icons、uni-tag、uni-link、uni-section
- **布局组件**：uni-row、uni-grid、uni-group、uni-title
- **导航组件**：uni-nav-bar、uni-breadcrumb
- **数据展示**：uni-card、uni-list、uni-table、uni-pagination、uni-load-more
- **数据录入**：uni-easyinput、uni-forms、uni-number-box、uni-data-checkbox、uni-data-picker、uni-data-select、uni-combox
- **日期时间**：uni-calendar、uni-datetime-picker、uni-dateformat
- **反馈组件**：uni-popup、uni-drawer、uni-notice-bar、uni-tooltip
- **操作反馈**：uni-rate、uni-fav、uni-fab、uni-swipe-action
- **其他组件**：uni-collapse、uni-countdown、uni-search-bar、uni-steps、uni-segmented-control、uni-file-picker、uni-goods-nav、uni-indexed-list、uni-swiper-dot、uni-transition

**完整示例代码**：每个 uni-ui 组件都有独立的完整示例文件，位于 `examples/uni-ui/` 目录。示例文件包含官网展示的所有示例场景，可直接复制使用。

**参考文档**：`references/components/uni-ui/` 目录下提供 uni-ui 组件的详细文档（属性、事件、平台兼容性、使用示例）

### API 查询

当需要查询 API 信息时，参考 `references/api/` 目录下的文档：

- **网络请求**：`references/api/network.md` - uni.request、uni.uploadFile 等
- **数据存储**：`references/api/storage.md` - uni.setStorage、uni.getStorage 等
- **设备信息**：`references/api/device.md` - uni.getSystemInfo、uni.getNetworkType 等
- **界面交互**：`references/api/ui.md` - uni.showToast、uni.showModal 等
- **位置服务**：`references/api/location.md` - uni.getLocation、uni.openLocation 等
- **媒体处理**：`references/api/media.md` - uni.chooseImage、uni.previewImage 等
- **页面路由**：`references/api/navigation.md` - uni.navigateTo、uni.switchTab 等
- **其他 API**：`references/api/other.md` - 文件、支付、分享等

### 开发规范

1. **组件使用**：
   - 所有组件和属性名使用小写，单词间用连字符 `-` 连接
   - 事件绑定使用 `@` 前缀，如 `@click="handleClick"`
   - 属性绑定使用 `:` 前缀，如 `:disabled="isDisabled"`

2. **API 调用**：
   - 使用 Promise 或回调函数处理异步操作
   - 注意平台兼容性，使用条件编译处理平台差异
   - 遵循 uni-app 的命名规范

3. **平台适配**：
   - 使用条件编译 `#ifdef`、`#endif` 处理平台差异
   - 注意不同平台的 API 差异和限制
   - 测试多平台兼容性

## 资源组织

### references/ 目录

**用途**：详细的参考文档，包含组件和 API 的完整文档（与官网一一对应）

**结构**：
- `references/components/` - 组件参考文档
  - `built-in/` - 内置组件详细文档（每个组件独立的 .md 文件，包含属性、事件、平台兼容性、使用示例）
  - `uni-ui/` - uni-ui 扩展组件详细文档（每个组件独立的 .md 文件，包含属性、事件、平台兼容性、使用示例）
  - `README.md` - 组件索引与导航（按内置组件 / uni-ui 分类）
- `references/api/` - API 参考文档（参数、返回值、平台兼容性）

**使用场景**：当需要查找组件的详细信息（属性、事件、平台兼容性、使用示例）时，参考此目录下的文档。每个组件都有独立的文档文件，包含完整信息，减少 token 消耗。

**注意**：
- 组件文档已按类型分类：内置组件在 `built-in/` 目录，扩展组件在 `uni-ui/` 目录
- 每个组件文档包含完整的属性表格、事件列表、平台兼容性表格和使用示例
- uni-ui 组件的完整示例代码在 `examples/uni-ui/` 目录

### examples/ 目录

**用途**：代码示例，包含完整的可运行代码

**结构**：
- `examples/uni-ui/` - uni-ui 组件的完整示例代码（每个组件一个独立的 .vue 文件）

**使用场景**：当需要查看组件的完整使用示例时，参考此目录下的示例文件。每个示例文件包含官网展示的所有示例场景，可直接复制使用。

**注意**：
- references/ 和 examples/ 职责不同，不应合并。references/ 提供文档说明，examples/ 提供可运行代码。
- 内置组件的示例代码请参考[官方文档](https://uniapp.dcloud.net.cn/component/)
- uni-ui 组件的完整示例代码在 `examples/uni-ui/` 目录

## 平台支持

uni-app 支持以下平台：

- **H5**：Web 浏览器
- **微信小程序**：WeChat Mini Program
- **支付宝小程序**：Alipay Mini Program
- **百度小程序**：Baidu Smart Program
- **字节跳动小程序**：ByteDance Mini Program
- **QQ 小程序**：QQ Mini Program
- **快手小程序**：Kuaishou Mini Program
- **App**：iOS、Android（nvue、vue）
- **快应用**：Quick App

每个组件和 API 的详细平台支持情况见对应文档。

## 参考资源

- **官方文档**：https://uniapp.dcloud.net.cn/
- **组件文档**：https://uniapp.dcloud.net.cn/component/
- **API 文档**：https://uniapp.dcloud.net.cn/api/
- **插件市场**：https://ext.dcloud.net.cn/
- **社区问答**：https://ask.dcloud.net.cn/

## 使用示例

### 组件使用示例

基础组件使用示例：

```vue
<template>
  <view class="container">
    <text>{{ message }}</text>
    <button @click="handleClick">点击按钮</button>
    <image :src="imageUrl" mode="aspectFit"></image>
  </view>
</template>

<script>
export default {
  data() {
    return {
      message: 'Hello UniApp',
      imageUrl: '/static/logo.png'
    }
  },
  methods: {
    handleClick() {
      uni.showToast({
        title: '按钮被点击',
        icon: 'success' 
      })
    }
  }
}
</script>
```

**更多组件示例**：
- **内置组件示例**：请参考[官方文档](https://uniapp.dcloud.net.cn/component/)或 `references/components/built-in/` 目录下的组件文档
- **uni-ui 组件完整示例**：见 `examples/uni-ui/` 目录（每个组件都有独立的 .vue 示例文件）
- **组件详细文档**：见 `references/components/built-in/` 和 `references/components/uni-ui/` 目录（每个组件都有独立的文档文件，包含属性、事件、平台兼容性、使用示例）

### API 使用示例

```javascript
// 网络请求
uni.request({
  url: 'https://api.example.com/data',
  method: 'GET',
  success: (res) => {
    console.log(res.data)
  },
  fail: (err) => {
    console.error(err)
  }
})

// 数据存储
uni.setStorage({
  key: 'userInfo',
  data: { name: 'John', age: 30 },
  success: () => {
    console.log('存储成功')
  }
})

// 页面跳转
uni.navigateTo({
  url: '/pages/detail/detail?id=123'
})
```

**更多 API 示例**：见 `references/api/` 目录中的详细文档

## 注意事项

1. **组件层级**：原生组件（如 video、map）层级高于普通组件，需要使用 cover-view 覆盖
2. **条件编译**：使用 `#ifdef`、`#endif` 处理平台差异
3. **生命周期**：注意 uni-app 的页面生命周期和组件生命周期
4. **样式单位**：推荐使用 rpx 作为响应式单位
5. **性能优化**：合理使用组件，避免过度嵌套，注意长列表优化
