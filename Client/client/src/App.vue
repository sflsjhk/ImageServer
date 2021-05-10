<template>
  <v-app>
    <v-main>
      <v-container>
      <h1>Ion Patient Image Search</h1>
      <SearchPatient @add-patient="addPatientName" />
      <Images :images='images' />
      </v-container>
    </v-main>
  </v-app>
</template>

<script>
import Images from './components/Images'
import SearchPatient from './components/searchPatient'
import { fetchImages } from './fetchImages.js'

export default {
  name: 'App',

  components: {
    Images,
    SearchPatient,
  },

  data: () => ({
      first_name: String,
      last_name: String,
      images: [],
  }),

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
};
</script>
