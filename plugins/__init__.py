# experimental package for non-core plugin modules
#
# A Zwiki plugin is a module (file) providing a mixin class that extends
# ZWikiPage, thereby adding extra features to all wiki pages at startup.
# A true plugin (a) can be removed without ill effect aside from disabling
# the feature it provides, and (b) could be provided by a separate
# product.
# 
# Mixins which used to be in the main ZWiki package are gradually being
# moved here and pluginised. Some of them still have dependencies in other
# parts of the code, eg
#
# PurpleNumbers
# - Editing calls purple numbers when setting text
# - pagetypes/* calls purple numbers methods
#
# page types are another kind of "plugin", residing in their own pagetypes
# package. 

from Products.ZWiki.Utils import BLATHER

# a nasty way to subclass a runtime list of classes, since we can't modify
# __bases__ of an extension class - ZWikiPage.ZWikiPage must subclass each
# of these slots explicitly
class Null: pass
PLUGINS = [
    Null,
    Null,
    Null,
    Null,
    Null,
    Null,
    Null,
    Null,
    Null,
    Null,
    Null,
    Null,
    Null,
    Null,
    Null,
    Null,
    ]

def registerPlugin(c):
    """
    Add a class to Zwiki's global plugin registry.

    >>> from Products.ZWiki.plugins import registerPlugin
    >>> registerPlugin(MyMixinClass)

    """
    name = '%s.%s' % (c.__module__,c.__name__)
    for i in range(len(PLUGINS)):
        if PLUGINS[i] == Null:
            PLUGINS[i] = c
            BLATHER('registered plugin: %s' % name)
            return
    BLATHER('could not register plugin: %s, need more plugin slots!' % name)

# import all modules in this directory so that each will register its plugin
import os,glob
os.chdir(__path__[0])
modules = glob.glob('*.py')
modules.remove('__init__.py')
modules = filter(lambda x:not x.startswith('test'), modules)
for file in modules:
    __import__('Products.ZWiki.plugins.%s' % file[:-3])

#print 'plugin registry:',PLUGINS