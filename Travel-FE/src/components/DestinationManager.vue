<template>
  <div class="main-div" :style="{ width: mainDivWidth }">
    <div class="title">{{ props.Title }}</div>
    <div class="content">
      <div v-for="(card, index) in filteredDestinations" :key="index" :style="{ width: cardWidth }">
        <DestinationCards :imageSrc="card.imageSrc" :cardBeginDate="card.beginDate" :cardEndDate="card.endDate"
          :cardTitle="card.title" :cardLocation="card.location" :cardDescription="card.description"
          :cardPrice="card.price" :cardDays="card.days" :displayButton="card.displayButton" />
      </div>
    </div>
  </div>
</template>

<script setup>
import DestinationCards from '@/components/DestinationCards.vue';
import { ref, defineProps, computed, watchEffect } from 'vue'
import SearchFilter from '@/DataTypes/SearchFilter.ts';
const beginDate = ref('15.02.2024');
const endDate = ref('22.02.2024');
const filteredDestinations = ref([{}, {}]);
const cardWidth = ref("calc(33.33% - 20px)");

const props = defineProps({
  Title: String,
  Filters: SearchFilter | null,
  ItemsPerRaw: Number | null,
  DisplaySeeMoreButton: Boolean
});

const destinationList = ref([
  {
    imageSrc: '../src/assets/schi.png',
    beginDate: beginDate,
    endDate: endDate,
    title: 'Baia Mare',
    location: 'Romania',
    description: 'Baia mare sunper faina aaa',
    price: 300,
    days: 7,
    displayButton: props.DisplaySeeMoreButton,
  },
  {
    imageSrc: '../src/assets/ImageMalta.png',
    beginDate: beginDate,
    endDate: endDate,
    title: 'Baia Mare',
    location: 'Romania',
    description: 'Baia mare sunper faina aaa',
    price: 300,
    days: 7,
    displayButton: props.DisplaySeeMoreButton,
  },
  {
    imageSrc: '../src/assets/hotel.png',
    beginDate: beginDate,
    endDate: endDate,
    title: 'Baia Mare',
    location: 'Romania',
    description: 'Baia mare sunper faina aaa',
    price: 300,
    days: 7,
    displayButton: props.DisplaySeeMoreButton,
  },
  {
    imageSrc: '../src/assets/schi.png',
    beginDate: beginDate,
    endDate: endDate,
    title: 'Paris',
    location: 'Ro',
    description: 'Baia mare sunper faina aaa',
    price: 300,
    days: 7,
    displayButton: props.DisplaySeeMoreButton,
  },
  {
    imageSrc: '../src/assets/corali.png',
    beginDate: beginDate,
    endDate: endDate,
    title: 'Londra',
    location: 'Ro',
    description: 'Baia mare sunper faina aaa',
    price: 300,
    days: 7,
    displayButton: props.DisplaySeeMoreButton,
  },
  {
    imageSrc: '../src/assets/baiamare.png',
    beginDate: beginDate,
    endDate: endDate,
    title: 'Craiova',
    location: 'Romania',
    description: 'Baia mare sunper faina aaa',
    price: 300,
    days: 7,
    displayButton: props.DisplaySeeMoreButton,
  },
]);

function checkCardWith() {
  // console.log('ItemsPerRaw:', props.ItemsPerRaw);
  // console.log('filteredDestinations:', filteredDestinations.value?.length);
  if (props.ItemsPerRaw === null) return `calc(33.33% - 20px)`;
  if (props.ItemsPerRaw > filteredDestinations.value?.length) return `calc(${100.0 / filteredDestinations.value.length}% - 20px)`;
  if (props.ItemsPerRaw <= 6) return `calc(${100.0 / props.ItemsPerRaw}% - 20px)`;
  return `calc(16.666666666666668% - 20px)`;
}


const mainDivWidth = computed(() => {
  if (props.ItemsPerRaw !== null && props.ItemsPerRaw > 4) return "100%";
  return "60%";
});

function filterDestinations(filters) {
  return destinationList.value.filter((destination) => {
    return destination.title.toLowerCase().includes(filters.place?.toLowerCase()) || filters.place?.toLowerCase().includes(destination.title.toLowerCase())
      || destination.location.toLowerCase().includes(filters.location?.toLowerCase()) || filters.location?.toLowerCase().includes(destination.location.toLowerCase())
      || destination.beginDate <= filters.startDate || destination.endDate >= filters.endDate
      || destination.price <= filters.price
      || destination.days <= filters.days
  });
}


watchEffect(() => {
  if (EnsureFilters()) {
    filteredDestinations.value = filterDestinations(props.Filters);
  } else {
    filteredDestinations.value = destinationList.value;
  }
  cardWidth.value = checkCardWith();
});

function EnsureFilters() {
  if (props.Filters === null || props.Filters === undefined) return false;
  const result = props.Filters?.place !== null
    || props.Filters?.startDate !== null
    || props.Filters?.endDate !== null
    || props.Filters?.location !== null
    || props.Filters?.price !== null
    || props.Filters?.days !== null;
  // console.log('EnsureFilters:', result);
  return result;
}
</script>

<style scoped>
.main-div {
  display: grid;
  place-items: center;
}

.title {
  color: var(--TitleColor, #3d3e48);
  white-space: nowrap;
  font: 700 28px/120% Poppins, sans-serif;
}

@media (max-width: 991px) {
  .title {
    white-space: initial;
  }
}

.content {
  margin-top: 100px;
  display: flex;
  flex-wrap: wrap;
  gap: 20px;
}

/* .content > * {
  width: calc(33.33% - 20px); 
}

@media (max-width: 768px) {
  .content > * {
    width: calc(50% - 20px); 
  }
} */
</style>