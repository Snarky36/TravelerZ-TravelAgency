<template>
   <div class="calendar">
    <datepicker :highlighted="highlightedDates"></datepicker>
    </div>
  <fwb-table style="height: 200px !important; overflow: scroll;">
    <fwb-table-head>
      <fwb-table-head-cell>Start Date</fwb-table-head-cell>
      <fwb-table-head-cell>End Date</fwb-table-head-cell>
      <fwb-table-head-cell>Nr places left</fwb-table-head-cell>
      <fwb-table-head-cell>Price</fwb-table-head-cell>
      <fwb-table-head-cell>
        <span class="sr-only">Edit</span>
      </fwb-table-head-cell>
    </fwb-table-head>
    <fwb-table-body>
      <fwb-table-row v-for="(availability, index) in reservations" :key="index">
        <fwb-table-cell>
          <input class="narrow-cell" type="date" v-model="availability.startDate">
        </fwb-table-cell>
        <fwb-table-cell>
          <input class="narrow-cell" type="date" v-model="availability.endDate">
        </fwb-table-cell>
        <fwb-table-cell>
          {{ availability.occupiedSeats }} /<input class="narrow-cell-3" type="number" v-model="availability.availableSeats">
        </fwb-table-cell>
        <fwb-table-cell>
          <input class="narrow-cell-3" type="number" v-model="availability.totalPrice">
        </fwb-table-cell>
        <fwb-table-cell>
          <v-btn size="x-small" color="var(--TravelTheme, #5bb0c4)" @click="updateReservation(availability.guid, availability)" v-if="props.isAdmin">Update</v-btn>
          <br>
          <v-btn size="x-small" color="rgb(255, 75, 51)" @click="deleteReservation(availability.guid)" v-if="props.isAdmin">Delete</v-btn>
          <br>
          <v-btn size="x-small" color="var(--TravelTheme, #5bb0c4)" @click="reservePlace(availability.guid)" :disabled="availability.occupiedSeats == availability.availableSeats">Reserve</v-btn>
        </fwb-table-cell>
      </fwb-table-row>
      <fwb-table-row :key="1">
        <fwb-table-cell>
          <input class="narrow-cell" type="date" v-model="newStartDate">
        </fwb-table-cell>
        <fwb-table-cell>
          <input class="narrow-cell" type="date" v-model="newEndDate">
        </fwb-table-cell>
        <fwb-table-cell>
          <input class="narrow-cell-3" type="number" v-model="newAvailableSeats">
        </fwb-table-cell>
        <fwb-table-cell>
          <input class="narrow-cell-3" type="number" v-model="newTotalPrice">
        </fwb-table-cell>
        <fwb-table-cell>
          <v-btn color="var(--TravelTheme, #5bb0c4)" @click.stop="addReservation()" v-if="props.isAdmin">Add</v-btn>
        </fwb-table-cell>
      </fwb-table-row>

    </fwb-table-body>
  </fwb-table>

</template>

<script setup>
import {
  FwbTable,
  FwbTableBody,
  FwbTableCell,
  FwbTableHead,
  FwbTableHeadCell,
  FwbTableRow,
} from 'flowbite-vue'
import { ref, defineProps, watchEffect, computed } from 'vue'
import axios from 'axios';
import { useAppStore } from '@/stores/appStore';
import Datepicker from 'vuejs3-datepicker';

const appStore = useAppStore();
const newStartDate = ref('');
const newEndDate = ref('');
const newAvailableSeats = ref('0');
const newTotalPrice = ref('0');
const reservations = ref([]);
const props = defineProps({
  availabilities: Array,
  location: String,
  isAdmin: Boolean,
  dest_guid: String
});


watchEffect(() => {
  if(props.availabilities.length === 0) return;

  reservations.value = props.availabilities;
});

const events = ref([]);
const highlightedDates = ref({
  dates: [],
  color:["#3498db"] // Highlighted dates array
});

watchEffect(() => {
  // Convert availabilities to highlighted dates
  const dates = reservations.value.flatMap(availability => {
    if(availability.occupiedSeats == 0)
      return [];
    const startDate = new Date(availability.startDate);
    const endDate = new Date(availability.endDate);
    const highlighted = [];
    const currentDate = new Date(startDate);
    while (currentDate <= endDate) {
      highlighted.push(new Date(currentDate)); // Add a new Date object
      currentDate.setDate(currentDate.getDate() + 1); // Move to next day
    }
    return highlighted;
  }, []);
  highlightedDates.value.dates = dates;
});


const addReservation = async () => {
  try {
    await axios.post(appStore.getRootUrl()+ `/api/add-reservation/${props.dest_guid}`, {
      startDate: newStartDate.value,
      endDate: newEndDate.value,
      availableSeats: newAvailableSeats.value,
      totalPrice: newTotalPrice.value,
      occupiedSeats: 0
    }).then((response) => {
      console.log("Response", response.data.destination);
      reservations.value = response.data.destination.availabilities;

    });
    
  } catch (error) {
    console.error('Error adding reservation:', error);
  }
};

const updateReservation = async (reserveGuid, availability) => {
  try {
    await axios.put(appStore.getRootUrl() + `/api/update-reservation/${props.dest_guid}/${reserveGuid}`, {
      startDate: availability.startDate,
      endDate: availability.endDate,
      availableSeats: availability.availableSeats,
      totalPrice: availability.totalPrice
    }).then((response) => {
      console.log("Response", response.data.destination);
      reservations.value = response.data.destination.availabilities;
    });
  } catch (error) {
    console.error('Error updating reservation:', error);
  }
};

const reservePlace = async (reserveGuid) => {
  try {
    await axios.get(appStore.getRootUrl() + `/api/reserve-place/${props.dest_guid}/${reserveGuid}`).then((response) => {
      console.log("Response", response.data);
      reservations.value = response.data.destination.availabilities;
    })
    
  } catch (error) {
    console.error('Error reserving place:', error);

  }
};

const deleteReservation = async (reserveGuid) => {
  console.log("Delete reservation", reserveGuid);
  try {
    const response = axios.delete(appStore.getRootUrl() + `/api/delete-reservation/${props.dest_guid}/${reserveGuid}`).then((response) => {
      console.log("Response", response.data);
      if(response.data){
      reservations.value = reservations.value.filter(reservation => reservation.guid !== reserveGuid);
      }
    })
    console.log(response.data);
    
  } catch (error) {
    console.error('Error deleting reservation:', error);
  }
};


</script>

<style scoped>
.calendar {
  width: 100%;
}
.narrow-cell{
  width: 150px;
}
.narrow-cell-2{
  width: 90px;
}
.narrow-cell-3{
  width: 80px;
}
</style>