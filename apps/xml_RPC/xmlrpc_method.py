#!/usr/bin/python
#-*- coding=utf-8 -*-
from models import  FileSource

class SingleLiveSource(object):
    """store the name of the livesource by using singleton pattern"""
    class __Wrapped(object):
        """the inner class wrapped by singleton class"""
        def __init__(self):
            self.names = []

        def getNames(self):
            return self.names

        def addSourceName(self, name):
            self.names.append(name)

        def removeSourceName(self, name):
            try:
                self.names.remove(name)
            except Exception, e:
                pass
            
    instance = None
        

    @staticmethod
    def getInstance():
        """docstring for getInstance"""
        if SingleLiveSource.instance is None:
            SingleLiveSource.instance = SingleLiveSource.__Wrapped()
        return SingleLiveSource.instance

   


def accessLiveSourceName(name):
    SingleLiveSource.getInstance().addSourceName(name)
    return ' '.join(SingleLiveSource.getInstance().getNames()) + " success access. "

def removeLiveSourceName(name):
    SingleLiveSource.getInstance().removeSourceName(name)
    return '%s success remove' %(name) 

def accessFileSourceName(names):
    FileSource.objects.all().delete()
    for each_name in names:
        FileSource.objects.create(name = each_name)
    
    return " ".join(names) + " success access. "
