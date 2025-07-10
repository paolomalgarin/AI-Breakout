<p align=center>
    <img src="./readme-stuff/banner.png" width=90%>
    <img src="./readme-stuff/board2.svg" width=90%>
</p>

<br>
<br>

# 📖 INDEX  
 * 📥 [Installation guide](https://github.com/paolomalgarin/DigitML/blob/main/docs/README%20-%20Stuff/Documentation/INSTALLATION-OPTIONS.md)
 * 📌 [Project overview](#-project-overview)  
 * 🏗️ [Project structure](#%EF%B8%8F-project-structure)  
 * 🛠️ [Technologies used](#%EF%B8%8F-technologies-used)  
 * 📷 [Gui example](#-gui-example)   
 * 📄 [Licence](#-licence)  

<br>
<br>
<br>

# 📌 Project Overview

This repository contains a complete re-creation of Atari’s Breakout game, enhanced with an AI agent evolved via NEAT (NeuroEvolution of Augmenting Topologies). The project demonstrates how neuroevolution can be applied to train an agent to play (and eventually master) the game from scratch.
> [!TIP]
> [Installation guide](https://github.com/paolomalgarin/DigitML/blob/main/docs/README%20-%20Stuff/Documentation/INSTALLATION-OPTIONS.md)

<br>

---
<br>

# 🏗️ Project Structure

 The project contains 4 main scripts inside the app folder:
- **train.py**: Script to train NEAT and generate a genome _(inside `app\assets\genomes\` folder)_ capable of beating the game
- **app.py**: Script that can be used to test the best genome
- **algo.py**: Script which beats the game without AI _(only with code)_
- **play.py**: Script to play the game normaly

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

# 📷 Gui Example  
> *Here’s a screenshot of the game in action:*

<p align=center>
    <img src="./readme-stuff/gameplay.png" width=80%>
</p>

> [!WARNING]
> To try it yourself, follow the [installation guide](https://github.com/paolomalgarin/DigitML/blob/main/docs/README%20-%20Stuff/Documentation/INSTALLATION-OPTIONS.md).

<br>

---
<br>

# 📄 Licence
This project is released under [MIT License](https://github.com/paolomalgarin/DigitML/blob/main/LICENSE.txt).
