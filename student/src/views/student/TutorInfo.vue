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
    const tutor = reactive({});
    let shift = {
      'man' :'男',
      'women': '女',
    }
    $.ajax({
      url: 'http://8.130.65.99:8002/student/get_tutor_info/',
      type: 'POST',
      data: {
        tutor_id: tutor_id,
      },
    
      success(resp) {
        if (resp.result === 'success') {
          tutor.username = resp.date.username;
          tutor.gender = shift[resp.date.gender];
          tutor.id = resp.date.id;
          tutor.date_of_birth = resp.date.date_of_birth;
          tutor.college = resp.date.college;
          tutor.email = resp.date.email;
          tutor.phone = resp.date.phone;
          tutor.photo = "http://8.130.65.99:8002" + resp.date.photo; // 添加头像
          tutor.research_area = resp.date.research_area;

        }
      },
      error(resp) {
        console.log(resp);
      }
    })
    // console.log(tutor.value);
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

      <div class="title">
          <div class="avatar-wrapper">
            <img :src="tutor.photo" alt="" class="avatar" />
          </div>
          <div class="title">导师信息</div>
        </div>
    <!-- <div class="avatar-wrapper">
      <img :src="tutor.photo" alt="导师头像" class="avatar" />
    </div> -->

    <a-descriptions bordered layout="vertical">
      <a-descriptions-item label="姓名">{{ tutor.username }}</a-descriptions-item>
      <a-descriptions-item label="性别">{{ tutor.gender }}</a-descriptions-item>
      <!-- <a-descriptions-item label="工号">{{ tutor.id }}</a-descriptions-item> -->
      <a-descriptions-item label="出生日期">{{ tutor.date_of_birth }}</a-descriptions-item>
      <a-descriptions-item label="学院">{{ tutor.college }}</a-descriptions-item>
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
  margin: 50px auto auto;
}
.info-card {
  width: 80%;
  margin: 50px auto auto;
  padding: 30px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.15);
}

.title {
  text-align: center;
  font-size: 24px;
  font-weight: bold;
  margin-bottom: 30px;
}

.avatar-wrapper {
  text-align: left;
  margin-bottom: 20px;
}

.avatar {
  width: 120px;
  height: 120px;
  border-radius: 50%;
}

.info-title {
  margin-left: 10px;
}

a-descriptions {
  margin-top: 30px;
}

a-descriptions-item {
  margin-bottom: 20px;
}

</style>






