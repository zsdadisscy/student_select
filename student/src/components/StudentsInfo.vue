<template>
    <div style="background: #ececec; padding: 30px">
      <a-card :title="name" :bordered="false" style="width: 300px"  class="custom-card">
        <img :src="avatar" style="position: absolute; top: 5px; right: 15px; width: 50px; height: 50px;">
        <!-- <p>姓名：{{ name }}</p> -->
        <p>类型：{{ type }}</p>
        <p>性别：{{ gender }}</p>
        <p>年龄：{{ age }}</p>
        <p>出生日期：{{ birth }}</p>
        <p>学号：{{ student_id }}</p>
        <p>邮箱：{{ email }}</p>
        <p>手机号：{{ phone }}</p>
        <p>个人介绍：{{ introduction }}</p>
      </a-card>
    </div>
  </template>

<script>

export default ({
    name: "StudentsInfo",
    props: {
        name: {
            type: String,
            default: "default"
        },
        gender: {
            type: String,
            default: "default"
        },
        birth: {
            type: String,
            default: "default"
        },
        age: {
            type: String,
            default: "default"
        },
        
        type: {
            type: String,
            default: "default"
        },
        introduction: {
            type: String,
            default: "default"
        },
        student_id: {
            type: String,
            default: 'default',
        },
        email: {
            type: String,
            default: 'default',
        },
        phone: {
            type: String,
            default: 'default',
        },
        avatar: {
            type: String,
            default: require('@/assets/student_photo.png')
        }
        


    },

})
</script>

<style scoped>
.custom-card .ant-card-head-title {
  font-size: 20px;  /* Change the font size to your preferred value */
  font-weight: bold; /* Makes the font bold */
}
</style>