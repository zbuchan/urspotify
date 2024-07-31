<script setup>
import { ref, computed, onMounted } from 'vue';

const flaskGreeting = ref({
  most_played_tracks: {}
});



const sortedMostPlayedTracks = computed(() => {
  return Object.entries(flaskGreeting.value.most_played_tracks)
    .sort((a, b) => b[1] - a[1])
    .map(([key, value]) => ({ key, value }));
});



const fetchFlaskGreeting = () => {
  fetch('http://localhost:5000/track', { method: 'GET' })
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
        <h2>Top Played Songs</h2>
          <div v-for="(item, index) in sortedMostPlayedTracks" :key="index">
            <p>{{ item.key }}: {{ item.value }}</p>
            <pre> </pre>
          </div>
      </div>
      
      

      
    </div>
  </div>

</template>


