<template>
  <div id="canvasContainer" ref="rendered"></div>
</template>

<script>
import * as THREE from 'three'
import { OrbitControls } from 'three/examples/jsm/controls/OrbitControls.js'
import ThreeGlobe from 'three-globe'

import moonTexture from '/src/assets/moon-texture.png'
import moonDisplacement from '/src/assets/moon-displacement.png'

let globeObject = null
let renderer = null
let scene = null
let camera = null
let controls = null

export default {
  props: ['enableDarkSide'],
  name: 'MoonComponent',
  data() {
    return {
      textureURL: moonTexture,
      displacementURL: moonDisplacement
    }
  },
  methods: {
    updateMoonquakeLocations(locations) {
      let pointsData = locations.map((l) => ({
        lat: l['lat'],
        lng: l['long'],
        size: 0.2,
        color: 'red'
      }))
      globeObject.pointsData(pointsData)
    },
    animateCycle() {
      controls.update()
      renderer.render(scene, camera)
      requestAnimationFrame(this.animateCycle)
    },
    createGlobeObject() {
      globeObject = new ThreeGlobe()
          .globeImageUrl(this.textureURL)
          .bumpImageUrl(this.displacementURL)
          .showAtmosphere(false)
          .pointAltitude('size')
          .pointColor('color')
      let globeMaterial = globeObject.globeMaterial()
      globeMaterial.bumpScale = 10
    },
    createRenderer() {
      renderer = new THREE.WebGLRenderer()
      renderer.setSize(window.innerWidth, window.innerHeight)
      document.getElementById('canvasContainer').appendChild(renderer.domElement)
    },
    createScene() {
      scene = new THREE.Scene()
      scene.add(globeObject)
      scene.add(new THREE.AmbientLight(0xbbbbbb))
      scene.add(new THREE.DirectionalLight(0xffffff, 0.6))
    },
    createCamera() {
      camera = new THREE.PerspectiveCamera()
      camera.aspect = window.innerWidth / window.innerHeight
      camera.updateProjectionMatrix()
      camera.position.z = 300
    },
    createControls() {
      controls = new OrbitControls(
        camera,
        renderer.domElement
      )
      controls.enablePan = false
    }
  },
  async mounted() {
    this.createGlobeObject()
    this.createRenderer()
    this.createScene()
    this.createCamera()
    this.createControls()
    this.animateCycle()
  }
}
</script>