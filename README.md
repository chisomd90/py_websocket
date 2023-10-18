# Multiplayer Game

The multiplayer game is a real-time, WebSocket-powered game that enables multiple players to connect and play together. It features player movements, ball movements, scoring, and chat functionality.

## Getting Started

### Prerequisites

- Python 3.x
- Flask
- Flask-SocketIO

### Installation

1. Clone the repository to your local machine.

```bash
   git clone https://github.com/yourusername/multiplayer-game.git
```

2. Create a Python virtual environment and activate it.

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```
3. Install the required dependencies from the requirements.txt file using pip.

```bash
pip install -r requirements.txt

```

## Running the Application
Start the Flask application by running:

```bash
python app.py

```
The application will be available at http://localhost:5000.

## WebSocket Connection

Players can connect to the game using a game ID and experience real-time interactions. To test a successful WebSocket connection, follow these steps:
1. Start the Flask application with python app.py.
2. Open a new browser tab and enter a URL like http://localhost:5000/start_game?game_id=my_game_id, replacing my_game_id with your desired game ID.
3. You should see a successful WebSocket connection and a displayed game ID.

## Gameplay

1. Player movements are synchronized in real-time between all connected players.
2. Ball movements are shared among players to maintain a consistent game state.
3. Scores, game state, and chat messages are updated and displayed in real-time.
4. Players can interact with each other within the game environment.

## Deployment

To deploy the multiplayer game for public access:

1. Host your Flask application on a web server.
2. Set up a domain or use a public IP address.
3. Update the WebSocket URL in the client-side code to match the server's address.


Happy Gaming!