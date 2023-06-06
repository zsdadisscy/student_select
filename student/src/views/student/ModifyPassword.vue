<script>
import { defineComponent, reactive } from 'vue';
import StudentLayOut from "@/components/StudentLayOut.vue";
import axios from 'axios'; // make sure axios is installed and imported

export default defineComponent({
  name: 'StudentModifyPassword',
  components: {
    StudentLayOut,
  },
  setup() {
    const formState = reactive({
      old_password: '',
      new_password: '',
      confirm_password: '',
    });

    const rules = {
      required: { required: true, message: '必填项', trigger: 'blur' },
      password: { validator: checkPassword, trigger: 'blur' },
      confirmPassword: { validator: checkConfirmPassword, trigger: 'blur' },
    };

    const handleSubmit = e => {
      e.preventDefault();
      axios.post('/api/change_password/', formState)
        .then(response => {
          console.log(response.data);
        })
        .catch(error => {
          console.log(error);
        });
    };

    function checkPassword(rule, value, callback) {
      if (value === '') {
        callback(new Error('请输入密码'));
      } else if (value !== formState.confirm_password) {
        callback(new Error('两次输入密码不一致!'));
      } else {
        callback();
      }
    }

    function checkConfirmPassword(rule, value, callback) {
      if (value === '') {
        callback(new Error('请再次输入密码'));
      } else if (value !== formState.new_password) {
        callback(new Error('两次输入密码不一致!'));
      } else {
        callback();
      }
    }

    return {
      formState,
      rules,
      handleSubmit,
      checkPassword,
      checkConfirmPassword,
    };
  },

});
</script>

<template>
<div>
  <StudentLayOut>
    <div class="change-password-container">
  <a-form 
    :model="formState" 
    :rules="rules"
    @submit="handleSubmit" 
    :class="['login-form']"
  >
    <a-form-item label="旧密码" name="oldPassword" :rules="[rules.required]">
      <a-input-password v-model:value="formState.old_password" placeholder="输入旧密码" style="width: 300px;"/>
    </a-form-item>
    <a-form-item label="新密码" name="newPassword" :rules="[rules.required, rules.password]">
      <a-input-password v-model:value="formState.new_password" placeholder="输入新密码" style="width: 300px;"/>
    </a-form-item>
    <a-form-item label="确认密码" name="confirmPassword" :rules="[rules.required, rules.password, rules.confirmPassword]">
      <a-input-password v-model:value="formState.confirm_password" placeholder="确认新密码" style="width: 300px;"/>
    </a-form-item>
    <a-form-item>
      <a-button type="primary" html-type="submit" class="login-form-button">
        提交
      </a-button>
    </a-form-item>
  </a-form>
</div>
  </StudentLayOut>
</div>
</template>

<style scoped>
.change-password-container {
  display: flex;
  justify-content: center;
  /* align-items: center; */
  height: 100vh;
}
</style>