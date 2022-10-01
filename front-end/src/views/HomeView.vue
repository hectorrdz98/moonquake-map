<template>
  <h1 class="text-3xl font-bold underline text-blue-600 cursor-pointer transition-all hover:text-blue-300">
    Home
  </h1>
  <router-link :to="{ 'name': 'moon' }">
    Moon
  </router-link>
</template>

<script>
export default {
  name: 'HomeView'
}
</script>