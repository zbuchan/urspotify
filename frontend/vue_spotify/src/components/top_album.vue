<template>


    <div id="app">
      <div class="row"> 
        
  
        <div class="column">
          <h2>Top Albums</h2>
            <div v-for="(item, index) in sortedTopAlbums" :key="index">
              <p>{{ item.key }}: {{ item.value }}</p>
            </div>
        </div>
  
      </div>
    </div>
  
  </template>


<script setup>
import { ref, computed, onMounted } from 'vue';

const flaskGreeting = ref({
  
  top_album: {}
});





const sortedTopAlbums = computed(() => {
  return Object.entries(flaskGreeting.value.top_album)
    .sort((a, b) => b[1] - a[1])
    .map(([key, value]) => ({ key, value }));
});

const fetchFlaskGreeting = () => {
  fetch('http://localhost:5000/album', { method: 'GET' })
    .then(response => response.json())
    .then(data => {
      flaskGreeting.value = data;
      
    });
};



onMounted(() => {
  fetchFlaskGreeting();
});
</script>




