# Flaskのフレームワークをインポート（FlaskとHTMLを表示するための関数を使う）
from flask import Flask, render_template, request
import random  # じゃんけんの相手（コンピュータ）の手をランダムに決めるため

# Flaskアプリを作成
app = Flask(__name__)

# ルートURL（"/"）にアクセスしたときに実行される処理を定義
@app.route("/")  # http://127.0.0.1:5000/ にアクセスしたらこの関数が呼ばれる
def index():
    return render_template("index.html")  # templates/index.html を表示する

# 新しいルート "/play" を作成
@app.route("/play")
def play():
    return render_template("play.html")  # play.html を表示する

# "/result" にアクセスしたときの処理（じゃんけんの勝敗判定）
@app.route("/result", methods=["POST"])
def result():
    hands = ["グー", "チョキ", "パー"]
    user_hand = request.form["hand"]
    computer_hand = random.choice(hands)

    # 勝敗判定
    if user_hand == computer_hand:
        result_message = "🤝 引き分け！次こそは！"
        result_class = "draw"
    elif(user_hand == "グー" and computer_hand == "チョキ") or \
        (user_hand == "チョキ" and computer_hand == "パー") or \
        (user_hand == "パー" and computer_hand == "グー"):
        result_message = "🎉 勝ち！おめでとう！ 🎉"
        result_class = "win"
    else:
        result_message = "😢 負けた…また挑戦しよう！"
        result_class = "lose"

    return render_template("result.html",
        result_message=result_message,
        result_class=result_class,
        user_hand=user_hand,
        computer_hand=computer_hand)

# Flaskアプリを実行する
if __name__ == "__main__":
    app.run(debug=True)  # debug=True でエラーがわかりやすくなる