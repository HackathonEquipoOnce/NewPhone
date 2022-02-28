<template>
<button @click="theBasket" class="basket">
  <h2 class="number" v-show="displaySelected">{{shoppingBasket}}</h2>
  <span class="cesta">🛒</span></button>
<div class="details">
  <section class="phone-details">
  <h2>{{phone.nombre}}</h2>
  <p>{{phone.precio }}</p>
  <p>{{phone.caracteristicas}}</p>
  <router-link :to="{name:'newphone'}" @click="volverAHomePage" ><button class="volver">volver a pagina de inicio</button></router-link><br><br>
  <button @click="Carrito">añadir al carrito</button>
  </section>
  </div>
</template>

<script>
import config from "@/config.js";
export default {
  name:'phonedetails',
  props:['id'],
  data() {
    return {
      phone: {},
      Response:'',
      cestaDeLaCompra:[],
      displaySelected: false
    };
  },
  async mounted() {
    await fetch(`${config.route_Path}/newphone/` + this.id)
    .then(res => res.json())
    .then(data => this.phone = data)
    .catch(err=> console.log(err.message))
  },
  computed:{
    shoppingBasket(){
      let productAmount= this.cestaDeLaCompra.length
      return productAmount
    }
  },
  methods:{
    volverAHomePage(){
      this.$router.push("/")
    },
    Carrito(){
      this.cestaDeLaCompra.push(this.phone)
      this.displaySelected= true
    },
    theBasket(){
      this.$router.push("/basket")
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
.basket{
  width: 10rem;
}
.number{
  color: #ff008c;
}
.cesta{
  font-size: 3em;
}
span{
  width: 50em;
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