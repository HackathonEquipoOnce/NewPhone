<template>
  <form @submit.prevent="postAds" class="ads">
  <input type="text" v-model="phone.price" placeholder="Phone.price" class="adding"/><br><br>
  <input type="text" v-model="phone.details" placeholder="Phone.price" class="adding"/><br><br>
  <input type="email" v-model="phone.name" placeholder="Phone.price" class="adding"/><br><br>
  <input type="number" v-model="phone.model" placeholder="Phone.price" class="adding"/><br><br><br>
  <button>Save phone</button>
  </form>
</template>

<script>
import { v4 as uuidv4 } from 'uuid';
uuidv4();
export default {
   data(){
       return{
           phone:[],
           firstName: '',
           lastName: '',
           email:'',
           
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
       postAds(){
            if(this.phone.price||this.phone.details||this.phone.name||this.phone.model !==''){
                let nextId= uuidv4()
				let newProduct={ 
                                "id": nextId,
                                "phone.price":this.phone.model,
                                "phone.details":this.phone.model,
                                "phone.name": this.phone.model,
                                "phone.model": this.phone.model
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
				this.phone.model='';
				this.phone.model='';
				this.phone.model='';
                this.phone.model=''
       }
   }
}
</script>

<style>

</style>