import { createRouter, createWebHistory } from 'vue-router';
import HomeView from '../views/HomeView.vue';
import CrearLeyendaView from '../views/CrearLeyenda.vue';
import EditarLeyendaView from '../views/EditarLeyenda.vue';

const routes = [
  { path: '/', component: HomeView },
  { path: '/crear', component: CrearLeyendaView },
  { path: '/editar/:id', component: EditarLeyendaView, props: true },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;