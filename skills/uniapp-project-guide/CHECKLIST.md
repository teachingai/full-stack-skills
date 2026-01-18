# uni-app 技能与官方文档对应核对清单

## 核对目标

确保所有 uni-app 相关技能与官方文档一一对应，每个组件和 API 都有独立的示例文件，包含原文档地址和官网全部示例。

## 官方文档参考

- **组件文档**: https://uniapp.dcloud.net.cn/component/
- **API 文档**: https://uniapp.dcloud.net.cn/api/
- **uni-app-x 组件**: https://doc.dcloud.net.cn/uni-app-x/component/
- **uni-app-x API**: https://doc.dcloud.net.cn/uni-app-x/api/

## 核对任务清单

### 1. uni-app 内置组件核对

#### 视图容器组件
- [x] view - ✅ 已有文档 + ✅ 已创建示例文件 `examples/components/built-in/view.md`
- [x] scroll-view - ✅ 已有文档 + ✅ 已创建示例文件 `examples/components/built-in/scroll-view.md`
- [x] swiper - ✅ 已有文档 + ✅ 已创建示例文件 `examples/components/built-in/swiper.md`
- [x] match-media - ✅ 已有文档
- [x] movable-area - ✅ 已有文档
- [x] movable-view - ✅ 已有文档
- [x] cover-view - ✅ 已有文档
- [x] cover-image - ✅ 已有文档

#### 基础内容组件
- [x] icon - ✅ 已有文档 + ✅ 已创建示例文件 `examples/components/built-in/icon.md`
- [x] text - ✅ 已有文档 + ✅ 已创建示例文件 `examples/components/built-in/text.md`
- [x] rich-text - ✅ 已有文档
- [x] progress - ✅ 已有文档

#### 表单组件
- [x] button - ✅ 已有文档 + ✅ 已创建示例文件 `examples/components/built-in/button.md`
- [x] checkbox - ✅ 已有文档 + ✅ 已创建示例文件 `examples/components/built-in/checkbox.md`
- [x] editor - ✅ 已有文档
- [x] form - ✅ 已有文档
- [x] input - ✅ 已有文档 + ✅ 已创建示例文件 `examples/components/built-in/input.md`
- [x] label - ✅ 已有文档
- [x] picker - ✅ 已有文档
- [x] picker-view - ✅ 已有文档
- [x] radio - ✅ 已有文档 + ✅ 已创建示例文件 `examples/components/built-in/radio.md`
- [x] slider - ✅ 已有文档
- [x] switch - ✅ 已有文档
- [x] textarea - ✅ 已有文档

#### 导航组件
- [x] navigator - ✅ 已有文档

#### 媒体组件
- [x] audio - ✅ 已有文档
- [x] camera - ✅ 已有文档
- [x] image - ✅ 已有文档 + ✅ 已创建示例文件 `examples/components/built-in/image.md`
- [x] video - ✅ 已有文档
- [x] live-player - ✅ 已有文档
- [x] live-pusher - ✅ 已有文档

#### 其他组件
- [x] map - ✅ 已有文档
- [x] canvas - ✅ 已有文档
- [x] web-view - ✅ 已有文档
- [x] ad - ✅ 已有文档
- [x] ad-draw - ✅ 已有文档
- [x] custom-tab-bar - ✅ 已有文档
- [x] navigation-bar - ✅ 已有文档
- [x] page-meta - ✅ 已有文档
- [x] unicloud-db - ✅ 已有文档

**状态**: ✅ 所有内置组件（40个）已有文档

### 2. uni-ui 扩展组件核对

**状态**: ✅ 所有 uni-ui 组件（44个）已有文档

### 3. uni-app API 核对

#### 网络请求 API
- [x] uni.request - ✅ 已创建示例文件 `examples/api/network/request.md`
- [ ] uni.uploadFile
- [ ] uni.downloadFile
- [ ] uni.connectSocket
- [ ] uni.onSocketOpen
- [ ] uni.onSocketError
- [ ] uni.sendSocketMessage
- [ ] uni.onSocketMessage
- [ ] uni.closeSocket
- [ ] uni.onSocketClose

