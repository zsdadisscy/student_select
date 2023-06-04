<template>
  <div>
    <div class="card-container">
      <div class="card-row">
        <a-card v-for="tutor in tutors" :key="tutor.id" :title="tutor.name" class="card" bordered>
          <!-- <template #extra><a href="#">more</a></template> -->
          <template #extra>
            <div class="avatar">
              <img :src="tutor.avatar" alt="..../media/tutor_photo/tutor_photo.png" />
            </div>
          </template>
          <p>性别：{{ tutor.gender }}</p>
          <p>邮箱：{{ tutor.email }}</p>
          <p>招生人数：{{ tutor.num }}</p>
          <p>目前招生人数：{{ tutor.nowNum }}</p>
          <p>研究方向：{{ tutor.research }}</p>
          <p>简介：{{ tutor.info }}</p>
          <div class="card-buttons">
            <a-button v-if="!tutor.selected" type="primary" @click="selectTutor(tutor)">
              选择
            </a-button>
            <a-button v-else type="default" disabled>
              不可选
            </a-button>
          </div>
        </a-card>
      </div>
    </div>
    <div class="submit-container">
      <a-button :disabled="selectedTutor === null" @click="submitTutor" class="submit">
        提交
      </a-button>
    </div>
  </div>
</template>

<script>
export default {
  name: 'TutorInfo',
  props: {
    addSelectedTutor: {
      type: Function,
      required: true
    },
  },
  data() {
    return {
      tutors: [
        // 导师数据...
        {
          id: 1,
          name: '明敏',
          gender: '女',
          email: '12345@qq.com',
          num: '10',
          nowNum: '2',
          research: 'Machine Learning',
          info: '帅气阳光',
          avatar: '../media/tutor_photo.png',
          selected: false
        },
        {
          id: 2,
          name: '强国',
          gender: '男',
          email: '123445@qq.com',
          num: '10',
          nowNum: '5',
          research: 'Machine Learning',
          info: '温柔体贴',
          avatar: '../media/tutor_photo.png',
          selected: false
        },
        {
          id: 3,
          name: '明明',
          gender: '男',
          email: '12334@qq.com',
          num: '10',
          nowNum: '8',
          research: 'Machine Learning',
          info: '帅气阳光',
          avatar: '../media/tutor_photo.png',
          selected: false
        }
      ],
      selectedTutor: null
    };
  },
  methods: {
    selectTutor(tutor) {
      this.tutors.forEach((t) => {
        if (t !== tutor) {
          t.selected = false;
        }
      });
      tutor.selected = true;
      this.selectedTutor = tutor;
    },
    submitTutor() {
      console.log(this.selectedTutor.id);
      // 执行提交逻辑
    },
    selectComponent(component) {
      this.$emit('selectComponent', component);
    },
    selectMenuItem(menuItem) {
      this.$emit('selectMenuItem', menuItem);
    }
  }
};
</script>

<style>
.card-container {
  display: flex;
  flex-wrap: wrap;
  justify-content: space-between;
}

.card-row {
  display: flex;
  flex-wrap: wrap;
  justify-content: space-between;
  flex-direction: row;
  margin-bottom: 20px;
}

.card {
  width: calc(50% - 10px);
  margin-bottom: 20px;
  border-color: black;
}

.ant-card-head-title {
  font-size: 18px;
  font-weight: bold;
}

.avatar {
  width: 30px;
  height: 30px;
  border-radius: 50%;
  overflow: hidden;
}

.avatar img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.card-buttons {
  display: flex;
  justify-content: space-between;
  margin-top: 10px;
}

.submit-container {
  display: flex;
  justify-content: center;
  margin-top: 20px;
}

.submit {
  width: 100px;
  font-size: 16px;
  font-weight: bold;
}
</style>
