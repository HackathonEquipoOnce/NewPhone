<template>
  <form @submit.prevent="addNewContact" class="add">
  <input type="text" v-model="firstName" placeholder="Contact First Name" class="adding"/><br><br>
  <input type="text" v-model="lastName" placeholder="Contact Last Name" class="adding"/><br><br>
  <input type="email" v-model="email" placeholder="Contact Email" class="adding"/><br><br>
  <input type="number" v-model="phone" placeholder="Contact Phone" class="adding"/><br><br><br>
  <button>Save Contact</button>
  </form>
</template>

<script>
import { v4 as uuidv4 } from 'uuid';
uuidv4();
export default {
   data(){
       return{
           contacts:[],
           firstName: '',
           lastName: '',
           email:'',
           phone:'',
       }
   },
   mounted(){
       this.loadData()
   },
   methods:{
       async loadData(){
          // const response = await fetch("http://localhost:5000/api/contact");
           //this.contacts = await response.json();
       },
       addNewContact(){
            if(this.firstName&&this.lastName &&this.email&&this.phone !==''){
                let nextId= uuidv4()
				let newProduct={ 
                                "id": nextId,
                                "first_name":this.firstName,
                                "last_name":this.lastName,
                                "email": this.email,
                                "phone": this.phone
                                }
				this.contacts.push(newProduct)
				//const settings={
					//method:'POST',
					//body:JSON.stringify(newProduct),
					//headers:{
						//'Content-Type': 'application/json'
					//}
				//}
				//fetch('http://localhost:5000/api/contact', settings)
			}
			else{
				alert ("must fill all camps before saving")
			}
				this.firstName='';
				this.lastName='';
				this.email='';
                this.phone=''
       }
   }
}
</script>

<style>

</style>