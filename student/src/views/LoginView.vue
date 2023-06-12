
<template>
  <div class="login">
    <div class="login-gray">
      <div class="login-header">
        <h1>登录</h1>
      </div>
      <div class="login-container">
        <a-form @submit="handleSubmit" :class="['login-form']">
          <a-form-item>
            <a-tooltip title="请选择你的身份">
              <a-select v-model="userType" style="width: 100%;" @change="handleChange" placeholder="选择身份">
                <a-select-option value="student">学生</a-select-option>
                <a-select-option value="tutor">导师</a-select-option>
              </a-select>
            </a-tooltip>
          </a-form-item>
          <input class="login-input"
              v-model=username
              :placeholder="userType === 'student' ? '请输入学号' : '请输入工号'"
            />
          <input class="login-input"
              v-model="password"
              type="password"
              placeholder="请输入密码"
            />
          <div class="error-message">
            {{error_message}}
          </div>
          <a-form-item>
            <a-button type="primary" html-type="submit" class="login-form-button">
              登陆
            </a-button>
          </a-form-item>
        </a-form>
      </div>
    </div>

  </div>
</template>

<script>
import {ref} from "vue";
import $ from 'jquery';
import {useStore} from 'vuex';
import ModuleStudent from "@/store/student";
import ModuleTutor from "@/store/tutor";
import router from '@/router/index.js';


export default {
  name: 'LoginView',
  setup() {
    const userType = ref('');
    const username = ref('');
    const password = ref('');
    let error_message = ref('');
    const store = useStore();

    if (ModuleStudent.state.user !== '') {
      $.ajax({
        url: "http://8.130.65.99:8002/get_status/",
        type: 'GET',
        data: {
          user: ModuleStudent.state.user,
        },
        success(resp) {
          // console.log(resp);
          if (resp.result === 'student') {
            store.dispatch('ModuleStudent/get_info');
            router.push({name: 'alltutor'});
          }
          else
            error_message.value = resp.result;
        },
        error() {
          error_message.value = '出现未知错误';
        }
      })
    }
    if (ModuleTutor.state.user !== '') {
      $.ajax({
        url: "http://8.130.65.99:8002/get_status/",
        type: 'GET',
        data: {
          user: ModuleTutor.state.user,
        },
        success(resp) {
          if (resp.result === 'tutor') {
            store.dispatch('ModuleTutor/get_info');
            router.push({name: 'selectstudent'});
          }
          else
            error_message.value = resp.result;
        },
        error() {
          error_message.value = '出现未知错误';
        }
      })
    }

    const handleSubmit = e => {
      e.preventDefault();
      error_message.value = '';
      // 表单验证
      if (userType.value === '') {
        error_message.value = '请选择用户类型';
        return;
      }
      if (!username.value) {
        error_message.value = '请输入学号/工号';
        return;
      }
      if (!password.value) {
        error_message.value = '请输入密码';
        return;
      }

      if (userType.value === 'student') {
        handleStudentLogin(username.value, password.value);
      } else {
        handleTutorLogin(username.value, password.value);
      }
    }


    const handleChange = value => {
      userType.value = value;

    };

    const handleStudentLogin = (username, password) => {
      $.ajax({
        url: 'http://8.130.65.99:8002/student/login/',
        type: 'POST',
        data: {
          id: username,
          password: password
        },
        success(resp) {
          if (resp.result === 'success') {
            // console.log(resp.user);
            ModuleStudent.state.user = resp.user;
            store.dispatch('ModuleStudent/get_info');
            router.push({name: 'alltutor'});
          }
          else
            error_message.value = resp.result;
        },
        error() {
          error_message.value = '出现未知错误';
        }
      })
    };

    const handleTutorLogin = (username, password) => {
      $.ajax({
        url: 'http://8.130.65.99:8002/tutor/login/',
        type: 'POST',
        data: {
          id: username,
          password: password
        },
        success(resp) {
          if (resp.result === 'success') {
            ModuleTutor.state.user = resp.user;
            store.dispatch('ModuleTutor/get_info');
            router.push({name: 'selectstudent'});
          }
          else
            error_message.value = resp.result;
        },
        error() {
          error_message.value = '出现未知错误';
        }
      })
    };

    return {
      userType,
      username,
      password,
      error_message,
      handleSubmit,
      handleChange };
  }
};
</script>

<style scoped>
.login-container {
  display: flex;
  justify-content: center;
  align-items: center;
}

.login-form {
  width: 400px;
  padding: 20px;
}

.login-form-button {
  width: 100%;
}

.has-error .ant-form-item-explain {
  color: #ff4d4f;
}

.login {
  display: flex;
  flex-direction: column;
  align-items: center;
  height: 100vh;
  padding-top: 20px; /* 调整此处的数值来改变标题与登录框之间的距离 */
  background-image: url("http://8.130.65.99:8002/media/photo/background.jpg");
  background-size: cover;
  background-position: center;
}

.login-gray {
  margin-top: 190px;
  background-image: url("http://8.130.65.99:8002/media/photo/graybackground.png");
  background-size: cover;
  background-position: center;
  border-radius: 5%;
}

.login-header {

  text-align: center;
}

.login-header h1 {
  font-size: 24px;
  margin-top: 0; /* 添加此行以重置默认的上边距 */
}

.error-message {
  color: red;
  margin-bottom: 15px;
}

.login-input {
  width: 100%;
  margin-bottom: 23px;
  height: 33px;
}



</style>