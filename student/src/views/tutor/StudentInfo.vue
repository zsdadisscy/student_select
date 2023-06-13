<script>
import {defineComponent, ref} from "vue";
import TeacherLayOut from "@/components/TeacherLayOut.vue";
import StudentsInfo from "@/components/StudentsInfo.vue"
import $ from 'jquery';
import ModuleTutor from "@/store/tutor";
// import { Module } from "module";

export default defineComponent({
  name: 'LookStudentInfo',
  components: {
    TeacherLayOut,
    StudentsInfo
  },

  data() {

  let students = ref([]);

// 第一步：从get_select_student接口获取学生ID
  $.ajax({
    url: 'http://8.130.65.99:8002/tutor/get_select_student/',
    type: 'GET',
    data: {
      user: ModuleTutor.state.user
    },
    success: function(response) {
      // console.log("123");
      // console.log("respid:",response.data.student_id);
        if (response.result === 'success' && response && response.data) {
            // console.log("进来了");
            let studentIds =  response.data.map(student => student.student_id);
            // console.log(studentIds);
            // console.log("len", studentIds,length);
            // 针对每个学生ID，我们将进行第二步的操作
            for(let i=0; i<studentIds.length; i++){
                let studentId = studentIds[i];
                // 第二步：使用学生ID从get_student_info接口获取学生信息
                $.ajax({
                    url: 'http://8.130.65.99:8002/tutor/get_student_info/',
                    type: 'POST',
                    data: {
                        user: ModuleTutor.state.user,
                        student_id: studentId
                    },
                    success: function(res) {
                      // console.log('Response:', res);
                        if (res.result === 'success') {
                            // console.log("data:",res.data);
                            if (res.date != null && typeof res.date === 'object' && res.date.hasOwnProperty.call(res.date, 'id')) {
                              // 将学生信息添加到students数组
                             
                              students.value.push(res.date);
                              // console.log("成功添加", res.date);
                          } else  console.log('Invalid data: ', res.data)
                        
                    }
                  }
                });
            
          } 
        }
    },
    error: function(err) {
        console.log(err);
    }
  });
  return {
    students,
  }
   },

   
  methods: {
    getGenderLabel(gender) {
      if (gender === 'man') {
        return '男';
      } else if (gender === 'women') {
        return '女';
      } else {
        return gender;
      }
    },
  },
  
   
});
</script>

<template>
  <div>
    <TeacherLayOut>   
      <div class="grid-container">
        <!-- <div>csd</div> -->
         <div v-for="student in students" :key="student.id" class="person-info-item">
          <!-- <div>fcwe</div> -->
          <StudentsInfo
            :name="student.username"
            :gender="getGenderLabel(student.gender)"
            :type="student.student_type"
            :birth="student.date_of_birth"
            :student_id="student.id"
            :email="student.email"
            :phone="student.phone"
            :introduction="student.bio"
            :avatar="'http://8.130.65.99:8002' + student.photo"
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
