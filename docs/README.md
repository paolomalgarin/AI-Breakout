<p align=center>
    <img src="./readme-stuff/banner.png" width=90%>
    <img src="./readme-stuff/board2.svg" width=90%>
</p>

<br>
<br>

# 📖 INDEX  
 * 📥 [Installation guide](./installaion-guide/README.md)
 * 📌 [Project overview](#-project-overview)  
 * 🏗️ [Project structure](#%EF%B8%8F-project-structure)  
 * 🛠️ [Technologies used](#%EF%B8%8F-technologies-used)  
 * 🎮 [Game example](#-game-example)   
 * 📄 [Licence](#-licence)  

<br>
<br>
<br>

# 📌 Project Overview

This repository contains a complete re-creation of Atari’s Breakout game, enhanced with an AI agent evolved via NEAT (NeuroEvolution of Augmenting Topologies). The project demonstrates how neuroevolution can be applied to train an agent to play (and eventually master) the game from scratch.
> [!TIP]
> [Installation guide](./installaion-guide/README.md)

<br>

---
<br>

# 🏗️ Project Structure

 The project contains 4 main scripts inside the app folder:
- **train.py**: Trains NEAT and saves a genome that can beat the game inside `app\assets\genomes\` folder.
- **app.py**: Loads and tests the best genome.
- **algo.py**: Implements a non-AI algorithm to beat the game.
- **play.py**: Lets you play the game manually.

<br>

---
<br>


# 🛠️ Technologies Used

<img src="https://skillicons.dev/icons?i=python,pygame,neat-python" /> <br>

- **Python**  
- **Pygame**  
- **NEAT-python**

<br>

---
<br>

# 🎮 Game Example  
> *Here’s a screenshot of the game in action:*

<p align=center>
    <img src="./readme-stuff/gameplay.png" width=80%>
</p>

> [!WARNING]
> To try it yourself, follow the [installation guide](./installaion-guide/README.md).

<br>

---
<br>

# 📄 Licence
This project is released under [MIT License](https://github.com/paolomalgarin/DigitML/blob/main/LICENSE.txt).
