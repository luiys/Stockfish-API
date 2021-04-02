from flask import Flask, jsonify, request
from flask import render_template
import chess
import chess.engine

app = Flask(__name__)
engine = chess.engine.SimpleEngine.popen_uci("./stockfish.exe")
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = False

# 5k2/4ppp1/8/7q/8/8/Bp6/2K2Q2 w - - 0 1


@app.route("/stockfish/<string:line8>/<string:line7>/<string:line6>/<string:line5>/<string:line4>/<string:line3>/<string:line2>/<string:line1>/", methods=["GET"])
def index(line8, line7, line6, line5, line4, line3, line2, line1,):

    fen = line8 + "/" + line7 + "/" + line6 + "/" + line5 + \
        "/" + line4 + "/" + line3 + "/" + line2 + "/" + line1

    board = chess.Board(fen)
    result = engine.play(board, chess.engine.Limit(time=0.1))

    board.push(result.move)

    fen = board.fen()

    jsonify(fen)

    return jsonify(fen)


@app.route("/")
def hello_world():
    return "Hello from flask"


if __name__ == "__main__":
    app.run()
