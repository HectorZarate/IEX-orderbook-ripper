import csv, operator, glob, json, pprint, urllib, urllib.request, math, codecs
from pymongo import MongoClient
from IEX import iex


client = MongoClient()
db = client.pymongo_test
posts = db.posts


class IEX_database:
    def post_data(self, symbol):
        iex_obj = iex()
        data = iex_obj.get_df_for_1y(symbol)
        return data


iex_db = IEX_database()
test_post = a.post_data("aapl")
result = posts.insert_one(test_post)
print('One Post: {0}'.format(result.inserted_id))
