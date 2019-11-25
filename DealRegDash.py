from flask import Flask, render_template, jsonify
from flask_bootstrap import Bootstrap
from DealRegDBInfo import errorInfo, auditInfo

app = Flask(__name__)
bootstrap = Bootstrap(app)

@app.route('/')
@app.route('/index')
def index():
    array = auditInfo()
    return render_template('home2.html', array=array)


@app.route('/update', methods=['POST'])
def update():
    array = auditInfo()
    return jsonify(array)


@app.route('/Dell')
def Dell():
    dell = errorInfo('Dell')
    return render_template('dell2.html', dell=dell)


@app.route('/VMware')
def VMware():
    vmware = errorInfo('VMware')
    return render_template('vmware2.html', vmware=vmware)


@app.route('/Lenovo')
def Lenovo():
    lenovo = errorInfo('Lenovo')
    return render_template('lenovo2.html', lenovo=lenovo)


@app.route('/APC')
def APC():
    apc = errorInfo('APC')
    return render_template('apc2.html', apc=apc)


@app.route('/HPE')
def HPE():
    hpe = errorInfo('HPE')
    return render_template('hpe2.html', hpe=hpe)


@app.route('/HPI')
def HPI():
    hpi = errorInfo('HPI')
    return render_template('hpi2.html', hpi=hpi)


if __name__ == '__main__':
    app.run()