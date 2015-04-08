#!/usr/bin/env python3

import json
from ..basics.elements import *
from ..utils.utils import *


class Element:
    def __init__(self, xml_element):
        self.element = {}
        for elem in Elements:
            if elem not in (Elements.Type,  Elements.Text):
                self.element[elem.name] = get_element_prop(xml_element, elem)
            elif elem == Elements.Type:
                (self.element['Layer'], self.element[elem.name]) = get_layer_and_type(break_complex_type_layer(get_element_prop(xml_element, elem)))
            else:
                continue
        self.element['relationships'] = []
        self.element['properties'] = {}

    def to_dict(self):
        return self.element

    def to_json(self):
        return json.dumps(self.element, ensure_ascii = False)

    def pretty_print(self):
        print(json.dumps(self.element, sort_keys = True,  indent = 4,  separators = (', ',  ': '), ensure_ascii = False))

    def add_relation(self, r):
        self.element['relationships'].append(r.to_dict())

    def id(self):
        return self.element[Elements.Identifier.name]
    
    def set_properties(self, props):
        self.element['properties'] = props