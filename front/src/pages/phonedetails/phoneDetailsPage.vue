<template>
  <p>{{id}} </p>
  <section class="phone-details">
  <h2>{{ phone.price }}</h2>
  <p>{{ phone.price }}</p>
  <p>{{ phone.price}}</p>
  <p>{{ phone.price }}</p><br><br>
  <button @click="volverAHomePage">remove phone</button>
  </section>
</template>

<script>
export default {
  name:'phonedetails',
  props:['id'],
  data() {
    return {
      phone: {},
      Response:''
    };
  },
  async mounted() {
   // await fetch("http://localhost:5000/api/phone/" + this.id)
   // .then(res => res.json())
   // .then(data => this.phone = data)
    //.catch(err=> console.log(err.message))
  },
  methods:{
     
  }
}
</script>

<style scoped>
.contact-details {
  border: 2px solid dodgerblue;
  border-radius: 1em;
  margin: 1em;
}
</style>