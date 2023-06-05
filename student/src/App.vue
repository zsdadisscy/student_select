<template>
  <LoginView />
<!--  <div class="top">-->
<!--    <p class="StudentPage">StudentPage</p>-->
<!--    <p class="selectedMenu">{{ selectedMenuItem }}</p>-->
<!--    <div class="right">-->
<!--      <StudentsHead />-->
<!--      <p class="yourName">your name</p>-->
<!--    </div>-->
<!--  </div>-->
<!--  <div class="container">-->
<!--    <div class="sidebar">-->
<!--      <NavStudents @selectComponent="selectComponent"  @selectMenuItem="selectMenuItem" />-->
<!--    </div>-->
<!--    <div class="content">-->

<!--      <component :is="currentComponent" v-model:selectedTutors="selectedTutors" :addSelectedTutor="addSelectedTutor" />-->
<!--      -->
<!--    </div>-->
<!--  </div>-->
</template>


<script>
// import StudentsHead from './components/StudentsHead.vue'
// import NavStudents from './components/NavStudents.vue'
// import StudentsInfo from './components/StudentsInfo.vue'
// import TutorInfo from './components/TutorInfo.vue'
// import SelectedTutor from './components/SelectedTutor.vue'
// import EditInfo from './components/EditInfo.vue'
import LoginView from './views/LoginView.vue';


export default {
    name: 'App',
    data() {
      return {
        // selectedTutors: [], // 初始化为空数组
        // currentComponent: TutorInfo,
        // selectedMenuItem: '选择您的导师' // 存储选中的菜单项名称
      }
    },
    components: {
      // NavStudents,
      // StudentsInfo,
      // StudentsHead,
      // TutorInfo,
      // SelectedTutor,
      // EditInfo,
      LoginView,
    },
    methods: {
      selectComponent(component) {
      this.currentComponent = component;
    },
    selectMenuItem(menuItem) {
      this.selectedMenuItem = menuItem;
    },

  }
}
</script>

<style>
.top {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 80px;
  background-color: rgb(24,116,205);
  display: flex;
  justify-content: space-between;
  align-items: center;
  z-index: 9999; /* 设置一个较高的 z-index 值以确保顶部栏位于最上层 */
}

.container {
  display: flex;
  flex-direction: row;
  margin-top: 80px; /* 将容器的上边距设为顶部栏的高度，以避免内容被遮挡 */
}

.sidebar {
  position: fixed; /* 固定位置 */
  top: 80px;
  bottom: 0;
  left: 0;
  width: 256px; /* 设置固定宽度 */
  background-color: rgb(0, 21, 41);

}


.content {
  flex-grow: 1;
  display: flex;
  /* justify-content: center; 居中显示内容 */
  /* align-items: center; */
  margin-top: 50px;
  margin-left: 450px;
}
.top .StudentPage,
.top .selectedMenu {
  font-size: 20px;
  font-weight: bold;
  color: white;
}
.StudentPage {
  margin-left: 20px;
}

.selectedMenu {
  font-size: 18px;
  text-align: center;
  /* flex-grow: 1; */
}
.right {
  margin-right: 50px;
}
.yourName {
  display: inline-block;
  margin-right: 10px;
  margin-left: 10px;
  color: white;
  font-size: 16px;
}

.studentsHead {
  display: inline-block;
}
</style>




