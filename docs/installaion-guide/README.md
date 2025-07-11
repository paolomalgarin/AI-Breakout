# Installation Guide

## Table of Contents
1. [Prerequisites](#prerequisites)  
2. [Clone the Repository](#clone-the-repository)  
3. [Set Up a Virtual Environment](#set-up-a-virtual-environment)  
4. [Install Dependencies](#install-dependencies)  
5. [Run the Project](#run-the-project)  

---

## Prerequisites
- **Python**: Version 3.10 or higher  
- **pip**: Version 23.0 or higher  
- (Optional) **git**: to clone the repo  

---

## Clone the Repository
```bash
git clone https://github.com/paolomalgarin/AI-Breakout.git
cd AI-Breakout\app # ⚠️ move inside the app folder
```

---

## Set Up a Virtual Environment
```bash
python -m venv VirtualEnv
.\VirtualEnv\Scripts\activate # activate the virtual environment
```

---

## Install Dependencies
```bash
pip install -r ./requirements.txt
```

---

## Run the Project
```bash
# Choose between:
python train.py  # Trains NEAT and saves (inside ".\assets\genomes" folder) a genome that can beat the game
python app.py  # Loads and tests the best genome
python algo.py  # Beat the game with a non-AI algorithm 
python app.py  # Lets you play the game manually
```