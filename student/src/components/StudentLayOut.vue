<template>
    <a-layout>
      <a-layout-sider
        breakpoint="lg"
        collapsed-width="0"
        @collapse="onCollapse"
        @breakpoint="onBreakpoint"
      >
        <div class="logo" />
        <a-menu theme="dark" mode="inline" v-model:selectedKeys="selectedKeys">
          <a-menu-item key="1">
            <router-link to="/student/alltutor/">
            <user-outlined />
            <span class="nav-text">所有导师</span>
          </router-link>
          </a-menu-item>
          <a-menu-item key="2">
            <router-link to="/student/tutorinfo/:tutorid/">
            <video-camera-outlined />
            <span class="nav-text">导师信息</span>
          </router-link>
          </a-menu-item>
          <a-menu-item key="3">
            <router-link to="/student/myselect/">
            <upload-outlined />
            <span class="nav-text">选择导师</span>
          </router-link>
          </a-menu-item>
          <a-menu-item key="4">
            <router-link to="/student/mytutor/">
            <user-outlined />
            <span class="nav-text">我的导师</span>
          </router-link>
          </a-menu-item>
          <a-menu-item key="5">
            <router-link to="/student/info/">
            <user-outlined />
            <span class="nav-text">注册信息</span>
          </router-link>
          </a-menu-item>
          <a-menu-item key="6">
            <router-link to="/student/modifyinfo/">
            <user-outlined />
            <span class="nav-text">修改信息</span>
          </router-link>
          </a-menu-item>
          <a-menu-item key="7">
            <router-link to="/student/modifypassword/">
            <user-outlined />
            <span class="nav-text">修改密码</span>
          </router-link>
          </a-menu-item>
        </a-menu>
      </a-layout-sider>
      <a-layout>
        <a-layout-header :style="{ background: '#fff', padding: 0 }" />
        <a-layout-content :style="{ margin: '24px 16px 0' }">
          <div :style="{ padding: '24px', background: '#fff', minHeight: '360px' }">
            <slot></slot>
          </div>
        </a-layout-content>
        <a-layout-footer style="text-align: center">
          Ant Design ©2018 Created by Ant UED
        </a-layout-footer>
      </a-layout>
    </a-layout>
  </template>
  <script>
  import { UserOutlined, VideoCameraOutlined, UploadOutlined } from '@ant-design/icons-vue';
  import { defineComponent, ref } from 'vue';
  export default defineComponent({
    name: 'StudentLayOut',
    components: {
      UserOutlined,
      VideoCameraOutlined,
      UploadOutlined,
    },
    setup() {
      const onCollapse = (collapsed, type) => {
        console.log(collapsed, type);
      };
      const onBreakpoint = broken => {
        console.log(broken);
      };
      return {
        selectedKeys: ref(['1']),
        onCollapse,
        onBreakpoint,
      };
    },
  });
  </script>
  <style>
  #components-layout-demo-responsive .logo {
    height: 32px;
    background: rgba(255, 255, 255, 0.2);
    margin: 16px;
  }
  
  .site-layout-sub-header-background {
    background: #fff;
  }
  
  .site-layout-background {
    background: #fff;
  }
  
  [data-theme='dark'] .site-layout-sub-header-background {
    background: #141414;
  }
  </style>
