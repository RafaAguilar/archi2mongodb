#!/usr/bin/env python3.4

"""TODO"""
import json
from pymongo import MongoClient
from ..basics.views import *


class MongoUtil:
    
    """TODO"""    
    def __init__(self, conf):
        self.client = None
        self.elements_col = None
        self.views_info_col = None
        self.views_details_col = None
        self.db = None
        
        if conf:
            self.client = MongoClient(conf['host'], conf['port'], tz_aware=conf['tz_aware'],connect=conf['connect']) 
        else:   
            self.client = MongoClient()
        self.initialize_database()         
        
    def get_client(self):
        return self.client
    
    def initialize_database(self):
        self.db = self.client.archimate
        self.elements_col = self.db.elements
        self.views_info_col = self.db.views_info
        self.views_details_col = self.db.views_details
        #self.elements_rel = self.db.relationships
                                         
    def insert_element(self,element=None):
        if element:
            try:
                element_id = self.elements_col.insert_one(element.to_dict()).inserted_id
            except:
                element_id = None
                print("Error al insertar el elemento:") #This would need an i8n strategy
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
                self.add_view_to_elements(view)                
            except Exception as e:
                view_info_id = None
                view_detail_id = None
                print("Error al insertar la vista : " + view[Views.Identifier.value])
                print(e)
        return [view_info_id,view_detail_id]
    
    #No todas las vistas estan funcionando #Abre el File Format, no el modelo en PMO
    def add_view_to_elements(self, view=None):
        if view:
            try:                
                query = { "Identifier": { "$in" :  view.elements_ref()  } }               
                update = { "$addToSet" : { "views" : view.id() } }
                options = { "multi" : "true"}
                print("{ " + str(query) + ", " + str(update) + " }")
                #self.elements_col.update( query, update)
            except Exception as e:
                print("Error al actualizar los elementos con esta vista : "  + view[Views.Identifier.value]) #This would need an i8n strategy
                print(e)
            
