#!/usr/bin/env python3.4

"""TODO"""
from pymongo import MongoClient

class MongoUtil:
    
    """TODO"""    
    def __new__(self, host=None, port=None, options={}):
        self.client = None
        self.archi_collection = None
        self.db = None
        try:
            if host and port:
                self.client = MongoClient(host,port) 
            else:   
                self.client = MongoClient()
            self.initialize_database()            
        except Exception:
            print(Exception) 
        
    def get_client(self):
        return self.client
    
    def initialize_database(self):
        print("pase")
        self.db = self.client.archimate
        self.elements_col = self.db.elements
        #self.elements_rel = self.db.relationships
                                         
    def insert_element(element=None):
        if element:
            try:
                element_id = self.elements_col.insert_one(element).inserted_id
            except Exception:
                element_id = None
        return element_id
    
    def insert_elements(elements=[]):
        if len(elements) > 0:        
            try:
                result = self.elements_col.insert_many(elements)
            except Exception:
                result = None
        return result
    
    def show_element(id=None):
        if id:
            self.elements_col.find_one({"_id" : id})
        else:
            self.elements_col.find_one()
        