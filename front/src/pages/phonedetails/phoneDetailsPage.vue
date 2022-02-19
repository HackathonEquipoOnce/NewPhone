<template>
<div class="details">
  <p>{{id}} </p>
  <section class="phone-details">
  <h2>{{phone.nombre}}</h2>
  <p>{{phone.precio }}</p>
  <p>{{phone.caracteristicas}}</p>
  <router-link :to="{name:'newphone'}" @click="volverAHomePage" ><button class="volver">volver a pagina de inicio</button></router-link>
  </section>
  </div>
</template>

<script>
import { config } from "@/config.js";
config;
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
    await fetch('http://192.168.1.131:5000/api/newphone' + this.id)
    .then(res => res.json())
    .then(data => this.phone = data)
    .catch(err=> console.log(err.message))
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

.volver{
padding:10px;
border-radius:5px;
background-color:#6457A6;
color:#ffffff;
box-shadow:  2px 2px 4px #0D0A96;
cursor:pointer;
margin:20px;
 } 

 .volver:hover{
padding:10px;
border-radius:5px;
background-color:#0D0A96;

 }  

 .details{
 display: flex;
 justify-content: center
 }
</style>