import os
from flask import Flask, render_template, request
from flask_socketio import SocketIO, join_room, emit
import secrets  # Import the 'secrets' library for random ID generation

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('FLASK_SECRET_KEY', 'default-secret-key')
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('game.html')

@socketio.on('connect', namespace='/game')
def handle_connect():
    room = request.sid
    join_room(room)
    emit('message', 'Connected to the game room.', room=room)

@socketio.on('player_movement', namespace='/game')
def handle_player_movement(data):
    emit('update_game', data, room=data['room'])

@socketio.on('ball_movement', namespace='/game')
def handle_ball_movement(data):
    emit('update_game', data, room=data['room'])

@app.route('/start_game')
def start_game():
    # Generate a random game ID and pass it to the template
    game_id = secrets.token_hex(6)  # Generate a random 12-character game ID
    return render_template('game.html', game_id=game_id)

if __name__ == '__main__':
    socketio.run(app, debug=True)
