<template>
  <div id="nav">
    <router-link class="home" to="/">Home</router-link>|
    <router-link class="contacts" :to="{name: 'contactsPage'}">Contacts</router-link>|
    <router-link class="newcontact" :to="{name: 'addNewContact'}">Add New Contact</router-link>
  </div>
  <router-view />
</template>
<style scoped>  
.home{
  background: rgb(35, 207, 230);
  padding: 5px;
  text-align: center;
  border-radius: 5px;
}
.contacts{
  background: rgb(9, 79, 231);
  padding: 5px;
  text-align: center;
  border-radius: 5px;
}
.newcontact{
  background: rgb(226, 5, 160);
  padding: 5px;
  text-align: center;
  border-radius: 5px;
}
</style>
