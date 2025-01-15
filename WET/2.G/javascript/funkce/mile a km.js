function prevod(km) {
    let mile = km * 0.61
    console.log(mile)
    return mile
}
prevod(10)
console.log(prevod(50))
let vysledekprevodu = prevod(30)
console.log(vysledekprevodu)

let textHTML = document.querySelector("#text")
textHTML.innerText = prevod(30)