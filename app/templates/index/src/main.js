import Vue from 'vue'
import App from './App.vue'
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'
import router from './router'
import BootstrapVue from 'bootstrap-vue'
/*
* add tree view js
*/

/*
end tree view js*
*/


Vue.config.productionTip = false
Vue.use(BootstrapVue)

new Vue({
  el: '#app',
  router,
  template: '<App/>',
  components: { App }
})