from flask import Flask, redirect, url_for, render_template, request
from game import Game

app = Flask(__name__)

_game = Game()

#new game
@app.route("/")
def home():
    _game.reset()
    return render_template("index.html", board=_game.get_board())

#ai turn, use minimax
@app.route("/ai")
def ai_turn():
    return None

#update board
@app.route("/<row>/<column>")
def game(row, column):
    _game.set_piece(row, column)
    win = _game.check_win()
    _game.switch_turn()
    return render_template("index.html", board=_game.get_board(), done=win, piece= 'X' if not _game.get_piece() else 'O')

if __name__ == "__main__":
    app.run(debug = True)
