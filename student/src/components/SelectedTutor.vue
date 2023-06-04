<template>
    <div class="selected-tutors">
      <h2 class="title">已选导师</h2>
      <table class="tutors-table">
        <!-- 表头省略 -->
        <thead>
        <tr>
          <th>姓名</th>
          <th>性别</th>
          <th>研究方向</th>
          <th>操作</th>
        </tr>
      </thead>
        <tbody>
          <tr v-for="tutor in selectedTutors" :key="tutor.id">
            <td>{{ tutor.name }}</td>
            <td>{{ tutor.gender }}</td>
            <td>{{ tutor.research }}</td>

          </tr>
        </tbody>
      </table>
      <div v-if="selectedTutors.length === 0" class="empty-message">
        暂无已选导师
      </div>
    </div>
  </template>
  
  <script>
  export default {
    name: 'SelectedTutor',
    props: {
      selectedTutors: {
        type: Array,
        default: () => []
      },
      // 声明一个名为 `value` 的 prop，用于双向绑定
      value: {
        type: Array,
        default: () => []
      }
    },

  };
  </script>
  
  <style>
  .selected-tutors {
    margin: 20px;
  }
  
  .title {
    font-size: 24px;
    font-weight: bold;
    margin-bottom: 10px;
  }
  
  .tutors-table {
    width: 100%;
    border-collapse: collapse;
  }
  
  .tutors-table th,
  .tutors-table td {
    padding: 10px;
    text-align: center;
    border: 1px solid #ddd;
  }
  
  .tutors-table th {
    background-color: #f5f5f5;
    font-weight: bold;
  }
  
  .remove-button {
    color: #f5222d;
    cursor: pointer;
  }
  
  .empty-message {
    margin-top: 10px;
    font-style: italic;
    text-align: center;
  }
  </style>
  