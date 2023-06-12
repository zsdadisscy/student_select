<script>
import {defineComponent, reactive} from "vue";
import StudentLayOut from "@/components/StudentLayOut.vue";
import ModuleStudent from '@/store/student';
import $ from 'jquery';

export default defineComponent({
  name: 'MyTutor',
  components: {
    StudentLayOut,
  },
  setup() {
    let tutor = reactive({});
    $.ajax({
      url: 'http://8.130.65.99:8002/student/get_my_tutor/',
      data: {
          user: ModuleStudent.state.user,
      },
      success(resp) {
        if (resp.result === 'success') {
          // console.log(resp);
          $.ajax({
            url: 'http://8.130.65.99:8002/student/get_tutor_info/',
            type: 'POST',
            data: {
              tutor_id: resp.data.tutor_id,
            },
            success(resp) {
              if (resp.result === 'success') {
                tutor.username = resp.date.username;
                tutor.gender = resp.date.gender;
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
      }
    }
    });
    return {
      tutor,
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
<div class="container">
  <StudentLayOut>
    <a-card class="info-card">
      <div class="title">我的导师</div>
      <a-descriptions bordered layout="vertical">
        <a-descriptions-item label="姓名">{{ tutor.username }}</a-descriptions-item>
        <a-descriptions-item label="性别">{{ getGenderLabel(tutor.gender) }}</a-descriptions-item>
        <a-descriptions-item label="工号">{{ tutor.id }}</a-descriptions-item>
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




