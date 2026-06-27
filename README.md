# Tic-Tac-Toe (Tris) with AI

This project is a graphical implementation of Tic-Tac-Toe (Tris) built with Python and Pygame. It features a playable AI opponent powered by the Minimax algorithm with adjustable difficulty levels.

The game allows a human player to compete against the computer in a 3x3 grid, with real-time rendering and interactive mouse controls.

## Features

- Graphical interface built with Pygame
- Human vs AI gameplay
- Three difficulty levels:
  - Easy (high randomness)
  - Medium (balanced behavior)
  - Hard (optimal play using Minimax)
- AI opponent based on the Minimax algorithm
- Win and draw detection
- Smooth turn-based gameplay system

## Requirements

- Python 3.10 or later
- Pygame

Install dependencies with:

```bash
pip install pygame
```

## How to Run

Run the game using:

```bash
python tris.py
```

## Gameplay Instructions

1. Launch the game
2. Select a difficulty level:
   - 1: Easy
   - 2: Medium
   - 3: Hard (unbeatable)
3. Click on the grid to place your move (X)
4. The AI will automatically respond with its move (O)
5. The game ends when a player wins or when the grid is full

## Project Structure

```
tic-tac-toe/
│
├── tris.py
├── README.md
└── requirements.txt
```

## AI Logic

The AI uses the Minimax algorithm to evaluate all possible future moves and select the optimal one. Difficulty levels are implemented by introducing randomness in decision-making:

- Easy: High probability of random moves
- Medium: Moderate probability of random moves
- Hard: Fully optimal Minimax-based decisions

## Notes

- The AI plays as 'O'
- The human player always plays as 'X'
- The game runs at 60 FPS for smooth rendering

## License

This project is released under the MIT License.
