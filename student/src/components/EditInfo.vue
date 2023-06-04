<template>
  <a-form :model="formState" :label-col="labelCol" :wrapper-col="wrapperCol" class="sInfo">
    <a-form-item label="姓名">
      <a-input v-model:value="formState.name" placeholder="input your name"/>
    </a-form-item>
    <a-form-item label="学号">
      <a-input v-model:value="formState.id" placeholder="input your student number"/>
    </a-form-item>
    <a-form-item label="学院">
      <a-select v-model:value="formState.college" placeholder="please select your college">
        <a-select-option value="tech">计算机学院</a-select-option>
        <a-select-option value="engineer">工学院</a-select-option>
        <a-select-option value="music">音乐学院</a-select-option>
        <a-select-option value="draw">美术学院</a-select-option>
        <a-select-option value="translation">翻译学院</a-select-option>
        <a-select-option value="politics">政治学院</a-select-option>
      </a-select>
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
    <a-form-item label="密码">

      <a-input-password v-model:value="PasswordValue" placeholder="input password" />
    </a-form-item>
    <a-form-item :wrapper-col="{ span: 10, offset: 10 }">
      <a-button type="primary" @click="onSubmit">Create</a-button>
      <a-button style="margin-left: 10px">Cancel</a-button>
    </a-form-item>
  </a-form>
</template>
<script>
import { defineComponent, reactive, toRaw, ref } from 'vue';
export default defineComponent({
  name: 'StudentsInfo',
  setup() {
    const formState = reactive({
      name: '',
      id: '',
      collage: undefined,
      date1: undefined,
      // delivery: false,
      sex: [],
      resource: '',
      info: '',
    });
    const onSubmit = () => {
      console.log('submit!', toRaw(formState));
    };
    const value = ref('');
    const PasswordValue = ref('');
    return {
      labelCol: {
        span: 10,
      
      },
      wrapperCol: {
        span: 10,
        offsetLeft: 300,
      },
      formState,
      onSubmit,
      value,
      PasswordValue
    };
  },
});
</script>

<style scoped>
.sInfo {
  width: 600px;
  /* margin-top: 100px; */

}
</style>


