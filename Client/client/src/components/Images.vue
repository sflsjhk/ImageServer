<template>
    <v-container>
        <v-card :key="image.image_url" v-for="image in images">
          <v-img
            class="white--text align-end"
            height="550"
            width="500"
            :src="image.image_url" />
          <v-card-title>{{image.date_taken}}</v-card-title>
        </v-card>
    </v-container>
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
image {
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
