# Chess Engine - First Year Project

Welcome to the Chess Engine project developed during my first year of Computer Science studies. This project aims to create a functional chess engine using Python, implementing fundamental chess mechanics and basic AI functionalities.

## Features

- **Chess Mechanics:** Implements standard chess rules, including piece movements, castling, en passant, and promotion.
- **Command-Line Interface:** Allows users to play chess games through a text-based interface.
- **AI Opponent:** Features a basic AI using the Minimax algorithm with alpha-beta pruning to evaluate possible moves.

## Prerequisites

- **Python 3.x:** Ensure you have Python installed. You can download it from the [official website](https://www.python.org/).
- **Pygame:** Used for rendering the chessboard and pieces. Install it using pip:

  ```bash
  pip install pygame
  ```

## Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/sergiugogo/Chess-Engine-First-Year-Project.git
   ```

2. **Navigate to the Project Directory:**

   ```bash
   cd Chess-Engine-First-Year-Project
   ```

3. **Install Dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

## Usage

To start the chess engine, run:

```bash
python main.py
```

Follow the on-screen instructions to play the game.

## Project Structure

- **chess/**: Contains the core modules for the chess engine.
  - `__init__.py`: Initializes the chess module.
  - `chess_ai.py`: Implements the AI logic using the Minimax algorithm.
  - `chess_engine.py`: Manages the chessboard, piece placements, and game rules.
  - `chess_main.py`: Entry point for running the chess game.
- **images/**: Contains image assets for the chess pieces and board.

## Future Improvements

- **Graphical User Interface (GUI):** Develop a more user-friendly interface for better interaction.
- **Enhanced AI:** Improve the AI's decision-making by integrating more advanced algorithms and heuristics.
- **Game Saving and Loading:** Implement functionality to save and load game states.

## Acknowledgments

This project was inspired by various open-source chess engines and tutorials available in the programming community. Special thanks to the contributors of these projects for their valuable resources.

## License

This project is licensed under the MIT License. See the [LICENSE](./LICENSE) file for more details.

> **Note:** This project is a work in progress and serves as a learning tool for understanding the development of a chess engine.
```
