import pymongo
from config import DATABASE_HOST, DATABASE_NAME
from common_functions import printException


# Database connector...
def mongoDBConnector():
    try:
        myclient = pymongo.MongoClient(DATABASE_HOST)
        mydb = myclient[DATABASE_NAME]
        return mydb
    except (Exception) as error:
        printException("mongoDBConnector()", error)

def insertData(col_name: str, data: dict|list) -> bool:
    try:
        connector = mongoDBConnector()
        col_cursor = connector[col_name]
        print(type(data), data)
        if type(data) == dict:
            insert = col_cursor.insert_one(data)
        else:
            insert = col_cursor.insert_many(data, ordered = False)
        print("inserted status: ",insert)
        return True
    except (Exception) as error:
        printException("insertData()", error)
        return False
    
def getAllData(col_name: str = "weather_data") -> bool|dict:
    try:
        connector = mongoDBConnector()
        col_cursor = connector[col_name]
        all_data = col_cursor.find({},{"_id":0})
        serilaized_data = [ document for document in all_data ]
        return serilaized_data
    except (Exception) as error:
        printException("getAllData()", error)
        return False

def getSelectiveData(col_name: str = "weather_data", request: dict = {}, output_param:dict = {}) -> bool|dict:
    try:
        connector = mongoDBConnector()
        col_cursor = connector[col_name]
        get_data = col_cursor.find_one(request, {"_id":0,**output_param})
        print("get one: ", get_data)
        # for i in insert:
        #     print(i)
        return get_data
    except (Exception) as error:
        printException("getSelectiveData()", error)
        return False
