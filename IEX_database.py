from pymongo import MongoClient
from pymongo import ReturnDocument
from bson.objectid import ObjectId
from pprint import pprint
from IEX import iex


client = MongoClient('localhost', 27017)
db = client.IEX_Database
ticker_data_collections = db.posts


class IEX_database:
    def grab_ticker_data(self, symbol):
        iex_obj = iex()
        data = iex_obj.get_df_for_1y(symbol)
        return data


IEX_db = IEX_database()
ticker_data = IEX_db.grab_ticker_data("aapl")
post_data_to_db = ticker_data_collections.insert_one(ticker_data)
print('Post ID: {0}'.format(post_data_to_db.inserted_id))
