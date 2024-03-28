<template>
    <div class="modal-container" v-if="props.isShowModal">
        <div class="modal">
            <div class="modal-header">
                <h2>Update destination: {{ props.title }}</h2>
                <button @click="closeModal" class="pi pi-times-circle icon"></button>
            </div>
            {{ console.log(props.availabilities) }}
            <div class="modal-body">
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
                <UpdateDisponibilityTable :availabilities="props.availabilities" :location="props.location" :isAdmin="true" />
            </div>
            <div class="modal-footer">
                <button class="update-button" @click="updateDestination()"> Update </button>
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

const title = ref('');
const location = ref('');
const description = ref('');
const price = ref(0);
const availableSeats = ref(0);
const discount = ref(0);

watchEffect(() => {
    title.value = props.title;
    location.value = props.location;
    description.value = props.description;
    price.value = props.price;
    discount.value = props.discount;
})

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

    .closeButton {
        padding: 10px 20px;
        border: none;
        border-radius: 5px;
        cursor: pointer;
    }
</style>