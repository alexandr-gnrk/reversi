# Reversi
This is client to play in [Reversi](https://en.wikipedia.org/wiki/Reversi)(with rule-set Othello).

## Stack
- Python3
- [PyGame](https://www.pygame.org/)

## Setup
Clone the repository and change the working directory:

    git clone https://github.com/alexandr-gnrk/nuwm_bot.git
    cd reversi
Create and activate the virtual environment:

    python3 -m venv ./venv
    source ./venv/bin/activate
Install requirements:

    pip3 install -r requirements.txt

Run the game:

    python3 main.py

## Rules
<p>The game begins with four disks placed in a square in the middle of the grid, two facing white-side-up, two dark-side-up, so that the same-colored disks are on a diagonal. The dark player moves first.</p>
<p>In every move Player must place a piece on the board and so that there exists at least one straight (horizontal, vertical, or diagonal) occupied line between the new piece and another this player's piece, with one or more contiguous other player's pieces between them.</p>
<p>Then in every straight, all other player's pieces between the new piece and another this player's piece reverse. </p>
<p>Players take alternate turns. If one player can not make a valid move, play passes back to the other player. When neither player can move, the game ends. This occurs when the grid has filled up or when neither player can legally place a piece in any of the remaining squares.</p>
<p>The player with the most pieces on the board at the end of the game wins.</p>

## Implementation
<p>The program is implemented according to the MVC pattern. Also we used The Observer Pattern in order to a view is updated automatically whenever the model's state changes.</p>
<p>In game you can choose one of the modes:</p>
<ul>
    <li>Player vs Player</li>
    <li>Player vs Bot</li>
</ul>
<p>In Player's turn, he can click on one of available position to make move.</p>
<p>Player can't make not available move.</p>
<p>Program have full game loop.</p>
