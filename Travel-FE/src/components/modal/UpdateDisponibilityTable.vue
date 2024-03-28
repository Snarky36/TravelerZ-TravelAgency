<template>
    <fwb-table>
      <fwb-table-head>
        <fwb-table-head-cell>Location</fwb-table-head-cell>
        <fwb-table-head-cell>Start Date</fwb-table-head-cell>
        <fwb-table-head-cell>End Date</fwb-table-head-cell>
        <fwb-table-head-cell>Nr places left</fwb-table-head-cell>
        <fwb-table-head-cell>Price</fwb-table-head-cell>
        <fwb-table-head-cell>
          <span class="sr-only">Edit</span>
        </fwb-table-head-cell>
      </fwb-table-head>
      <fwb-table-body>
      <fwb-table-row v-for="(availability, index) in props.availabilities" :key="index">
        <fwb-table-cell>{{ props.location }}</fwb-table-cell>
        <fwb-table-cell>{{ availability.startDate }}</fwb-table-cell>
        <fwb-table-cell>{{ availability.endDate }}</fwb-table-cell>
        <fwb-table-cell>{{ availability.availableSeats }}</fwb-table-cell>
        <fwb-table-cell>{{ availability.totalPrice }}</fwb-table-cell>
        <fwb-table-cell>
          <fwb-a href="#" v-if="props.isAdmin">Edit</fwb-a>
          <fwb-a href="#" v-if="props.isAdmin">Delete</fwb-a>
          <fwb-a href="#" v-if="!props.isAdmin">Reserve</fwb-a>
        </fwb-table-cell>
      </fwb-table-row>
    </fwb-table-body>
    </fwb-table>
  </template>
  
  <script setup>
  import {
    FwbA,
    FwbTable,
    FwbTableBody,
    FwbTableCell,
    FwbTableHead,
    FwbTableHeadCell,
    FwbTableRow,
  } from 'flowbite-vue'
  import { defineProps } from 'vue'
 
  const props = defineProps({
    availabilities: Array,
    location: String,
    isAdmin: Boolean
  });

  console.log("Avaialabilities", props.avaialbilities);
  </script>