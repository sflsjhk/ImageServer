<template>
  <div class="container">
    <h1>Ion Patient Image Search</h1>
    <SearchPatient @add-patient="addPatientName" />
    <Images :images='images' />
  </div>
</template>

<script>
import Images from './components/Images'
import SearchPatient from './components/searchPatient'
import { fetchImages } from './fetchImages.js'
export default {
  name: 'App',
  components: {
    Images,
    SearchPatient
  },
  data () {
    return {
      first_name: String,
      last_name: String,
      images: []
    }
  },
  methods: {
    async addPatientName (newSerachQuery) {
      this.first_name = newSerachQuery.first_name
      this.last_name = newSerachQuery.last_name
      this.images = await fetchImages(this.first_name, this.last_name)
    }
  },
  created () {
    this.images = fetchImages(this.first_name, this.last_name)
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
