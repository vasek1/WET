let tlacitko = document.querySelector("#tlacitko")
let nadpis = document.getElementById("nadpis1")
let input = document.querySelector("#input")
let input1 = document.querySelector("#input2")

tlacitko.addEventListener("click", finale)


function finale(){

    let  textInputu = input.value
    let textInputu1 = input1.value
    
    textInputu1 = parseInt(textInputu1)
if(textInputu === "f"){
     nadpis.innerText = prevod(textInputu1)
  }else (textInputu === "c")
    nadpis.innerText = prevod1(textInputu1)
  
    function prevod(cel) {
        let fahrenheit = cel*9/5+ 32
        return fahrenheit
    
    }
    
    function prevod1(fahrenheit) {
        let cel = fahrenheit/1.8 - 32
        return cel
        
    
    }  

}
