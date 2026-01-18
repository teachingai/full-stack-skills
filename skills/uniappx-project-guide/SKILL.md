---
name: uniappx-project-guide
description: UniApp-x 项目开发指南，包括 TypeScript 使用、Composition API、组件开发、API 调用、状态管理等开发技巧和最佳实践。适用于使用 uni-app x 开发跨平台应用的场景。
---

# UniApp-x 项目开发指南

## 概述

uni-app x 是 uni-app 的下一代版本，使用 Vue 3 + TypeScript + Vite 技术栈。本技能提供 uni-app x 项目的完整开发指南。

## 核心开发技能

### 1. TypeScript 使用

**类型定义**：

```typescript
// 定义接口
interface User {
  id: number
  name: string
  email: string
}

// 使用接口
const user: User = {
  id: 1,
  name: 'John',
  email: 'john@example.com'
}

// 定义函数类型
type Handler = (data: User) => void

const handleUser: Handler = (user) => {
  console.log(user.name)
}
```

**组件 Props 类型**：

```vue
<script setup lang="ts">
interface Props {
  title: string
  count?: number
  items: string[]
}

const props = withDefaults(defineProps<Props>(), {
  count: 0
})
</script>
```

**API 响应类型**：

```typescript
// 定义 API 响应类型
interface ApiResponse<T> {
  code: number
  message: string
  data: T
}

interface UserListResponse {
  users: User[]
  total: number
}

// 使用
const fetchUsers = async (): Promise<ApiResponse<UserListResponse>> => {
  // ...
}
```

### 2. Composition API

**基本用法**：

```vue
<script setup lang="ts">
import { ref, reactive, computed, watch, onMounted } from 'vue'

// 响应式引用
const count = ref<number>(0)
const message = ref<string>('Hello')

// 响应式对象
interface State {
  name: string
  age: number
}

const state = reactive<State>({
  name: 'uni-app x',
  age: 1
})

// 计算属性
const doubleCount = computed(() => count.value * 2)

// 监听器
watch(count, (newVal, oldVal) => {
  console.log(`count: ${oldVal} -> ${newVal}`)
})

// 生命周期
onMounted(() => {
  console.log('Component mounted')
})
</script>
```

**组合式函数（Composables）**：

```typescript
// composables/useCounter.ts
import { ref, computed } from 'vue'

export function useCounter(initialValue: number = 0) {
  const count = ref<number>(initialValue)
  
  const doubleCount = computed(() => count.value * 2)
  
  const increment = () => {
    count.value++
  }
  
  const decrement = () => {
    count.value--
  }
  
  return {
    count,
    doubleCount,
    increment,
    decrement
  }
}
```

**在组件中使用**：

```vue
<script setup lang="ts">
import { useCounter } from '@/composables/useCounter'

const { count, doubleCount, increment, decrement } = useCounter(10)
</script>
```

### 3. 组件开发

**组件定义**：

```vue
<template>
  <view class="my-component">
    <text class="title">{{ title }}</text>
    <text class="content">{{ content }}</text>
    <button @click="handleClick">点击</button>
  </view>
</template>

<script setup lang="ts">
import { ref } from 'vue'

interface Props {
  title: string
  content?: string
}

const props = withDefaults(defineProps<Props>(), {
  content: ''
})

const emit = defineEmits<{
  (e: 'update', value: string): void
  (e: 'delete'): void
}>()

const handleClick = () => {
  emit('update', 'new value')
}
</script>

<style scoped>
.my-component {
  padding: 20px;
}
.title {
  font-size: 18px;
  font-weight: bold;
}
</style>
```

### 4. API 调用

**网络请求封装**：

```typescript
// utils/request.ts
interface RequestOptions {
  url: string
  method?: 'GET' | 'POST' | 'PUT' | 'DELETE'
  data?: any
  header?: Record<string, string>
}

interface ApiResponse<T> {
  code: number
  message: string
  data: T
}

export const request = <T = any>(options: RequestOptions): Promise<ApiResponse<T>> => {
  return new Promise((resolve, reject) => {
    uni.request({
      url: options.url,
      method: options.method || 'GET',
      data: options.data,
      header: {
        'Content-Type': 'application/json',
        ...options.header
      },
      success: (res) => {
        if (res.statusCode === 200) {
          resolve(res.data as ApiResponse<T>)
        } else {
          reject(new Error(res.data.message || '请求失败'))
        }
      },
      fail: (err) => {
        reject(err)
      }
    })
  })
}
```

