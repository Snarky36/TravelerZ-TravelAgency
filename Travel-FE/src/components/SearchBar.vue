<template>
    <v-text-field :loading="loading" append-inner-icon="mdi-magnify" density="compact" label="Search destinations"
        variant="solo" hide-details single-line @click:append-inner="onClick"></v-text-field>
</template>

<script setup lang="ts">
import { ref } from "vue";

const loaded = ref(false);
const loading = ref(false);
const isHovered = ref(false);

const onClick = () => {
    loading.value = true;
    //o sa fac un request catre server
    setTimeout(() => {
        loading.value = false;
        loaded.value = true;
    }, 1000);
};
</script>

<style scoped></style>