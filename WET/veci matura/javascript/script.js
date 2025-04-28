// let pizzy = ["quattro formaggi", "hawaii", "margherita", "vegetariana","prosciutto"]

// for (let i = 0; i < pizzy.length; i++) {
//     console.log(pizzy[i])
    
// }
// for (let i = 0; i < 10; i++) {
//     console.log("Zadne pizzy")
// }
// let x = 3
// let y = "3"

// if (x===y){
//     console.log("rovná se")
// }else{
//     console.log("nerovná se")
// }


// const nechceme měnit v průbehu a let chceme
//nadpis.textContent
//innerHtml nechceme tam kde to mění uživatel
// popsání syntaxu javascriptu

const nadpis = document.querySelector("#nadpis")
const button = document.querySelector(".button")
const tlacitko2 = document.querySelector(".tlacitko2")

button.addEventListener("click",function(){
    console.log("funkce funguje")
    nadpis.innerText ="Diskuze o Rakousku"
    nadpis.style.fontSize ="100px"
    nadpis.style.color = "red"
    //nadpis.classList.add("hokus") prida classu hokus nadpisu
})

// button.addEventListener("click",()=>{
//     console.log("funkce funguje")
// })


// button.addEventListener("click",zmen)
// function zmen(){
//     console.log("Funkce funguje")
// }
tlacitko2.addEventListener("click", function(){
    const input = document.querySelector(".input")
    console.log(input) // vypíše celý input
    console.log(input.value) //vypíše hodnotu prvku
})
