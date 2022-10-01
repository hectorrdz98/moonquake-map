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
  },
  data() {
    return {
      moonquakeLocations: []
    }
  },
  methods: {
    async loadMoonquakeLocation() {
      this.moonquakeLocations = [
        {
          'side': 'N',
          'lat': -15.7,
          'lat-err': 2.4,
          'long': -36.6,
          'long-err': 4.6,
          'depth': 867,
          'depth-err': 29,
          'assumed': false
        },
        {
          'side': 'N',
          'lat': -2.9,
          'lat-err': 1.7,
          'long': -50.3,
          'long-err': 6.3,
          'depth': 946,
          'depth-err': 22,
          'assumed': false
        },
        {
          'side': 'N',
          'lat': 1.1,
          'lat-err': 94.2,
          'long': -44.7,
          'long-err': 16.4,
          'depth': 933,
          'depth-err': 109,
          'assumed': true
        },
        {
          'side': 'N',
          'lat': 43.5,
          'lat-err': 2.9,
          'long': 55.5,
          'long-err': 9.5,
          'depth': 844,
          'depth-err': 33,
          'assumed': false
        },
        {
          'side': 'N',
          'lat': 25,
          'lat-err': 1.7,
          'long': 53.2,
          'long-err': 8,
          'depth': 893,
          'depth-err': 27,
          'assumed': false
        }
      ]
      this.$refs.moonComponent.updateMoonquakeLocations(this.moonquakeLocations)
    }
  },
  async mounted() {
    await this.loadMoonquakeLocation()
  }
}
</script>