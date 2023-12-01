import sys
import json
import pymongo


# Database connector...
def mongoDBConnector():
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    # myclient = pymongo.MongoClient("mongodb+srv://anand:anand@cluster0.z46hviw.mongodb.net/WeatherData?retryWrites=true&w=majority")
    mydb = myclient["WeatherData"]
    return mydb

def printException(func_name: str, error: str) -> None:
    print(f'{func_name}: {error}')
    _, __, exc_tb = sys.exc_info()
    print(f'Line No: {exc_tb.tb_lineno}')


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

# With Filter...
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
    


if __name__ == '__main__':
    # get_col_name = str(input("Enter collection name: "))
    # get_document = input("Enter document(s): ")
    # print("get_document : str: ",get_document)
    # get_document = json.loads(get_document)
    # print("get_document : dict: ",get_document)
    # print("Insert status : ",insertData(get_col_name, get_document))


    # print("all data------>",getAllData("new_cols"))
    # user_input = 
    print("all data------>",getSelectiveData("weather_data", {"name":"Solapur"},{"main.temp":1,"main.humidity":1}))
