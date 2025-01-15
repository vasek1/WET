let tlacitko = document.querySelector("#tlacitko")
let nadpis = document.getElementById("nadpis")
tlacitko.addEventListener("click", zmenNadpis)
let random = Math.floor(Math.random() * 6)
function zmenNadpis() {
    if (random === 1) {
        nadpis.innerText = "umřeš"
    } else if (random === 2) {
        nadpis.innerText = "zbohatneš"
    } else if (random === 3) {
        nadpis.innerText = "budeš mít dobrej den"
    } else if (random === 4) {
        nadpis.innerText = "ztratíš všechno"
    } else {
        nadpis.innerText = "najdeš pravou lásku"
    }
}
