<template>
  <h2>{{welcome}} </h2>
   <section class="phone-list">
    <article
      class="phone-item"
      v-for="phone in phones"
      :key="phone.id"
    >
    <h2>{{ phone.price }}</h2>
    <p>{{ phone.price }}</p>
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
        phones: [],
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
      this.phone_removed=this.phones.splice(index, 1)
      console.log("elemento borrado")
    }
  },
}
</script>

<style>

</style>