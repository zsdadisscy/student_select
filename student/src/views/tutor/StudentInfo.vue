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
        if (resp.result === 'success') {
            for (const student_id of resp.data) {
              $.ajax({
                url: 'http://8.130.65.99:8002/tutor/get_student_info/',
                type: 'POST',
                data: {
                  user: ModuleTutor.state.user,
                  student_id: student_id,
                },
                success: (resp) => {
                  if (resp.result === 'success') {
                    students.value.push(resp.data);
                  } 
                },
              });
              
          }
          students.value = resp.data;
          // console.log("123",students, students.value);
          console.log("123", students.value)
        }
      },
      error: (err) => {
        console.error('Error fetching students: ', err);
      },
    
    });
    return {
      students,
      // calculateAge,
    };
   },
});
</script>

<template>
  <div>
    <TeacherLayOut>   
      <div class="grid-container">
        <div>csd</div>
         <div v-for="student in students" :key="student.id" class="person-info-item">
          <div>fcwe</div>
          <StudentsInfo

            :gender="student.gender"
            :type="student.student_type"
            :birth="student.date_of_birth"
            :student_id="student.id"
            :email="student.email"
            :phone="student.phone"
            :introduction="student.bio"
          />
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
