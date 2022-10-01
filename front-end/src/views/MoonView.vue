<template>
  <div id="canvasContainer" ref="rendered"></div>
</template>

<script>
import * as THREE from 'three'
import { OrbitControls } from 'three/examples/jsm/controls/OrbitControls'

import moonTexture from '/src/assets/moon-texture.png'
import moonDisplacement from '/src/assets/moon-displacement.png'

let scene = null
let camera = null
let renderer = null
let controls = null

let moon = null

let light = null
let hemiLight = null

export default {
  name: 'MoonView',
  data() {
    return {
      textureURL: moonTexture,
      displacementURL: moonDisplacement,
    }
  },
  methods: {
    setupThree() {
      scene = new THREE.Scene()
      camera = new THREE.PerspectiveCamera( 
          75, 
          window.innerWidth / window.innerHeight, 
          0.1, 
          1000
      )
      renderer = new THREE.WebGLRenderer()
      controls = new OrbitControls(
          camera, 
          renderer.domElement
      )
      controls.enablePan = false
    },
    setupCanvas() {
      renderer.setSize(window.innerWidth, window.innerHeight)
      this.$refs.rendered.appendChild(renderer.domElement)
    },
    setupCamera(x, y, z) {
      camera.position.x = x
      camera.position.y = y
      camera.position.z = z
    },
    rotateMoon(deltaX, deltaY, deltaZ) {
      moon.rotation.x += deltaX
      moon.rotation.y += deltaY
      moon.rotation.z += deltaZ
    },
    createMoonObject() {
      let geometry = new THREE.SphereGeometry(2,60,60)
      
      let textureLoader = new THREE.TextureLoader()
      let texture = textureLoader.load(this.textureURL)
      let displacementMap = textureLoader.load(this.displacementURL)
      let worldTexture = textureLoader.load(this.worldURL)

      let material = new THREE.MeshPhongMaterial(
        {
          color: 0xffffff ,
          map: texture ,
          displacementMap: displacementMap,
          displacementScale: 0.06,
          bumpMap: displacementMap,
          bumpScale: 0.04,
          reflectivity:0,
          shininess :0
        }
      )

      moon = new THREE.Mesh(geometry, material)
      scene.add(moon)
    },
    createLights() {
      light = new THREE.DirectionalLight(0xFFFFFF, 1)
      light.position.set(-100, 10,50)
      scene.add(light)

      hemiLight = new THREE.HemisphereLight(0xffffff, 0xffffff, 0.1)
      hemiLight.color.setHSL(0.6, 1, 0.6)
      hemiLight.groundColor.setHSL(0.095, 1, 0.75)
      hemiLight.position.set(0, 0, 0)
      scene.add(hemiLight)
    },
    animateMoon() {
      requestAnimationFrame(this.animateMoon)
      this.rotateMoon(0, 0.0005, 0)
      renderer.render(scene, camera)
    }
  },
  async mounted() {
    this.setupThree()
    this.setupCanvas()
    this.setupCamera(0, 0, 5)
    this.createMoonObject()
    this.createLights()
    this.animateMoon()
  }
}
</script>