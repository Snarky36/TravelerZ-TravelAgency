<template>
    <div class="modal-container" v-if="props.isShowModal">
        <div class="modal">
            <div class="modal-header">
                <h2>Update destination: {{ props.title }}</h2>
                <button @click="closeModal" class="pi pi-times-circle icon"></button>
            </div>
            <div class="modal-body">
                <div v-if="!showStats" class="modal-body">
                <v-text-field variant="outlined" v-model="title" label="Title" class="text-field"></v-text-field>
                <v-text-field variant="outlined" v-model="location" label="Location" class="text-field"></v-text-field>
                <v-text-field variant="outlined" v-model="description" label="Description"
                    class="text-field"></v-text-field>

                <v-text-field variant="outlined" type="number" min="0" v-model.number="price" label="Price"
                    class="text-field"></v-text-field>
                <v-text-field variant="outlined" type="number" min="0" v-model.number="availableSeats"
                    label="Available Seats" class="text-field"></v-text-field>
                <v-text-field variant="outlined" type="number" min="0" v-model.number="discount" label="Discount %"
                    class="text-field"></v-text-field>
                </div>
                
                <UpdateDisponibilityTable :availabilities="props.availabilities" :location="props.location" :isAdmin="true" :dest_guid="props.guid"/>
                
                <DoughnutChart v-if="showStats" :chartData="chartData"/>
            </div>
            <div class="modal-footer">
                <button v-if="!showStats" class="show-button" @click="handelShowStats()"> Show Statistics </button>
                <button v-if="showStats" class="closeButton" @click="handelCloseStats()"> Close Statistics </button>
                <button v-if="!showStats" class="update-button" @click="updateDestination()"> Update </button>
                <button class="closeButton" @click="closeModal()"> Close </button>
            </div>
        </div>
    </div>
</template>

<script setup >
import { ref, defineProps, defineEmits, watchEffect } from 'vue'
import UpdateDisponibilityTable from './UpdateDisponibilityTable.vue'
import axios from 'axios'
import { useAppStore } from '@/stores/appStore'
import { useToast } from 'vue-toast-notification';
import { DoughnutChart } from 'vue-chart-3';
import { Chart, registerables } from 'chart.js';
Chart.register(...registerables);

const $toast = useToast();
const appStore = useAppStore();

const props = defineProps({
    guid: String,
    isShowModal: Boolean,
    title: String,
    location: String,
    description: String,
    price: Number,
    discount: Number,
    availabilities: Array
})
const showStats = ref(false);
const title = ref('');
const location = ref('');
const description = ref('');
const price = ref(0);
const availableSeats = ref(0);
const discount = ref(0);
const reservationsPerMonth = ref([0,0,0,0,0,0,0,0,0,0,0,0]);
const reservations = ref([]);
const chartData = ref({
  labels: ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'],
  datasets: [
    {
      label: 'Reservations per Month',
      data: reservationsPerMonth.value,
      backgroundColor: [
        'rgba(255, 255, 255, 0.9)', 'rgba(227, 1, 38, 0.9)', 'rgba(80, 200, 120, 0.9)', 'rgba(255, 255, 102, 0.9)',
        'rgba(230, 224, 240, 0.9)', 'rgba(250, 218, 221, 0.9)', 'rgba(255, 127, 80, 0.9)', 'rgba(255, 64, 64, 0.9)',
        'rgba(183, 65, 14, 0.9)', 'rgba(128, 0, 128, 0.9)', 'rgba(165, 42, 42, 0.9)', 'rgba(0, 100, 0, 0.9)'
      ],
    },
  ],
});


watchEffect(() => {
    title.value = props.title;
    location.value = props.location;
    description.value = props.description;
    price.value = props.price;
    discount.value = props.discount;
})

function handelShowStats() {
    getDestination().then(() => {
        
        reservations.value.forEach((availability) => {
            const startDate = new Date(availability.startDate);
            const month = startDate.getMonth();
            reservationsPerMonth.value[month] += availability.occupiedSeats;
        });
        showStats.value = true;
    });

}
function handelCloseStats() {
    showStats.value = false;
}

const emit = defineEmits(['closeModal', 'cardUpdated']);

function closeModal() {
    emit('closeModal');
}

async function updateDestination() {
    try {
        const url = `${appStore.getRootUrl()}/api/update-destination/${props.guid}`;
        const destination_data = {
            name: title.value,
            location: location.value,
            description: description.value,
            price: price.value,
            availableSeats: availableSeats.value,
            discountPercent: discount.value,
            availabilities: props.availabilities,
            availableSeats: availableSeats.value,
        };

        const response = await axios.put(url, destination_data);
        if (response.status === 200) {
            console.log('Destination updated successfully');
            emit('cardUpdated');
 
        } else {
            console.error('Failed to update destination:', response.data);
        }
    } catch (error) {

        console.error('Error updating destination:', error);
    }
}

async function getDestination() {
    try {
        const url = `${appStore.getRootUrl()}/api/destination/${props.guid}`;

        await axios.get(url).then((response) => {
            reservations.value = response.data.availabilities;   
        });
    } catch (error) {

        console.error('Error updating destination:', error);
    }
}

</script>


<style scoped>
.modal-container {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-color: rgba(0, 0, 0, 0.5);
    display: flex;
    z-index: 1000;
    justify-content: center;
    align-items: center;
}

.modal {
    background-color: white;
    padding: 20px;
    border-radius: 8px;
    width: 40%;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.3);
    overflow-y: auto;
}

.modal-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 30px;
}

.modal-header h2 {
    margin: 0;
    font-size: 30px;
}

.modal-header button {
    background-color: transparent;
    border: none;
    cursor: pointer;
    font-size: 20px;
}

.text-field {
    font-size: 16px;
    margin-top: 10px;
}

.v-label {
    font-size: 28px;
}

.modal-footer {
        display: flex;
        justify-content: center;
        align-items: center;
        margin-top: 20px; 
    }

    .update-button {
        background-color: var(--TravelTheme, #5bb0c4);
        color: white;
        padding: 10px 20px;
        border: none;
        border-radius: 5px;
        cursor: pointer;
    }
    .update-button:hover {
        background-color: var(--TravelTheme, #45acc4); 
    }

    .show-button {
        background-color: var(--TravelTheme, #5bb0c4);
        color: white;
        padding: 10px 20px;
        border: none;
        border-radius: 5px;
        cursor: pointer;
        margin-right:10%;
    }
    .show-button:hover {
        background-color: var(--TravelTheme, #45acc4); 
    }

    .closeButton {
        padding: 10px 20px;
        border: none;
        border-radius: 5px;
        cursor: pointer;
    }
</style>