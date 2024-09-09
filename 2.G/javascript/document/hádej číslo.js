let tlacitko = document.querySelector("#tlacitko")
let nadpis = document.getElementById("nadpis")
let input = document.querySelector("#input") 
let tajneCislo = Math.floor(Math.random() * 101);


tlacitko.addEventListener("click", zmenNadpis)


function zmenNadpis(){
    let  textInputu = input.value
        textInputu = parseInt(textInputu)
        if(textInputu === tajneCislo){
          nadpis.innerText ="uhádl si🥳" 
        }else if(textInputu > tajneCislo){
          nadpis.innerText ="míň 🔽"
        }else if(textInputu < tajneCislo )
        {
            nadpis.innerText ="víc 🔼" 
        }else{
          nadpis.innerText ="hádej znovu"
        }
    }