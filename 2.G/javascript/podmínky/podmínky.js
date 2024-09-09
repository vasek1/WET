let cislo = 10
// pro porovnání píšeme 3x = (===)
// pokud se číslo rovná 10
if(cislo === 10) { 
    // proveď tento příkaz
    console.log("Číslo je 10")
// v ostatních případech (else)...
} else if (cislo === 5){
     //...proveď tento příkaz
console.log("Číslo je 5")
}
else{
    //...proveď tento příkaz
    console.log("Číslo není ani 10 ani 5")
}
 
//alert("Pozor!!!") 

let input = prompt("Zadej číslo")
input = parseInt(input)
console.log(input)