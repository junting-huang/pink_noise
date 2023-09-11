import streamlit as st
from streamlit.components.v1 import html
import random

class MarkovChain:
    def __init__(self):
        self.lookup_dict = {}

    def add_string(self, text):
        words = list(text.replace(" ", "").replace("\n", ""))
        for i in range(0, len(words)-2):
            key = (words[i], words[i + 1])
            if key in self.lookup_dict:
                self.lookup_dict[key].append(words[i + 2])
            else:
                self.lookup_dict[key] = [words[i + 2]]

    def generate_text(self, max_length=25):
        key = random.choice(list(self.lookup_dict.keys()))
        gen_words = []
        gen_words.append(key[0])
        gen_words.append(key[1])
        while len(gen_words) < max_length:
            key = tuple(gen_words[-2:])
            if key in self.lookup_dict:
                gen_words.append(random.choice(self.lookup_dict[key]))
            else:
                break
        return ''.join(gen_words)

def format_output(generated_text, num_lines=4):
    chars_per_line = len(generated_text) // num_lines
    formatted_text = ''
    for i in range(num_lines):
        formatted_text += generated_text[i*chars_per_line:(i+1)*chars_per_line] + '\n'
    return formatted_text

def load_default_text():
    with open('data/pink_noise_chn.txt', 'r', encoding='utf-8') as file:
        text = file.read()
    return text

text_data = load_default_text()
formatted_text = ''

# Define your javascript
my_js = """
let title, subtitle;

function setup() {
  // create canvas
  createCanvas(710, 400);

  title = createElement('h2', 'Pink Noise Generator 粉红色噪音诗歌生成器');
  title.position(20, 5);

  subtitle = createElement('h5', 'a literary experiment inspired by Hsia Yu 基于夏宇的文学实验');
  subtitle.position(300, 50);

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
"""

# Wrap the javascript as html code
my_html =f'''
<!DOCTYPE html>
<html>
  <head>
    <script src="https://cdn.jsdelivr.net/npm/p5@1.7.0/lib/p5.js"></script>
    <script>{my_js}</script>
  </head>
  <body>
    <main>
    </main>
  </body>
</html>
'''

# Execute your app
st.components.v1.html(my_html,height=100)
                      
if text_data and st.button('Generate Text 生成文本'):
    markov_chain = MarkovChain()
    markov_chain.add_string(text_data)
    generated_text = markov_chain.generate_text()
    formatted_text = format_output(generated_text)

st.text_area("Pink Noise Peotry 粉红色噪音诗歌:", value=formatted_text, height=200)