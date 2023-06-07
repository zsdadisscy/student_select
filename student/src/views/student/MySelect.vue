
<template>
  <div class="container">
    <StudentLayOut>
      <div class="content-wrapper">
        <div v-for="student in students" :key="student.id" class="student">
          <div class="student-info">
            <img :src="student.avatar" alt="Student Avatar" class="avatar" />
            <span class="name">{{ student.name }}</span>
          </div>
          <input
            type="checkbox"
            :id="student.id"
            :value="student.id"
            v-model="selectedStudentIds"
          />
          <label :for="student.id">选择</label>
        </div>
        <div v-if="selectedStudentIds.length > 0" class="selected-student">
          你选择的学生是: {{ getSelectedStudentNames() }}
        </div>
        <button v-if="!submitted" @click="submit" class="submit-button">提交</button>
        <div v-if="submitted" class="submission-message">你已经提交过选择了</div>
      </div>
    </StudentLayOut>
  </div>
</template>

<script>
import { defineComponent } from 'vue';
import StudentLayOut from "@/components/StudentLayOut.vue";

// Import images
import student1 from '@/assets/student_photo.png';
import student2 from '@/assets/student_photo.png';
import student3 from '@/assets/student_photo.png';

export default defineComponent({
  name: 'MySelect',
  components: {
    StudentLayOut,
  },
  data() {
    return {
      students: [
        { id: 1, name: '张三', avatar: student1 },
        { id: 2, name: '李四', avatar: student2 },
        { id: 3, name: '王五', avatar: student3 },
        // 添加更多学生...
      ],
      selectedStudentIds: [],
      submitted: false,
    };
  },
  methods: {
    getSelectedStudentNames() {
      return this.students.filter((s) => this.selectedStudentIds.includes(s.id)).map((s) => s.name).join(', ');
    },
    submit() {
      if (!this.submitted && this.selectedStudentIds.length > 0) {
        // 提交逻辑，可以在这里处理提交的数据
        console.log('提交的学生ID：', this.selectedStudentIds);
        this.submitted = true;
      }
    },
  },
});
</script>


<style scoped>
.container {
  display: flex;
  justify-content: center;
  align-items: center;
}

.content-wrapper {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  text-align: center;
}

.tutor {
  display: flex;
  align-items: center;
  margin-bottom: 20px;
}

.tutor-info {
  display: flex;
  align-items: center;
  margin-right: 30px;
}

.avatar {
  width: 80px;
  height: 80px;
  border-radius: 50%;
  margin-right: 20px;
}

.name {
  font-weight: bold;
  font-size: 18px;
}

input[type='radio'] {
  margin-right: 10px;
  transform: scale(1.3);
}

label {
  font-size: 18px;
}

.selected-tutor {
  margin-top: 30px;
  font-weight: bold;
  font-size: 18px;
}

.submit-button {
  margin-top: 20px;
  font-size: 18px;
  padding: 10px 20px;
}

.submission-message {
  color: red;
  margin-top: 20px;
  font-size: 18px;
  font-weight: bold;
}
</style>

