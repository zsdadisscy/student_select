<!-- 
<script>
import {defineComponent} from "vue";
import StudentLayOut from "@/components/StudentLayOut.vue";

export default defineComponent({
  name: 'MySelect',
  components: { 
      StudentLayOut ,

    },
 data() {
    return {
      tutors: [
        { id: 1, name: '张三', avatar: 'tutor1.jpg' },
        { id: 2, name: '李四', avatar: 'tutor2.jpg' },
        { id: 3, name: '王五', avatar: 'tutor3.jpg' },
        // 添加更多导师...
      ],
      selectedTutorId: null,
    };
  },
  methods: {
    getSelectedTutorName() {
      const tutor = this.tutors.find((t) => t.id === this.selectedTutorId);
      return tutor ? tutor.name : '';
    },
  },
});
</script>
 <template>
  <div class="container">
    <StudentLayOut>
      <div class="content-wrapper">
        <div v-for="tutor in tutors" :key="tutor.id" class="tutor">
          <div class="tutor-info">
            <img :src="tutor.avatar" alt="Tutor Avatar" class="avatar" />
            <span class="name">{{ tutor.name }}</span>
          </div>
          <input
            type="radio"
            :id="tutor.id"
            :value="tutor.id"
            v-model="selectedTutorId"
          />
          <label :for="tutor.id">选择</label>
        </div>
        <div v-if="selectedTutorId" class="selected-tutor">
          你选择的导师是: {{ getSelectedTutorName() }}
        </div>
      </div>
    </StudentLayOut>
  </div>
</template>

<style scoped>
.container {
  display: flex;
  justify-content: center; /* 水平居中 */
  align-items: center; /* 垂直居中 */
}

.content-wrapper {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  text-align: center;
}


.tutor {
  display: flex;
  align-items: center;
  margin-bottom: 20px;
}

.tutor-info {
  display: flex;
  align-items: center;
  margin-right: 30px;
}

.avatar {
  width: 80px;
  height: 80px;
  border-radius: 50%;
  margin-right: 20px;
}

.name {
  font-weight: bold;
  font-size: 18px;
}

input[type='radio'] {
  margin-right: 10px;
  transform: scale(1.3); /* 放大选择框 */
}

label {
  font-size: 18px;
}

.selected-tutor {
  margin-top: 30px;
  font-weight: bold;
  font-size: 18px;
}
</style>
 -->
 <template>
  <div class="container">
    <StudentLayOut>
      <div class="content-wrapper">
        <div v-for="tutor in tutors" :key="tutor.id" class="tutor">
          <div class="tutor-info">
            <img :src="tutor.avatar" alt="Tutor Avatar" class="avatar" />
            <span class="name">{{ tutor.name }}</span>
          </div>
          <input
            type="radio"
            :id="tutor.id"
            :value="tutor.id"
            v-model="selectedTutorId"
          />
          <label :for="tutor.id">选择</label>
        </div>
        <div v-if="selectedTutorId" class="selected-tutor">
          你选择的导师是: {{ getSelectedTutorName() }}
        </div>
        <button v-if="!submitted" @click="submit" class="submit-button">提交</button>
        <div v-if="submitted" class="submission-message">你已经提交过选择了</div>
      </div>
    </StudentLayOut>
  </div>
</template>

<script>
import { defineComponent} from 'vue';
import StudentLayOut from "@/components/StudentLayOut.vue";

export default defineComponent({
  name: 'MySelect',
  components: {
    StudentLayOut,
  },
  data() {
    return {
      tutors: [
        { id: 1, name: '张三', avatar: 'tutor1.jpg' },
        { id: 2, name: '李四', avatar: 'tutor2.jpg' },
        { id: 3, name: '王五', avatar: 'tutor3.jpg' },
        // 添加更多导师...
      ],
      selectedTutorId: null,
      submitted: false,
    };
  },
  methods: {
    getSelectedTutorName() {
      const tutor = this.tutors.find((t) => t.id === this.selectedTutorId);
      return tutor ? tutor.name : '';
    },
    submit() {
      if (!this.submitted && this.selectedTutorId) {
        // 提交逻辑，可以在这里处理提交的数据
        console.log('提交的导师ID：', this.selectedTutorId);
        this.submitted = true;
      }
    },
  },
});
</script>

<style scoped>
.container {
  display: flex;
  justify-content: center;
  align-items: center;
}

.content-wrapper {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  text-align: center;
}

.tutor {
  display: flex;
  align-items: center;
  margin-bottom: 20px;
}

.tutor-info {
  display: flex;
  align-items: center;
  margin-right: 30px;
}

.avatar {
  width: 80px;
  height: 80px;
  border-radius: 50%;
  margin-right: 20px;
}

.name {
  font-weight: bold;
  font-size: 18px;
}

input[type='radio'] {
  margin-right: 10px;
  transform: scale(1.3);
}

label {
  font-size: 18px;
}

.selected-tutor {
  margin-top: 30px;
  font-weight: bold;
  font-size: 18px;
}

.submit-button {
  margin-top: 20px;
  font-size: 18px;
  padding: 10px 20px;
}

.submission-message {
  color: red;
  margin-top: 20px;
  font-size: 18px;
  font-weight: bold;
}
</style>