#### 数据存储 API
- [x] uni.setStorage - ✅ 已创建示例文件 `examples/api/storage/set-storage.md`
- [ ] uni.setStorageSync
- [x] uni.getStorage - ✅ 已创建示例文件 `examples/api/storage/get-storage.md`
- [ ] uni.getStorageSync
- [ ] uni.getStorageInfo
- [ ] uni.getStorageInfoSync
- [ ] uni.removeStorage
- [ ] uni.removeStorageSync
- [ ] uni.clearStorage
- [ ] uni.clearStorageSync

#### 设备信息 API
- [x] uni.getSystemInfo - ✅ 已创建示例文件 `examples/api/device/get-system-info.md`
- [ ] uni.getSystemInfoSync
- [ ] uni.getNetworkType
- [ ] uni.onNetworkStatusChange
- [ ] uni.getBatteryInfo
- [ ] uni.getBatteryInfoSync
- [ ] uni.setScreenBrightness
- [ ] uni.getScreenBrightness
- [ ] uni.setKeepScreenOn

#### 界面交互 API
- [x] uni.showToast - ✅ 已创建示例文件 `examples/api/ui/show-toast.md`
- [x] uni.showLoading - ✅ 已创建示例文件 `examples/api/ui/show-loading.md`
- [ ] uni.hideToast
- [ ] uni.hideLoading
- [x] uni.showModal - ✅ 已创建示例文件 `examples/api/ui/show-modal.md`
- [ ] uni.showActionSheet
- [ ] uni.setNavigationBarTitle
- [ ] uni.setNavigationBarColor
- [ ] uni.showNavigationBarLoading
- [ ] uni.hideNavigationBarLoading
- [ ] uni.setTabBarBadge
- [ ] uni.removeTabBarBadge
- [ ] uni.showTabBarRedDot
- [ ] uni.hideTabBarRedDot
- [ ] uni.setTabBarStyle
- [ ] uni.setTabBarItem

#### 位置服务 API
- [x] uni.getLocation - ✅ 已创建示例文件 `examples/api/location/get-location.md`
- [ ] uni.openLocation
- [ ] uni.chooseLocation

#### 媒体处理 API
- [x] uni.chooseImage - ✅ 已创建示例文件 `examples/api/media/choose-image.md`
- [x] uni.previewImage - ✅ 已创建示例文件 `examples/api/media/preview-image.md`
- [ ] uni.getImageInfo
- [ ] uni.saveImageToPhotosAlbum
- [ ] uni.chooseVideo
- [ ] uni.saveVideoToPhotosAlbum
- [ ] uni.chooseMedia
- [ ] uni.chooseFile

#### 页面路由 API
- [x] uni.navigateTo - ✅ 已创建示例文件 `examples/api/navigation/navigate-to.md`
- [ ] uni.redirectTo
- [ ] uni.reLaunch
- [ ] uni.switchTab
- [x] uni.navigateBack - ✅ 已创建示例文件 `examples/api/navigation/navigate-back.md`

#### 文件操作 API
- [ ] uni.saveFile
- [ ] uni.getFileInfo
- [ ] uni.getSavedFileList
- [ ] uni.getSavedFileInfo
- [ ] uni.removeSavedFile

#### 支付 API
- [ ] uni.requestPayment

#### 分享 API
- [ ] uni.share

#### 其他 API
- [ ] uni.canIUse
- [ ] uni.getProvider
- [ ] uni.login
- [ ] uni.getUserInfo
- [ ] uni.checkSession
- [ ] uni.authorize
- [ ] uni.openSetting
- [ ] uni.getSetting

**状态**: 🔄 进行中 - 已创建部分 API 独立示例文件（request.md, set-storage.md, get-storage.md, show-toast.md, show-modal.md, show-loading.md, navigate-to.md, navigate-back.md, choose-image.md, preview-image.md, get-location.md, get-system-info.md），需要继续创建其他 API 示例文件

### 4. uni-app-x 组件和 API 核对

**状态**: ❌ 需要创建完整的 uni-app-x 组件和 API 文档

### 5. 文档完整性检查

#### 每个组件文档应包含
- [ ] 组件概述
- [ ] 所有属性说明（类型、默认值、说明）
- [ ] 所有事件说明
- [ ] 插槽说明（如果有）
- [ ] 平台兼容性表格
- [ ] 使用示例（基础用法）
- [ ] 更多示例（官网全部示例）
- [ ] 官方文档链接

