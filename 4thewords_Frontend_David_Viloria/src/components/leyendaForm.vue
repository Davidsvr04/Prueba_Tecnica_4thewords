<template>
  <form @submit.prevent="guardarLeyenda" class="leyenda-form">
    <div class="form-group">
      <label for="nombre">Nombre</label>
      <input v-model="leyenda.nombre" id="nombre" required>
    </div>
    <div class="form-group">
      <label for="categoria">Categoría</label>
      <input v-model="leyenda.categoria" id="categoria" required>
    </div>
    <div class="form-group">
      <label for="descripcion">Descripción</label>
      <textarea v-model="leyenda.descripcion" id="descripcion" required></textarea>
    </div>
    <div class="form-group">
      <label for="fecha">Fecha</label>
      <input v-model="leyenda.fecha" type="date" id="fecha" required>
    </div>
    <div class="form-group">
      <label for="provincia">Provincia</label>
      <input v-model="leyenda.provincia" id="provincia" required>
    </div>
    <div class="form-group">
      <label for="canton">Cantón</label>
      <input v-model="leyenda.canton" id="canton" required>
    </div>
    <div class="form-group">
      <label for="distrito">Distrito</label>
      <input v-model="leyenda.distrito" id="distrito" required>
    </div>
    <div class="form-group">
      <label for="imagen_url">URL de la imagen</label>
      <input v-model="leyenda.imagen_url" id="imagen_url" type="url" required class="imagen-url">
    </div>
    <button type="submit" class="btn-guardar">Guardar</button>
  </form>
</template>

<script setup>
import { ref, watch } from 'vue';
import Swal from 'sweetalert2';

const props = defineProps({
  leyendaInicial: {
    type: Object,
    default: () => ({
      nombre: '',
      categoria: '',
      descripcion: '',
      fecha: '',
      provincia: '',
      canton: '',
      distrito: '',
      imagen_url: '',
    }),
  },
});

const emit = defineEmits(['guardar']);

const leyenda = ref({ ...props.leyendaInicial });

watch(() => props.leyendaInicial, (newVal) => {
  Object.assign(leyenda.value, newVal);
});

const guardarLeyenda = () => {
  const form = document.querySelector('.leyenda-form');
  if (form.checkValidity()) {
    Swal.fire({
      title: '¿Estás seguro?',
      text: "¿Quieres guardar esta leyenda?",
      icon: 'warning',
      showCancelButton: true,
      confirmButtonColor: '#3085d6',
      cancelButtonColor: '#d33',
      confirmButtonText: 'Sí, guardar',
      cancelButtonText: 'Cancelar'
    }).then((result) => {
      if (result.isConfirmed) {
        emit('guardar', leyenda.value);
        Swal.fire(
          '¡Guardado!',
          'La leyenda ha sido guardada.',
          'success'
        );
      }
    });
  } else {
    form.classList.add('was-validated');
  }
};
</script>

<style scoped>
/* ----- ESTILOS GENERALES ----- */
.leyenda-form {
  max-width: 500px;
  margin: 40px auto;
  padding: 25px;
  border-radius: 12px;
  background: rgba(255, 255, 255, 0.1);
  backdrop-filter: blur(10px);
  box-shadow: 0 8px 16px rgba(0, 0, 0, 0.15);
  font-family: 'Inter', sans-serif;
  border: 1px solid rgba(255, 255, 255, 0.2);
  animation: fadeIn 0.5s ease-in-out;
}

/* ----- INPUTS Y TEXTAREA ----- */
.form-group {
  margin-bottom: 20px;
}

.form-group label {
  display: block;
  font-weight: 600;
  margin-bottom: 6px;
  color: #333;
  font-size: 14px;
}

.form-group input,
.form-group textarea {
  width: 95%;
  padding: 12px;
  font-size: 14px;
  border-radius: 8px;
  border: 1px solid rgba(0, 0, 0, 0.2);
  background: rgba(255, 255, 255, 0.6);
  transition: all 0.3s ease;
}

.form-group textarea {
  min-height: 120px;
  resize: vertical;
}

/* Efecto de enfoque */
.form-group input:focus,
.form-group textarea:focus {
  border-color: #6a11cb;
  box-shadow: 0 0 8px rgba(106, 17, 203, 0.3);
  outline: none;
  background: rgba(255, 255, 255, 0.9);
}

/* ----- BOTÓN GUARDAR ----- */
.btn-guardar {
  width: 100%;
  padding: 14px;
  font-size: 16px;
  font-weight: bold;
  color: white;
  background: linear-gradient(135deg, #6a11cb, #2575fc);
  border: none;
  border-radius: 8px;
  cursor: pointer;
  transition: all 0.3s ease-in-out;
  text-transform: uppercase;
  letter-spacing: 1px;
  box-shadow: 0 4px 10px rgba(106, 17, 203, 0.2);
}

/* Efecto hover y active */
.btn-guardar:hover {
  background: linear-gradient(135deg, #5b0e9f, #1e63d4);
  transform: translateY(-2px);
  box-shadow: 0 6px 14px rgba(106, 17, 203, 0.3);
}

.btn-guardar:active {
  transform: scale(0.98);
  box-shadow: 0 2px 6px rgba(106, 17, 203, 0.2);
}

/* ----- EFECTOS RESPONSIVOS ----- */
@media (max-width: 600px) {
  .leyenda-form {
    padding: 20px;
  }

  .btn-guardar {
    font-size: 14px;
    padding: 12px;
  }
}

/* ----- ANIMACIÓN DE ENTRADA ----- */
@keyframes fadeIn {
  from {
    opacity: 0;
    transform: translateY(-10px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}


</style>