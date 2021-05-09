<template>
  <form @submit="onSubmit" class="add-form">
    <div class="form-control">
      <label>First Name</label>
      <input type="text" v-model="first_name" name="first_name" placeholder="Patient's First Name" />
    </div>

    <div class="form-control">
      <label>Last Name</label>
      <input
        type="text"
        v-model="last_name"
        name="last_name"
        placeholder="Patient's Last Name"
      />
    </div>

    <input type="submit" value="Search" class="btn btn-block" />
  </form>
</template>

<script>
export default {
  name: 'SearchPatient',
  data () {
    return {
      first_name: '',
      last_name: ''
    }
  },
  methods: {
    onSubmit (e) {
      e.preventDefault()

      if (!this.first_name || !this.last_name) {
        alert('Please enter patient name')
        return
      }

      const newSerachQuery = {
        first_name: this.first_name,
        last_name: this.last_name
      }

      this.$emit('add-patient', newSerachQuery)
      this.first_name = ''
      this.last_name = ''
    }
  }
}
</script>

<style scoped>
.add-form {
  margin-bottom: 40px;
}

.form-control {
  margin: 20px 0;
}

.form-control label {
  display: block;
}

.form-control input {
  width: 100%;
  height: 40px;
  margin: 5px;
  padding: 3px 7px;
  font-size: 17px;
}

.form-control-check {
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.form-control-check label {
  flex: 1;
}

.form-control-check input {
  flex: 2;
  height: 20px;
}
</style>
