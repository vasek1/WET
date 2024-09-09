// proměná = variable

// var je zastaralý způsob vytváření proměných
var veta = "Hello world"
console.log("Píšu do konzole")
console.log(veta)

//let také vytváří proměné - dnes požívanější
let veta2 = "Věta číslo dvě"

// const(constant)  vytváří proměné, které nelze přepsat
const veta3 = "Const je třetí způsob, jak vytvářet proměné"


veta2 = "Veta2 byla přepsána"
console.log(veta2)


// pod proměnou mohu "schovat" text (string), čísla (intenger) a další
// text musí být v uvozovkách, číslo (int) není v uvozovkách 

let cislo = 5
let cislo2 = 10

let vysledek = cislo  + cislo2

console.log(vysledek)
 
let slovo1 ="5"
let slovo2 ="10"

// + spojuje text
console.log(slovo1 + slovo2 )