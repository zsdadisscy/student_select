<script>
import {defineComponent} from "vue";
import $ from 'jquery';
import { useRoute } from 'vue-router'; 

export default defineComponent({
  name: 'LookTutorInfo',
  setup() {
    const route = useRoute();
    const tutor_id = parseInt(route.params.tutor_id);
    $.ajax({
      url: 'http://8.130.65.99:8002/student/get_tutor_info/',
      type: 'POST',
      data: {
        tutor_id: tutor_id,
      },
      success(resp) {
          console.log(resp);
      },
      error(resp) {
        console.log(resp);
      }
    })
  }
});
</script>

<template>
<div></div>
</template>

<style scoped>

</style>