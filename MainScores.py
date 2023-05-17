# This file’s sole purpose is to serve the user’s score currently in the scores.txt file over HTTP
# with HTML. This will be done by using python’s flask library.

from flask import Flask

app = Flask(__name__)


@app.route("/")
def score_server():
    try:
        with open('score.txt', 'r') as f:
            # with open('score.txt', 'r', encoding='utf-8'):
            score = f.read()
            a = f'''<head>
                        <title> Scores Game </title>
                    </head>
                    <body>
                        <h1> The score is <div id = "score"> {score} </div> </h1>
                    </body>
                    </html>'''
        return a, 200  # status code
    except:
        a = ''' <head>
                    <title> Scores Game </title>
                </head>
                <body>
                    <h1><div id="score" style="color:red">{ERROR}</div></h1>
                </body>
                </html>'''
        return a, 200  # status code


app.run(host='0.0.0.0', debug=True, port=5000)


