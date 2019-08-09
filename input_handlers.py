import tcod

def handle_keys(key):
  # movement keys
  if key.vk == tcod.KEY_UP:
    return {'move': (0, -1)}  
  elif key.vk == tcod.KEY_DOWN:
    return {'move': (0, 1)}  
  elif key.vk == tcod.KEY_LEFT:
    return {'move': (-1, 0)}  
  elif key.vk == tcod.KEY_RIGHT:
    return {'move': (1, 0)}  

  if key.vk == tcod.KEY_ENTER and key.lalt:
    # alt+enter: toggle full-screen
    return {'fullscreen': True}

  elif key.vk == tcod.KEY_ESCAPE:
    # exit the game
    return {'exit': True}

  # no key pressed:
  return {}