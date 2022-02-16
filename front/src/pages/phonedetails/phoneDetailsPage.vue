<template>
  <p>{{id}} </p>
  <section class="phone-details">
  <h2>{{ phone.price }}</h2>
  <p>{{ phone.price }}</p>
  <p>{{ phone.price}}</p>
  <p>{{ phone.price }}</p><br><br>
  <router-link :to="{name:'phonedetails'}" @click="removephone" ><button>remove phone</button></router-link>
  </section>
</template>

<script>
import Swal from 'sweetalert2';
//window.Swal= Swal;
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
   // await fetch("http://localhost:5000/api/contact/" + this.id)
   // .then(res => res.json())
   // .then(data => this.contact = data)
    //.catch(err=> console.log(err.message))
  },
  methods:{
    removephone(){
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
          //this.Response= fetch("http://localhost:5000/api/newphone/" + this.id, {method: "DELETE"});
          this.$router.push('/newphone')
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