<script>
import {defineComponent, ref} from "vue";
import $ from 'jquery';

import StudentLayOut from "@/components/StudentLayOut.vue";
import TutorsInfo from "@/components/TutorsInfo.vue";
import ModuleStudent from "@/store/student";

export default defineComponent({
    name: "AllTutor",
    components: { 
      StudentLayOut ,
      TutorsInfo
    },
    data() {
      let persons = ref([]);
      $.ajax({
        url: "http://8.130.65.99:8002/student/get_tutor/",
        type: "GET",
        data: {
          user: ModuleStudent.state.user,
        },
        success(resp) {
          if (resp.result === 'success') {
              persons.value = resp.data;
              console.log(persons.value);
          }
        }
      })
    return {
        persons
    };
  },
    

});
</script>

<template>
  <div class="container">
    <StudentLayOut>
      <div class="person-info-wrapper">
        <div v-for="person in persons" :key="person.id" class="person-info-item">
          <TutorsInfo :name="person.username" :gender="person.gender" :type="person.college" :research="person.research_area" :tutor_id="person.id" />
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

