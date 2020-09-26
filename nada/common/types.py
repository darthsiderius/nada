#!/usr/bin/env pypy

import enum


class PluginStatus(enum.Enum):
   """
   Plugin Status represents a plugins stability, used a lot in plugin files.
   """
   STABLE      = "Stable"
   UNSTABLE    = "Unstable"
   DEPRECATED  = "Deprecated"

class PluginClassification(enum.Enum):
   """
   Plugin Status represents a plugins stability, used a lot in plugin files.
   """
   GENERAL  = "General"
   DESIGN   = "Design"
   UTILITY  = "Utility"
