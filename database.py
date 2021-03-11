import pymysql
import requests
import codecs
from decimal import Decimal

class Database:
    def __init__(self):
        self.conn = pymysql.connect(host="localhost", user="root", passwd="",db="gtfs")
        self.cursor= self.conn.cursor()
        #cursor.execute()
       # conn.commit()


    def content(self):
        with codecs.open("stops.txt", "r", "utf8") as v:
            content = v.readlines()
            data = []
            for line in content:
                splitline = line.split(','.strip())
                data.append(str((splitline[0], splitline[1])))
            return data

