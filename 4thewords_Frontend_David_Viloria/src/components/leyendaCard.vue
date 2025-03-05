<template>
  <div class="leyenda-card">
    <img :src="leyenda.imagen_url" :alt="leyenda.nombre" class="leyenda-imagen">
    <div class="leyenda-content">
      <h2 class="leyenda-nombre">{{ leyenda.nombre }}</h2>
      <p class="leyenda-categoria"><strong>Categoría:</strong> {{ leyenda.categoria }}</p>
      <p class="leyenda-fecha"><strong>Fecha:</strong> {{ leyenda.fecha }}</p>
      <p class="leyenda-ubicacion"><strong>Ubicación:</strong> {{ leyenda.provincia }}, {{ leyenda.canton }}, {{ leyenda.distrito }}</p>
      <p class="leyenda-descripcion">{{ leyenda.descripcion }}</p>
      <div class="leyenda-acciones">
        <button @click="editarLeyenda" class="btn-editar">Editar</button>
        <button @click="confirmarEliminarLeyenda" class="btn-eliminar">Eliminar</button>
      </div>
    </div>
  </div>
</template>

<script setup>
import { useRouter } from 'vue-router';
import Swal from 'sweetalert2';

const props = defineProps({
  leyenda: {
    type: Object,
    required: true,
  },
});

const emit = defineEmits(['eliminar']);

const router = useRouter();

const editarLeyenda = () => {
  router.push(`/editar/${props.leyenda.id}`);
};

const confirmarEliminarLeyenda = () => {
  Swal.fire({
    title: '¿Estás seguro?',
    text: "¡No podrás revertir esto!",
    icon: 'warning',
    showCancelButton: true,
    confirmButtonColor: '#3085d6',
    cancelButtonColor: '#d33',
    confirmButtonText: 'Sí, eliminar',
    cancelButtonText: 'Cancelar'
  }).then((result) => {
    if (result.isConfirmed) {
      eliminarLeyenda();
    }
  });
};

const eliminarLeyenda = () => {
  emit('eliminar', props.leyenda.id);
  Swal.fire(
    '¡Eliminado!',
    'La leyenda ha sido eliminada.',
    'success'
  );
};
</script>

<style scoped>
.leyenda-card {
  background-color: white;
  border-radius: 10px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  overflow: hidden;
  transition: transform 0.3s ease;
  width: 350px;
  height: 460px; 
  display: flex;
  flex-direction: column;
}

.leyenda-card:hover {
  transform: translateY(-5px);
}

.leyenda-imagen {
  width: 100%;
  height: 150px;
  object-fit: cover; 
}

.leyenda-content {
  padding: 15px;
  flex: 1;
  display: flex;
  flex-direction: column;
}

.leyenda-nombre {
  font-size: 1.5rem;
  margin: 0 0 10px;
}

.leyenda-categoria, .leyenda-fecha, .leyenda-ubicacion {
  color: #666;
  margin: 5px 0;
}

.leyenda-descripcion {
  margin: 10px 0;
  flex: 1; 
}

.leyenda-acciones {
  display: flex;
  gap: 10px;
  justify-content: center;
}

.btn-editar, .btn-eliminar {
  padding: 8px 16px;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  font-weight: bold;
}

.btn-editar {
  background-color: #3498db;
  color: white;
}

.btn-eliminar {
  background-color: #e74c3c;
  color: white;
}
</style>