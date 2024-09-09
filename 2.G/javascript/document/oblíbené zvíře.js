
let tlacitko = document.querySelector("#tlacitko")
let nadpis = document.getElementById("nadpis")
let input = document.querySelector("#input") 
let nadpis2 = document.getElementById("nadpis2")
let body = document.querySelector("body")

tlacitko.addEventListener("click", zmenNadpis)


function zmenNadpis(){
    let  textInputu = input.value 

        if(textInputu === "želva"){
          nadpis2.innerText ="I like turtles"
          body.style.backgroundColor ="green"
        }else if(textInputu === "liška"){
          nadpis2.innerText ="What does the fox say"
          body.style.backgroundColor ="orange"
        }else if(textInputu === "plameňák"  )
        {
            nadpis2.innerText ="🦩" 
            body.style.backgroundColor ="pink"
        }else{
          nadpis2.innerText ="toto zvíře neznám"
          body.style.backgroundColor ="black"
          nadpis2.style.color ="white"
          nadpis.style.color ="white"
        }
    }