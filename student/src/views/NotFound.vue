<script>
import {defineComponent} from "vue";
import ContentBase from "@/components/ContentBase.vue";

export default defineComponent({
  name: 'NotFound',
  components: {ContentBase},
});
</script>

<template>
  <content-base>
    <h1>Not Found</h1>
  </content-base>
</template>

<style scoped>

</style>