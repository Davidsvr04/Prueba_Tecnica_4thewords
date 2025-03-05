<template>
  <div>
    <NavBar />
    <LeyendaForm @guardar="crearLeyenda" />
  </div>
</template>

<script setup>
import { useRouter } from 'vue-router';
import axios from 'axios';
import LeyendaForm from '../components/leyendaForm.vue';
import NavBar from '../components/NavBar.vue';

const router = useRouter();

const crearLeyenda = async (leyenda) => {
  await axios.post('http://localhost:8080/leyenda/', leyenda);
  router.push('/');
};
</script>