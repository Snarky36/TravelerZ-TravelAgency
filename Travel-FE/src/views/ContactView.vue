<template>
    <div class="contact-page">
        <div class="title-div">
            <div class="title-text">
                <p>Contact Us</p>
            </div>
            <img alt="BackgroundImage" class="img" src="@/assets/ContactImage.png" />
        </div>
        <div class="title">
            <h2>Contact us</h2>
        </div>
        <div class="home-content">
            <div class="contact-form">
                <v-text-field label="Name"></v-text-field>
                <v-text-field label="Email"></v-text-field>
                <v-text-field label="Message"></v-text-field>
            </div>
            <div class="contact-form">
                <iframe src="https://www.google.com/maps/d/embed?mid=1G-iW8YgBcxWzklxH-46rVX9ZWII&hl=ro&ehbc=2E312F" width="100%" height="580"></iframe>
            </div>
        </div>

    </div>

</template>


<style scoped>
.title {
    margin-top: 1%;
    font-size: 24px;
    color: black;
    text-align: center;
    font-family: 'Poppins', sans-serif;
}

.title-text {
    color: var(--TitleColor, #f5f5f5);
    white-space: nowrap;
    font: 700 72px/120% Poppins, sans-serif;
    z-index: 1;
    margin-top: -15%;
    position: absolute;
}

.title-div {
    flex-direction: column;
    overflow: hidden;
    position: relative;
    display: flex;
    min-height: 200px;
    height: 700px;
    width: 100%;
    justify-content: center;
    align-items: center;
    padding: 50px 60px;
}

.title-div .img {
    position: absolute;
    inset: 0;
    height: 100%;
    width: 100%;

    object-fit: cover;
    object-position: center;
}

.contact-page {
    justify-content: center;
    align-content: center;
    flex-wrap: wrap;
    background-color: #fff;
    display: flex;
    flex-direction: column;
}

.home-content {
    justify-content: center;
    align-content: center;
    display: flex;
    margin-top: 2%;
}

.contact-form {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-content: center;
    margin-top: 2%;
    margin-left: 10%;
    margin-right: 10%;
    padding: 20px;
    padding-bottom: 3%;
    background-color: #ffffff;
    /* Card background color */
    border-radius: 10px;
    /* Adjust the border radius as needed */
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    /* Card shadow */
    padding: 20px;
    padding-bottom: 3%;
    /* Padding inside the card */
    justify-content: center;
    align-content: center;
    display: flex;
    margin-top: 2%;
    width: 40%;
}
</style>