<template>
  <h2>{{welcome}} </h2>
  <img class="Log" src="@/assets/img/Logo1.png" />
    <img src="@/assets/img/firstimage.png" />
   <section class="phone-list">
    <article
      class="phone-item"
      v-for="phone in phones"
      :key="phone.id"
    >
    <div> <header class="App-header">
      
      <img class='star' src={Star} alt='this is the fav' />
      <input type="checkbox" id='menu-button' />
      <label htmlFor="menu-button" class='menu-btn'>
        <img class='menu' src={Menu} alt='this is the menu' />
      </label>
      <ul class='menu-content'>
         <li class='active'> <a href="#">Usados</a></li>
         <li> <a href="#">Nuevos</a></li>
      </ul>
    </header></div>
    <h2>{{ phone.nombre }}</h2>
    <p>Precio {{ phone.precio }}</p>
    <p>{{ phone.price }}</p><br>
    <router-link :to="{name:'phonedetails', params:{id: phone.id}}" ><button>detaills</button></router-link><br>
    </article>
  </section>
</template>

<script>
export default {
    data(){
      return{
        welcome:"Tu movil viejo por uno nuevo facil a poco precio ",
        imgage:'./Logo1.png',
        img: './firstimage.png',
        phones: [
          {id:1, nombre:"xiaomi redmi 10", precio:"230 $", caracteristicas:"camera 64MP"},
          {id:3, nombre:"xiaomi popofone", precio:"230 $", caracteristicas:"camera 64MP"},
          {id:4, nombre:"samsung", precio:"230 $", caracteristicas:"camera 64MP"},
          {id:5, nombre:"samsung", precio:"290 $", caracteristicas:"camera 64MP"},
          {id:6, nombre:"iphone", precio:"330 $", caracteristicas:"camera 64MP"}, 
          {id:7, nombre:"iphone", precio:"330 $", caracteristicas:"camera 64MP",},    
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
*{
  text-decoration: none;
  list-style: none;
}

.App-header {
    width: 100%;
    height: 70px;
    background-color: #a5a5a555;
    
   }
   .Log{
     width: 150px;
     height: 130px;
     
   }
   .star{
     position: absolute;
     top: 15px;
     right: 90px;
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

  @media only screen and (min-width: 768px) {
    .App-header {
    width: 100%;
    height: 100px;
    background-color: #a5a5a555;
    
   }
    
    .Log{
      width: 220px;
      height: 200px;
      
    }
    .star{
      position: absolute;
      top: 25px;
      right: 520px;
      width: 50px;
      height: 50px;
    }
    .menu-btn{
      display: none;
    }
    .menu-content{
      position: absolute;
      height: 100px;
      top: 30px;
      background: none;
      text-align: right;
      transition:  none;
      margin-right: 50px;
      
    }
    .menu-content li{
      display: inline-block;
      line-height: 10px;
      margin-right: 100px;
      margin-top: 0px;
      transition: none;
      
    }
    .menu-content li a{
      font-size: 22px;
      
    }
    .menu-content li a{
      color: #6457A6;
     
    }
    .menu-content li a.active, .menu-content li a:hover{
      color: #0D0A96;
      transition: .3s;
    }

  }
</style>