<script>
import { defineComponent, reactive, toRaw, ref } from 'vue';
// import {defineComponent} from "vue";
import StudentLayOut from "@/components/StudentLayOut.vue";

export default defineComponent({
  name: 'StudentInfo',
  components: {
    StudentLayOut,
  },
  setup() {
    const formState = reactive({
      name: '',
      id: '',
      date1: undefined,
      sex: [],
      resource: '',
      info: '',
      avatar: null,  // 头像
    });
    const onSubmit = () => {
      console.log('submit!', toRaw(formState));
    };
    const value = ref('');
    // const PasswordValue = ref('');
    const beforeUpload = file => {
    const reader = new FileReader();
    reader.onload = e => {
      formState.avatar = {
        url: e.target.result,
      };
    };
    reader.readAsDataURL(file);
    return false;
  };
    return {
      labelCol: {
        span: 8,
      
      },
      wrapperCol: {
        span: 10,
        offsetLeft: 150,
      },
      formState,
      onSubmit,
      value,
      beforeUpload,
    };
  },

});
</script>

<template>
<div>
  <StudentLayOut>
    <a-form :model="formState" :label-col="labelCol" :wrapper-col="wrapperCol" class="sInfo">
    <a-form-item label="姓名">
      <a-input v-model:value="formState.name" placeholder="input your name"/>
    </a-form-item>
    <a-form-item label="学号">
      <a-input v-model:value="formState.id" placeholder="input your student number"/>
    </a-form-item>
    <a-form-item label="出生日期">
      <a-date-picker
        v-model:value="formState.date1"
        disabledTime={disabledDateTime}
        type="date"
        placeholder="Pick a date"
        style="width: 100%"
      />
    </a-form-item>
    <a-form-item label="性别">
      <a-checkbox-group v-model:value="formState.sex">
        <a-checkbox value="1" name="sex">男</a-checkbox>
        <a-checkbox value="2" name="sex">女</a-checkbox>
      </a-checkbox-group>
    </a-form-item>
    <a-form-item label="类型">
      <a-radio-group v-model:value="formState.resource">
        <a-radio value="1">专硕</a-radio>
        <a-radio value="2">学硕</a-radio>
      </a-radio-group>
    </a-form-item>
    <a-form-item label="个人简介">
      <!-- <a-input v-model:value="formState.desc" type="textarea" /> -->
      <a-textarea :rows="4" placeholder="input your information" :maxlength="6" v-model:value="formState.info" type="textarea"/>
    </a-form-item>
    <!-- <a-form-item label="密码">

      <a-input-password v-model:value="PasswordValue" placeholder="input password" />
    </a-form-item> -->

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
      <!-- <a-button style="margin-left: 10px">Cancel</a-button> -->
    </a-form-item>
  </a-form>
  </StudentLayOut>

</div>
</template>

<style scoped>

</style>