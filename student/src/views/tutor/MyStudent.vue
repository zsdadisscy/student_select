<script>
import {defineComponent} from "vue";
import TutorLayOut from "@/components/StudentLayOut.vue";

export default defineComponent({
  name: 'MyStudent',
  components: {
    TutorLayOut,
  },
});
</script>

<template>
<div>
  <TutorLayOut>

  </TutorLayOut>
</div>
</template>

<style scoped>

</style>