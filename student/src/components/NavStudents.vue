<template>
  <!-- <div class="top">
    <p>StudentPage</p>
</div> -->
  <div class="Nav">
    <a-switch
        :checked="theme === 'dark'"
        checked-children="Dark"
        style="float: left"
        un-checked-children="Light"
        @change="changeTheme"/>
    <br/>
    <br/>
    <a-menu
        v-model:openKeys="openKeys"
        v-model:selectedKeys="selectedKeys"
        :theme="theme"
        mode="inline"
        style="width: 256px"
    >
      <a-menu-item key="1">
        <template #icon>
          <MailOutlined/>
        </template>
        个人信息注册
      </a-menu-item>
      <a-menu-item key="2">
        <template #icon>
          <CalendarOutlined/>
        </template>
        导师信息
      </a-menu-item>
      <a-sub-menu key="sub1">
        <template #icon>
          <AppstoreOutlined/>
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
          <SettingOutlined/>
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
import {defineComponent, reactive, toRefs} from 'vue';
import {AppstoreOutlined, CalendarOutlined, MailOutlined, SettingOutlined} from '@ant-design/icons-vue';

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

