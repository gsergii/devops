# 💰 converter: The Money Magic Calculator
### ✨ Turning one set of numbers into another with container sorcery!

## 🧙‍♂️ About This Spellbook

Tired of doing mental math to figure out how many Ukrainian Hryvnyas you can get for your Dollars? Fret no more! This **Money Magic Calculator** is a simple web application that does all the heavy lifting for you. It's built with Python, powered by Flask, and packaged in a Docker container to protect it from pesky dependency curses.

Forget `pip install`, `virtualenv`, and other dark arts. All you need is Docker, and we'll handle the rest of the magic.

## 🛠️ How to Perform the Incantation

### Step 1: Summon the Docker Spirit

Make sure you have **Docker** installed on your computer. If not, you can find the ancient scrolls [here](https://www.docker.com/get-started/).

### Step 2: Build the Magical Artifact

Navigate to the project directory and run this command in your terminal. It will forge all our files into a magical artifact (a Docker image).

```bash
docker build -t web-converter .
```

### Step 3: Release the Genie from the Bottle
Now, it's time to run our container. Just chant this incantation into your terminal:

```bash
docker run -p 8000:8000 web-converter
```

### Step 4: Bask in the Results!
Open your web browser and travel to this enchanted address:

http://localhost:8000

Voila! You are now the master of currencies.

## 🔮 The Inner Magic (for the Curious)

app.py: The main spell scroll. It contains all the logic for our web application.

templates/index.html: The ancient parchment that holds everything the user sees.

requirements.txt: The list of essential ingredients (libraries) to make the magic work.

Dockerfile: The detailed guide for the Docker Spirit to follow.

## 📜 Gratitude
This project was created with love and Python, spiced with a dash of Flask, and sealed in a Docker container. A special thanks to the ExchangeRate-API for providing the up-to-date currency rates, without which our sorcery would be impossible.