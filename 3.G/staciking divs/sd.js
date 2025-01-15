const wrapper = document.querySelector(".wrapper")

let r = Math.floor(Math.random()* 255) // nahodna barva rgb do 255 
let b = Math.floor(Math.random()* 255) // kdyz nad forem tak stejna barva
let g = Math.floor(Math.random()* 255)

for(let i = 0;i<6; i++){
    let novyDiv = document.createElement("div") // vytvori novy  div
    novyDiv.classList.add("square") //prirazeni classy
    wrapper.appendChild(novyDiv)


novyDiv.style.backgroundColor = `rgb(${r},${g},${b})` //obarveni pozadi

wrapper.appendChild(novyDiv) //pridani do divu wrapper
}
