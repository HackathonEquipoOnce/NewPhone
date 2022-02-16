<template>
  <h2>{{welcome}} </h2>
   <section class="contact-list">
    <article
      class="contact-item"
      v-for="contact in contacts"
      :key="contact.phone"
    >
    <h2>{{ contact.first_name }}</h2>
    <p>{{ contact.last_name }}</p>
    <p>{{ contact.phone }}</p><br>
    <router-link :to="{name:'phonedetails', params:{id: contact.id}}" ><button>detaills</button></router-link><br><br>
    <button class="remove" @click="del(contact)" >remove contact</button>
    </article>
  </section>
</template>

<script>
export default {
    data(){
      return{
        welcome:"Welcome To Your new phone page",
        contacts: [],
        contact_removed:'',
      }
    },
      methods: {
    async loadData() {
     // const response = await fetch("http://localhost:5000/api/contact");
      //this.contacts = await response.json();
    },
    del(contact){
      
      let index=this.contacts.indexOf(contact)
      this.contact_removed=this.contacts.splice(index, 1)
      console.log("elemento borrado")
    }
  },
}
</script>

<style>

</style>