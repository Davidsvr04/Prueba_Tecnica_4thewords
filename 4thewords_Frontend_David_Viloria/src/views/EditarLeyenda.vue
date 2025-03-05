<template>
  <div>
    <NavBar />
    <div class="container">
      <LeyendaForm :leyendaInicial="leyenda" @guardar="actualizarLeyenda" />
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { useRoute, useRouter } from 'vue-router';
import axios from 'axios';
import LeyendaForm from '../components/leyendaForm.vue';
import NavBar from '../components/NavBar.vue';

const route = useRoute();
const router = useRouter();
const leyenda = ref({});

onMounted(async () => {
  try {
    const response = await axios.get(`http://localhost:8080/leyenda/${route.params.id}`);
    leyenda.value = response.data;
  } catch (error) {
    alert('Error al cargar la leyenda. Por favor, inténtalo de nuevo.');
  }
});

const actualizarLeyenda = async (leyendaActualizada) => {
  try {
    await axios.put(`http://localhost:8080/leyenda/${route.params.id}`, leyendaActualizada);
    router.push('/');
  } catch (error) {
    alert('Error al actualizar la leyenda. Por favor, inténtalo de nuevo.');
  }
};
</script>