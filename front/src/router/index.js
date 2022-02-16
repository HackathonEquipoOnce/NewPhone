import { createRouter, createWebHistory } from 'vue-router'
import NewPhone from '../views/Home.vue'

const routes = [
  {
    path: '/',
    name: 'Home',
    component: NewPhone
  },
  {
    path: '/about',
    name: 'About',
    component: () => import(/* webpackChunkName: "about" */ '../views/About.vue')
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
