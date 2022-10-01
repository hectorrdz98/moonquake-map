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

let moonquakeLocations = []
let moonquakeSphereLocations = []

export default {
  props: ['enableDarkSide'],
  name: 'MoonComponent',
  data() {
    return {
      textureURL: moonTexture,
      displacementURL: moonDisplacement,
      
    }
  },
  methods: {
    updateMoonquakeLocations(locations) {
      moonquakeLocations = locations.map((l) => ({
        lat: l['lat'],
        lng: l['long'],
        pointAlt: l['depth'] * 0.2 / 1200,
        maxAlt: l['depth'] * 0.2 / 1200,
        pointColor: this.getDepthColor(l['depth'])
      }))
      
      moonquakeSphereLocations = locations.map((l) => ({
        lat: l['lat'],
        lng: l['long'],
        objectAlt: (l['depth'] * 0.2 / 1200) + 0.02
      }))
      
      const satGeometry = new THREE.SphereGeometry(0.8)
      const satMaterial = new THREE.MeshLambertMaterial({ color: '#caf0f8', transparent: true, opacity: 1 })
      globeObject.objectThreeObject(() => new THREE.Mesh(satGeometry, satMaterial))
      globeObject.objectAltitude('objectAlt')

      globeObject.pointsData(moonquakeLocations)
      globeObject.objectsData(moonquakeSphereLocations)
    },
    getDepthColor(depth) {
      let depthMargin = depth % 300
      switch (depthMargin) {
        case 0: return '#184E77';
        case 1: return '#1A759F';
        case 2: return '#34A0A4';
        case 3: return '#76C893';
      }
      return '#B5E48C'
    },
    animateCycle() {
      controls.update()
      renderer.render(scene, camera)
      requestAnimationFrame(this.animateCycle)
    },
    animateLocations() {
      for (let i = 0; i < moonquakeLocations.length; ++i) {
        if (moonquakeLocations[i]['pointAlt'] === 0) {
          moonquakeLocations[i]['pointAlt'] = moonquakeLocations[i]['maxAlt']
        } else if (Math.random() < 0.1) {
          moonquakeLocations[i]['pointAlt'] = 0
        }
      }
      globeObject.pointsData(moonquakeLocations)
      setTimeout(this.animateLocations, 1000)
    },
    createGlobeObject() {
      globeObject = new ThreeGlobe()
          .globeImageUrl(this.textureURL)
          .bumpImageUrl(this.displacementURL)
          .showAtmosphere(false)
          .pointAltitude('pointAlt')
          .pointColor('pointColor')
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
      controls.zoomSpeed = 0.1
      controls.rotateSpeed = 0.1
    }
  },
  async mounted() {
    this.createGlobeObject()
    this.createRenderer()
    this.createScene()
    this.createCamera()
    this.createControls()
    this.animateCycle()
    this.animateLocations()
  }
}
</script>