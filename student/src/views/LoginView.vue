<template>
 
    <ContentBase>
        <a-form
          :model="formState"
          name="basic"
          :label-col="{ span:  16}"
          :wrapper-col="{ span: 16 }"
          autocomplete="off"
          @finish="onFinish"
          @finishFailed="onFinishFailed"
        >
          <a-form-item
            label="用户名"
            name="username"
            :rules="[{ required: true, message: '请输入用户名！' }]"
          >
            <a-input v-model:value="formState.username" />
          </a-form-item>

          <a-form-item
            label="密码"
            name="password"
            :rules="[{ required: true, message: '请输入密码！' }]"
          >
            <a-input-password v-model:value="formState.password" />
          </a-form-item>
          <a-form-item :wrapper-col="{ offset: 8, span: 16 }">
            <a-button type="primary" html-type="submit">登录</a-button>
          </a-form-item>
        </a-form>
    </ContentBase>

</template>
<script>
import { defineComponent, reactive } from 'vue';
import ContentBase from '../components/ContentBase.vue';

export default defineComponent({
  name: 'LoginView',
  components: {
    ContentBase,
  },
  setup() {
    const formState = reactive({
      username: '',
      password: '',
    });
    const onFinish = values => {
      console.log('Success:', values);
    };
    const onFinishFailed = errorInfo => {
      console.log('Failed:', errorInfo);
    };
    return {
      formState,
      onFinish,
      onFinishFailed,
    };
  },
});
</script>

<style scoped>

</style>