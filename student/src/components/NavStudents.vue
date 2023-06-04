<template>
    <!-- <div class="top">
      <p>StudentPage</p>
  </div> -->
    <div class="Nav">
      <a-switch
        :checked="theme === 'dark'"
        checked-children="Dark"
        un-checked-children="Light"
        @change="changeTheme"
      style="float: left"/>
      <br />
      <br />
      <a-menu
        v-model:openKeys="openKeys"
        v-model:selectedKeys="selectedKeys"
        style="width: 256px"
        mode="inline"
        :theme="theme"
      >
        <a-menu-item key="1">
          <template #icon>
            <MailOutlined />
          </template>
          个人信息注册
        </a-menu-item>
        <a-menu-item key="2">
          <template #icon>
            <CalendarOutlined />
          </template>
          导师信息
        </a-menu-item>
        <a-sub-menu key="sub1">
          <template #icon>
            <AppstoreOutlined />
          </template>
          <template #title>已选导师</template>
          <a-menu-item key="3">Option 3</a-menu-item>
          <a-menu-item key="4">Option 4</a-menu-item>
          <a-sub-menu key="sub1-2" title="Submenu">
            <a-menu-item key="5">Option 5</a-menu-item>
            <a-menu-item key="6">Option 6</a-menu-item>
          </a-sub-menu>
        </a-sub-menu>
        <a-sub-menu key="sub2">
          <template #icon>
            <SettingOutlined />
          </template>
          <template #title>修改资料</template>
          <a-menu-item key="7">Option 7</a-menu-item>
          <a-menu-item key="8">Option 8</a-menu-item>
          <a-menu-item key="9">Option 9</a-menu-item>
          <a-menu-item key="10">Option 10</a-menu-item>
        </a-sub-menu>
      </a-menu>
    </div>
  </template>
  <script>
  import { defineComponent, reactive, toRefs } from 'vue';
  import { MailOutlined, CalendarOutlined, AppstoreOutlined, SettingOutlined } from '@ant-design/icons-vue';
  export default defineComponent({
    name: 'NavStudents',
    components: {
      MailOutlined,
      CalendarOutlined,
      AppstoreOutlined,
      SettingOutlined,
    },
    setup() {
      const state = reactive({
        theme: 'dark',
        selectedKeys: ['1'],
        openKeys: ['sub1'],
      });
      const changeTheme = checked => {
        state.theme = checked ? 'dark' : 'light';
      };
      return {
        ...toRefs(state),
        changeTheme,
      };
    },
  });
  </script>

