#!/usr/bin/env python3.4

"""TODO"""
from pymongo import MongoClient

class MongoUtil:
    
    """TODO"""    
    def __init__(self, conf):
        self.client = None
        self.elements_col = None
        self.views_info_col = None
        self.views_details_col = None
        self.db = None
        
        if host and port:
            self.client = MongoClient(conf['host'], conf['port'], conf['db'], conf['tz_aware'], conf['connect']) 
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
        self.views_col = self.db.views_info
        self.views_details_col = self.db.views_details
        #self.elements_rel = self.db.relationships
                                         
    def insert_element(self,element=None):
        if element:
            try:
                element_id = self.elements_col.insert_one(element.to_dict()).inserted_id
            except:
                element_id = None
                print("Error al insertar el elemento:")
                element.pretty_print()
            return element_id
        return None
   
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
            
    def insert_view(self,view=None):
        if view:
            try:
                view_info_id = self.views_info_col.insert_one(view.info()).inserted_id
                view_detail_id = self.views_details_col.insert_one(view.details()).inserted_id
            except:
                view_info_id = None
                view_detail_id = None
                print("Error al insertar la vista:")
                view.pretty_print()
        return [view_info_id,view_detail_id]
            
