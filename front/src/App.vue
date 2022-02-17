<template>
  <div id="nav">
    <router-link class="home" :to="{name: 'newphone'} "><div>
    <img src="@/assets/img/Star.png" /></div> new Phone</router-link>|
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
       }
     } 
}
</script>
<style scoped>  
</style>
