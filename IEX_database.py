import csv, operator, glob, json, pprint, urllib, urllib.request, math, codecs
from pymongo import MongoClient
from IEX import iex

iex_obj = iex()
client = MongoClient()
db = client.pymongo_test
posts = db.posts

def post_data(symbol):
    post_data = iex_obj.get_df_for_1y(symbol)
    return post_data

result = posts.insert_many(post_data)
print('Post: {0}'.format(result.inserted_ids))


# class iex:
#     @staticmethod
#     def chart_1y(symbol):
#         url = "https://api.iextrading.com/1.0/stock/" + str(symbol) + "/chart/1y"
#         response = urllib.request.urlopen(url)
#         reader = codecs.getreader("utf-8")
#         data = json.load(reader(response))
#         return data
#
#
#     def get_df_for_1y(self, symbol):
#         raw = self.chart_1y(symbol)
#
#         data = {
#             'date' : [],
#             'open' : [],
#             'high' : [],
#             'low' : [],
#             'close' : [],
#             'volume' : [],
#             'vwap' : [],
#             'label' : []
#             }
#
#         for row in raw:
#             date = row["date"]
#             price_open = row["open"]
#             price_close = row["close"]
#             price_high = row["high"]
#             price_low = row["low"]
#             vwap = row["vwap"]
#             volume = row["volume"]
#             label = row["label"]
#
#             data['date'].append(date)
#             data['label'].append(label)
#             data['open'].append(float(price_open))
#             data['high'].append(float(price_high))
#             data['low'].append(float(price_low))
#             data['close'].append(float(price_close))
#             data['volume'].append(int(volume))
#             data['vwap'].append(float(vwap))
#         return data
