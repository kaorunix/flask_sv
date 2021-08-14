import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/about',
    name: 'About',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/About.vue')
  },
  {
    path: '/account',
    name: 'アカウント一覧',
    component: () => import('../views/account/List.vue')
  },
  {
    path: '/account/get',
    name: 'アカウント詳細',
    component: () => import('../views/account/Get.vue')
  },
  {
    path: '/account/create',
    name: 'アカウント作成',
    component: () => import('../views/account/Create.vue')
  },
  {
    path: '/account/update',
    name: 'アカウント更新',
    component: () => import('../views/account/Update.vue')
  },
  {
    path: '/account/delete',
    name: 'アカウント削除',
    component: () => import('../views/account/Delete.vue')
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
