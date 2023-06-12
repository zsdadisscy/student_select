<script>
import { defineComponent, ref } from 'vue';
import TeacherLayOut from '@/components/TeacherLayOut.vue';
import $ from 'jquery';
import ModuleTutor from '@/store/tutor';

export default defineComponent({
  name: 'MyStudent',
  components: {
    TeacherLayOut,
  },
  data() {
    let students = ref([]);
    let loading = ref(true);
    let student = ref({});

    // 第一步：从get_select_student接口获取学生ID
    $.ajax({
      url: 'http://8.130.65.99:8002/tutor/get_my_student/',
      type: 'GET',
      data: {
        user: ModuleTutor.state.user,
      },
      success: function(response) {
        if (response.result === 'success' && response.data) {
          // console.log("进来了");
          let studentIds = response.data.map(student => student.id);
          // console.log(studentIds);

          // 针对每个学生ID，我们将进行第二步的操作
          for (let i = 0; i < studentIds.length; i++) {
            let studentId = studentIds[i];
            // 第二步：使用学生ID从get_student_info接口获取学生信息
            $.ajax({
              url: 'http://8.130.65.99:8002/tutor/get_student_info/',
              type: 'POST',
              data: {
                user: ModuleTutor.state.user,
                student_id: studentId,
              },
              success: function(res) {
                if (res.result === 'success') {
                  if (res.date != null && typeof res.date === 'object' && Object.prototype.hasOwnProperty.call(res.date, 'id')) {
                    // 将学生信息添加到students数组
                    students.value.push(res.date);
                    // console.log("res", res.date);
                  } else {
                    console.log('Invalid data: ', res.data);
                  }
                }
              },
            });
          }
        }
      },
      error: function(err) {
        console.log(err);
      },
      complete: function() {
        loading.value = false; // 请求完成后设置loading为false
      },
    });

    return {
      students,
      loading,
      student, 
    };
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
      <a-card class="student-card" :loading="loading" v-for="student in students" :key="student.id">
        <template #title>
          <a-avatar :src=" 'http://8.130.65.99:8002/' + student.photo" size="large"  />
          <div class="student-title">
            <h2>{{ student && student.username }}</h2>
            <!-- <p>{{ student && student.student_type }}</p> -->
          </div>
        </template>

        <a-descriptions bordered >
          <a-descriptions-item label="姓名">{{ student && student.username }}</a-descriptions-item>
          <a-descriptions-item label="性别">{{ student && getGenderLabel(student.gender)}}</a-descriptions-item>
          <!-- <a-descriptions-item label="年龄">{{ student && student.age }}</a-descriptions-item> -->
          <a-descriptions-item label="出生日期">{{ student && student.date_of_birth }}</a-descriptions-item>
          <a-descriptions-item label="学号">{{ student && student.id }}</a-descriptions-item>
          <a-descriptions-item label="学院">{{ student && student.college }}</a-descriptions-item>
          <a-descriptions-item label="邮箱">{{ student && student.email }}</a-descriptions-item>
          <a-descriptions-item label="手机号">{{ student && student.phone }}</a-descriptions-item>
          <a-descriptions-item label="个人介绍">{{ student && student.bio }}</a-descriptions-item>
        </a-descriptions>
      </a-card>
    </TeacherLayOut>
  </div>
</template>



<style scoped>
.student-card {
  width: 600px;
  margin: auto;
}

.student-title {
  display: inline-block;
  vertical-align: top;
  margin-left: 20px;
}
</style>
