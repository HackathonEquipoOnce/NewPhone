<template>
<h2>{{welcome}}  </h2>
 <input class="filtro" type="text" v-model="filtered_product" placeholder="buscar productos">
  <button class="buscar"  @click="filteredProducts()"><span>buscar</span></button><br>
    <img class="banner" src="@/assets/img/firstimage.png" /><br>
     <h1>Populares</h1>
      <div class="container">
  <ul class="slider">
    <li id="slide1">
      <img src="https://tigocolombia.vteximg.com.br/arquivos/ids/159022-1000-1000/Motorola-G30-GrisTornasol_1.png?v=637545576852730000"/>
    </li>
    <li id="slide2">
      <img src="https://tigocolombia.vteximg.com.br/arquivos/ids/159797-1000-1000/Samsung-A72-Negro_1.png?v=637650061521070000"/>
    </li>
    <li id="slide3">
    <img src="https://tigocolombia.vteximg.com.br/arquivos/ids/159782-1000-1000/SM_A325_GalaxyA32_Awesome-Blue_Front-min.png?v=637650041524070000"/>
    </li>
    <li id="slide4">
    <img src="https://www.alkomprar.com/medias/6941059631002-001-750Wx750H?context=bWFzdGVyfGltYWdlc3w0NDM0NDR8aW1hZ2UvcG5nfGltYWdlcy9oNTUvaDJmLzkyMjQ0NjE2MTUxMzQucG5nfDEwNGYyOWNhNmM2MWZjNGI1YWMyMmFlYzA1NTcyNjcyNzU5YmYzZjJmYTFkYmM5MDNkNzk3ZjM4MmZlYmVjNmU"/>
    </li>
  </ul>
  
  <ul class="menu">
    <li>
      <a href="#slide1">1</a>
    </li>
    <li>
      <a href="#slide2">2</a>
    </li>
     <li>
      <a href="#slide3">3</a>
    </li>
    <li>
      <a href="#slide4">4</a>
    </li>
  </ul>
</div>
   <section class="phone-list">
    <article
      class="phone-item"
      v-for="phone in filteredProducts()"
      :key="phone.id"
    >
    <div class='info'>
    <h2>{{ phone.nombre }}</h2>
    <p>{{ phone.precio }}</p>
    <router-link :to="{name:'phonedetails', params:{id: phone.id}}" ><button class="button">Detalles</button></router-link><br>
    </div>
    </article>
     <div class="footer">&copy;Hackathon2022@Coders-sin-Fronteras-Grupo11</div>
  </section>
</template>

<script>
import { config } from "@/config.js";
config;
export default {
    data(){
      return{
        welcome:"Tu movil viejo por uno nuevo facil por poco 👍",
        img: './firstimage.png',

        phones:[],
        filtered_product:'',
        phone_removed:'',
      }
    },
    mounted(){
      this.loadData()
    },
    methods: {
      async loadData() {
        const response = await fetch('http://192.168.21.88:5000/api/newphone');
        this.phones = await response.json();
    },
    filteredProducts(){
      const phones = this.phones
      const filtered_product= this.filtered_product
      return phones.filter((phone) => phone.nombre.includes(filtered_product))
    }
 
  },
}
</script>

<style> 
*{
  text-decoration: none;
  list-style: none;
}

.button{
padding:10px;
border-radius:5px;
background-color:#6457A6;
color:#ffffff;
box-shadow:  2px 2px 4px #0D0A96;
cursor:pointer;
 }  

.button:hover{
padding:10px;
border-radius:5px;
background-color:#0D0A96;

 } 
  .filtro{
   border: solid 1px;
   border-radius: 5px;
   width: 30%;
   padding: 20px;
   margin-bottom: 10%;
 }
 ::placeholder{
   color: #1a191b;
   font-size: 1em;
 }
 .buscar{
   border: solid 1px;
   border-radius: 5px;
   width: 15%;
   padding: 20px;
   margin-bottom: 10%;
   margin-left: 1%;
 }
 .buscar> span{
   display: grid;
   justify-content: center;
   margin: auto;
   color: rgba(54, 41, 235, 0.699);
 } 
   
   .menu-button{
    position: absolute;
    top: 10px;
    right: 70px;
   }
   .menu-btn{
    position: absolute;
    top: 10px;
    right: 2px;
    cursor: pointer;
   }
  .menu-content{
    position: fixed;
    width: 100%;
    height: 0vh;
    top: 100px;
    background: rgba(255, 255, 255, 0.699);
    text-align: start;
    transition:  all .5s;

  }
  .menu-content li{
    display: none;
    line-height: 30px;
    margin: 50px 0;
    transition:  all .5s;
  }
  .menu-content li a{
    color: black;
    font-size: 16px;
    text-transform: uppercase;
    font-weight: 600;
  }

  .phone-list{
    display: flex;
    justify-content: center;
    margin-bottom:20px;
    flex-wrap: wrap;
    align-items: center;
  }
  .menu-content li a.active, .menu-content li a:hover{
    color: blue;
    transition: .3s;
  }
  #menu-button{
    display: none;

  }
  #menu-button:checked ~ .menu-content{
    height: 100vh;
  }
  #menu-button:checked ~ .menu-content li{
   display: block;
  }

  .banner{
  max-width:1500px;
  width: 100%;
  margin: 30px 0px;
 
 
  }
.footer{
background-color:#6457A6;
padding:20px 0px;
width: 100%;
}
  .info{

  width:300px;
   
  border: 2px solid #FFE600;
  border-radius: 10px;
  text-align:center;
  margin: 20px;
  padding: 20px ;
  border-radius:10px;
  box-shadow:  2px 2px 4px #0D0A96;
}



</style>