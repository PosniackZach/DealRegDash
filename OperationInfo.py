from datetime import date
from typing import List

today = date.today()
currentDay = today.day
currentMonth = today.month
currentYear = today.year
currentDate = str(currentMonth) + '/' + str(currentDay) + "/" + str(currentYear)

def occurenceTime(occurence):
    lastOccurrence = occurrence.split(':')
    if lastOccurrence[2].find('PM') != -1:
        if int(lastOccurrence[0]) >= 8 and int(lastOccurrence[0]) != 12:
            lastOccurrenceHour = int(lastOccurrence[0]) - 7
            lastOccurrenceCycle = 'PM'
        elif int(lastOccurrence[0]) == 7:
            lastOccurrenceHour = 12
            lastOccurrenceCycle = 'PM'
        elif int(lastOccurrence[0]) <= 6:
            if int(lastOccurrence[0]) == 6:
                lastOccurrenceHour = 11
            if int(lastOccurrence[0]) == 5:
                lastOccurrenceHour = 10
            if int(lastOccurrence[0]) == 4:
                lastOccurrenceHour = 9
            if int(lastOccurrence[0]) == 3:
                lastOccurrenceHour = 8
            if int(lastOccurrence[0]) == 2:
                lastOccurrenceHour = 7
            if int(lastOccurrence[0]) == 1:
                lastOccurrenceHour = 6
            lastOccurrenceCycle = 'AM'
        else:
            lastOccurrenceHour = 5
            lastOccurrenceCycle = 'AM'

    else:
        if int(lastOccurrence[0]) >= 8 and int(lastOccurrence[0]) != 12:
            lastOccurrenceHour = int(lastOccurrence[0]) - 7
            lastOccurrenceCycle = 'AM'
        elif int(lastOccurrence[0]) == 7:
            lastOccurrenceHour = 12
            lastOccurrenceCycle = 'AM'
        elif int(lastOccurrence[0]) <= 6:
            if int(lastOccurrence[0]) == 6:
                lastOccurrenceHour = 11
            if int(lastOccurrence[0]) == 5:
                lastOccurrenceHour = 10
            if int(lastOccurrence[0]) == 4:
                lastOccurrenceHour = 9
            if int(lastOccurrence[0]) == 3:
                lastOccurrenceHour = 8
            if int(lastOccurrence[0]) == 2:
                lastOccurrenceHour = 7
            if int(lastOccurrence[0]) == 1:
                lastOccurrenceHour = 6
            lastOccurrenceCycle = 'PM'
        else:
            lastOccurrenceHour = 5
            lastOccurrenceCycle = 'PM'
    lastOccurrenceMinute = lastOccurrence[1]
    return "{}:{} {}".format(lastOccurrenceHour, lastOccurrenceMinute, lastOccurrenceCycle)

from AuditData import auditDell

result, occurrence = auditDell(currentDate)
timeAZDell = occurenceTime(occurrence)

if result == 'True':
    resultDell = 'Yes'
    print('Dell ran today {} and was last deployed at {} AZ time.'.format(currentDate, timeAZDell))
else:
    resultDell = 'No'
    print('Dell is currently not running')

'''from AuditData import auditVMware

result, occurrence = auditVMware(currentDate)
timeAZVMware = occurenceTime(occurrence)

if result == 'True':
    resultVMware = 'Yes'
    print('VMware ran today {} and was last deployed at {} AZ time.'.format(currentDate, timeAZVMware))
else:
    resultVMware = 'No'
    print('VMware is currently not running')'''
resultVMware = 'Yes'
timeAZVMware = timeAZDell

from AuditData import auditLenovo

result, occurrence = auditLenovo(currentDate)
timeAZLenovo = occurenceTime(occurrence)

if result == 'True':
    resultLenovo = 'Yes'
    print('Lenovo ran today {} and was last deployed at {} AZ time.'.format(currentDate, timeAZLenovo))
else:
    resultLenovo = 'No'
    print('Lenovo is currently not running')

from AuditData import auditAPC

result, occurrence = auditAPC(currentDate)
timeAZAPC = occurenceTime(occurrence)

if result == 'True':
    resultAPC = 'Yes'
    print('APC ran today {} and was last deployed at {} AZ time.'.format(currentDate, timeAZAPC))
else:
    resultAPC = 'No'
    print('APC is currently not running')

from AuditData import auditHPE

result, occurrence = auditHPE(currentDate)
timeAZHPE = occurenceTime(occurrence)

if result == 'True':
    resultHPE = 'Yes'
    print('HPE ran today {} and was last deployed at {} AZ time.'.format(currentDate, timeAZHPE))
else:
    resultHPE = 'No'
    print('HPE is currently not running')

from AuditData import auditHPI

result, occurrence = auditHPI(currentDate)
timeAZHPI = occurenceTime(occurrence)

if result == 'True':
    resultHPI = 'Yes'
    print('HPI ran today {} and was last deployed at {} AZ time.'.format(currentDate, timeAZHPI))
else:
    resultHPI = 'No'
    print('HPI is currently not running')

results = [resultDell, resultVMware, resultLenovo, resultAPC, resultHPE, resultHPI]
times = [timeAZDell, timeAZVMware, timeAZLenovo, timeAZAPC, timeAZHPE, timeAZHPI]
