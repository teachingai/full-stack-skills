# Installation

## 在 UniApp 项目中安装 uCharts

uCharts 是专为 UniApp 设计的图表库，需要正确集成到 UniApp 项目中。

### 方式一：通过 DCloud 插件市场安装（推荐）

1. 访问 DCloud 插件市场：https://ext.dcloud.net.cn/plugin?id=271
2. 在 HBuilderX 中：
   - 打开项目
   - 点击"工具" → "插件安装"
   - 搜索 "uCharts" 或直接输入插件 ID: 271
   - 点击"导入插件"
3. 插件会自动导入到 `uni_modules/qiun-data-charts` 目录

### 方式二：通过 npm 安装

```bash
npm install @qiun/ucharts
```

安装后，uCharts 位于 `node_modules/@qiun/ucharts` 目录。

### 方式三：手动下载安装

1. 从官方仓库下载 uCharts
2. 将下载的文件解压到项目的 `uni_modules/qiun-data-charts` 目录

## UniApp 项目配置

### 1. 引入 uCharts

在页面中引入 uCharts 组件：

```vue
<template>
  <view class="chart-container">
    <qiun-data-charts 
      type="line"
      :opts="opts"
      :chartData="chartData"
    />
  </view>
</template>

<script>
export default {
  data() {
    return {
      chartData: {},
      opts: {}
    }
  }
}
</script>
```

### 2. 配置 easycom（推荐）

在 `pages.json` 中配置 easycom，实现组件自动引入：

```json
{
  "easycom": {
    "autoscan": true,
    "custom": {
      "qiun-data-charts": "@/uni_modules/qiun-data-charts/components/qiun-data-charts/qiun-data-charts.vue"
    }
  },
  "pages": [
    // ... 页面配置
  ]
}
```

### 3. 验证安装

创建测试页面验证安装是否成功：

```vue
<template>
  <view class="container">
    <qiun-data-charts 
      type="line"
      :opts="opts"
      :chartData="chartData"
    />
  </view>
</template>

<script>
export default {
  data() {
    return {
      chartData: {
        categories: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],
        series: [{
          name: '数据',
          data: [120, 200, 150, 80, 70, 110, 130]
        }]
      },
      opts: {
        color: ['#409EFF'],
        padding: [15, 15, 0, 15],
        enableScroll: false,
        legend: {
          show: false
        },
        xAxis: {
          disableGrid: true
        },
        yAxis: {
          gridType: 'dash',
          dashLength: 2
        }
      }
    }
  }
}
</script>

<style scoped>
.container {
  width: 100%;
  height: 400px;
}
</style>
```

如果图表正常显示，说明安装成功。

## 目录结构

安装后的项目结构：

```
uniapp-project/
├── uni_modules/
│   └── qiun-data-charts/   # uCharts 插件
│       ├── components/     # 组件目录
│       └── ucharts/        # uCharts 核心文件
├── pages/                  # 页面目录
├── static/                 # 静态资源
├── App.vue                 # 应用入口
├── main.js                 # 主入口文件
├── pages.json              # 页面配置
├── manifest.json           # 应用配置
└── uni.scss                # 全局样式变量
```

## 注意事项

1. **Canvas 支持**：确保目标平台支持 Canvas
2. **easycom 配置**：配置 easycom 后，组件会自动引入
3. **路径问题**：如果使用 npm 安装，注意路径可能需要调整
4. **版本兼容**：确保 uCharts 版本与 UniApp 版本兼容
5. **平台差异**：不同平台对 Canvas 的支持可能有差异

## 常见问题

### 图表不显示

- 检查组件是否正确引入
- 检查数据格式是否正确
- 检查容器是否有明确的高度
- 检查平台是否支持 Canvas

### 组件找不到

- 检查 easycom 配置是否正确
- 检查组件路径是否正确
- 检查是否在正确的目录下

### 样式问题

- 确保容器有明确的高度
- 检查 rpx 单位是否正确转换
- 检查平台特定的样式限制
