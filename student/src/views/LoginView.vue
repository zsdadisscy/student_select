<template>
  <div class="login-container">
    <h2 class="login-title">登录</h2>
    <a-form ref="form" :model="form" class="login-form">
      <h2 class="title">用户登录</h2>
      <div class="account-type-wrapper">
        <div class="account-type-label">账号类型:</div>
        <div class="account-type-select">
          <a-select v-model="id_name" style="width: 200px">
            <a-select-option value="">请选择账号类型</a-select-option>
            <a-select-option value="学生">学生</a-select-option>
            <a-select-option value="导师">导师</a-select-option>
          </a-select>
        </div>
      </div>
      <a-form-item>
        <a-input v-model="id" placeholder="学号/工号">
        </a-input>
      </a-form-item>
      <a-form-item>
        <a-input-password v-model="password" placeholder="密码">
        </a-input-password>
      </a-form-item>
      <div class="error_message">{{ error_message }}</div>
      <a-form-item>
        <a-button class="submit" type="primary" @click="login">登录</a-button>
      </a-form-item>
    </a-form>
  </div>
</template>

<script>
import { defineComponent, ref } from 'vue';
import { Select } from 'ant-design-vue';

export default defineComponent({
  name: 'LoginView',
  components: {
    'a-select': Select,
    'a-select-option': Select.Option
  },
  setup() {
    const id = ref('');
    const password = ref('');
    const error_message = ref('');
    const id_name = ref('');

    const login = () => {
      error_message.value = '错误';
      console.log(id_name.value);
    };

    return {
      id,
      password,
      error_message,
      login,
      id_name
    };
  }
})
</script>

<style scoped>
.error_message {
  font-family: Microsoft Yahei;
  color: red;
  margin-bottom: 5px;
}
.account-type-wrapper {
  display: flex;
  align-items: center;
  margin-bottom: 13px;
}

.account-type-label {
  margin-right: 59px;
  font-size: 20px;
  font-family: Microsoft Yahei;
}
.login-form {
  width: 565px;
  height: 372px;
  margin: 0 auto;
  background: url("../assets/graybackground.png");
  padding: 40px 110px;
}

/* 背景 */
.login-container {
  position: absolute;
  width: 100%;
  height: 100%;
  background: url("../assets/background.jpg") no-repeat;
  background-size: 100% 100%;
}

/* Log */
.login-title {
  color: #fff;
  text-align: center;
  margin: 100px 0 60px 0;
  font-size: 36px;
  font-family: Microsoft Yahei;
}
/* 登陆按钮 */
.submit {
  width: 100%;
  height: 45px;
  font-size: 16px;
}
/* 用户登陆标题 */
.title {
  text-align: center;
  margin-bottom: 50px;
  color: #fff;
  font-weight: 700;
  font-size: 24px;
  font-family: Microsoft Yahei;
}
/* 输入框 */
.inputBox {
  height: 45px;
}
/* 输入框内左边距50px */
.ant-input-affix-wrapper .ant-input:not(:first-child) {
  padding-left: 50px;
}
</style>