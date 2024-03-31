<template>
  <div class="main-card">
    <v-card class="mx-auto" max-width="344" hover>
      <img :src="imageSrc" class="image"></img>
      <v-card-item>
        <v-card-title class="title">{{ cardTitle }}, {{ cardLocation }}</v-card-title>
        <v-card-subtitle class="subtitle">Date: {{ beginDate }} - {{ endDate }}</v-card-subtitle>
      </v-card-item>
      <v-card-text>
        <p>
          {{ cardDescription }}
        </p>
        <br>
        <div class="price-days">
          <span class="price" :class="{ oldPrice: discount > 0 }">{{ cardPrice }}$</span>
          <span class="days">{{ cardDays }} days</span>
          <span v-if="discount > 0" class="discountedPrice"> / {{ discountedPrice }}$</span>
        </div>
      </v-card-text>
      <v-btn v-if="displayButton && !isAdmin" class="cardBtn" @click="handleSeeMore">See more</v-btn>
      <div v-if="isAdmin" class="adminBtns">
        <v-btn class="cardBtnUpdate" @click="showModal">Update</v-btn>
        <v-btn class="cardBtnDelete" @click="deleteCard">Delete</v-btn>
      </div>
    </v-card>
  </div>
  <div class="update-banner">
    <UpdateDestinationModal :isShowModal="isShowModal" @closeModal="closeModal" 
      :title="props.cardTitle"
      :location="props.cardLocation" 
      :description="props.cardDescription" 
      :price="props.cardPrice"
      :availableSeats="props.cardDays" 
      :discount="props.discount" 
      :availabilities="reservations"
      :guid="cardGuid" 
      @cardUpdated="handleCardUpdated" />

    <ShowMoreModal :isShowModal="showMoreModal" @closeModal="closeModal" 
      :title="props.cardTitle"
      :location="props.cardLocation" 
      :description="props.cardDescription" 
      :price="props.cardPrice"
      :availableSeats="props.cardDays" 
      :discount="props.discount" 
      :availabilities="props.availabilities"
      :guid="cardGuid" />
  </div>
</template>


<script setup>
import axios from 'axios';
import { defineProps, ref, watchEffect, defineEmits } from 'vue';
import { useAppStore } from '@/stores/appStore';
import { useToast } from 'vue-toast-notification';
import UpdateDestinationModal from '@/components/modal/UpdateDestinationModal.vue';
import ShowMoreModal from '@/components/modal/ShowMoreModal.vue';
import { ProgramUpdateLevel } from 'typescript';
const $toast = useToast();
const appStore = useAppStore();
const emit = defineEmits(['destinationDeleted', 'destinationUpdated']);
const props = defineProps({
  imageSrc: String,
  cardTitle: String,
  cardLocation: String,
  cardDescription: String,
  cardPrice: Number,
  cardDays: Number,
  displayButton: Boolean,
  isAdmin: Boolean,
  discount: Number,
  cardGuid: String,
  availabilities: Array
})
const reservations = ref([]);
const beginDate = ref('');
const endDate = ref('');
const cardDays = ref('');
const discountedPrice = ref(0);
const isShowModal = ref(false);
const cardUpdated = ref(false);
const showMoreModal = ref(false);

function closeModal() {
  isShowModal.value = false;
  showMoreModal.value = false;
}
function showModal() {
  getDestination().then(() => {
    isShowModal.value = true;
  });
}
watchEffect(() => {
  if(props.availabilities)
    reservations.value = props.availabilities;

  if (cardUpdated.value) {
    showToast('success', 'Destination updated successfully');
    emit('destinationUpdated');
    cardUpdated.value = false;
  }
  if (props.availabilities) {
    beginDate.value = props.availabilities[0].startDate;
    endDate.value = props.availabilities[0].endDate;
  }
  if (props.discount > 0) {
    discountedPrice.value = props.cardPrice - (props.cardPrice * props.discount / 100)
  }
  cardDays.value = (Date.parse(endDate.value) - Date.parse(beginDate.value)) / (1000 * 60 * 60 * 24);
});

async function getDestination() {
    try {
        const url = `${appStore.getRootUrl()}/api/destination/${props.cardGuid}`;

        await axios.get(url).then((response) => {
            reservations.value = response.data.availabilities;   
        });
    } catch (error) {

        console.error('Error updating destination:', error);
    }
}
const deleteCard = async () => {
  try {
    const response = await axios.delete(appStore.getRootUrl() + `/api/delete-destination/${props.cardGuid}`);
    if (response.status === 200) {
      showToast('success', 'Destination deleted successfully');
      emit('destinationDeleted');
    } else {
      showToast('error', 'Failed to delete destination');
    }
  } catch (error) {
    console.error('Error deleting destination:', error);
    showToast('error', 'Failed to delete destination');
  }
};

function showToast(errorType, message = '') {
  $toast.open({
    message: message,
    type: errorType,
    position: 'top-right',
  });
}

function startUpdateModal() {
  console.log('Update modal');
}

function handleCardUpdated() {
  cardUpdated.value = true;
}

function handleSeeMore() {
  showMoreModal.value = true;
}
</script>

<style scoped>
.discountedPrice {
  color: rgb(8, 175, 3);
  font-weight: bold;
  font-size: medium;
  margin-left: 2px;
}

.oldPrice {
  text-decoration: line-through;
  color: red;
}

.cardBtn {
  margin-left: 20%;
  background-color: var(--TravelTheme, #5bb0c4);
  color: white;
  margin-top: 10px;
  margin-bottom: 10px;
}

.adminBtns {
  display: flex;
  margin-top: 10px;
  margin-bottom: 10px;
  justify-content: space-around;
}

.cardBtnDelete {
  background-color: rgb(255, 75, 51);
  color: white;
}

.cardBtnDelete:hover {
  background-color: rgb(250, 30, 1);
}

.cardBtnUpdate {
  color: white;
  background-color: var(--TravelTheme, #5bb0c4);
}

.cardBtnUpdate:hover {
  color: white;
  background-color: var(--TravelTheme, #44c2df);
}

.title {
  font-size: 30px;
}

.subtitle {
  font-size: 20px;
  color: black;
}

.image {
  width: 100%;
  transition: transform 0.5s ease-in-out;
  /* Add transition for width */
}

.image:hover {
  transform: scale(1.1);
}

.main-card {
  margin-top: auto;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

.price {
  float: left;
  margin-bottom: 20px;
}

.days {
  float: right;
  margin-bottom: 20px;
}
</style>