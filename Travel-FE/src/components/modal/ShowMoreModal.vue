<template>
    <div class="modal-container" v-if="props.isShowModal">
        <div class="modal">
            <div class="modal-header">
                <h2>Available Dates for : {{ props.title }}</h2>
                <button @click="closeModal" class="pi pi-times-circle icon"></button>
            </div>
            <div class="modal-body">
                <UpdateDisponibilityTable :dest_guid="props.guid" :availabilities="props.availabilities" :location="location" :isAdmin="false" />
            </div>
            <div class="modal-footer">
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
    availabilities: Array
})

const title = ref('');
const location = ref('');
const description = ref('');
const availableSeats = ref(0);

watchEffect(() => {
    title.value = props.title;
    location.value = props.location;
    description.value = props.description;
})

const emit = defineEmits(['closeModal']);

function closeModal() {
    emit('closeModal');
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
    overflow-y: scroll;
}

.modal {
    background-color: white;
    padding: 20px;
    border-radius: 8px;
    width: 40%;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.3);
    overflow-y: scroll;
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