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
            self.view[v.name] = get_relation_prop(xml_view, r)

    def to_dict(self):
        return self.view

    def to_json(self):
        return json.dumps(self.view, ensure_ascii=False)

    def pretty_print(self):
        print(json.dumps(self.view, ensure_ascii=False, sort_keys=True, indent=4, separators=(',', ': ')))

    def id(self):
        return self.view[Views.Identifier.name]
