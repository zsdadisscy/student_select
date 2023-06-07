<script>
import {defineComponent, reactive} from "vue";
import $ from 'jquery';
import { useRoute } from 'vue-router'; 
import StudentLayOut from "@/components/StudentLayOut.vue";

export default defineComponent({
  name: 'LookTutorInfo',
  components: {
    StudentLayOut,
  },
  setup() {
    const route = useRoute();
    const tutor_id  = route.params.tutor_id;
    const tutor = reactive([]);
    $.ajax({
      url: 'http://8.130.65.99:8002/student/get_tutor_info/',
      type: 'POST',
      data: {
        tutor_id: tutor_id,
      },
      success(resp) {
        if (resp.result === 'success') {
          tutor.value = resp.date;
          console.log(tutor.value);
        }
      },
      error(resp) {
        console.log(resp);
      }
    })
    console.log(tutor.value);
   return {
      tutor
   }
  },

});
</script>

<template>
<div>
  <StudentLayOut>
    <a-card class="info-card">
    <div class="title">导师信息</div>
    <a-descriptions bordered layout="vertical">
      <a-descriptions-item label="姓名">{{ tutor.username }}</a-descriptions-item>
      <a-descriptions-item label="性别">{{ tutor.gender }}</a-descriptions-item>
      <a-descriptions-item label="工号">{{ tutor.id }}</a-descriptions-item>
      <a-descriptions-item label="出生日期">{{ tutor.date_of_birth }}</a-descriptions-item>
      <a-descriptions-item label="学院">{{ tutor.collage }}</a-descriptions-item>
      <a-descriptions-item label="邮箱">{{ tutor.email }}</a-descriptions-item>
      <a-descriptions-item label="手机号">{{  tutor.phone }}</a-descriptions-item>
      <a-descriptions-item label="研究方向">{{ tutor.research_area }}</a-descriptions-item>

    </a-descriptions>
  </a-card>
  </StudentLayOut>
  
</div>
</template>

<style scoped>
.info-card {
  width: 50%;
  margin: auto;
  margin-top: 50px;
}
.info-card {
  width: 80%;
  margin: auto;
  margin-top: 50px;
  padding: 30px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.15);
}

.title {
  text-align: center;
  font-size: 24px;
  font-weight: bold;
  margin-bottom: 30px;
}

</style>