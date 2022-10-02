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
<!--        <button @click="this.selectedMoonquake(Math.floor(Math.random() * this.moonquakeLocations.length))"-->
<!--          class="bg-white hover:bg-blue-500 text-blue-700 font-semibold hover:text-white py-2 px-4 border border-blue-500 hover:border-transparent rounded">-->
<!--          Show random!-->
<!--        </button>-->
      </div>
      <transition name="fade"
        enter-active-class="duration-500 ease-out"
        enter-from-class="transform opacity-0"
        enter-to-class="opacity-100"
        leave-active-class="duration-500 ease-in"
        leave-from-class="opacity-100"
        leave-to-class="transform opacity-0">
        <div v-if="currentMoonquake != null" class="absolute top-1/2 left-1/2 m-4 overflow-hidden rounded-lg">
          <div class="block max-w-sm border shadow-md bg-gray-800 border-gray-700">
            <div class="relative px-6 pt-6 flex justify-between items-center">
              <div class="mb-2 flex justify-start items-center">
                <h5 class="text-2xl font-bold tracking-tight text-gray-900 dark:text-white">
                  ID: {{ currentMoonquake['id'] }}
                </h5>
                <div class="text-xs inline-flex items-center font-bold leading-sm uppercase p-2
                  bg-gunmetal-two text-white/90 rounded-full ml-4 h-4">
                  {{ currentMoonquake['year'] }}
                </div>
              </div>
              <div class="absolute top-0 right-0 h-40 w-40 -mr-20 -mt-20 bg-gunmetal-two rounded-full">
                <template v-if="currentMoonquake['side'] === 'N'">
                  <span class="absolute bottom-0 left-0 ml-10 mb-8 text-white/80 text-2xl">
                    <i class="fas fa-moon"></i>
                  </span>
                </template>
                <template v-else-if="currentMoonquake['side'] === 'F'">
                  <span class="absolute bottom-0 left-0 ml-10 mb-8 text-black/70 text-2xl">
                    <i class="fas fa-moon"></i>
                  </span>
                </template>
              </div>
            </div>
            <p class="mb-6 px-6 font-normal text-gray-700 dark:text-gray-400">
              <template v-if="currentMoonquake['lat-err'] != null">
                Lat: {{ currentMoonquake['lat'] }} (± {{ currentMoonquake['lat-err'] }})<br>
              </template>
              <template v-else>
                Lat: {{ currentMoonquake['lat'] }}<br>
              </template>
              <template v-if="currentMoonquake['long-err'] != null">
                Lat: {{ currentMoonquake['long'] }} (± {{ currentMoonquake['long-err'] }})<br>
              </template>
              <template v-else>
                Lat: {{ currentMoonquake['long'] }}<br>
              </template>
              Depth: {{ currentMoonquake['depth'] }}<br>
            </p>
            <div class="px-6 pb-6 flex items-center justify-start">
              <template v-if="currentMoonquake['type'] === 'moonquake'">
                <div class="text-xs inline-flex items-center font-bold leading-sm uppercase px-3 py-1 
                  bg-red-200 text-red-700 rounded-full mr-4 h-8">
                  <span class="material-symbols-outlined mr-2">
                    blur_circular
                  </span>
                  Moonquake
                </div>
                <div class="text-xs inline-flex items-center font-bold leading-sm uppercase px-3 py-1 
                  bg-red-100 text-red-500 rounded-full h-8">
                  {{ currentMoonquake['sub-type'] }}
                </div>
              </template>
              <template v-else-if="currentMoonquake['type'] === 'artificial-impact'">
                <div class="text-xs inline-flex items-center font-bold leading-sm uppercase px-3 py-1 
                  bg-blue-200 text-blue-700 rounded-full mr-4 h-8">
                  <span class="material-symbols-outlined mr-2">
                    precision_manufacturing
                  </span>
                  Artificial Impact
                </div>
                <div class="text-xs inline-flex items-center font-bold leading-sm uppercase px-3 py-1 
                  bg-blue-100 text-blue-500 rounded-full h-8">
                  {{ currentMoonquake['sub-type'] }}
                </div>
              </template>
            </div>
          </div>
        </div>
      </transition>
      <transition name="fade"
        enter-active-class="delay-500 duration-500 ease-out"
        enter-from-class="transform opacity-0"
        enter-to-class="opacity-100"
        leave-active-class="duration-500 ease-in"
        leave-from-class="opacity-100"
        leave-to-class="transform opacity-0">
        <div v-if="!showEvents"
          class="absolute bottom-0 right-0 m-4 
          p-2 bg-indigo-800 items-center text-indigo-100 leading-none rounded-full flex 
          cursor-pointer transition-all duration-300 hover:bg-indigo-600" role="alert"
          @click="showEvents = true">
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
      </transition>
      <transition name="fade"
        enter-active-class="delay-500 duration-500 ease-out"
        enter-from-class="transform opacity-0"
        enter-to-class="opacity-100"
        leave-active-class="duration-500 ease-in"
        leave-from-class="opacity-100"
        leave-to-class="transform opacity-0">
        <div v-if="showEvents" class="absolute bottom-0 right-0 m-4 flex flex-col justify-start items-end gap-4">
          <div class="max-h-96 p-4 bg-indigo-800 text-indigo-100 
            flex justify-start items-start flex-col rounded-2xl">
            <h1 class="w-full text-2xl text-white/80 font-bolder family-open-sans text-center">
              Found events
            </h1>
            <div class="w-full overflow-y-auto mt-4 h-full bg-indigo-900/80 text-indigo-800 flex justify-start 
              items-start flex-col rounded-2xl p-4">
              <div v-for="(l, index) in moonquakeLocations" @click="selectedMoonquake(index)"
                :class="'w-full flex justify-between items-center gap-4 cursor-pointer ' +
                'p-2 rounded-2xl transition-all duration-300 ' +
                (selectedIndex === index ? 'bg-indigo-600/60' : 'hover:bg-indigo-600/60')">
                <h5 class="text-lg font-normal tracking-tight text-gray-900 dark:text-white text-left">
                  <i class="fas fa-circle text-xs text-white/80 mr-2"></i>
                  {{ l['type'] === 'moonquake' ? 'Moonquake' : 'Artificial Impact' }} ({{ l['id'] }})
                </h5>
                <div class="text-xs inline-flex items-center font-bold leading-sm uppercase p-2
                  bg-gunmetal-two text-white/90 rounded-full h-4">
                  {{ l['year'] }}
                </div>
              </div>
            </div>
          </div>
          <div class="p-2 bg-indigo-800 items-center text-indigo-100 rounded-full flex
            cursor-pointer transition-all duration-300 hover:bg-indigo-600" role="alert"
            @click="closedMoonquake">
            <span class="flex rounded-full bg-indigo-500 uppercase px-2 py-1 text-xs font-bold mr-3">
              <i class="fas fa-times"></i>
            </span>
            <span class="font-semibold mr-2 text-left flex-auto">
              Hide events!
            </span>
            <svg class="fill-current opacity-75 h-4 w-4" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20">
              <path d="M12.95 10.707l.707-.707L8 4.343 6.586 5.757 10.828 10l-4.242 4.243L8 15.657l4.95-4.95z"/>
            </svg>
          </div>
        </div>
      </transition>
    </section>
  </transition>
  <section class="bg-moon-gradient -z-10 absolute top-0 left-0 w-screen h-screen overflow-hidden">
    <MoonComponent ref="moonComponent" :enable-dark-side="true" />
  </section>
