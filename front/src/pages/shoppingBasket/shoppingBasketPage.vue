<template>
<div class="details">
<section>
<button @click="getBackToPreviousPage" class="previous">volver a la pagina anterior</button>
<button @click="getBackToHomePage" class="backhome">volver a la pagina principal</button>
</section>
</div>
</template>

<script>
export default {
  name:'shoppingBasket',
  data() {
    return {
      phone: {}
    };
  },
  async mounted() {
  },
  computed:{
    
  },
  methods:{
    getBackToPreviousPage(){
      this.$router.push('/newphone/:id')
    },
    getBackToHomePage(){
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
.basket{
  width: 10rem;
}
span{
  width: 50em;
}

.previous{
padding:10px;
border-radius:5px;
background-color:#6457A6;
color:#ffffff;
box-shadow:  2px 2px 4px #0D0A96;
cursor:pointer;
margin:20px;
 } 
 .backhome{
padding:10px;
border-radius:5px;
background-color:#6457A6;
color:#ffffff;
box-shadow:  2px 2px 4px #0D0A96;
cursor:pointer;
margin:20px;
 } 

</style>