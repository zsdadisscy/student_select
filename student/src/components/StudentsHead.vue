<template>

    <a-avatar size="large">
      <template #icon><UserOutlined /></template>
    </a-avatar>

   
  </template>
  <script>
  import { UserOutlined } from '@ant-design/icons-vue';
  import { defineComponent } from 'vue';
  export default defineComponent({
    name: 'StudentsHead',
    components: {
      UserOutlined,
    },
  });
  </script>