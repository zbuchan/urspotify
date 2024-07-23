<script setup>
import { ref, computed, onMounted } from 'vue';

const flaskGreeting = ref({
  
  top_artists: {}
});


const sortedTopArtists = computed(() => {
  return Object.entries(flaskGreeting.value.top_artists)
    .sort((a, b) => b[1] - a[1])
    .map(([key, value]) => ({ key, value }));
});



const fetchFlaskGreeting = () => {
  fetch('http://localhost:5000/artist', { method: 'GET' })
    .then(response => response.json())
    .then(data => {
      flaskGreeting.value = data;
      
    });
};



onMounted(() => {
  fetchFlaskGreeting();
});
</script>

<template>
  
  

  <div id="app">
    <div class="row"> 
      
      
      <div class="column">
        <h2>Top Listened to Artist</h2>
          <div v-for="(item, index) in sortedTopArtists" :key="index">
            <p>{{ item.key }}: {{ item.value }}</p>
          </div>
      </div>

      
    </div>
  </div>

</template>


