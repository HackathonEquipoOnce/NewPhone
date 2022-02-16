<template>
  <section class="contact-list">
    <article
      class="contact-item"
      v-for="contact in contacts"
      :key="contact.phone"
    >
    <h2>{{ contact.first_name }}</h2>
    <p>{{ contact.last_name }}</p>
    <p>{{ contact.phone }}</p><br>
    <router-link :to="{name:'contactdetails', params:{id: contact.id}}" ><button>detaills</button></router-link><br><br>
    <router-link :to="{name:'contactSetup', params:{id: contact.id}}"><button>modificar</button></router-link>
    <button class="remove" @click="del(contact)" >remove contact</button>
    </article>
  </section>
</template>

<script>
export default {
  name: "contacts",
  data() {
    return {
      contacts: [],
      contact_removed:'',
    };
  },
  mounted() {
    this.loadData();
  },
  methods: {
    async loadData() {
      const response = await fetch("http://localhost:5000/api/contact");
      this.contacts = await response.json();
    },
    del(contact){
      
      let index=this.contacts.indexOf(contact)
      this.contact_removed=this.contacts.splice(index, 1)
      console.log("elemento borrado")
    }
  },
};
</script>

<style scoped>
h1 {
  font-style: italic;
}
.contact-item {
  border: 2px solid dodgerblue;
  border-radius: 1em;
  margin: 1em;
}
</style>
