<script>
import { defineComponent, reactive, ref, readonly } from 'vue';
import TeacherLayOut from "@/components/TeacherLayOut.vue";

import ModuleTutor from "@/store/tutor"
import $ from 'jquery';

export default defineComponent({
  name: 'TutorModifyInfo',
  components: {
    TeacherLayOut,
  },
  setup() {
    let shift = {
    'man' :'男',
    'women': '女',
  }
  const initialData = {

    name: ModuleTutor.state.username,
    id: ModuleTutor.state.id,
    date1: ModuleTutor.state.date_of_birth,
    college: ModuleTutor.state.college,
    sex: shift[ModuleTutor.state.gender],
    research: ModuleTutor.state.research_area, // 研究方向
    email: ModuleTutor.state.email,
    phone: ModuleTutor.state.phone,
    bio: ModuleTutor.state.bio, // 个人简历
      
    avatar: {
      url: 'http://8.130.65.99:8002' + ModuleTutor.state.photo,
    },
  };
  const formState = reactive({
    name: readonly(ref(initialData.name)),
    id: readonly(ref(initialData.id)),
    date1: readonly(ref(initialData.date1)),
    sex: readonly(ref(initialData.sex)),
    college: readonly(ref(initialData.college)),

    bio: ref(initialData.bio),
    email: ref(initialData.email),
    phone: ref(initialData.phone),
    research: ref(initialData.research),
    avatar: ref(initialData.avatar),
  });
  // ...
  const onSubmit = () => {
      $.ajax({
        url: 'http://8.130.65.99:8002/tutor/modify_info/',
        type: 'POST',
        data: {
          user: ModuleTutor.state.user,
          bio: formState.bio,
          email: formState.email,
          phone: formState.phone,
          photo: formState.avatar,
          research: formState.research,
        },
        success(resp) {
            console.log(formState.avatar);
            console.log(resp);
            alert("提交成功");
        }
      })
  }
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
  <TeacherLayOut>
    <a-form :model="formState" :label-col="labelCol" :wrapper-col="wrapperCol" class="sInfo">
        <!-- ... 其他表单项 ... -->
        <a-form-item label="* 姓名">
          <a-input :value="formState.name" readonly />
        </a-form-item>
        <a-form-item label="* 工号">
          <a-input :value="formState.id" readonly />
        </a-form-item>
        <a-form-item label="* 出生日期">
          <a-input :value="formState.date1" readonly />
        </a-form-item>
        <a-form-item label="* 性别">
          <a-input :value="formState.sex" readonly />
        </a-form-item>
        <a-form-item label="* 学院">
          <a-input :value="formState.college" readonly />
        </a-form-item>

        <a-form-item label="邮箱">
          <a-input v-model:value="formState.email" />
        </a-form-item>
        <a-form-item label="手机号">
          <a-input v-model:value="formState.phone" />
        </a-form-item>
        <a-form-item label="研究方向">
          <a-input v-model:value="formState.research" />
        </a-form-item>

        <a-form-item label="个人简介">
          <a-textarea :rows="4" v-model:value="formState.bio" />
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
    
  </TeacherLayOut>

</div>
</template>

<style scoped>

</style>