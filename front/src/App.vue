<template>
  <div id="nav">
    <router-link class="home" :to="{name: 'newphone'} "><div>
    <img src="@/assets/img/Star.png" /></div> <div class="ph">new Phone</div></router-link>|
    <br>
    <router-link class="newphone" :to="{name: 'newphone'}">phones</router-link>|
    <router-link class="adsposting" :to="{name: 'adsposting'}">post Ads for free</router-link>
  </div>
  <router-view />
</template>
<script>
export default {
     data(){
       return{
         img: './Star.png',
         image: './Logo1.png',
       }
     } 
}
</script>
<style scoped>  
.ph{
  color: #0D0A96;
  
}
</style>
