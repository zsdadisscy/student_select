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
            <router-link to="/tutor/studentinfo/">
            <user-outlined />
            <span class="nav-text">学生信息</span>
          </router-link>
          </a-menu-item>
          <a-menu-item key="2">
            <router-link to="/tutor/selectStudent/">
            <video-camera-outlined />
            <span class="nav-text">选择学生</span>
          </router-link>
          </a-menu-item>
          <a-menu-item key="3">
            <router-link to="/tutor/mystudent/">
            <upload-outlined />
            <span class="nav-text">我的学生</span>
          </router-link>
          </a-menu-item>
          <!-- <a-menu-item key="4">
            <router-link to="/tutor/info/">
            <user-outlined />
            <span class="nav-text">注册信息</span>
          </router-link>
          </a-menu-item> -->
          <a-menu-item key="4">
            <router-link to="/tutor/modifyinfo/">
            <user-outlined />
            <span class="nav-text">修改信息</span>
          </router-link>
          </a-menu-item>
          <a-menu-item key="5">
            <router-link to="/tutor/modifypassword/">
            <user-outlined />
            <span class="nav-text">修改密码</span>
          </router-link>
          </a-menu-item>

        </a-menu>
      </a-layout-sider>
      <a-layout>
        <a-layout-header :style="{ background: '#fff', padding: 0, display: 'flex', justifyContent: 'flex-end'  }" >
        <div class="user-info">
          <img :src="user.photo" class="avatar" />
          <span class="username">{{ user.username }}</span>
        </div>

         </a-layout-header>
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
  import { defineComponent, ref, watch,reactive } from 'vue';
  
  import { useRoute } from 'vue-router';
  import $ from 'jquery'
  import ModuleTutor from '@/store/tutor'

  export default defineComponent({
    name: 'StudentLayOut',
    components: {
      UserOutlined,
      VideoCameraOutlined,
      UploadOutlined,
    },
    setup() {
      const route = useRoute(); // Access the current route
    const selectedKeys = ref([]); // Initialize selectedKeys as an empty array

    // Update selectedKeys based on the current route
    const updateSelectedKeys = () => {
      const { path } = route;
      if (path.startsWith('/tutor/studentinfo/')) {
        selectedKeys.value = ['1'];
      } else if (path.startsWith('/tutor/selectStudent/')) {
        selectedKeys.value = ['2'];
      } else if (path.startsWith('/tutor/mystudent/')) {
        selectedKeys.value = ['3'];
      // } else if (path.startsWith('/tutor/info/')) {
      //   selectedKeys.value = ['4'];
      } else if (path.startsWith('/tutor/modifyinfo/')) {
        selectedKeys.value = ['4'];
      } else if (path.startsWith('/tutor/modifypassword/')) {
        selectedKeys.value = ['5'];
      } else {
        selectedKeys.value = [];
      }
    };

    // Call updateSelectedKeys initially and on route change
    updateSelectedKeys();
    watch(
      () => route.path,
      () => {
        updateSelectedKeys();
      }
    );

      const onCollapse = (collapsed, type) => {
        console.log(collapsed, type);
      };
      const onBreakpoint = broken => {
        console.log(broken);
      };
      const user = reactive({});
      $.ajax({

        url: "http://8.130.65.99:8002/tutor/get_info/", 
        type: "GET",
        data: {
          user: ModuleTutor.state.user,
        },
        success(resp) {
          if (resp.result === 'success') {
              user.username = resp.date.username;
              user.photo = "http://8.130.65.99:8002" + resp.date.photo;
      // persons.value = resp.data;
      // console.log(persons.value);
      // userInfo.value.avatar = resp.avatar; 
      // userInfo.value.username = resp.username; 
          }
        }
});

      return {
        user,
        selectedKeys,
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

  
  .user-info {
  display: flex;
  align-items: center;
  margin-left: auto; 
  margin-right: 50px;
}

.avatar {
  width: 48px; /* Increase the width of the avatar */
  height: 48px; /* Increase the height of the avatar */
  border-radius: 50%;
  margin-right: 8px;
}
.username {
  font-weight: bold;
}
  </style>
