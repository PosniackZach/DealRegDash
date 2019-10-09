from datetime import date
import datetime

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

def isRunning(time):
    now = datetime.datetime.now()
    nowMin = now.minute
    dif = nowMin - time
    if dif <= 0:
        x = (60 - time) + nowMin
        if x > 20 and x != 60:
            return 'No'
        else:
            return 'Yes'
    else:
        x = dif
        if x > 20:
            return 'No'
        else:
            return 'Yes'


from AuditData import auditDell

try:
    result, occurrence = auditDell(currentDate)
    timeAZDell = occurenceTime(occurrence)

    if result == 'True':
        x = int(timeAZDell[3:5])
        resultDell = isRunning(x)
        if __name__ == '__main__':
            print('Dell ran today {} and was last deployed at {} AZ time.'.format(currentDate, timeAZDell))
except:
    resultDell = 'No'
    if __name__ == '__main__':
        print('Dell is currently not running')

from AuditData import auditVMware

try:
    result, occurrence = auditVMware(currentDate)
    timeAZVMware = occurenceTime(occurrence)

    if result == 'True':
        x = int(timeAZVMware[3:5])
        resultVMware = isRunning(x)
        if __name__ == '__main__':
            print('VMware ran today {} and was last deployed at {} AZ time.'.format(currentDate, timeAZVMware))
except:
    resultVMware = 'No'
    if __name__ == '__main__':
        print('VMware is currently not running')

from AuditData import auditLenovo

try:
    result, occurrence = auditLenovo(currentDate)
    timeAZLenovo = occurenceTime(occurrence)

    if result == 'True':
        x = int(timeAZLenovo[3:5])
        resultLenovo = isRunning(x)
        if __name__ == '__main__':
            print('Lenovo ran today {} and was last deployed at {} AZ time.'.format(currentDate, timeAZLenovo))
except:
    resultLenovo = 'No'
    if __name__ == '__main__':
        print('Lenovo is currently not running')

from AuditData import auditAPC

try:
    result, occurrence = auditAPC(currentDate)
    timeAZAPC = occurenceTime(occurrence)

    if result == 'True':
        x = int(timeAZAPC[3:5])
        resultAPC = isRunning(x)
        if __name__ == '__main__':
            print('APC ran today {} and was last deployed at {} AZ time.'.format(currentDate, timeAZAPC))
except:
    resultAPC = 'No'
    if __name__ == '__main__':
        print('APC is currently not running')

from AuditData import auditHPE

try:
    result, occurrence = auditHPE(currentDate)
    timeAZHPE = occurenceTime(occurrence)

    if result == 'True':
        x = int(timeAZHPE[3:5])
        resultHPE = isRunning(x)
        if __name__ == '__main__':
            print('HPE ran today {} and was last deployed at {} AZ time.'.format(currentDate, timeAZHPE))
except:
    resultHPE = 'No'
    if __name__ == '__main__':
        print('HPE is currently not running')

from AuditData import auditHPI

try:
    result, occurrence = auditHPI(currentDate)
    timeAZHPI = occurenceTime(occurrence)

    if result == 'True':
        x = int(timeAZHPI[3:5])
        resultHPI = isRunning(x)
        if __name__ == '__main__':
            print('HPI ran today {} and was last deployed at {} AZ time.'.format(currentDate, timeAZHPI))
except:
    resultHPI = 'No'
    if __name__ == '__main__':
        print('HPI is currently not running')

results = [resultDell, resultVMware, resultLenovo, resultAPC, resultHPE, resultHPI]
times = [timeAZDell, timeAZVMware, timeAZLenovo, timeAZAPC, timeAZHPE, timeAZHPI]