**使用示例**：

```typescript
// api/user.ts
import { request } from '@/utils/request'

interface User {
  id: number
  name: string
  email: string
}

export const getUserList = async (): Promise<User[]> => {
  const res = await request<User[]>({
    url: '/api/users',
    method: 'GET'
  })
  return res.data
}

export const getUserById = async (id: number): Promise<User> => {
  const res = await request<User>({
    url: `/api/users/${id}`,
    method: 'GET'
  })
  return res.data
}
```

### 5. 状态管理（Pinia）

**Store 定义**：

```typescript
// store/user.ts
import { defineStore } from 'pinia'

interface User {
  id: number
  name: string
  email: string
}

interface UserState {
  user: User | null
  token: string | null
}

export const useUserStore = defineStore('user', {
  state: (): UserState => ({
    user: null,
    token: null
  }),
  
  getters: {
    isLoggedIn: (state) => !!state.token,
    userName: (state) => state.user?.name || ''
  },
  
  actions: {
    setUser(user: User) {
      this.user = user
    },
    
    setToken(token: string) {
      this.token = token
    },
    
    logout() {
      this.user = null
      this.token = null
    }
  }
})
```

**在组件中使用**：

```vue
<script setup lang="ts">
import { useUserStore } from '@/store/user'

const userStore = useUserStore()

// 访问 state
console.log(userStore.user)

// 使用 getter
console.log(userStore.isLoggedIn)

// 调用 action
userStore.setUser({ id: 1, name: 'John', email: 'john@example.com' })
</script>
```

### 6. 页面导航

**编程式导航**：

```typescript
// 跳转到新页面
const goToDetail = (id: number) => {
  uni.navigateTo({
    url: `/pages/detail/detail?id=${id}`
  })
}

// 返回上一页
const goBack = () => {
  uni.navigateBack({
    delta: 1
  })
}

// 接收页面参数
import { onLoad } from '@dcloudio/uni-app'

onLoad((options) => {
  const id = Number(options.id)
  console.log('Page id:', id)
})
```

### 7. 平台适配

**条件编译**：

```vue
<template>
  <view>
    <!-- #ifdef H5 -->
    <view>H5 平台</view>
    <!-- #endif -->
    
    <!-- #ifdef MP-WEIXIN -->
    <view>微信小程序</view>
    <!-- #endif -->
    
    <!-- #ifdef APP -->
    <view>App 平台</view>
    <!-- #endif -->
  </view>
</template>

<script setup lang="ts">
// #ifdef H5
console.log('H5 平台')
// #endif

// #ifdef MP-WEIXIN
console.log('微信小程序')
// #endif
</script>
```

## 最佳实践

### 1. TypeScript 最佳实践

- 为所有函数和变量添加类型
- 使用接口定义数据结构
- 利用类型推断减少冗余
- 使用泛型提高代码复用性

### 2. Composition API 最佳实践

- 使用 `<script setup>` 语法
- 提取可复用的组合式函数
- 合理组织代码逻辑
- 使用 `ref` 和 `reactive` 合理选择

### 3. 性能优化

- 使用 `v-memo` 缓存列表项
- 合理使用懒加载
- 优化图片资源
- 使用分包加载

### 4. 代码组织

- 按功能模块组织代码
- 提取公共组件和工具函数
- 统一 API 接口管理
- 使用类型定义文件

## 示例 Prompt

- "如何在 uni-app x 中使用 TypeScript 定义组件 Props？"
- "uni-app x 中如何使用 Composition API 和 Pinia？"
- "如何封装 uni-app x 的网络请求？"
- "uni-app x 中如何实现页面导航和参数传递？"
- "如何优化 uni-app x 项目的性能？"
