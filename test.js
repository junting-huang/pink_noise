let button, greeting, text;

function setup() {
  // create canvas
  createCanvas(710, 400);

  button = createButton('Generate 生成文本');
  button.position(20, 65);
  button.mousePressed(greet);

  greeting = createElement('h2', 'Pink Noise Generator 粉红色噪音诗歌生成器');
  greeting.position(20, 5);

  textAlign(CENTER);
  textSize(50);
}

function greet() {

  for (let i = 0; i < 200; i++) {
    push();
    fill(255, random(150,255), 255);
    translate(random(width), random(height));
    rotate(random(2 * PI));
    text('Pink Noise', 0, 0);
    pop();
  }
  
  let s = 'The quick brown fox jumped over the lazy dog.';
  textSize(18);
  fill(50);
  text(s,250,150,300,300);

}