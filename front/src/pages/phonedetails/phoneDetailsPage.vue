<template>
  <p>{{id}} </p>
  <section class="phone-details">
  <h2>{{phone.nombre}}</h2>
  <p>{{phone.precio }}</p>
  <p>{{phone.caracteristicas}}</p>
  <router-link :to="{name:'newphone'}" @click="volverAHomePage" ><button class="volver">volver a pagina de inicio</button></router-link>
  </section>
</template>

<script>
export default {
  name:'phonedetails',
  props:['id'],
  data() {
    return {
       phone: [
          {id:1, nombre:"xiaomi redmi 10", precio:"230 $", caracteristicas:"camera 64MP"},
          {id:3, nombre:"xiaomi popofone", precio:"230 $", caracteristicas:"camera 64MP"},
          {id:4, nombre:"samsung", precio:"230 $", caracteristicas:"camera 64MP"},
          {id:5, nombre:"samsung", precio:"290 $", caracteristicas:"camera 64MP"},
          {id:6, nombre:"iphone", precio:"330 $", caracteristicas:"camera 64MP"}, 
          {id:7, nombre:"iphone", precio:"330 $", caracteristicas:"camera 64MP",},    
        ],
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
.phone-details{
  max-width:400px;
  border: 2px solid #FFE600;
  border-radius: 1em;
  margin: 1em;
  text-align: center;
}
</style>