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
        <h2>Top Songs</h2>         
  <table class="table table-striped">
    

    <tbody>
      <tr v-for="(item, index) in sortedMostPlayedTracks" :key="index">
        <td>{{ item.key }}</td>
        <td>{{ item.value }}</td>
      </tr>
    </tbody>
    </table>
      </div>
      
      

      
    </div>
  </div>







  
</template>


