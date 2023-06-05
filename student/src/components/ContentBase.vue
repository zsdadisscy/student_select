<template>
  <a-card style="width: 300px">
    <slot></slot>
  </a-card>
</template>




<script>
export default {
    name: 'ContentBase',
}
</script>

<style scoped>
.container {
  margin-top: 20px;
}
</style>