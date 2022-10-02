<template>
  <transition name="fade"
    enter-active-class="duration-500 ease-out"
    enter-from-class="transform opacity-0"
    enter-to-class="opacity-100"
    leave-active-class="duration-500 ease-in"
    leave-from-class="opacity-100"
    leave-to-class="transform opacity-0">
    <section v-if="step === 1">
      <section class="w-screen h-screen bg-gray-900/75 flex justify-center items-center flex-col gap-16 hide-section transition-all">
        <h1 class="text-6xl text-white font-bolder family-open-sans flex justify-center items-center flex-col gap-1.5">
          Explore the moon history with
          <span class="text-moon-gradient text-7xl">
            Moonquake Map 🦆
          </span>
        </h1>
        <button @click="changeStep(2)"
          class="px-8 py-4 rounded-2xl border border-white bg-transparent text-white family-open-sans font-bolder
          cursor-pointer transition-all duration-300 hover:bg-white hover:text-zinc-800">
          Launch App
        </button>
      </section>
      <section class="absolute bottom-0 w-screen text-center mb-4 hide-section transition-all">
        <p class="text-xs text-gray-500 font-light family-open-sans tracking-widest">
          Developed by Jesica, Antonio, André & Héctor
        </p>
      </section>
    </section>
  </transition>
  <transition name="fade"
    enter-active-class="delay-500 duration-500 ease-out"
    enter-from-class="transform opacity-0"
    enter-to-class="opacity-100"
    leave-active-class="duration-500 ease-in"
    leave-from-class="opacity-100"
    leave-to-class="transform opacity-0">
    <section v-if="step === 2">
      <div class="absolute bottom-0 left-0 m-4">
        <button @click="this.selectedMoonquake(Math.floor(Math.random() * this.moonquakeLocations.length))"
          class="bg-white hover:bg-blue-500 text-blue-700 font-semibold hover:text-white py-2 px-4 border border-blue-500 hover:border-transparent rounded">
          Show random!
        </button>
      </div>
      <div class="absolute bottom-0 right-0 m-4">
        <div class="p-2 bg-indigo-800 items-center text-indigo-100 leading-none lg:rounded-full flex lg:inline-flex
          cursor-pointer transition-all duration-300 hover:bg-indigo-600" role="alert"
          @click="closedMoonquake">
          <span class="flex rounded-full bg-indigo-500 uppercase px-2 py-1 text-xs font-bold mr-3">
            <i class="fas fa-stream"></i>
          </span>
          <span class="font-semibold mr-2 text-left flex-auto">
            Show events!
          </span>
          <svg class="fill-current opacity-75 h-4 w-4" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20">
            <path d="M12.95 10.707l.707-.707L8 4.343 6.586 5.757 10.828 10l-4.242 4.243L8 15.657l4.95-4.95z"/>
          </svg>
        </div>
      </div>
    </section>
  </transition>
  <section class="bg-moon-gradient -z-10 absolute top-0 left-0 w-screen h-screen overflow-hidden">
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
      moonquakeLocations: [],
      step: 1
    }
  },
  methods: {
    changeStep(nextStep) {
      this.step = nextStep
    },
    selectedMoonquake(index) {
      this.$refs.moonComponent.targetMoonquake(this.moonquakeLocations[index])
    },
    closedMoonquake() {
      this.$refs.moonComponent.returnToWholeView()
    },
    async loadMoonquakeLocation() {
      this.moonquakeLocations = [
        {
          'id': 1,
          'side': 'N',
          'lat': -15.7,
          'lat-err': 2.4,
          'long': -36.6,
          'long-err': 4.6,
          'depth': 900,
          'depth-err': 29,
          'assumed': false
        },
        {
          'id': 1,
          'side': 'N',
          'lat': -2.9,
          'lat-err': 1.7,
          'long': -50.3,
          'long-err': 6.3,
          'depth': 1200,
          'depth-err': 22,
          'assumed': false
        },
        {
          'id': 2,
          'side': 'N',
          'lat': 1.1,
          'lat-err': 94.2,
          'long': -44.7,
          'long-err': 16.4,
          'depth': 290,
          'depth-err': 109,
          'assumed': true
        },
        {
          'id': 3,
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
          'id': 4,
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