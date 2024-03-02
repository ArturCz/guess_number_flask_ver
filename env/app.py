from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def game():
    if request.method == 'GET':
        return render_template('game.html', min_num=0, max_num=1000, guess=int(1000/2), tries=0)

    if request.method == 'POST':
        min_num = int(request.form['min_num'])
        max_num = int(request.form['max_num'])
        guess = int(request.form['guess'])
        tries = int(request.form['tries'])

        answer = request.form['answer']

        if answer == "too_big":
            max_num = guess
            guess = int((max_num - min_num) / 2 + min_num)
        elif answer == "too_small":
            min_num = guess
            guess = int((max_num - min_num) / 2 + min_num)
        elif answer == "correct":
            message = f"Great! I guessed it in {tries + 1} tries."
            return render_template('game.html', min_num=min_num, max_num=max_num, guess=guess, tries=tries, message=message)

        tries += 1

        return render_template('game.html', min_num=min_num, max_num=max_num, guess=guess, tries=tries)

if __name__ == '__main__':
    app.run(debug=True)
