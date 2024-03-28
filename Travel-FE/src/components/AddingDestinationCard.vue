<template>
  <div class="main-card">
    <v-card class="card">
      <div class="card-header">
        <h1 class="title">Add a destination</h1>
        <h2 v-if="errorFields" class="error">All fileds are required!</h2>
      </div>
      <v-card-item>

        <VueDatePicker v-model="selectedDate" range :enable-time-picker="false" modeHeight="50px" class="calendar" />
        <v-text-field variant="outlined" v-model="title" label="Title"></v-text-field>
        <v-text-field variant="outlined" v-model="location" label="Location"></v-text-field>
        <v-text-field variant="outlined" v-model="description" label="Description"></v-text-field>

        <v-text-field variant="outlined" type="number" min="0" v-model.number="price" label="Price"></v-text-field>
        <v-text-field variant="outlined" type="number" min="0" v-model.number="availableSeats" label="Available Seats"></v-text-field>
        <v-text-field variant="outlined" type="number" min="0" v-model.number="discount" label="Discount %"></v-text-field>
        <v-file-input v-model="image" accept="image/*" label="Upload Image" prepend-icon="mdi-camera"
          placeholder="No file chosen" outlined @change="handleImageUpload2"></v-file-input>
      </v-card-item>

      <v-card-actions class="card-actions">
        <v-btn class="add-button" @click="addDestination" >Add Destination</v-btn>
      </v-card-actions>
    </v-card>
  </div>
</template>

<script setup>
import { ref, watchEffect, defineEmits } from 'vue';
import { useAppStore } from '@/stores/appStore';
import axios from 'axios';
import { useToast } from 'vue-toast-notification';
import { WatchDirectoryFlags } from 'typescript';

const errorFields = ref(false); 
const emit = defineEmits(['destinationAdded']);
const $toast = useToast();
const appStore = useAppStore();
const selectedDate = ref(null);
const title = ref('');
const location = ref('');
const description = ref('');
const price = ref(0);
const days = ref(0);
const availableSeats = ref(0);
const discount = ref(0);
const imageSrc = ref('');
const image = ref(null);

const destinationSaved = ref(false);
// Method to add the new destination
const addDestination = async () => {
  days.value = selectedDate.value[1].getDate() - selectedDate.value[0].getDate();
  if(!checkForm()){
    showToast('error', 'Please fill all the required fields');
    errorFields.value = true;
    return;
  }else{
    errorFields.value = false;
  }

  try {
    
    const totalPrice = (price.value - (price.value * discount.value / 100)) * days.value;
    const availabillity = {
      'startDate': selectedDate.value[0],
      'endDate': selectedDate.value[1],
      'totalPrice': totalPrice,
      'availableSeats': availableSeats.value,
    }

    const destination_data = {
      'name': title.value,
      'location': location.value,
      'description': description.value,
      'price': price.value,
      'days': days.value,
      'availableSeats': availableSeats.value,
      'discountPercent': discount.value,
      'image': imageSrc.value,
      'availabilities': [availabillity]
    };

    const response = await axios.post(appStore.getRootUrl() + '/api/add-destination', destination_data);

    if (response.status !== 200) {
      console.error('Error adding destination:', response.data);
      showToast('error', 'Error adding destination');
    }
    else {
      showToast('success', 'Destination added successfully').then(() => {
        title.value = '';
        location.value = '';
        description.value = '';
        price.value = 0;
        days.value = 0;
        availableSeats.value = 0;
        discount.value = 0;
        imageSrc.value = null;
        selectedDate.value = null;
      }).then(() => {
        emit('destinationAdded', true);
      }).then(() => {
        emit('destinationAdded', false);
      });
    }
  } catch (error) {
    console.error('Error adding destination:', error);
  }
};

function checkForm(){
  if(title.value ==''){
    return false;
  }
  if(location.value ==''){
    return false;
  }
  if(description.value ==''){
    return false;
  }
  if(price.value == 0){
    return false;
  }
  if(days.value == 0){
    return false;
  }
  if(availableSeats.value == 0){
    return false;
  }
  return true;

}

const handleImageUpload2 = (event) => {
  const file = event.target.files[0];
  imageSrc.value = file.name;
};



async function showToast(errorType, message = '') {
  $toast.open({
    message: message,
    type: errorType,
    position: 'top-right',
  });
}


watchEffect(() => {
  if(title.value || description.value || location.value || price.value || days.value || availableSeats.value || discount.value){
    errorFields.value = false;
  }
});

</script>

<style scoped>
.main-card {
  width: 20%;

  margin-top: auto;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

.card {
  width: 100%;
  height: 100%;
}
.title{
  margin-top: 10px;
  margin-bottom: 10px;
  font-size: 20px;
  font-weight: bold;
}
.card-header{
  align-items: center;
  margin-left: 30%;
}
.error{
  color: red;
  font-size: 15px;
}

.card-actions{
  margin-top: 10px;
  margin-bottom: 10px;
  display: flex;
  justify-content: center;

}
.add-button {
  color: white;
  background-color: var(--TravelTheme, #5bb0c4);
}

.add-button:hover {
  color: white;
  background-color: var(--TravelTheme, #44c2df);
}
</style>