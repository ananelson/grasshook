from tables import *
import time

class PluginMeta(type):
    def __init__(cls, name, bases, attrs):
        if '__metaclass__' in attrs:
            cls.plugins = {}
        if hasattr(cls, 'alias'):
            print "registering class %s to alias %s" % (cls, cls.alias)
            cls.register_plugin(cls.alias, cls)

    def register_plugin(cls, alias, klass):
        cls.plugins[alias] = klass

    def create_instance(cls, alias, kwargs):
        klass = cls.plugins[alias]
        return klass(kwargs)
    
class Collector(object):
    __metaclass__ = PluginMeta

    def __init__(self, kwargs):
        self.settings = kwargs

    def name(self):
        return self.settings['name'] % self.settings

    def collect(self, row):
        row['name'] = self.name()
        row['value'] = self.value()
        row['collected_at'] = time.time()
        row.append()

    def value(self):
        raise Exception("not implemented")

class Dummy(Collector):
    alias = "dummy"

    def value(self):
        return 5.0
