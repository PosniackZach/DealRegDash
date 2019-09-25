from ErrorData import errorDell

errorsDell, occurencesDell = errorDell()

from ErrorData import errorVMware

errorsVMware, occurencesVMware = errorVMware()

from ErrorData import errorLenovo

errorsLenovo, occurencesLenovo = errorLenovo()

from ErrorData import errorAPC

errorsAPC, occurencesAPC = errorAPC()

from ErrorData import errorHPE

errorsHPE, occurencesHPE = errorHPE()

from ErrorData import errorHPI

errorsHPI, occurencesHPI = errorHPI()

if __name__ == '__main__':
    print("Errors for Dell are {} and occurred {} times perspectively".format(errorsDell, occurencesDell))
    print("Errors for VMware are {} and occurred {} times perspectively".format(errorsVMware, occurencesVMware))
    print("Errors for Lenovo are {} and occurred {} times perspectively".format(errorsLenovo, occurencesLenovo))
    print("Errors for APC are {} and occurred {} times perspectively".format(errorsAPC, occurencesAPC))
    print("Errors for HPE are {} and occurred {} times perspectively".format(errorsHPE, occurencesHPE))
    print("Errors for HPI are {} and occurred {} times perspectively".format(errorsHPI, occurencesHPI))