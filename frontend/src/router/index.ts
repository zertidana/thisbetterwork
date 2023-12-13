// Example of how to use Vue Router

import { createRouter, createWebHistory } from 'vue-router'

// 1. Define route components.
// These can be imported from other files
import MainPage from '../pages/MainPage.vue';
import AllCategories from '../pages/AllCategories.vue';
import ArtPage from '../pages/ArtPage.vue';
import ProfilePage from '../pages/ProfilePage.vue';
import EducationPage from '../pages/EducationPage.vue';
import FashionPage from '../pages/FashionPage.vue';
import FinancePage from '../pages/FinancePage.vue';
import SportsPage from '../pages/SportsPage.vue';
import WorldPage from '../pages/WorldPage.vue';


let base = (import.meta.env.MODE == 'development') ? import.meta.env.BASE_URL : ''

// 2. Define some routes
// Each route should map to a component.
// We'll talk about nested routes later.
const router = createRouter({
    history: createWebHistory(base),
    routes: [
        { path: '/', name: 'Home', component: MainPage },
        { path: '/AllCategories/', name: 'All Categories', component: AllCategories },
        { path: '/ProfilePage', name: 'Profile Page', component: ProfilePage },
        { path: '/ArtPage', name: 'Art Page', component: ArtPage },
        { path: '/EducationPage', name: 'EducationPage', component: EducationPage },
        { path: '/FashionPage', name: 'Fashion Page', component: FashionPage },
        { path: '/FinancePage', name: 'Finance Page', component: FinancePage },
        { path: '/SportsPage', name: 'Sport Page', component: SportsPage },
        { path: '/WorldPage', name: 'World Page', component: WorldPage },
    ]
})

export default router
