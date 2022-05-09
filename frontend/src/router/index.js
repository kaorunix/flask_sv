// import Vue from 'vue'
// import { createRouter, createWebHashHistory } from 'vue-router'
import VueRouter from 'vue-router'
import Vue from 'vue'
import Home from '../views/Home.vue'
import { authorizeToken } from './guards'
import About from '../views/About.vue'
import List from '../views/account/List.vue'
import Create from '../views/account/Create.vue'
import Login from '../views/auth/Login.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home,
    meta: {
      requiredAuth: true
    }
  },
  {
    path: '/about',
    name: 'About',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: About // () => import(/* webpackChunkName: "about" */ '../views/About.vue')
  },
  {
    path: '/account',
    name: 'アカウント一覧',
    component: List, // () => import('../views/account/List.vue'),
    meta: {
      requiredAuth: true
    }
  },
  {
    path: '/account/create',
    name: 'アカウント作成',
    component: Create, // () => import('../views/account/Create.vue'),
    meta: {
      requiredAuth: true
    }
  },
  {
    path: '/login',
    name: 'Login',
    component: Login // () => import('../views/auth/Login.vue')
  }
]

const router = new VueRouter({
// const router = new VueRouter({
//  history: createWebHashHistory(),
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})
router.beforeEach(authorizeToken)

export default router