#### 每个 API 文档应包含
- [ ] API 概述
- [ ] 参数说明
- [ ] 返回值说明
- [ ] 平台兼容性
- [ ] 使用示例
- [ ] 官方文档链接

## 更新任务

### 优先级 1: 为每个 API 创建独立示例文件

**任务**: 在 `examples/api/` 目录下为每个 API 创建独立的示例文件

**进度**: 
- ✅ 已创建: `examples/api/network/request.md`
- ✅ 已创建: `examples/api/storage/set-storage.md`
- ✅ 已创建: `examples/api/ui/show-toast.md`
- ✅ 已创建: `examples/api/navigation/navigate-to.md`
- ✅ 已创建: `examples/api/navigation/navigate-back.md`
- ✅ 已创建: `examples/api/media/choose-image.md`
- ✅ 已创建: `examples/api/media/preview-image.md`
- ✅ 已创建: `examples/api/location/get-location.md`
- ✅ 已创建: `examples/api/device/get-system-info.md`
- ✅ 已创建: `examples/api/storage/get-storage.md`
- ✅ 已创建: `examples/api/ui/show-modal.md`
- ✅ 已创建: `examples/api/ui/show-loading.md`
- ⏳ 待创建: 其他所有 API 示例文件（约40+个）

**需要创建的目录结构**:
```
examples/
├── api/
│   ├── network/
│   │   ├── request.md ✅
│   │   ├── upload-file.md ⏳
│   │   ├── download-file.md ⏳
│   │   └── websocket.md ⏳
│   ├── storage/
│   │   ├── set-storage.md ✅
│   │   ├── get-storage.md ⏳
│   │   └── ... ⏳
│   ├── device/ ⏳
│   ├── ui/
│   │   ├── show-toast.md ✅
│   │   └── ... ⏳
│   ├── location/ ⏳
│   ├── media/ ⏳
│   ├── navigation/ ⏳
│   ├── file/ ⏳
│   ├── payment/ ⏳
│   ├── share/ ⏳
│   └── other/ ⏳
```

### 优先级 2: 为每个内置组件创建独立示例文件

**任务**: 在 `examples/components/built-in/` 目录下为每个内置组件创建独立的示例文件

**进度**:
- ✅ 已创建: `examples/components/built-in/view.md`
- ✅ 已创建: `examples/components/built-in/scroll-view.md`
- ✅ 已创建: `examples/components/built-in/swiper.md`
- ✅ 已创建: `examples/components/built-in/text.md`
- ✅ 已创建: `examples/components/built-in/button.md`
- ✅ 已创建: `examples/components/built-in/input.md`
- ✅ 已创建: `examples/components/built-in/image.md`
- ⏳ 待创建: 其他33个内置组件示例文件

**当前进度统计**:
- API 示例文件: 12/50+ (约24%)
- 组件示例文件: 10/40 (25%)

**需要创建的目录结构**:
```
examples/
├── components/
│   ├── built-in/
│   │   ├── view.md ✅
│   │   ├── scroll-view.md ⏳
│   │   ├── swiper.md ⏳
│   │   └── ... (其他37个组件) ⏳
```

### 优先级 3: 创建 uni-app-x 完整文档

**任务**: 为 uniappx-project-guide 创建完整的组件和 API 文档

**需要创建的目录结构**:
```
uniappx-project-guide/
├── examples/
│   ├── components/
│   │   └── ... (所有 uni-app-x 组件)
│   └── api/
│       └── ... (所有 uni-app-x API)
├── api/
│   └── ... (API 参考文档)
└── templates/
```

### 优先级 4: 验证所有文档链接

**任务**: 检查所有组件和 API 文档中的官方文档链接是否正确

### 优先级 5: 补充缺失的 API

**任务**: 检查官方文档，找出所有 API，确保没有遗漏

## 核对进度

- [x] 内置组件文档完整性检查
- [x] uni-ui 组件文档完整性检查
- [ ] API 文档完整性检查
- [ ] 每个 API 独立示例文件检查
- [ ] 每个组件独立示例文件检查
- [ ] uni-app-x 文档完整性检查
- [ ] 官方文档链接验证

## 下一步行动

1. 先完成 API 独立示例文件的创建
2. 再完成内置组件独立示例文件的创建
3. 最后完成 uni-app-x 完整文档的创建
