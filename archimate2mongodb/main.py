#!/usr/bin/env python3.4
# -*- coding: utf-8 -*-
from pkg.utils.utils import *
from pkg.relations.relation import *
from pkg.elements.element import *
from pkg.views.view import *
from pkg.basics.model import *
from pkg.basics.relations import *
from pkg.mongo.util import *

if __name__ == '__main__':
    
mongoclient = MongoUtil()  

    archi_model = load_model_to_dict('../examples/file_format_archimate.xml')
    
    property_defs=get_property_defs(archi_model)
    
    # relationships=[]
    # for relation in get_model_child(archi_model, Model.Relationships, Model.Relation):
    #     relationships.append(Relation(relation))
        
    # elements=[]
    # for element in get_model_child(archi_model,Model.Elements,Model.Element):
    #     element_instance = Element(element)  
    #     for r in relationships:
    #         if element_instance.id() == r.source_id():
    #             element_instance.add_relation(r)
    #     element_instance.set_properties(get_element_props(element, property_defs))
    #     elements.append(element_instance)
        #mongoclient.insert_element(element_instance)
        
    views=[]
    for view in get_model_child(archi_model, Model.Views, Model.View):
        views.append(View(view))
                
    print(views[0].details())
