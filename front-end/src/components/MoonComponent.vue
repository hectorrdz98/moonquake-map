<template>
  <div id="canvasContainer" ref="rendered"></div>
</template>

<script>
import * as THREE from 'three'
import { TrackballControls } from 'three/examples/jsm/controls/TrackballControls.js'
import ThreeGlobe from 'three-globe'

import moonTexture from '/src/assets/moon-texture.png'
import moonDisplacement from '/src/assets/moon-displacement.png'

let globeMaterial = null
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
    getPointsData() {
      let N = 20
      return [...Array(N).keys()].map(() => ({
        lat: (Math.random() - 0.5) * 180,
        lng: (Math.random() - 0.5) * 360,
        size: Math.random() / 3,
        color: 'white'
      }))
    },
    animateCycle() {
      (function animate() {
        controls.update()
        renderer.render(scene, camera)
        requestAnimationFrame(animate)
      })()
    },
    createGlobeObject() {
      globeObject = new ThreeGlobe()
          .globeImageUrl(this.textureURL)
          .bumpImageUrl(this.displacementURL)
          // .globeMaterial(globeMaterial)
          .showAtmosphere(false)
          .pointsData(this.getPointsData())
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
      controls = new TrackballControls(camera, renderer.domElement)
      controls.minDistance = 101
      controls.rotateSpeed = 5
      controls.zoomSpeed = 0.8
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