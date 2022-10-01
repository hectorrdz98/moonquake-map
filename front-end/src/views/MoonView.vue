<template>
  <section></section>
  <section class="-z-10 absolute top-0 left-0 w-screen h-screen overflow-hidden">
    <MoonComponent ref="moonComponent" :enable-dark-side="true" />
  </section>
</template>

<script>
import MoonComponent from "../components/MoonComponent.vue";

export default {
  name: 'MoonView',
  components: {
    MoonComponent
  }
}
</script>