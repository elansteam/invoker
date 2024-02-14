from config import Config

def get_database():
 
   # Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
   client = MongoClient(Config.CONNECTION_STRING)
 
   # Create the database for our example (we will use the same database throughout the tutorial
   return client[Config.DATABASE_NAME]
