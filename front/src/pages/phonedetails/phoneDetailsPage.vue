<template>
  <p>{{id}} </p>
  <section class="phone-details">
  <h2>{{ phone.price }}</h2>
  <p>{{ phone.price }}</p>
  <p>{{ phone.price}}</p>
  <p>{{ phone.price }}</p><br><br>
  <router-link :to="{name:'newphone'}" @click="volverAHomePage" ><button class="volver">volver a pagina de inicio</button></router-link>
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
    volverAHomePage(){
      this.$router.push("/")
    }
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