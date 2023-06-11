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
          <!-- <a-menu-item key="2">
            <router-link to="/student/tutorinfo/:tutorid/">
            <video-camera-outlined />
            <span class="nav-text">导师信息</span>
          </router-link>
          </a-menu-item> -->
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
          <!-- <a-menu-item key="5">
            <router-link to="/student/info/">
            <user-outlined />
            <span class="nav-text">注册信息</span>
          </router-link>
          </a-menu-item> -->
          <a-menu-item key="5">
            <router-link to="/student/modifyinfo/">
            <user-outlined />
            <span class="nav-text">修改信息</span>
          </router-link>
          </a-menu-item>
          <a-menu-item key="6">
            <router-link to="/student/modifypassword/">
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
          <span class="username">你好，{{ user.username }}同学</span>
        </div>
        <a-button type="primary" @click="logout">登出</a-button>
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
  import { UserOutlined,  UploadOutlined} from '@ant-design/icons-vue';
  import { defineComponent, ref, watch, reactive } from 'vue';
  import { useRoute } from 'vue-router';
  import { useRouter } from 'vue-router';
  import { message } from 'ant-design-vue';

  import axios from 'axios';
  import $ from 'jquery'
  import ModuleStudent from '@/store/student'

  export default defineComponent({
    name: 'StudentLayOut',
    components: {
      UserOutlined,
      // VideoCameraOutlined,
      UploadOutlined,

    },
    setup() {
      const router = useRouter();

      const route = useRoute(); // Access the current route

      const selectedKeys = ref([]); // Initialize selectedKeys as an empty array

    // Update selectedKeys based on the current route
    const updateSelectedKeys = () => {
      const { path } = route;
      if (path.startsWith('/student/alltutor/')) {
        selectedKeys.value = ['1'];
      } else if (path.startsWith('/student/tutorinfo/')) {
        selectedKeys.value = ['2'];
      } else if (path.startsWith('/student/myselect/')) {
        selectedKeys.value = ['3'];
      } else if (path.startsWith('/student/mytutor/')) {
        selectedKeys.value = ['4'];
      // } else if (path.startsWith('/student/info/')) {
      //   selectedKeys.value = ['5'];
      } else if (path.startsWith('/student/modifyinfo/')) {
        selectedKeys.value = ['5'];
      } else if (path.startsWith('/student/modifypassword/')) {
        selectedKeys.value = ['6'];
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
    // const userInfo = ref({
    //   avatar: '/path/to/default-avatar.jpg',
    //   username: 'Guest',
    // });
    $.ajax({

      url: "http://8.130.65.99:8002/student/get_info/",
      type: "GET",
      data: {
        user: ModuleStudent.state.user,
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
    const logout = async () => {
      try {
        let data = {"user": " ModuleStudent.state.user"};
        const response = await axios.get('http://8.130.65.99:8002/student/logout/', data);
        if (response.data.result === 'success') {
          // 登出成功
          message.success('登出成功');
          // 重定向到登录页面
          router.push('@/views/LoginView.vue'); // 替换 '/login' 为您的登录页面路由路径
        } else {
          // 登出失败
          message.error('登出失败');
        }
      } catch (error) {
        console.error(error);
        message.error('发生错误');
      }
    };

    

    return {
      user,
      // persons,
      // userInfo,
      // dynamicText,
      selectedKeys,
      onCollapse,
      onBreakpoint,
      logout,
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
