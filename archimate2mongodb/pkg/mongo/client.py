#!/usr/bin/env python3.4

"""TODO"""
from pymongo import MongoClient


class MongoClient:
    
    """TODO"""    
    def __new__(self, host=None, port=None, options={}):
        self.client=None
        try:
            if host and port:
                self.client = MongoClient(host,port) 
            else:   
                self.client = MongoClient()
            self.initialize_database()
            return 0
        except Exception:
            print(Exception)
            return 1
     
    def get_client(self):
        return self.client
    
    def initialize_database(self):
        self.db = self.client.archimate
        self.archi_collection = db.elements
                                         
    def find_one(self):
        print(self.archi_collection.find_one())