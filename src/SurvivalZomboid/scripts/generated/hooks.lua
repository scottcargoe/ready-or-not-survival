return {
  ["player_tick"] = {id = "player_tick", purpose = "advance survival state", adapter_method = "on_tick", required = true, implemented = true},
  ["player_damage"] = {id = "player_damage", purpose = "apply injury and infection", adapter_method = "on_player_damage", required = true, implemented = true},
  ["use_item"] = {id = "use_item", purpose = "consume survival item", adapter_method = "on_use_item", required = true, implemented = true},
  ["search_container"] = {id = "search_container", purpose = "roll scavenging loot", adapter_method = "on_search_container", required = true, implemented = true},
  ["safehouse_stash"] = {id = "safehouse_stash", purpose = "persist returned supplies", adapter_method = "on_safehouse_stash", required = true, implemented = true},
}
