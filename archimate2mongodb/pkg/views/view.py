#!/usr/bin/env python3

"""TODO"""
import json
from ..basics.views import *
from ..utils.utils import *

class View:


    """TODO"""
    def __init__(self, xml_view):
        self.view = {}
        for v in Views:            
            self.view[v.name] = get_view_prop(xml_view, v)

    def to_dict(self):
        return self.view

    def to_json(self):
        return json.dumps(self.view, ensure_ascii=False)

    def pretty_print(self):
        print(json.dumps(self.view, ensure_ascii=False, sort_keys=True, indent=4, separators=(',', ': ')))

    def id(self):
        return self.view[Views.Identifier.name]
    
    def info(self):
        return {prop: self.view.get(prop, None) for prop in (Views.Identifier.name, Views.Documentation.name, Views.Label.name, Views.Viewpoint.name)}
    
    def details(self):
        return {prop: self.view.get(prop, None) for prop in (Views.Identifier.name, Views.Connection.name, Views.Node.name)}
    
    def elements_ref(self):
        nodes = self.view.get(Views.Node.name, None)
        return [node.get('@elementref',None) for node in nodes]
        
        
        