
let nadpis = document.getElementById(".nadpis")
let nadpis2 = document.getElementById(".nadpis2")
let slunce = document.querySelector("#slunce")
let ucebnice = document.querySelector("#ucebnice")



function zmenNadpis() {
   
}
slunce.addEventListener("click", zmenIkonu)
ucebnice.addEventListener("click", zmenZpět)

function zmenIkonu (){
slunce.style.display = "none"
ucebnice.style.display = "inline"
nadpis2.style.display = "inline"
nadpis.style.display = "none"
}

function zmenZpět (){
    slunce.style.display = "inline"
    ucebnice.style.display = "none"
    nadpis2.style.display = "none"
    nadpis.style.display = "inline"
    }