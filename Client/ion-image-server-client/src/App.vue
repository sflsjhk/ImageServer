<template>
  <div class="container">
    <h1>Ion Patient Image Search</h1>
    <input type="text" v-model="search" placeholder="First Name" />
    <input type="text" v-model="search" placeholder="Last Name" />
    <Images :images='images' />
  </div>
</template>

<script>
import Images from './components/Images'
// import { fetchImages } from './fetchImages.js'
export default {
  name: 'App',
  components: {
    Images
  },
  data () {
    return {
      images: []
    }
  },
  created () {
    // this.images = fetchImages('Jim', 'Jones')
    this.images = [
      {
        id: 1,
        image_url: 'https://hekangjia.s3.us-east-2.amazonaws.com/ion_image/1.jpg'
      },
      {
        id: 4,
        image_url: 'https://hekangjia.s3.us-east-2.amazonaws.com/ion_image/4.jpg'
      }]
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
