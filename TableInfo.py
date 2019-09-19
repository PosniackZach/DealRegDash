from ErrorData import errorDell

errorsDell, occurencesDell = errorDell()

print("Errors for Dell are {} and occurred {} times perspectively".format(errorsDell, occurencesDell))

from ErrorData import errorVMware

errors, occurences = errorVMware()

print("Errors for VMware are {} and occurred {} times perspectively".format(errors, occurences))

from ErrorData import errorLenovo

errors, occurences = errorLenovo()

print("Errors for Lenovo are {} and occurred {} times perspectively".format(errors, occurences))

from ErrorData import errorAPC

errors, occurences = errorAPC()

print("Errors for APC are {} and occurred {} times perspectively".format(errors, occurences))

from ErrorData import errorHPE

errors, occurences = errorHPE()

print("Errors for HPE are {} and occurred {} times perspectively".format(errors, occurences))

from ErrorData import errorHPI

errors, occurences = errorHPI()

print("Errors for HPI are {} and occurred {} times perspectively".format(errors, occurences))