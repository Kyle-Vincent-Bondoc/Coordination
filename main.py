import keyboard

# Define Coordinate Variables
x = 0
y = 0
z = 0
position = [x, y, z]
moves = 0

# Define Moving Functions
# Right
def px():
  global x
  x += 1
  moves += 1
# Left
def nx():
  global x
  x -= 1
  moves += 1
# Up
def py():
  global y
  y += 1
  moves += 1
# Down
def ny():
  global y
  y -= 1
  moves += 1
# Forward
def pz():
  global z
  z += 1
  moves += 1
# Backward
def nz():
  global z
  z -= 1
  moves += 1

# Define Coordinate Function
def show_coords():
  global position
  return position

# Define Moves Function
def show_moves():
  global moves
  return moves

# Define Teleport Function
def teleport():
  global position, x, y, z
  teleport_position_x = input("Teleport to what x? : ")
  teleport_position_y = input("Teleport to what y? : ")
  teleport_position_z = input("Teleport to what z? : ")
  x = teleport_position_x
  y = teleport_position_y
  z = teleport_position_z
  position = [x, y, z]
  return f"New Position is: {position}"

# Define Keyboard Hotkeys
keyboard.add_hotkey('q', px)
keyboard.add_hotkey('w', nx)
keyboard.add_hotkey('e', py)
keyboard.add_hotkey('r', ny)
keyboard.add_hotkey('t', pz)
keyboard.add_hotkey('y', nz)
keyboard.add_hotkey('shift + ctrl + p', show_coords)
keyboard.add_hotkey('shift + ctrl + m', show_moves)
keyboard.add_hotkey('shift + ctrl + t', teleport)
