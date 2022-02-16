<template>
  <p>{{id}} </p>
  <section class="contact-details">
  <h2>{{ contact.first_name }}</h2>
  <p>{{ contact.last_name }}</p>
  <p>{{ contact.email }}</p>
  <p>{{ contact.phone }}</p><br><br>
  <router-link :to="{name:'contactdetails'}" @click="removeContact" ><button>remove contact</button></router-link>
  </section>
</template>

<script>
import Swal from 'sweetalert2';
//window.Swal= Swal;
export default {
  name:'contactdetails',
  props:['id'],
  data() {
    return {
      contact: [],
      Response:''
    };
  },
  async mounted() {
    await fetch("http://localhost:5000/api/contact/" + this.id)
    .then(res => res.json())
    .then(data => this.contact = data)
    .catch(err=> console.log(err.message))
  },
  methods:{
    removeContact(){
          Swal.fire({
      title: 'estas seguro?',
      text: "You won't be able to revert this!",
      icon: 'warning',
      showCancelButton: true,
      confirmButtonColor: '#3085d6',
      cancelButtonColor: '#d33',
      confirmButtonText: 'Yes, delete it!'
    }).then((result) => {
      if (result.isConfirmed) {
          this.Response= fetch("http://localhost:5000/api/contact/" + this.id, {method: "DELETE"});
          this.$router.push('/contact')
          Swal.fire(
            'Deleted!',
            'Your file has been deleted.',
            'success'
        )
      }
    })
     
    }
  }
}
</script>

<style scoped>
.contact-details {
  border: 2px solid dodgerblue;
  border-radius: 1em;
  margin: 1em;
}
</style>