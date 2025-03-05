<template>
  <nav>
    <router-link to="/">Inicio</router-link>
    <router-link to="/crear">Crear Leyenda</router-link>
  </nav>
</template>

<script setup>
</script>

<style scoped>
nav {
  width: 100%;
  background-color: #333;
  color: white;
  padding: 15px 20px;
  margin-bottom: 20px;
}

nav a {
  color: white;
  text-decoration: none;
  margin-right: 15px;
}

nav a:hover {
  text-decoration: none;
  background: linear-gradient(135deg, #6a11cb, #2575fc);
  border-radius: 10px;
  padding: 5px;
  transition: .6s;
}
</style>