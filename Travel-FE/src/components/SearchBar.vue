<template>
    <v-text-field v-model="searchText" :loading="loading" append-inner-icon="mdi-magnify" density="compact" label="Search destinations"
    variant="solo" hide-details single-line @click:append-inner="onClick"></v-text-field>
</template>

<script setup lang="ts">
import { ref, defineEmits } from "vue";

const emit = defineEmits(["search"]);
const loaded = ref<Boolean>(false);
const loading = ref(false);
const isHovered = ref<Boolean>(false);
const searchText = ref<string>('');

const onClick = () => {
    loading.value = true;
    //o sa fac un request catre server
    setTimeout(() => {
        loading.value = false;
        search();
        loaded.value = true;
    }, 1000);
};

const search = () => {
    emit('search', searchText.value);
    console.log('Searching...');
  };
</script>

<style scoped></style>