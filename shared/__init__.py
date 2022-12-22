from dotenv import load_dotenv
from os import getenv
from datetime import datetime, timedelta

load_dotenv()

def env(key, defaultValue=None):
    return getenv(key, defaultValue)

def getDate(value):
    finalDate = value
    if not isinstance(value, datetime):
        # Parts of date
        year, month, day = value.split('-')
        finalDate = datetime(
            int(year), int(month), int(day)
        )
    return finalDate

def getSqlDate(value):
    dt = getDate(value)
    return dt.strftime('%Y-%m-%d')

def onlyNumbers(value):
    return ''.join(filter(lambda x: x.isdigit(), value))

def getPriorValidDate(date):
    date = getDate(date)
    # check if it is sunday or saturday
    offset = 0
    if date.weekday() == 6:
        # Sunday
        offset = 2
    if date.weekday() == 5:
        # Saturday
        offset = 1

    return date - timedelta(days = offset)
    
def isSubscription(code):
    value = onlyNumbers(code)
    if value is None or value == '':
        return False
    
    subscriptionCodes = [1, 2, 9, 10, 12, 13, 14, 15]
    return int(value) in subscriptionCodes
