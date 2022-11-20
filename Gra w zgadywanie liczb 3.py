from flask import Flask, request

app = Flask(__name__)


HTML_start = """
<!DOCTYPE html>
<html lang='en'>
<head>
    <meta charset="UTF-8">
    <title>Guess the number!</title>
</head>
<body>
<h4>Imagine the number between 1 and 1000</h4>
<form action='/' method='POST'>
    <input type='hidden' name='min' value='{min}'></input>
    <input type='hidden' name='max' value='{max}'></input>
    <input type='submit' value='ok'></input>
</form>

</body>
</html>    
"""


HTML = """
<!DOCTYPE_html>
<html lang='en'>
<head>
    <meta charset='UTF-8'>
    <title>Guess the number</title>
</head>
<body>
<h4>It is number <h3>{guess}</h3></h4>
<form action='' method='POST'>
    <input type='submit' name='user_answer' value='to big'>
    <input type='submit' name='user_answer' value='to small'>
    <input type='submit' name='user_answer' value='You won'>
    <input type='hidden' name='min' value='{min}'>
    <input type='hidden' name='max' value='{max}'>
    <input type='hidden' name='guess' value='{guess}'>
</form>

</body>
</html>
"""


HTML_WON = """
<!DOCTYPE_html>
<html lang='en'>
<head>
    <meta charset='UTF-8'>
    <title>Guess the number!</title>    
</head>
<body>
<h1>Hurra! I guess! Your number is {g}</h1>

</body>
</html>
"""


@app.route("/", methods=["GET", "POST"])
def guess_number():
    if request.method == "GET":
        return HTML_start.format(min=0, max=1000)
    else:
        min_number = int(request.form.get("min"))
        max_number = int(request.form.get("max"))
        user_answer = request.form.get("user_answer")
        guess = int(request.form.get("guess", 500))
        if user_answer == "to big":
            max_number = guess
        elif user_answer == "to small":
            min_number = guess
        elif user_answer == "You won":
            return HTML_WON.format(g=guess)

        guess = (max_number - min_number) // 2 + min_number
    return HTML.format(guess=guess, min=min_number, max=max_number)


if __name__ == "__main__":
    app.run()
