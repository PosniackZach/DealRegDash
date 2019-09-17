from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def home():
    return '''<html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Reggie's Home</title>
    </head>
    <body style="background-color:#0F0118 ;">
        <h1 style="color:white;text-align:left;font-size:200%">DealReg Dash</h1>
    </body>
</html>'''


if __name__ == '__main__':
    app.run()