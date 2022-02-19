<template>

  <div id="nav">
    <router-link class="home" :to="{name: 'newphone'} "></router-link>
    </div>
    <img class="Log" src="@/assets/img/Logo1.png" />
      <div class="star">
        <img src="@/assets/img/Star.png" />
      </div>
    <div>
    
    <router-link class="newphone" :to="{name: 'newphone'}"> Usados</router-link>
    <router-link class="adsposting" :to="{name: 'secondHandPhone'}">Nuevos</router-link>
  </div>
  <router-view />
</template>
<script>
export default {
     data(){
       return{
         imgage:'./Logo1.png',
         img:'./assets/img/Star.png',
          menus:[
        {code:0, name:''},
        {code:1, name:'Usados'},
        {code:2, name: 'Nuevos'},
      ],
       }
     } 
}
</script>
<style scoped>  

</style>
