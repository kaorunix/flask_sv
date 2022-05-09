// import Vue from 'vue'
// import Vuex from 'vuex'
import actions from '@/store/modules/actions'
import mutations from '@/store/modules/mutations'

const state = {
  auth: {
    token: localStorage.getItem('token'),
    userId: null
  }
}

export default {
  state,
  actions,
  mutations
}
