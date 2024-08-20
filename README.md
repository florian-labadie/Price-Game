# 🎯 Juste Prix - Le Jeu du Juste Prix

Bienvenue dans le **Jeu du Juste Prix**, un jeu de devinettes simple mais captivant, développé en Python ! Votre objectif est de deviner un nombre secret compris entre 1 et 10 000 en un minimum de tentatives. Saurez-vous trouver le juste prix ?

## 📜 Table des Matières

- [Fonctionnalités](#fonctionnalités)
- [Installation](#installation)
- [Utilisation](#utilisation)
- [Exemple de Partie](#exemple-de-partie)
- [Règles du Jeu](#règles-du-jeu)
- [Structure du Projet](#structure-du-projet)
- [Contributeurs](#contributeurs)

## ✨ Fonctionnalités

- **Jeu aléatoire :** Un nouveau nombre secret est généré à chaque nouvelle partie.
- **Tentatives illimitées :** Continuez à deviner jusqu'à trouver le nombre secret.
- **Indices fournis :** Le jeu vous indique si le nombre secret est plus grand ou plus petit que votre proposition.

## 🛠 Installation

Pour commencer, clonez ce dépôt sur votre machine locale :

```bash
git clone git@github.com:florian-labadie/Price-Game.git
cd Price-Game
```

Assurez-vous d'avoir Python installé sur votre système (la version 3.x est recommandée).

## 🚀 Utilisation

Pour lancer le jeu, exécutez simplement le script :

```bash
./price_game
```

## Exemple de Partie

```bash
Welcome to the Just Right Price game!
Find the number between 1 and 10000.
Guess the secret number!
5000
The secret number is smaller.
Guess the secret number!
2500
The secret number is greater.
...
Congratulations! You found the secret number in 15 attempts.
Thank you for playing!
```

## 🎮 Règles du Jeu

1. Le jeu choisit un nombre secret aléatoire entre 1 et 10 000.
2. Vous devez deviner ce nombre en entrant vos propositions.
3. Après chaque proposition, le jeu vous indique si le nombre secret est plus grand ou plus petit que votre devinette.
4. Continuez à deviner jusqu'à ce que vous trouviez le bon nombre.
5. Le jeu vous félicitera lorsque vous aurez trouvé le nombre secret et vous indiquera le nombre de tentatives nécessaires.

## Structure du Projet

Le projet est organisé comme suit :

``` bash
Price-Game/
├── src/                # Code source principal
│   └── price_game.py   # Script principal pour l'interaction utilisateur
├── .gitignore  
├── main.py             # Point d'entrée du script principal
├── price_game          # Executable
└── README.md           # Documentation du projet
```

## Contributeurs

- Labadie Florian ([GitHub](https://github.com/florian-labadie))
