<template>
  <div id="nav">
    <router-link class="home" :to="{name: 'newphone'} ">
      <div class="star">
        <img src="@/assets/img/Star.png" />
      </div>
    <div class="ph">Usados</div></router-link>
    <router-link class="newphone" :to="{name: 'newphone'}">Nuevos</router-link>
    <router-link class="adsposting" :to="{name: 'adsposting'}">post Ads for free</router-link>
  </div>
  <router-view />
</template>
<script>
export default {
     data(){
       return{
         img:'./assets/img/Star.png',
       }
     } 
}
</script>
<style scoped>  
.ph{
  color: #0D0A96;
  font-size: 25px;
  position: absolute;
  top: 50px;
  right: 50px;
  
}
#nav{
   width: 100%;
    height: 70px;
    background-color: #a5a5a555;
}
.star{
     
     position: absolute;
     top: 50px;
     right: 530px;
   }
</style>
