 //propojení id z html s javascriptem 2 možnosti:
let tlacitko = document.querySelector("#tlacitko")
let nadpis = document.getElementById("nadpis")




tlacitko.addEventListener("click", zmenNadpis)

function zmenNadpis(){
  
    nadpis.style.fontSize = "50px" 
    
}