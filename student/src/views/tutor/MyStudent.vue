<script>
import {defineComponent} from "vue";
import TeacherLayOut from "@/components/TeacherLayOut.vue";
import { ref } from 'vue'
import { Card, Descriptions, Avatar } from 'ant-design-vue'
// import axios from 'axios'

export default defineComponent({
  name: 'MyStudent',
  components: {
    TeacherLayOut,
    ACard: Card,
    ADescriptions: Descriptions,
    ADescriptionsItem: Descriptions.Item,
    AAvatar: Avatar
  },
  setup() {
    const student = ref({})
    const loading = ref(true)

    const fetchStudentInfo = async () => {
      
    }

    fetchStudentInfo()

    return {
      student,
      loading
    }
  }
});
</script>

<template>
<div>
  <TeacherLayOut>
    <a-card class="student-card" :loading="loading">
    <template #title>
      <a-avatar :src="student.avatar" size="large" />
      <div class="student-title">
        <h2>{{ student.name }}</h2>
        <p>{{ student.type }}</p>
      </div>
    </template>

    <a-descriptions bordered>
      <a-descriptions-item label="姓名">{{ student.name }}</a-descriptions-item>
      <a-descriptions-item label="性别">{{ student.gender }}</a-descriptions-item>
      <a-descriptions-item label="年龄">{{ student.age }}</a-descriptions-item>
      <a-descriptions-item label="出生日期">{{ student.dob }}</a-descriptions-item>
      <a-descriptions-item label="学号">{{ student.studentNumber }}</a-descriptions-item>
      <a-descriptions-item label="学院">{{ student.college }}</a-descriptions-item>
      <a-descriptions-item label="邮箱">{{ student.email }}</a-descriptions-item>
      <a-descriptions-item label="手机号">{{ student.phone }}</a-descriptions-item>
      <a-descriptions-item label="个人介绍">{{ student.introduction }}</a-descriptions-item>
    </a-descriptions>
  </a-card>

  </TeacherLayOut>
</div>
</template>
<style scoped>
.student-card {
  width: 600px;
  margin: auto;
}

.student-title {
  display: inline-block;
  vertical-align: top;
  margin-left: 20px;
}
</style>