// GLOBAL VARIABLES
let map
let directionsService
let directionsRenderer


// INITIALIZE MAP
function initMap(){

map = new google.maps.Map(document.getElementById("map"),{

zoom:5,
center:{lat:39.5,lng:-98.35},   // USA center

})


directionsService = new google.maps.DirectionsService()

directionsRenderer = new google.maps.DirectionsRenderer({

polylineOptions:{
strokeColor:"#22c55e",
strokeWeight:6
}

})

directionsRenderer.setMap(map)



// AUTOCOMPLETE FOR INPUTS
const startInput = document.getElementById("start")
const endInput = document.getElementById("end")

new google.maps.places.Autocomplete(startInput)
new google.maps.places.Autocomplete(endInput)

}



// FIND ROUTE BUTTON
function calculateRoute(){

const start = document.getElementById("start").value
const end = document.getElementById("end").value


if(start === "" || end === ""){
alert("Please enter both locations")
return
}


directionsService.route({

origin:start,
destination:end,
travelMode:'DRIVING'

},function(result,status){

if(status === "OK"){

directionsRenderer.setDirections(result)


// GET ROUTE DATA
const route = result.routes[0].legs[0]

const lat = route.start_location.lat()
const lng = route.start_location.lng()

const hour = new Date().getHours()


// SEND DATA TO FASTAPI MODEL
fetch("http://127.0.0.1:8000/predict",{

method:"POST",

headers:{
"Content-Type":"application/json"
},

body:JSON.stringify({

latitude:lat,
longitude:lng,
crime:0.6,
lighting:(hour > 6 && hour < 19) ? 0.8 : 0.3,
crowd:0.6,
hour:hour

})

})

.then(response => response.json())

.then(data => {

updateSafetyCards(data.risk_class)

})

.catch(error => {

console.error("API Error:", error)

})


}

})

}



// UPDATE UI CARDS
function updateSafetyCards(risk){

let safest = document.querySelector(".safe")
let moderate = document.querySelector(".moderate")
let risky = document.querySelector(".risky")


if(risk === "Safe"){

safest.innerText = "Safety Score: Safe"
moderate.innerText = "Safety Score: Moderate"
risky.innerText = "Safety Score: High Risk"

}

else if(risk === "Moderate"){

safest.innerText = "Safety Score: Moderate"
moderate.innerText = "Safety Score: Moderate"
risky.innerText = "Safety Score: High Risk"

}

else{

safest.innerText = "Safety Score: High Risk"
moderate.innerText = "Safety Score: Moderate"
risky.innerText = "Safety Score: High Risk"

}

}



// RUN MAP WHEN PAGE LOADS
window.initMap = initMap