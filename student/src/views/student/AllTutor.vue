<script>
import {defineComponent} from "vue";


import StudentLayOut from "@/components/StudentLayOut.vue";
import PersonInfo from "@/components/PersonInfo.vue";


export default defineComponent({
    name: "AllTutor",
    components: { 
      StudentLayOut ,
      PersonInfo
    },
    data() {
    return {
      persons: [
        { name: "耀耀", gender: "男", research: "AI", tutor_id: '2019416199' },
        { name: "萍萍", gender: "女", research: "Machine", tutor_id: '2019416199'},
        { name: "花花", gender: "女", research: "sing", tutor_id: '2019416199' },
        { name: "张三", gender: "男", research: "Coding", tutor_id: '2019416199' },
        { name: "张三", gender: "男", research: "Coding", tutor_id: '2019416199' },
        // 添加更多人员信息...
      ],
    };
  },
    

});
</script>

<template>
  <div class="container">
    <StudentLayOut>
      <div class="person-info-wrapper">
        <div v-for="(person, index) in persons" :key="index" class="person-info-item">
          <PersonInfo :name="person.name" :gender="person.gender" :research="person.research" :tutor_id="person.tutor_id" />
        </div>
      </div>
    </StudentLayOut>
  </div>
</template>


<style scoped>
.container {
  display: flex;
  justify-content: center;
}

.person-info-wrapper {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
}

.person-info-item {
  flex-basis: 33.33%;
  margin: 10px;
}
</style>

