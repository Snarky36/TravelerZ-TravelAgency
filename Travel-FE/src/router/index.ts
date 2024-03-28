import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import ContactView from '../views/ContactView.vue'
import DestinationsView from '../views/DestinationsView.vue'
import LoginView from '../views/LoginView.vue'
import RegisterView from '../views/RegisterView.vue'
import ManageDestinations from '@/views/ManageDestinations.vue'


const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  scrollBehavior(to, from, savedPosition) {
    if (to.hash) {
      const targetElement = document.getElementById(to.hash.slice(1));
      if (targetElement) {
        return { el: to.hash, behavior: 'smooth' };
      }
    }
    return { left: 0, top: 0, behavior: 'smooth' };
  },
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/destinations',
      name: 'destinations',
      component: DestinationsView,
      props: route => ({ filterKey: route.params.filterKey })
    },
    {
      path: '/contact',
      name: 'contact',
      component: ContactView
    },
    {
      path: '/login',
      name: 'login',
      component: LoginView
    },
    {
      path: '/register',
      name: 'register',
      component: RegisterView
    },
    {
      path: '/manage-destinations',
      name: 'manageDestinations',
      component: ManageDestinations
    },
    
  ]
})

export default router
