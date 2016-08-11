--uzapper = {}

-- Define tables here

dofile( minetest.get_modpath("uzapper")..'/replacement_table.lua' )
dofile( minetest.get_modpath("uzapper")..'/replacement.lua' )

dofile( minetest.get_modpath("uzapper")..'/removal_table.lua' )
dofile( minetest.get_modpath("uzapper")..'/removal.lua' )

dofile( minetest.get_modpath("uzapper")..'/zaptool.lua' ) -- use the replacement and removal tables

minetest.chat_send_all("Uzapper loaded")
