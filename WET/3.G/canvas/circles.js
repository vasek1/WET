let circles = []

function setup() {
    createCanvas(400, 400)
    for (let i = 0; i < 10; i++) {
        let createCircle = drawCircle()
        circles.push(createCircle)
    }
}
function draw() {
    background(220)

    for (let circle of circles) {
        ellipse(circle.x, circle.y, 30)
    }
}

function drawCircle() {
    let newCircle = {
        x: random(0, width),
        y: random(0, height),
    }
    return newCircle
}
