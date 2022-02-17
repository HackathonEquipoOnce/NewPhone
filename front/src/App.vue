<template>
  <div id="nav">
    <router-link class="home" :to="{name: 'newphone'} "></router-link>
    </div>
    <img class="Log" src="@/assets/img/Logo1.png" />
      <div class="star">
        <img src="@/assets/img/Star.png" />
      </div>
    <div>
    
    <router-link class="newphone" :to="{name: 'newphone'}">Nuevos</router-link>
    <router-link class="adsposting" :to="{name: 'adsposting'}">Usados</router-link>
  </div>
  <router-view />
</template>
<script>
export default {
     data(){
       return{
         imgage:'./Logo1.png',
         img:'./assets/img/Star.png',
       }
     } 
}
</script>
<style scoped>  

</style>
