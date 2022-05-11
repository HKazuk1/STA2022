from flask import Flask, render_template,request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', num="")

@app.route('/result', methods=["GET"])
def result_get():
    # GET送信の処理
    field = int(request.args.get("field",""))
    if field%2 == 0:
        return render_template('result.html', num = "{}は偶数です。".format(field))
    else:
        return render_template('result.html', num = "{}は奇数です。".format(field))

@app.route('/result', methods=["POST"])
def result_post():
    # POST送信の処理
    field = int(request.form["field"])
    if field <= 1: return render_template('result.html', num = "{}は素数ではありません".format(field))
    for i in range(2,int(field ** 0.5) + 1):
        if field%i == 0:
            return render_template('result.html', num = "{}は素数ではありません".format(field))
            break
    else:
        return render_template('result.html', num = "{}は素数です".format(field))


if __name__ == '__main__':
    app.run()
    