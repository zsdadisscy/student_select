<template>
  <div class="container">
    <StudentLayOut>
      <div class="content-wrapper">
        <div v-for="tutor in tutors" :key="tutor.id" class="student">
          <div class="student-info">
            <img :src="'http://8.130.65.99:8002' + tutor.photo" alt="tutor Avatar" class="avatar" />
            <span class="name">姓名：{{ tutor.username }}</span>
          </div>
          <input
            type="radio"
            :id="tutor.id"
            :value="tutor.id"
            v-model="selectedTutorId"
          />
          <label :for="tutor.id">选择</label>
        </div>
        <div v-if="selectedTutorId" class="selected-student">
          你选择的导师是: {{ getSelectedTutorName() }}
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
import $ from 'jquery';
import ModuleStudent from '@/store/student';

export default defineComponent({
  name: 'MySelect',
  components: {
    StudentLayOut,
  },
  data() {
    return {
      tutors: [],
      selectedTutorId: null,
      submitted: false,
    };
  },
  created() {
    this.fetchTutors();
  },
  methods: {
    fetchTutors() {
      $.ajax({
        url: 'http://8.130.65.99:8002/student/get_tutor',
        type: 'GET',
        data: {
          user: ModuleStudent.state.user,
        },
        success: (resp) => {
          if (resp.result === 'success') {
            this.tutors = resp.data;
            console.log(this.tutors);
          }
        },
        error: (err) => {
          console.error('Error fetching tutors: ', err);
        },
      });
    },
    getSelectedTutorName() {
      const selectedTutor = this.tutors.find(tutor => tutor.id === this.selectedTutorId);
      return selectedTutor ? selectedTutor.username : '';
    },
    submit() {
      console.log('User:', ModuleStudent.state.user);
      console.log('Selected Tutors IDs:', this.selectedTutorsIds); // No need for .value
      if (!this.submitted && this.selectedTutorsIds.length > 0) {
        // Submit logic
        console.log(this.selectedTutorsIds, this.selectedTutorsIds[0]);
        $.ajax({
          url: 'http://8.130.65.99:8002/student/select_tutor/',
          type: 'POST',
          data: {
            tutor_id: this.selectedTutorsIds[0], // Use the array directly
            user: ModuleStudent.state.user,
          },
          success: (response) => {
            console.log('Successfully submitted tutor selection', response);
            this.submitted = true;
          },
          error: (err) => {
            console.error('Error submitting tutor selection: ', err);
          },
        });
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

.student {
  display: flex;
  align-items: center;
  margin-bottom: 20px;
}

.student-info {
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

.selected-student {
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
