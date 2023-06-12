<script>
// import {defineComponent} from "vue";
import { defineComponent, reactive, ref, readonly } from 'vue';
import ModuleStudent from '@/store/student';
import StudentLayOut from "@/components/StudentLayOut.vue";
import $ from 'jquery';

export default defineComponent({
  name: 'StudentModifyInfo',
  components: {
    StudentLayOut,
  },
  setup() {
  let shift = {
    'man' :'男',
    'women': '女',
  }
  const initialData = {
    // 这些应该是从后端获取的初始数据
    name: ModuleStudent.state.username,
    id: ModuleStudent.state.id,
    date1: ModuleStudent.state.date_of_birth,
    sex: shift[ModuleStudent.state.gender],
    resource: ModuleStudent.state.student_type,
    email: ModuleStudent.state.email,
    phone: ModuleStudent.state.phone,
    info: ModuleStudent.state.bio,
  
    avatar: {
      url: 'http://8.130.65.99:8002' + ModuleStudent.state.photo,
    },
  };
  const formState = reactive({
    name: readonly(ref(initialData.name)),
    id: readonly(ref(initialData.id)),
    date1: readonly(ref(initialData.date1)),
    sex: readonly(ref(initialData.sex)),
    resource: readonly(ref(initialData.resource)),
    info: ref(initialData.info),
    avatar: ref(initialData.avatar),
    email: ref(initialData.email),
    phone: ref(initialData.phone),
  });
  const onSubmit = () => {
      $.ajax({
        url: 'http://8.130.65.99:8002/student/modify_info/',
        type: 'POST',
        data: {
          user: ModuleStudent.state.user,
          bio: formState.info,
          email: formState.email,
          phone: formState.phone,
          photo: formState.avatar,
        },
        success(resp) {
            // console.log(formState.avatar);
            // console.log(resp);
            if (resp.result === 'success')
              alert("提交成功");
        }
      })
  }
  // ...
  return {
    formState,
    onSubmit
    // ...
  };
}


});
</script>

<template>
  <div>
    <StudentLayOut>
      <a-form :model="formState" :label-col="labelCol" :wrapper-col="wrapperCol" class="sInfo">
        <!-- ... 其他表单项 ... -->
        <a-form-item label="姓名">
          <a-input :value="formState.name" readonly />
        </a-form-item>
        <a-form-item label="学号">
          <a-input :value="formState.id" readonly />
        </a-form-item>
        <a-form-item label="出生日期">
          <a-input :value="formState.date1" readonly />
        </a-form-item>
        <a-form-item label="性别">
          <a-input :value="formState.sex" readonly />
        </a-form-item>
        <a-form-item label="类型">
          <a-radio-group :value="formState.resource" readonly>
            <a-radio value="1">专硕</a-radio>
            <a-radio value="2">学硕</a-radio>
          </a-radio-group>
        </a-form-item>
        <a-form-item label="邮箱">
          <a-input v-model:value="formState.email" />
        </a-form-item>
        <a-form-item label="手机号">
          <a-input v-model:value="formState.phone" />
        </a-form-item>
        <a-form-item label="个人简介">
          <a-textarea :rows="4" v-model:value="formState.info" />
        </a-form-item>
        <a-form-item label="头像">
          <a-upload
            v-model:value="formState.avatar"
            name="file"
            list-type="picture-card"
            show-upload-list="false"
            :before-upload="beforeUpload"
          >
            <div v-if="formState.avatar">
              <a-avatar :src="formState.avatar.url" size="large" />
            </div>
            <div v-else>
              <a-icon type="plus" />
              <div class="ant-upload-text">上传头像</div>
            </div>
          </a-upload>
        </a-form-item>
        <a-form-item :wrapper-col="{ span: 10, offset: 12 }">
          <a-button type="primary" @click="onSubmit">提交</a-button>
        </a-form-item>
      </a-form>
    </StudentLayOut>
  </div>
</template>


<style scoped>

</style>