#!/usr/bin/env python3

from enum import Enum


class Views(Enum):
    
  """TODO"""  
  Identifier = '@identifier'
  #Information = 'Information' #TOGAF Supports Information Layer, Archimate don't
  Viewpoint = '@viewpoint'
  Documentation = 'documentation' #No han sido probadas
  Node = 'node' #No han sido probadas
  Connection = 'connection'
  Label = 'label'

