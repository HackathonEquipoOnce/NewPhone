<template>
  <h2>{{welcome}} </h2>
    <img src="@/assets/img/firstimage.png" />
   <section class="phone-list">
    <article
      class="phone-item"
      v-for="phone in phones"
      :key="phone.id"
    >
    <h2>{{ phone.nombre }}</h2>
    <p>{{ phone.precio }}</p>
    <p>{{ phone.price }}</p><br>
    <router-link :to="{name:'phonedetails', params:{id: phone.id}}" ><button>detaills</button></router-link><br><br>
    <button class="remove" @click="del(phone)" >remove contact</button>
    </article>
  </section>
</template>

<script>
export default {
    data(){
      return{
        welcome:"Welcome To Your new phone page",
        img: './firstimage.png',
        phones: [
          {id:1, nombre:"xiaomi redmi 10", precio:"230", caracteristicas:"camera 64MP"},
          {id:3, nombre:"xiaomi popofone", precio:"230", caracteristicas:"camera 64MP"},
          {id:4, nombre:"samsung", precio:"230", caracteristicas:"camera 64MP"},
          {id:5, nombre:"samsung", precio:"290", caracteristicas:"camera 64MP"},
          {id:6, nombre:"iphone", precio:"330", caracteristicas:"camera 64MP"}, 
          {id:7, nombre:"iphone", precio:"330", caracteristicas:"camera 64MP",},    
        ],
        phone_removed:'',
      }
    },
      methods: {
    async loadData() {
     // const response = await fetch("http://localhost:5000/api/phone");
      //this.phones = await response.json();
    },
    del(phone){
      
      let index=this.phones.indexOf(phone)
      this.phones.splice(index, 1)
      console.log("elemento borrado")
    }
  },
}
</script>

<style>

</style>