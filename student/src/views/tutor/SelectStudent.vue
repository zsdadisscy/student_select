
<script>
import {defineComponent, ref} from "vue";
import TeacherLayOut from "@/components/TeacherLayOut.vue";
import { Card, Button} from 'ant-design-vue';

import $ from 'jquery';
import ModuleTutor from '@/store/tutor'


export default defineComponent({
  name: 'SelectStudent',
  components: {
    TeacherLayOut,
    'a-card': Card,
    'a-button': Button,
    // 'a-alert': Alert,
  },
  data() {
    let students =  ref([]);
    let alertMessage = ref('');
    // console.log(students.value.length);
    $.ajax({
          url: 'http://8.130.65.99:8002/tutor/get_select_student',
          type: 'GET',
          data: {
            user: ModuleTutor.state.user,
          },
          success(resp) {
            if (resp.result === 'success') {
              console.log("修改",resp);
            
              students.value = resp.data; // 直接赋值给students数组

            }

          },
          error: (err) => {
            console.error('Error fetching students: ', err);
          },
    });
    
    return {
      students,
      alertMessage,
      selectedStudentsIds: [],
      submitted: false,
    }
  },

  methods: {
    getSelectedStudentsNames() {
      return this.students.value.filter((s) => this.selectedStudentsIds.includes(s.id)).map((s) => s.username).join(', ');
    },

    processApplication(studentId, studentName, decision){
      console.log(decision);
        // 提交逻辑，可以在这里处理提交的数据
        $.ajax({
          
          url: 'http://8.130.65.99:8002/tutor/processing_application/',
          type: 'POST',
          data: {
            student_id: studentId,
            processing: decision,
            user: ModuleTutor.state.user,
          },
          success: (response) => {
            console.log(response);
            if (response.result === 'success') {
              console.log('成功处理学生申请', response);
              this.alertMessage = `您${decision}了${studentName}的申请`;
              // 你可以在这里添加代码，更新你的students数组
              if (this.students.value) {
                let student = this.students.value.find((s) => s.id === studentId);
                // ...
                if (student) student.processed = true;  // 标记为已处理
              }
              
            }
          },
          error: (err) => {
            console.error('提交学生选择出错：', err);
          },
        });
    },

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
            <img src="@/assets/student_photo.png" alt="Student Avatar" class="avatar" />

            <div class="student-details">
       
              <p>姓名：{{ student.student_name }}</p>
              <p>学号：{{ student.student_id }}</p>
            </div>
            <a-button 
            @click="processApplication(student.student_id, student.student_name, '通过')"
            type="primary"
            class="choice"
            :disabled="student.processed"
            >
             通过
            </a-button>

            <a-button 
              @click="processApplication(student.student_id, student.student_name, '拒绝')"
              type="danger"
              class="choice"
              :disabled="student.processed" 
            >
              拒绝
            </a-button>

          </div>
        </a-card>
      </div>
      <!-- <a-button type="primary" @click="submit" class="submit-button">提交</a-button> -->
      <p>{{ alertMessage }}</p> 
      <!-- <a-alert v-if="submitted" type="success" message="提交成功" show-icon /> -->
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
  font-size: 18px;
  gap: 10px;
}

.avatar {
  width: 100px;
  height: 100px;
  border-radius: 50%;
}

.submit-button {
  margin-top: 30px;
  font-size: 18px;
  padding: 10px 18px;
}

.submission-message {
  margin-top: 20px;
  font-size: 18px;
  font-weight: bold;
}
</style>
