#!/usr/bin/env python3

import xmltodict
from ..basics.types import *
from ..basics.layers import *
from ..basics.elements import *
from ..basics.property import *
from ..basics.model import *
from collections import OrderedDict


def load_model_to_dict(xml_file):
    
    """TODO"""
    with open(xml_file, encoding="utf8") as file_format:
        archi_model = xmltodict.parse(file_format.read())
        return archi_model


def get_model_child(archi_model, child, grandchild=None):

    """TODO"""
    return archi_model['model'][child.value] if grandchild is None else archi_model['model'][child.value][grandchild.value]


def reverse_enum(enum, value):

    """TODO"""
    for e in enum:
        if e.value == value:
            return e
    return None


def get_layer_and_type(xml_types):

    """TODO: Este metodo requiere de mucho mantenimiento, tratar de mejorar"""
    result = None
    if len(xml_types) > 1:
        result = (reverse_enum(Layers, xml_types[0]).name, reverse_enum(Types, xml_types[1]).name)
    else:
        if xml_types[0] == 'Goal':
            result = (Layers.Motivation.value, reverse_enum(Types, xml_types[0]).value)
        elif xml_types[0] == 'Principle':
            result = (Layers.Motivation.value, reverse_enum(Types, xml_types[0]).value)
        elif xml_types[0] == 'Driver':
            result = (Layers.Motivation.value, reverse_enum(Types, xml_types[0]).value)
        elif xml_types[0] == 'Constraint':
            result = (Layers.Motivation.value, reverse_enum(Types, xml_types[0]).value)
        elif xml_types[0] == 'Stakeholder':
            result = (Layers.Motivation.value, reverse_enum(Types, xml_types[0]).value)
        elif xml_types[0] == 'Requirement':
            result = (Layers.Motivation.value, reverse_enum(Types, xml_types[0]).value)
        elif xml_types[0] == 'Assessment':
            result = (Layers.Motivation.value, reverse_enum(Types, xml_types[0]).value)
    return result


def get_element_prop(element, prop_key):

    """TODO"""
    return element[Elements.Label.value][Elements.Text.value] if prop_key == Elements.Text else element[prop_key.value]


def break_complex_type_layer(complex_type):

    """TODO"""
    import re
    return re.findall('[A-Z][^A-Z]*', complex_type)


def get_relation_prop(relation, prop_key):

    """TODO"""
    return relation[prop_key.value]

def get_element_props(xml_element,property_defs):
        
    """TODO"""
    properties={}
    if Model.Properties.value in xml_element.keys():
        #if isinstance(xml_element[Model.Properties.value][Model.Property.value],OrderedDict):
        if isinstance(xml_element[Model.Properties.value][Model.Property.value],list): 
            for xml_property in xml_element[Model.Properties.value][Model.Property.value]:                       
                prop_key = property_defs[xml_property[Property.IdentifierRef.value]]
                prop_value = xml_property[Property.Value.value][Property.Text.value] 
                properties[prop_key] =  prop_value
        else:
            prop_key = xml_element[Model.Properties.value][Model.Property.value][Property.IdentifierRef.value]
            prop_value = xml_element[Model.Properties.value][Model.Property.value][Property.Value.value][Property.Text.value] 
            properties[prop_key]  =  prop_value
    return properties

def get_property_defs(archi_model):
    property_defs={}
    xml_properties = get_model_child(archi_model, Model.PropertyDefs, Model.PropertyDef)
    if isinstance(xml_properties,list):
        for prop_def in get_model_child(archi_model, Model.PropertyDefs, Model.PropertyDef):
            property_defs[prop_def['@identifier']]=prop_def['@name'].lower()
    else:
        property_defs[xml_properties['@identifier']]=xml_properties['@name'].lower()   
    return property_defs
    