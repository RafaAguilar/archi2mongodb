#!/usr/bin/env python3

"""TODO"""
import json
from ..basics.relations import *
from ..utils.utils import *

class Relation:


    """TODO"""
    def __init__(self, xml_relationship):
        self.relation = {}
        for r in Relations:
            self.relation[r.name] = get_relation_prop(xml_relationship, r)

    def to_dict(self):
        return self.relation

    def to_json(self):
        return json.dumps(self.relation, ensure_ascii=False)

    def pretty_print(self):
        print(json.dumps(self.relation, ensure_ascii=False, sort_keys=True, indent=4, separators=(',', ': ')))

    def id(self):
        return self.relation[Relations.Identifier.name]

    def source_id(self):
        return self.relation[Relations.Source.name]
