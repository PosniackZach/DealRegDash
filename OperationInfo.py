from datetime import date

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
timeAZ = occurenceTime(occurrence)

if result == 'True':
    print('Dell ran today {} and was last deployed at {} AZ time.'.format(currentDate, timeAZ))
else:
    print('Dell is currently not running')

'''from AuditData import auditVMware

result, occurrence = auditVMware(currentDate)
timeAZ = occurenceTime(occurrence)

if result == 'True':
    print('VMware ran today {} and was last deployed at {} AZ time.'.format(currentDate, timeAZ))
else:
    print('VMware is currently not running')'''

from AuditData import auditLenovo

result, occurrence = auditLenovo(currentDate)
timeAZ = occurenceTime(occurrence)

if result == 'True':
    print('Lenovo ran today {} and was last deployed at {} AZ time.'.format(currentDate, timeAZ))
else:
    print('Lenovo is currently not running')

from AuditData import auditAPC

result, occurrence = auditAPC(currentDate)
timeAZ = occurenceTime(occurrence)

if result == 'True':
    print('APC ran today {} and was last deployed at {} AZ time.'.format(currentDate, timeAZ))
else:
    print('APC is currently not running')

from AuditData import auditHPE

result, occurrence = auditHPE(currentDate)
timeAZ = occurenceTime(occurrence)

if result == 'True':
    print('HPE ran today {} and was last deployed at {} AZ time.'.format(currentDate, timeAZ))
else:
    print('HPE is currently not running')

from AuditData import auditHPI

result, occurrence = auditHPI(currentDate)
timeAZ = occurenceTime(occurrence)

if result == 'True':
    print('HPI ran today {} and was last deployed at {} AZ time.'.format(currentDate, timeAZ))
else:
    print('HPI is currently not running')