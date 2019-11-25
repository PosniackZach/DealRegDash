import sqlite3
from sqlite3 import Error


def create_connection():
    conn = None
    try:
        conn = sqlite3.connect(r"C:\Users\ZPOSNIAC\PycharmProjects\DealRegDash\DealRegDB\dealreg.db")
    except Error:
        print(Error)

    return conn

def create_errorArray(vendor, conn):
    array = []
    cur = conn.cursor()
    sql = '''SELECT error, COUNT(error)
                FROM errorTable
                WHERE vendor = ?
                GROUP BY error
                ORDER BY COUNT(error) DESC;'''
    var = [vendor]
    cur.execute(sql, var)
    rows = cur.fetchall()
    for row in rows:
        line = []
        line.append(row[0])
        line.append(row[1])
        requests = errorIDs(vendor, row[0], conn)
        for x in requests:
            request = x[0]
            line.append(request)
        array.append(line)
    return array


def errorIDs(vendor, error, conn):
    cur = conn.cursor()
    sql = '''SELECT id
                FROM errorTable
                WHERE vendor = ? AND error = ?
                GROUP BY id;'''
    var = (vendor, error)
    cur.execute(sql, var)
    requests = cur.fetchall()
    return requests

def errorInfo(vendor):
    conn = create_connection()
    errorArray = create_errorArray(vendor, conn)
    return errorArray

def auditInfo():
    conn = create_connection()
    cur = conn.cursor()
    sql = '''SELECT * FROM audit;'''
    cur.execute(sql)
    array = cur.fetchall()
    auditArray = []
    for x in array:
        line = {}
        line['vendor'] = x[0]
        line['running'] = x[1]
        line['lastrun'] = x[2]
        auditArray.append(line)
    return auditArray