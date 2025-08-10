from flask import Flask,request,jsonify
from dotenv import load_dotenv
import pymongo,os

#Flask module object initialization
appObj=Flask(__name__)

#Configuration to load from .env file.
load_dotenv()
MONGODB_CONNECTION=os.getenv('PYMONGO_URL')

#Initialization of PyMongoDB Atlas client
client=pymongo.MongoClient(MONGODB_CONNECTION)
#PyMongo Atlas Document/NoSQL DB Creation
db=client.qaops_db
#PyMongo Atlas Document/NoSQL Collection Creation
db_collection=db['todoCRUD_app']

"""
'/api' call to fetch information from DB & convert into JSON.
"""
@appObj.route("/api")
def getJsonDataLists():
    rawData=list(db_collection.find())
    for ri in rawData:
        print("\nData Raw : ",ri)
        del ri['_id']
    
    jsonResponse={
     'data':rawData
    }
    return jsonify(jsonResponse)


"""
'/api/submit' call to insert/push information into PyMongo Atlas Document/NoSQL 'todoCRUD_app' Collection
"""
@appObj.route("/api/submit",methods=['POST'])
def insertDataToDb():
    form_data=dict(request.json)
    db_collection.insert_one(form_data)
    return "Data submitted successfully"


"""
call for 'main' module - for back-end app.
"""
if __name__ == '__main__':
   appObj.run(debug=True,port=1011)