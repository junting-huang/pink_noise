let greeting;

function setup() {
  // create canvas
  createCanvas(710, 400);

  greeting = createElement('h1', 'Pink Noise Generator 粉红色噪音诗歌生成器');
  greeting.position(20, 5);

  textAlign(CENTER);
  textSize(50);

  // Call the greet function every 1 second
  setInterval(greet, 1000);
}

function greet() {
  background(255); // Clear the canvas

  for (let i = 0; i < 200; i++) {
    push();
    fill(255, random(150,255), 255);
    translate(random(width), random(height));
    rotate(random(2 * PI));
    text('Pink Noise', 0, 0);
    pop();
  }
}