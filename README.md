# Tic-Tac-Toe AI

A Python-based Tic-Tac-Toe game where a player competes against an AI bot. The bot uses the **Minimax algorithm with Alpha-Beta Pruning** to evaluate possible moves and make strategic decisions.

## About the Project

This project implements a classic Tic-Tac-Toe game with an AI opponent. The player uses `O`, while the bot uses `X`.

The main goal of the project is to demonstrate how **game-playing algorithms** can be used to make an AI evaluate different possible game states and choose the best available move.

## Features

* Player vs. AI gameplay
* AI decision-making using the **Minimax algorithm**
* **Alpha-Beta Pruning** to reduce unnecessary game-state evaluations
* Automatic win and draw detection
* Input validation for player moves
* Prevention of moves in occupied positions
* Console-based game board

## How It Works

The game board is represented using a Python dictionary where positions `1` to `9` represent the available cells.

The AI evaluates possible moves using the Minimax algorithm:

* The AI tries to maximize its score.
* The player is treated as the minimizing opponent.
* Winning moves receive a positive score.
* Losing moves receive a negative score.
* Draws receive a score of `0`.
* The search depth is considered when calculating scores, allowing the AI to prefer faster wins and delay losses.

### Alpha-Beta Pruning

Alpha-Beta Pruning is used with Minimax to skip game states that do not need to be evaluated. This reduces the number of possible moves the algorithm needs to explore while maintaining the same decision quality.

## Technologies Used

* Python
* Minimax Algorithm
* Alpha-Beta Pruning
* Recursion
* Game State Evaluation

## Project Structure

```text
Tic-Tac-Toe/
│
├── tic_tac_toe.py
└── README.md
```

## How to Run

1. Make sure Python is installed.
2. Clone the repository.
3. Run the Python file:

```bash
python tic_tac_toe.py
```

4. Enter a position from `1` to `9` when prompted.

## Example Board

```text
1|2|3
-----
4|5|6
-----
7|8|9
```

The player enters the number of the position where they want to place `O`.

## Learning Outcomes

Through this project, I practiced:

* Implementing algorithms using Python
* Understanding recursion and game-state search
* Applying the Minimax algorithm
* Using Alpha-Beta Pruning to optimize search
* Handling user input and game conditions
* Building a simple AI-based application
