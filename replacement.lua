
-- ========== Perform node replacement when in range of a player

for _,node_name in pairs(replacement_nodes) do
    minetest.register_alias(":"..node_name[1], {
        groups = {old=1},
	newnode = node_name[2],
    })
end

minetest.register_abm({
    nodenames = {"group:old"},
    interval = 1,
    chance = 1,
    action = function(pos, node)
        minetest.env:remove_node(pos) -- TODO do a replacement to node's newnode
    end,
})

-- ========== Perform entity replacement when in range of a player

for _,entity_name in ipairs(replacement_entities) do
    minetest.register_entity(":"..entity_name[1], {
        on_activate = function(self, staticdata)
            self.object:remove()
	    -- TODO add line to get numbers, spawn an entity stack
        end,
    })
end
