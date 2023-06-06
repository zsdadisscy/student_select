<script>
import {defineComponent} from "vue";
import StudentLayOut from "@/components/StudentLayOut.vue";

export default defineComponent({
  name: 'MyTutor',
  components: {
    StudentLayOut,
  },
  data() {
    return {
      tutor: {
        name: "李四",
        gender: "男",
        id: "20230001",
        birthdate: "1980-01-01",
        school: "计算机学院",
        email: "lisi@example.com",
        phone: "13000000000",
        research: "人工智能",
        in: '英俊帅气'
      },
    };
  },

});
</script>

<template>
<div class="container">
  <StudentLayOut>
    <a-card class="info-card">
    <div class="title">我的导师</div>
    <a-descriptions bordered layout="vertical">
      <a-descriptions-item label="姓名">{{ tutor.name }}</a-descriptions-item>
      <a-descriptions-item label="性别">{{ tutor.gender }}</a-descriptions-item>
      <a-descriptions-item label="工号">{{ tutor.id }}</a-descriptions-item>
      <a-descriptions-item label="出生日期">{{ tutor.birthdate }}</a-descriptions-item>
      <a-descriptions-item label="学院">{{ tutor.school }}</a-descriptions-item>
      <a-descriptions-item label="邮箱">{{ tutor.email }}</a-descriptions-item>
      <a-descriptions-item label="手机号">{{  tutor.phone }}</a-descriptions-item>
      <a-descriptions-item label="研究方向">{{ tutor.research }}</a-descriptions-item>
      <a-descriptions-item label="研究方向">{{ tutor.research }}</a-descriptions-item>
    </a-descriptions>
  </a-card>
  </StudentLayOut>
</div>
</template>

<style scoped>
.info-card {
  width: 50%;
  margin: auto;
  margin-top: 50px;
}
.info-card {
  width: 80%;
  margin: auto;
  margin-top: 50px;
  padding: 30px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.15);
}

.title {
  text-align: center;
  font-size: 24px;
  font-weight: bold;
  margin-bottom: 30px;
}
</style>




