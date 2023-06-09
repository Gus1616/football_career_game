import { createRouter, createWebHistory, } from 'vue-router'

import HomePage from '../components/pages/HomePage.vue'
import MainPage from '../components/pages/MainPage.vue'

const routes = [
    {path: '/',
    componenet: HomePage
    },
    {path: '/MainPage',
    componenet: MainPage
    }
]


const router = createRouter({
    history: createWebHistory(),
    routes,
})

export default router