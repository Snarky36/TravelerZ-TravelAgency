<template>
    <div class="main-div">
        <div class="title">Destination packs</div>
        <div class="content">
            <DestinationCards imageSrc='\src\assets\ImageMalta.png' :cardBeginDate="beginDate"  :cardEndDate="endDate" cardTitle="Baia Mare" cardDescription="Baia mare sunper faina aaa" :cardPrice="300" :cardDays="7"/>
            <DestinationCards imageSrc='\src\assets\ImageMalta.png' :cardBeginDate="beginDate"  :cardEndDate="endDate" cardTitle="Baia Mare" cardDescription="Baia mare sunper faina aaa" :cardPrice="300" :cardDays="7"/>
            <DestinationCards imageSrc='\src\assets\ImageMalta.png' :cardBeginDate="beginDate"  :cardEndDate="endDate" cardTitle="Baia Mare" cardDescription="Baia mare sunper faina aaa" :cardPrice="300" :cardDays="7"/>
            <DestinationCards imageSrc='\src\assets\ImageMalta.png' :cardBeginDate="beginDate"  :cardEndDate="endDate" cardTitle="Baia Mare" cardDescription="Baia mare sunper faina aaa" :cardPrice="300" :cardDays="7"/>
            <DestinationCards imageSrc='\src\assets\ImageMalta.png' :cardBeginDate="beginDate"  :cardEndDate="endDate" cardTitle="Baia Mare" cardDescription="Baia mare sunper faina aaa" :cardPrice="300" :cardDays="7"/>
            <DestinationCards imageSrc='\src\assets\ImageMalta.png' :cardBeginDate="beginDate"  :cardEndDate="endDate" cardTitle="Baia Mare" cardDescription="Baia mare sunper faina aaa" :cardPrice="300" :cardDays="7"/>
            <DestinationCards imageSrc='\src\assets\ImageMalta.png' :cardBeginDate="beginDate"  :cardEndDate="endDate" cardTitle="Baia Mare" cardDescription="Baia mare sunper faina aaa" :cardPrice="300" :cardDays="7"/>
            <DestinationCards imageSrc='\src\assets\ImageMalta.png' :cardBeginDate="beginDate"  :cardEndDate="endDate" cardTitle="Baia Mare" cardDescription="Baia mare sunper faina aaa" :cardPrice="300" :cardDays="7"/>
            <DestinationCards imageSrc='\src\assets\ImageMalta.png' :cardBeginDate="beginDate"  :cardEndDate="endDate" cardTitle="Baia Mare" cardDescription="Baia mare sunper faina aaa" :cardPrice="300" :cardDays="7"/>
            <DestinationCards imageSrc='\src\assets\ImageMalta.png' :cardBeginDate="beginDate"  :cardEndDate="endDate" cardTitle="Baia Mare" cardDescription="Baia mare sunper faina aaa" :cardPrice="300" :cardDays="7"/>
            <DestinationCards imageSrc='\src\assets\ImageMalta.png' :cardBeginDate="beginDate"  :cardEndDate="endDate" cardTitle="Baia Mare" cardDescription="Baia mare sunper faina aaa" :cardPrice="300" :cardDays="7"/>
            <DestinationCards imageSrc='\src\assets\ImageMalta.png' :cardBeginDate="beginDate"  :cardEndDate="endDate" cardTitle="Baia Mare" cardDescription="Baia mare sunper faina aaa" :cardPrice="300" :cardDays="7"/>
            <DestinationCards imageSrc='\src\assets\ImageMalta.png' :cardBeginDate="beginDate"  :cardEndDate="endDate" cardTitle="Baia Mare" cardDescription="Baia mare sunper faina aaa" :cardPrice="300" :cardDays="7"/>
            

        </div>
    </div>
</template>

<script setup>
    import DestinationCards from '@/components/DestinationCards.vue';
    import {ref} from 'vue'
    const beginDate = ref('15.02.2024');
    const endDate = ref('22.02.2024');
</script>

<style scoped>
.main-div{
    display: grid;
    place-items: center;
    width:60%;
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

.content > * {
  width: calc(33.33% - 20px); 
}

@media (max-width: 768px) {
  .content > * {
    width: calc(50% - 20px); 
  }
}
</style>