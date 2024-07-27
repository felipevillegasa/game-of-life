# Conway's Game of Life

This project is an implementation of Conway's Game of Life using Python and Flask for the backend, and HTML, CSS, and JavaScript for the frontend. The game includes additional features such as live metrics and session metrics to track the game's progress.

## Project Structure

### Files and Directories

- `app.py`: The main Flask application file that handles the backend logic, including grid initialization, cell toggling, stepping through generations, clearing the grid, and randomizing the grid.
- `game.py`: Contains the core game logic for Conway's Game of Life, including the functions to initialize the grid, update the grid based on game rules, and check for end conditions.
- `static/`
  - `styles.css`: The CSS file for styling the web application, including the grid, buttons, and metrics containers.
- `templates/`
  - `index.html`: The main HTML file for the web application, which includes the structure for the grid, buttons, and metrics display.
- `README.md`: This file, providing an overview of the project and its structure.

## Usage

To run the application, follow these steps:

1. **Install dependencies**: Make sure you have Flask installed. You can install it using pip:
   ```bash
   pip install Flask

2. **Run the app**: Execute the following command to start the Flask server:
    ```bash
    python app.py

3. **Open the application**: Open your web browser and navigate to http://127.0.0.1:5000 to access the application.