#!/usr/bin/env python3

from enum import Enum


class Views(Enum):
    
  """TODO"""  
  Identifier = '@identifier'
  #Information = 'Information' #TOGAF Supports Information Layer, Archimate don't
  Motivation = '@viewpoint'
  Infrastructure = 'Infrastructure' #No han sido probadas
  Application = 'Application' #No han sido probadas

