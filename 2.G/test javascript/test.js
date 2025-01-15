let tlacitko = document.querySelector("#tlacitko")
let tlacitko2 = document.querySelector("#tlacitko2")
let input = document.querySelector("#input")
let dlouha = document.querySelector("#dlouha")
let kratka= document.querySelector("#kratka")
let seznam = document.querySelector("#seznam")
let Seznamslov = []
tlacitko.addEventListener("click", pridejslovo)



function pridejslovo(){
Seznamslov.push(input.value)
seznam.innerText = Seznamslov
input.value = ""
}



let srdicka = document.querySelector("#srdicka")
let tlacitko3 = document.querySelector("#tlacitko3")
let input2 = document.querySelector("#input2")
tlacitko3.addEventListener("click", zmenNadpis)

function zmenNadpis(){
    let hodnoceni = []
    let  textInputu2 = input.value
    textInputu2 = parseInt(textInputu2)
    if(textInputu2=== hodnoceni)
    srdicka.innerText = "❤️"
    console.log(textInputu2)
}
