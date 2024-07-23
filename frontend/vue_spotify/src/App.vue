<script setup>
import top_play_song from './components/top_play_song.vue'
import top_listen_song from './components/top_listen_song.vue'
import top_genre from './components/top_genre.vue'
import top_album from './components/top_album.vue'


</script>

<template>
  <div class="header">
    URSpotifyData
  </div>


  <div class="grid-container">
  <div class="grid-item">  <top_listen_song></top_listen_song>
  </div>
  <div class="grid-item">  <top_genre></top_genre>
  </div>  
  <div class="grid-item">  <top_album></top_album>
  </div>
 
  <div class="grid-item"><top_play_song></top_play_song></div>  
   
</div>


</template>

<style>
.grid-container {
  display: grid;
  grid-template-columns: auto  auto;
  padding: 150px;
}
.grid-item {
  padding: 10px;
  font-size: 30px;
  text-align: center;
}
</style>
