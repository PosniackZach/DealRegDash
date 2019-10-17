from flask import Flask, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)

@app.route('/')
@app.route('/index', methods=['GET', 'POST'])
def index():
        from OperationInfo import results, times
        return render_template('home.html', dell=results[0], dellTime=times[0], vmware=results[1], vmwareTime=times[1],
                               lenovo=results[2], lenovoTime=times[2], apc=results[3], apcTime=times[3], hpe=results[4],
                               hpeTime=times[4], hpi=results[5], hpiTime=times[5])
@app.route('/updateTable', methods=['GET'])
def updateTable():
        from OperationInfo import results, times
        dell = results[0]
        dellTime = times[0]
        vmware = results[1]
        vmwareTime = times[1]
        lenovo = results[2]
        lenovoTime = times[2]
        apc = results[3]
        apcTime = times[3]
        hpe = results[4]
        hpeTime = times[4]
        hpi = results[5]
        hpiTime = times[5]
        return (dell, dellTime, vmware, vmwareTime, lenovo, lenovoTime, apc, apcTime, hpe, hpeTime, hpi, hpiTime)
@app.route('/Dell')
def Dell():
        from TableInfo import errorsDell, occurencesDell
        return render_template('dell.html', errorsDell=errorsDell, occurencesDell=occurencesDell)
@app.route('/VMware')
def VMware():
        from TableInfo import errorsVMware, occurencesVMware
        return render_template('vmware.html', errorsVMware=errorsVMware, occurencesVMware=occurencesVMware)
@app.route('/Lenovo')
def Lenovo():
        from TableInfo import errorsLenovo, occurencesLenovo
        return render_template('lenovo.html', errorsLenovo=errorsLenovo, occurencesLenovo=occurencesLenovo)
@app.route('/APC')
def APC():
        from TableInfo import errorsAPC, occurencesAPC
        return render_template('apc.html', errorsAPC=errorsAPC, occurencesAPC=occurencesAPC)
@app.route('/HPE')
def HPE():
        from TableInfo import errorsHPE, occurencesHPE
        return render_template('hpe.html', errorsHPE=errorsHPE, occurencesHPE=occurencesHPE)
@app.route('/HPI')
def HPI():
        from TableInfo import errorsHPI, occurencesHPI
        return render_template('hpi.html', errorsHPI=errorsHPI, occurencesHPI=occurencesHPI)

if __name__ == '__main__':
    app.run()