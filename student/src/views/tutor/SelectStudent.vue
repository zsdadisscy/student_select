<script>
import {defineComponent} from "vue";
import TeacherLayOut from "@/components/TeacherLayOut.vue";
import { Card, Button, Alert } from 'ant-design-vue';
import student1 from '@/assets/student_photo.png';
import student2 from '@/assets/student_photo.png';
import student3 from '@/assets/student_photo.png';

export default defineComponent({
  name: 'SelectStudent',
  components: {
    TeacherLayOut,
    'a-card': Card,
    'a-button': Button,
    'a-alert': Alert,
  },
  data() {
    return {
      students: [
        { id: 1, name: '张三', type: '文科', avatar: student1 },
        { id: 2, name: '李四', type: '理科', avatar: student2 },
        { id: 3, name: '王五', type: '文科', avatar: student3 },
      ],
      selectedStudentIds: [],
      submitted: false,
    };
  },
  computed: {
    selectedNames() {
      return this.students
        .filter(student => this.selectedStudentIds.includes(student.id))
        .map(student => student.name)
        .join(', ');
    },
  },
  methods: {
    toggleSelection(id) {
      if (this.selectedStudentIds.includes(id)) {
        this.selectedStudentIds = this.selectedStudentIds.filter(studentId => studentId !== id);
      } else {
        this.selectedStudentIds.push(id);
      }
    },
    submit() {
      console.log('提交的学生ID：', this.selectedStudentIds);
      this.submitted = true;
    },
  },
});
</script>

<template>
  <TeacherLayOut>
    <div class="container">
      <div class="student-grid">
        <a-card
          v-for="student in students"
          :key="student.id"
          class="student-card"
        >
          <div class="student-info">
            <img :src="student.avatar" alt="Student Avatar" class="avatar" />
            <div class="student-details">
              <p><b>类型：</b>{{ student.type }}</p>
              <p><b>姓名：</b>{{ student.name }}</p>
            </div>
            <a-button 
              @click="toggleSelection(student.id)"
              :type="selectedStudentIds.includes(student.id) ? 'primary' : 'default'"
              class="choice"
            >
              {{ selectedStudentIds.includes(student.id) ? '取消' : '选择' }}
            </a-button>
          </div>
        </a-card>
      </div>
      <a-button type="primary" @click="submit" class="submit-button">提交</a-button>
      <p v-if="selectedStudentIds.length > 0" class="submission-message">已选择的学生：{{ selectedNames }}</p>
      <a-alert v-if="submitted" type="success" message="提交成功" show-icon />
    </div>
  </TeacherLayOut>
</template>

<style scoped>
.container {
  display: flex;
  flex-direction: column;
  align-items: center;
  width: 100%;
}

.student-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  grid-gap: 20px;
  width: 100%;
  max-width: 1200px;
}

.student-card {
  display: flex;
  justify-content: space-around;
  align-items: center;
}

.student-info {
  display: flex;
  gap: 20px;
  align-items: center;
}

.student-details {
  display: flex;
  flex-direction: column;
  font-size: 20px;
  gap: 10px;
}

.avatar {
  width: 100px;
  height: 100px;
  border-radius: 50%;
}

.submit-button {
  margin-top: 20px;
  font-size: 18px;
  padding: 10px 20px;
}

.submission-message {
  margin-top: 20px;
  font-size: 18px;
  font-weight: bold;
}
</style>
