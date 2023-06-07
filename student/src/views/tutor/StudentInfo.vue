<script>
import {defineComponent} from "vue";
import TeacherLayOut from "@/components/TeacherLayOut.vue";
import StudentsInfo from "@/components/StudentsInfo.vue"

export default defineComponent({
  name: 'LookStudentInfo',
  components: {
    TeacherLayOut,
    StudentsInfo
  },
  data() {
    return {
      persons: [
        { name: "耀耀", gender: "男",type:"学硕", age:"20", birth:"2001-05-21",student_id: '2019416199',email:"245892@qq.com",phone:"124687654",introduction:"成绩优异" },
        { name: "耀耀", gender: "男",type:"学硕", age:"20", birth:"2001-05-21",student_id: '2019416199',email:"245892@qq.com",phone:"124687654",introduction:"成绩优异" },
        { name: "耀耀", gender: "男",type:"学硕", age:"20", birth:"2001-05-21",student_id: '2019416199',email:"245892@qq.com",phone:"124687654",introduction:"成绩优异" },
        { name: "耀耀", gender: "男",type:"学硕", age:"20", birth:"2001-05-21",student_id: '2019416199',email:"245892@qq.com",phone:"124687654",introduction:"成绩优异" },
        { name: "耀耀", gender: "男",type:"学硕", age:"20", birth:"2001-05-21",student_id: '2019416199',email:"245892@qq.com",phone:"124687654",introduction:"成绩优异" },

        // 添加更多人员信息...
      ],
    };
  },

});
</script>

<template>
  <div>
    <TeacherLayOut>   
      <div class="grid-container">
        <div v-for="(person, index) in persons" :key="index" class="person-info-item">
          <StudentsInfo 
          :name="person.name" 
          :gender="person.gender" 
          :type="person.type" 
          :age="person.age" 
          :birth="person.birth" 
          :student_id="person.student_id" 
          :email="person.email" 
          :phone="person.phone"
          :introduction="person.introduction"  />
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
