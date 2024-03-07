<template>
      <v-card
        class="footer-body"
        flat
        tile
      >
        <v-card-title class="teal">
            You can follow us on:
            <v-btn
              class="mx-4 icons"
              size="small"
              variant="plain"
            ><span class="pi pi-twitter icon"></span></v-btn>
            <v-btn
              class="mx-4 icons"
              size="small"
              variant="plain"
            ><span class="pi pi-facebook icon"></span></v-btn>
            <v-btn
              class="mx-4 icons"
              size="small"
              variant="plain"
            ><span class="pi pi-linkedin icon"></span></v-btn>
            <v-btn
              class="mx-4 icons"
              size="small"
              variant="plain"
            ><span class="pi pi-telegram icon"></span></v-btn>
        </v-card-title>
        <v-card-text class="py-2 white--text text-center">
          {{ new Date().getFullYear() }} — <strong>TravelerZ</strong>
        </v-card-text>
      </v-card>
</template>

<script setup lang="ts">
    import 'primeicons/primeicons.css'
</script>

<style scoped>
  .icons{
    width: 50px;
    height: 50px;
    border-radius: 100%;
  }
  .icons .icon{
    font-size: 40px;
    color: white;
  }
  .footer-body {
    object-position: center;
    background-color: var(--TravelTheme, #5bb0c4);
    height: 100px;
  }
  @media (max-width: 991px) {
    .img {
      max-width: 100%;
      margin-top: 40px;
    }
  }
</style>