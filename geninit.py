#!/usr/bin/python

import fnmatch
import os
import sys
import re

'''
Examples 
minetest.register_node("mobs:spawner"

minetest.register_tool("mobs:shears"
minetest.register_craftitem("mobs:meat"

mobs:register_mob
mobs:register_egg
mobs:register_arrow
'''



def getStringsIn(filepath,namespace,itemtype):
    ''' return a list of itemstrings in a Lua file matching the item type '''
    local_nodes = []
    fh = open(filepath)
    for fline in fh.readlines():
        if isRegistrationLine(fline,namespace,itemtype):
            local_nodes.append(getRegistrationString(fline) )
    fh.close()
    return local_nodes

def getRegistrationString(thestring,namespace):
    registration_pat = re.compile(namespace.'[.:]register_([a-zA-Z0-9_]+)\("(.+?)"')
    return registration_pat.match(thestring).group(2)

def isRegistrationLine(thestring,namespace,itemtype):
    return "minetest.register_"+itemtype in thestring


# ====================================================

minetest_entities = []
minetest_nodes = []

for moddir in sys.argv:
	rootPath = moddir
	pattern = '*.lua'
	 
	for root, dirs, files in os.walk(rootPath):
		for filename in fnmatch.filter(files, pattern):
			filepath = os.path.join(root, filename)
			minetest_entities.extend ( getStringsIn( filepath,"minetest", "craftitem" ) )
			minetest_entities.extend ( getStringsIn( filepath,"minetest", "tool"      ) )
            minetest_entities.extend ( getStringsIn( filepath, "mobs", "mob")
			minetest_nodes.extend    ( getStringsIn( filepath, "node"      ) )

print "All the things:"
print "Entities"
print '"'+'","'.join(minetest_entities)+'"'
print "Nodes"
print '"'+'","'.join(minetest_nodes)+'"'