</template>

<script>
import MoonComponent from "../components/MoonComponent.vue";
import MoonquakeService from "../services/MoonquakeService";

export default {
  name: 'MoonView',
  components: {
    MoonComponent
  },
  data() {
    return {
      moonquakeLocations: [],
      currentMoonquake: null,
      showEvents: false,
      selectedIndex: null,
      step: 1
    }
  },
  methods: {
    changeStep(nextStep) {
      this.step = nextStep
    },
    selectedMoonquake(index) {
      this.selectedIndex = index
      this.$refs.moonComponent.targetMoonquake(this.moonquakeLocations[index])
      this.currentMoonquake = this.moonquakeLocations[index]
    },
    closedMoonquake() {
      this.showEvents = false
      this.selectedIndex = null
      this.$refs.moonComponent.returnToWholeView()
      this.currentMoonquake = null
    },
    async loadMoonquakeLocation() {
      let getMoonquakesResponse = await MoonquakeService.searchMoonquakes([])
      if (getMoonquakesResponse.status === 200) {
        this.moonquakeLocations = getMoonquakesResponse.data.map(l => {
          return {
            'id': l[0],
            'side': l[7] !== '' ? l[7] : 'N',
            'type': l[5],
            'sub-type': l[6],
            'year': l[8] !== '' ? parseFloat(l[8]) : null,
            'lat': l[1] !== '' ? parseFloat(l[1]) : null,
            'lat-err': l[2] !== '' ? parseFloat(l[2]) : null,
            'long': l[3] !== '' ? parseFloat(l[3]) : null,
            'long-err': l[4] !== '' ? parseFloat(l[4]) : null,
            'depth': l[9] !== '' ? parseFloat(l[9]) : null,
            'depth-err': l[10] !== '' ? parseFloat(l[10]) : null,
            'assumed': l[11] === 'Y'
          }
        })
      }
      this.$refs.moonComponent.updateMoonquakeLocations(this.moonquakeLocations)
    }
  },
  async mounted() {
    await this.loadMoonquakeLocation()
  }
}
</script>