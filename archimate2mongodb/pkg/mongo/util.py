#!/usr/bin/env python3.4

"""TODO"""
from pymongo import MongoClient

class MongoUtil:
    
    """TODO"""    
    def __init__(self, host=None, port=None, options={}):
        self.client = None
        self.elements_col = None
        self.db = None
        
        if host and port:
            self.client = MongoClient(host,port) 
        else:   
            self.client = MongoClient()
        self.initialize_database()            
        # except: # catch *all* exceptions
        #     e = sys.exc_info()[0]
        #     print("Error: %s" % e )
        
    def get_client(self):
        return self.client
    
    def initialize_database(self):
        self.db = self.client.archimate
        self.elements_col = self.db.elements
        #self.elements_rel = self.db.relationships
                                         
    def insert_element(self,element=None):
        if element:
            try:
                element_id = self.elements_col.insert_one(element.to_dict()).inserted_id
            except Exception:
                element_id = None
        return element_id
   
    # This wont work 'cause elements is an array of Element,
    # not an array of dict or bson.son.SON objects require for "insert_many" method
    # def insert_elements(self,elements=[]):
    #     if len(elements) > 0:        
    #         try:
    #             result = self.elements_col.insert_many(elements)
    #         except Exception:
    #             result = None
    #     return result
    
    def show_element(self,id=None):
        if id:
            print(self.elements_col.find_one({"_id" : id}))
        else:
            print(self.elements_col.find_one())
        