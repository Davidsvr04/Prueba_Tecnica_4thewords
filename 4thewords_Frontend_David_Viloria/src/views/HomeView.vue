<template>
  <div>
    <NavBar />
    <header class="hero-section">
      <div class="hero-content">
        <h1>Bienvenido a Leyendas</h1>
        <p>Descubre las leyendas más fascinantes de nuestra cultura.</p>
        <button class="cta-button">Explorar</button>
      </div>
    </header>
    <section class="filtros-section">
      <h2>Filtrar Leyendas</h2>
      <div class="filtros-container">
        <input v-model="filtros.nombre" placeholder="Nombre" />
        <input v-model="filtros.categoria" placeholder="Categoría" />
        <input v-model="filtros.fecha" type="date" placeholder="Fecha" />
        <input v-model="filtros.provincia" placeholder="Provincia" />
        <input v-model="filtros.canton" placeholder="Cantón" />
        <input v-model="filtros.distrito" placeholder="Distrito" />
        <button @click="aplicarFiltros">Aplicar Filtros</button>
      </div>
    </section>
    <section class="leyendas-section">
      <h2>Nuestras Leyendas</h2>
      <div class="leyendas-container">
        <LeyendaCard
          v-for="leyenda in leyendasFiltradas"
          :key="leyenda.id"
          :leyenda="leyenda"
          @eliminar="eliminarLeyenda"
        />
      </div>
    </section>
    <footer class="footer">
      <p>&copy; 2025 Leyendas. Todos los derechos reservados.</p>
    </footer>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue';
import axios from 'axios';
import LeyendaCard from '../components/leyendaCard.vue';
import NavBar from '../components/NavBar.vue';

const leyendas = ref([]);
const filtros = ref({
  nombre: '',
  categoria: '',
  fecha: '',
  provincia: '',
  canton: '',
  distrito: ''
});

onMounted(async () => {
  const response = await axios.get('http://localhost:8080/leyenda/');
  leyendas.value = response.data;
});

const eliminarLeyenda = async (id) => {
  await axios.delete(`http://localhost:8080/leyenda/${id}`);
  leyendas.value = leyendas.value.filter((leyenda) => leyenda.id !== id);
};

const aplicarFiltros = () => {
};

const leyendasFiltradas = computed(() => {
  return leyendas.value.filter((leyenda) => {
    return (
      (!filtros.value.nombre || leyenda.nombre.toLowerCase().includes(filtros.value.nombre.toLowerCase())) &&
      (!filtros.value.categoria || leyenda.categoria.toLowerCase().includes(filtros.value.categoria.toLowerCase())) &&
      (!filtros.value.fecha || leyenda.fecha === filtros.value.fecha) &&
      (!filtros.value.provincia || leyenda.provincia.toLowerCase().includes(filtros.value.provincia.toLowerCase())) &&
      (!filtros.value.canton || leyenda.canton.toLowerCase().includes(filtros.value.canton.toLowerCase())) &&
      (!filtros.value.distrito || leyenda.distrito.toLowerCase().includes(filtros.value.distrito.toLowerCase()))
    );
  });
});
</script>

<style scoped>
.hero-section {
  position: relative;
  height: 60vh;
  background: url('/path/to/your/hero-image.jpg') no-repeat center center/cover;
  display: flex;
  align-items: center;
  justify-content: center;
  text-align: center;
  overflow: hidden;
}

.hero-content {
  position: relative;
  max-width: 600px;
  z-index: 1;
  animation: fadeIn 1s ease-in-out;
}

.hero-content h1 {
  font-size: 3rem;
  font-weight: bold;
  margin-bottom: 10px;
}

.hero-content p {
  font-size: 1.2rem;
  opacity: 0.9;
}

.cta-button {
  display: inline-block;
  padding: 12px 24px;
  font-size: 16px;
  font-weight: bold;
  color: white;
  background: linear-gradient(135deg, #ff7e5f, #feb47b);
  border: none;
  border-radius: 8px;
  cursor: pointer;
  transition: all 0.3s ease-in-out;
  margin-top: 20px;
  box-shadow: 0 4px 10px rgba(255, 126, 95, 0.2);
}

.cta-button:hover {
  transform: translateY(-3px);
  box-shadow: 0 6px 14px rgba(255, 126, 95, 0.3);
}

.cta-button:active {
  transform: scale(0.98);
}

.leyendas-section {
  padding: 60px 20px;
  background-color: #f3f3f3;
  text-align: center;
}

.leyendas-section h2 {
  font-size: 2.5rem;
  margin-bottom: 30px;
  font-weight: bold;
  color: #333;
}

.leyendas-container {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 20px;
  max-width: 1200px;
  margin: 0 auto;
  padding: 10px;
}

.footer {
  background: #222;
  color: white;
  text-align: center;
  padding: 20px 0;
  margin-top: 50px;
  font-size: 14px;
}

.footer p {
  margin: 0;
  opacity: 0.8;
}

@media (max-width: 768px) {
  .hero-content h1 {
    font-size: 2.2rem;
  }

  .hero-content p {
    font-size: 1rem;
  }

  .leyendas-section h2 {
    font-size: 2rem;
  }

  .cta-button {
    font-size: 14px;
    padding: 10px 20px;
  }
}

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
.filtros-section {
  padding: 40px 20px;
  background-color: #f9f9f9;
  text-align: center;
}

.filtros-container {
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
  justify-content: center;
}

.filtros-container input {
  padding: 10px;
  border: 1px solid #ddd;
  border-radius: 5px;
  width: 200px;
}

.filtros-container button {
  padding: 10px 20px;
  background-color: #2ecc71;
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  font-weight: bold;
}

.filtros-container button:hover {
  background-color: #27ae60;
}
</style>