<template>
    <div :key="image" v-for="image in images">
        <img :src=image>
    </div>
</template>

<script>
export default {
  name: 'Images',
  props: {
    images: Array
  }
}
</script>

<style scoped>
img {
  height:500px;
  width: 550px;
  border-radius: 2px;
  box-shadow: 1px 1px 3px 1px rgba(0, 0, 0, 0.5);
  transition: width 1s;
}
img:hover {
  cursor: pointer;
}
</style>
