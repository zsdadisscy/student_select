<script>
import { defineComponent, reactive, ref } from 'vue';
import StudentLayOut from "@/components/StudentLayOut.vue";
import $ from 'jquery';
import ModuleStudent from '@/store/student';

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
    let error_message = ref('');
    const rules = {
      required: { required: true, message: '必填项', trigger: 'blur' },
      password: { validator: checkPassword, trigger: 'blur' },
      confirmPassword: { validator: checkConfirmPassword, trigger: 'blur' },
    };

    const handleSubmit = e => {
      error_message.value = '';
      e.preventDefault();
      if (formState.new_password !== formState.confirm_password) {
        error_message.value = '两次密码不一致';
        return;
      }
      $.ajax({
        url: 'http://8.130.65.99:8002/student/modify_password/',
        type: 'POST',
        data: {
          user: ModuleStudent.state.user,
          old_password : formState.old_password,
          new_password: formState.new_password,
          confirm_password: formState.confirm_password,
        },
        success(resp) {
          if (resp.result === 'successs')
            alert('密码修改成功');
          else error_message.value = resp.result;
        }
      })
      
    };

    function checkPassword(rule, value, callback) {
      if (value === '') {
        callback(new Error('请输入新密码'));
      } else {
        callback();
      }
    }

    function checkConfirmPassword(rule, value, callback) {
      if (value === '') {
        callback(new Error('请再次输入密码'));
      }  else {
        callback();
      }
    }

    return {
      error_message,
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
    <div class="tips">{{ error_message }}</div>
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
  margin-top: 50px;
  display: flex;
  justify-content: center;
  /* align-items: center; */
  height: 100vh;
}
.tips {
  color: red;
}
.login-form-button {
  margin-left: 50%;
}
</style>