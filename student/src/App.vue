<template>
  <div class="top">
      <p>StudentPage</p>
  </div>
  <div class="container">
    <div class="sidebar">
      <NavStudents />
    </div>
    <div class="content">
      <StudentsInfo />
    </div>
  </div>

</template>

<script>
import NavStudents from './components/NavStudents.vue'
import StudentsInfo from './components/StudentsInfo.vue'
export default {
    name: 'App',
    components: {
      NavStudents,
      StudentsInfo,
    }
  }
</script>

<style>
  .top {
    width: 100%;
    height: 80px;
    background-color: rgb(0,21,41);
  }
  .top p {
    font-size: 20;
    font-weight: bold;
    line-height: 80px;
    text-align: center;
    color: white;
  }
  .container {
    display: flex;
    flex-direction: row;
    /* justify-content: first center; */
  }
  .content {
  flex-grow: 1;
  display: flex;
  /* justify-content: center; */
  /* align-items: center; */
  margin-top: 50px;
  margin-left: 200px;
}
</style>




