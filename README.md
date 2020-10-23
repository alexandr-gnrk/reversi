
# Reversi
This is a implementation of game [Reversi](https://en.wikipedia.org/wiki/Reversi) (with rule-set [Othello](https://en.wikipedia.org/wiki/Reversi#Othello)).

***Reversi*** is a board game for two players with simple rules and deep strategy.

This client supports two types of interaction through a **graphical interface** or **console**.


## Stack
- Python3
- [PyGame](https://www.pygame.org/)

## Setup
Clone the repository and change the working directory:

    git clone https://github.com/alexandr-gnrk/reversi.git
    cd reversi
Create and activate the virtual environment:

    python3 -m venv ./venv
    source ./venv/bin/activate
Install requirements:

    pip3 install -r requirements.txt

Run the game:

    python3 main.py

## Usage

    usage: main.py [-h] [-m {gui,console}] [-e]
    
    Reversi game with Othello rule-set
    
    optional arguments:
      -h, --help            show this help message and exit
      -m {gui,console}, --mode {gui,console}
                            game mode
      -e, --experimental    enable experimental features
### Examples
Run with GUI mode is enabled by default:

    python3 main.py

Run with console mode:

    python3 main.py -m console

Run with GUI mode and experimental features:

    python3 main.py -m gui -e

## Implementation

Patterns that were used:
- [ModelViewController](https://en.wikipedia.org/wiki/Model%E2%80%93view%E2%80%93controller)
- [Observer](https://en.wikipedia.org/wiki/Observer_pattern)

The game supports three modes:
- Player vs Player
- Player vs Bot
- Bot vs Bot (only in experimental mode)

Cheklist:
- [x] All Othello rules implemented
- [x] The user can choose: either go for both opponents, or play against a computer player
- [x] The program does not allow you to make incorrect moves
- [x] The program determines the winner
- [x] Implemented a full game loop
