<template>
  <div class="main-div" :style="{ width: mainDivWidth }">
    <div class="title">{{ props.Title }}</div>
    <div class="content">
      <div v-for="(card, index) in filteredDestinations" :key="index" :style="{ width: cardWidth }">
        <DestinationCards :imageSrc="`../src/assets/${card.image}`" :availabilities="card.availabilities"
          :cardTitle="card.name" :cardLocation="card.location" :cardDescription="card.description"
          :cardPrice="card.price" :cardDays="card.days" :displayButton="card.displayButton? card.displayButton: true" 
          :isAdmin="isAdmin" :discount=card.discountPercent :cardGuid="card.destination_guid" 
          @destinationDeleted="handleDestinationDeleted"
          @destinationUpdated="handleDestinationUpdated"/>
      </div>
    </div>
  </div>
</template>

<script setup>
import DestinationCards from '@/components/DestinationCards.vue';
import { ref, defineProps, computed, watchEffect } from 'vue'
import SearchFilter from '@/DataTypes/SearchFilter.ts';
import { useAppStore } from '@/stores/appStore';
import axios from 'axios';
const appStore = useAppStore();

const beginDate = ref('');
const endDate = ref('');
const filteredDestinations = ref([{}, {}]);
const destinationList = ref([{}, {}]);
const cardWidth = ref("calc(33.33% - 20px)");
const destinationUpdated = ref(false);
const destinationDeleted = ref(false);

const props = defineProps({
  Title: String,
  Filters: SearchFilter | null,
  ItemsPerRaw: Number | null,
  DisplaySeeMoreButton: Boolean,
  isAdmin: Boolean,
  newDestinationAdded: Boolean,
  showDiscountCards: String,
});


const getDestinations = async () => {
  //console.log('getDestinations',);
  try {
    const response = await axios.get(appStore.getRootUrl() + '/api/destinations');

    if(response.status !== 200) {
      console.error('Error fetching destinations:', response.data);
      return;
    }

    if(props.showDiscountCards === "discount"){
      destinationList.value = response.data.filter((destination) => destination.discountPercent > 0);
    } else if(props.showDiscountCards === "fullPrice"){
      destinationList.value = response.data.filter((destination) => destination.discountPercent == 0);
    }else{
      destinationList.value = response.data;
    }

  } catch (error) {
    console.error('Error fetching destinations:', error);
  }
};
getDestinations();


const destinationList2 = ref([
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
  let filteringDate = false;
  let filterStartDate = new Date();
  let filterEndDate = new Date();
  if(filters.startDate !== null && filters.endDate !== null){
  filterStartDate = filters.startDate;
  filterEndDate = filters.endDate;
  filteringDate = true;
  console.log('filterStartDate:', filterStartDate);
  console.log('filterEndDate:', filterEndDate);
  }
  return destinationList.value.filter((destination) => {
    if(destination.availabilities?.length > 0){
      beginDate.value = new Date(destination.availabilities[0].startDate);
      endDate.value = new Date(destination.availabilities[0].endDate);
      console.log('beginDate:', beginDate.value);
      console.log('endDate:', endDate.value);
    }
    console.log("result" ,(beginDate.value >= filters.startDate && endDate.value <= filters.endDate))
    const locationFilter = destination.name.toLowerCase().includes(filters.place?.toLowerCase()) || filters.place?.toLowerCase().includes(destination.name.toLowerCase())
    const dateFilter = filteringDate ? (beginDate.value >= filters.startDate && endDate.value <= filters.endDate) : true;

    return locationFilter && dateFilter
      // || destination.price <= filters.price
      // || destination.days <= filters.days
  });
}

watchEffect(() => {
  if(destinationUpdated.value){
    getDestinations();
    destinationUpdated.value = false;
  }
  if(destinationDeleted.value){
    getDestinations();
    destinationDeleted.value = false;
  }
  if(props.newDestinationAdded){
    getDestinations();
  }
  if (EnsureFilters()) {
    filteredDestinations.value = filterDestinations(props.Filters);
  }else{
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
function handleDestinationUpdated(){
  destinationUpdated.value = true;
}
function handleDestinationDeleted() {
  destinationDeleted.value = true;
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