from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def home():
    return '''<html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Reggie's Home</title>
        <style>
img {
  display: block;
  margin-left: auto;
  margin-right: auto;
}
</style>
    </head>
    <body style="background-color:#0F0118 ;">
        <h1 style="color:white;text-align:center;font-size:200%">DealReg Dash</h1>
        <img src="https://newevolutiondesigns.com/images/freebies/robot-wallpaper-2.jpg" alt="Reggie" width="1000" height="300" border="10" style="border-color:#BD08D6;">
        <h2
    </body>
</html>'''


if __name__ == '__main__':
    app.run()