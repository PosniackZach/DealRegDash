from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def home():
        from OperationInfo import results
        from OperationInfo import times
        from TableInfo import errorsDell
        from TableInfo import occurencesDell

        return render_template('home.html', dell=results[0], dellTime=times[0], vmware=results[1], vmwareTime=times[1], lenovo=results[2], lenovoTime=times[2], apc=results[3], apcTime=times[3], hpe=results[4], hpeTime=times[4], hpi=results[5], hpiTime=times[5], errorsDell=errorsDell, occurencesDell=occurencesDell)


if __name__ == '__main__':
    app.run()