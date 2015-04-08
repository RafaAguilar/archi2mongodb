#!/usr/bin/env python3

from enum import Enum


class Layers(Enum):
    
  """TODO"""  
  Business = 'Business'
  #Informacion = 'Information' #TOGAF Supports Information Layer, Archimate don't
  Motivation = 'Motivation'
  Infrastructure = 'Infrastructure' #No han sido probadas
  Application = 'Application' #No han sido probadas
