
<script>
import {defineComponent, ref} from "vue";
import TeacherLayOut from "@/components/TeacherLayOut.vue";
import { Card, Button, Alert } from 'ant-design-vue';

import $ from 'jquery';
import ModuleTutor from '@/store/tutor'


export default defineComponent({
  name: 'SelectStudent',
  components: {
    TeacherLayOut,
    'a-card': Card,
    'a-button': Button,
    'a-alert': Alert,
  },
  data() {
    let students =  ref([]);
    // console.log(students.value.length);
    $.ajax({
          url: 'http://8.130.65.99:8002/tutor/get_select_student',
          type: 'GET',
          data: {
            user: ModuleTutor.state.user,
          },
          success(resp) {
            if (resp.result === 'success') {
              console.log(resp);
              // students.value = resp.data;
              students.value = resp.data; // 直接赋值给students数组
              // console.log(typeof(students.value));
              // console.log(students.value.length);
            }

          },
          error: (err) => {
            console.error('Error fetching students: ', err);
          },
    });
    
    return {
      students,
      selectedStudentsIds: [],
      submitted: false,
    }
  },

  methods: {
    getSelectedStudentsNames() {
      return this.students.value.filter((s) => this.selectedStudentsIds.includes(s.id)).map((s) => s.username).join(', ');
    },

    submit() {
      if (!this.submitted && this.selectedStudentsIds.length > 0) {
        // 提交逻辑，可以在这里处理提交的数据
        $.ajax({
          
          url: 'http://8.130.65.99:8002/student/processing_application/',
          type: 'POST',
          data: {
            user: ModuleTutor.state.user,
            selectedStudentsIds: this.selectedStudentsIds
          },
          success: (response) => {
            console.log('成功提交学生选择', response);
            this.submitted = true;
          },
          error: (err) => {
            console.error('提交学生选择出错：', err);
          },

        });

      }
    },
    log(message) {
      console.log(message.value);
      console.log(message.length);
    }
  },
});
</script>

<template>
  <TeacherLayOut>
    <div class="container">
      <div  v-if="students && students.length" class="student-grid">
        <a-card
          v-for="student in students" 
          :key="student.id"
          class="student-card"
        >
          <div class="student-info">
            <img :src="`@/assets/student_photo.png`" alt="Student Avatar" class="avatar" />

            <div class="student-details">
       
              <p><b>姓名：</b>{{ student.username }}</p>
            </div>
            <a-button 
              @click="toggleSelection(student.id)"
              :type="selectedStudentsIds.includes(student.id) ? 'primary' : 'default'"
              class="choice"
            >
              {{ selectedStudentsIds.includes(student.id) ? '取消' : '选择' }}
            </a-button>
          </div>
        </a-card>
      </div>
      <a-button type="primary" @click="submit" class="submit-button">提交</a-button>
      <p v-if="selectedStudentsIds.length > 0" class="submission-message">已选择的学生：{{ selectedNames }}</p>
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
