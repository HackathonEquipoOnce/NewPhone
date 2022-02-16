<template>
  <p>{{id}} </p>
  <section class="contact-setup">
  <form @submit.prevent="saveContact">
<input type="text" v-model="contact">
<div v-for="element in contact" :key="element"></div>
</form>
  </section>
</template>

<script>
export default {
  name:'contactSetup',
  props:['id'],
  data() {
    return {
      contact: [],
    };
  },
  mounted() {
    fetch("http://localhost:5000/api/contact/" + this.id)
    .then(res => res.json())
    .then(data => this.contact = data)
    .catch(err=> console.log(err.message))
  },
}
</script>

<style scoped>
.contact-details {
  border: 2px solid dodgerblue;
  border-radius: 1em;
  margin: 1em;
}
</style>