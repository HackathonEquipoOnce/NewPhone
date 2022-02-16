import { createRouter, createWebHistory } from 'vue-router'
import newphone from '@/pages/home/NewPhonePage.vue'
import phonedetails from '@/pages/phonedetails/phoneDetailsPage.vue'
import adsposting  from '@/pages/ads/adsPostingPage.vue'


const routes = [
  {
    path: '/',
    name: 'newphone',
    component: newphone
  },
  {
    path: '/newphone/:id',
    name: 'phonedetails',
    component: phonedetails,
    props: true
  },
  {
    path: '/newphone/add',
    name: 'adsposting',
    component: adsposting
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
})

export default router
