<script>
import {defineComponent, ref} from "vue";
import TeacherLayOut from "@/components/TeacherLayOut.vue";
import StudentsInfo from "@/components/StudentsInfo.vue"
import $ from 'jquery';
import ModuleTutor from "@/store/tutor";

export default defineComponent({
  name: 'LookStudentInfo',
  components: {
    TeacherLayOut,
    StudentsInfo
  },

      
    data() {
      let students = ref([]);

      $.ajax({
        url: 'http://8.130.65.99:8002/tutor/get_select_student/',
        type: 'GET',
        data: {
          user: ModuleTutor.state.user,
        },
        success(resp) {
          console.log(resp);
          // if(resp.result === 'success') {
          //   student.username = resp.date.username;
          //   student.date_of_birth = resp.date.data_of_birth;
          //   student.bio = resp.date.bio;
          //   student. email = resp.date.email;
          //   student.photo = "http://8.130.65.99:8002" + resp.date.photo;
          //   student.collage = resp.date.collage;
          //   student.id = resp.date.id;
          //   student.gender = resp.date.gender;
          //   student.id = resp.date.id;
          //   student.student_type = resp.date.student_type;
          // }
          if (resp.result === 'success') {
              students.value = resp.date;
              console.log(students.value);
          }
        }
    })
  
   return {
      students,
      // calculateAge,
   }
  },
});
</script>

<template>
  <div>
    <TeacherLayOut>   
      <div class="grid-container">
         <div v-for="student in students" :key="student.id" class="person-info-item">
          <!-- <StudentsInfo
            :name="student.username"
            :gender="student.gender"
            :type="student.student_type"

            :birth="student.date_of_birth"
            :student_id="student.id"
            :email="student.email"
            :phone="student.phone"
            :introduction="student.bio"
          /> -->
          <StudentsInfo
            :name="student.username"

          />
        </div>
      </div>
    </TeacherLayOut>
  </div>
</template>

<style scoped>
.grid-container {
  display: flex;
  flex-wrap: wrap;
  justify-content: space-between;
}
.grid-container .person-info-item {
  flex: 1 0 calc(33.33% - 1rem);
  margin: 0.5rem;
}
</style>
