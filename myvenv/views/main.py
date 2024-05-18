import os 
import sys
import dearpygui.dearpygui as dpg

# Define paths
path = os.path.join("C:","Users","user","Desktop","Project 308","myvenv","views","utils")
path2 = os.path.join("C:","Users","user","Desktop","Project 308","myvenv","models","utils")
pathroot = os.path.join("C:","Users","user","Desktop","Project 308","myvenv") 

# Append paths to sys.path
sys.path.append(pathroot)
sys.path.append(path)
sys.path.append(path2)

# Import modules
from views.utils.Login import Login
from views.utils.Register import Register
# from views.utils.front import Front

# Create instances
log = Login()
# reg = Register()

# Define function to start GUI
def start_gui():
    # dpg.create_context()
    # dpg.create_viewport(title="Clarity", width=1300, height=600)
    # dpg.setup_dearpygui()
    # dpg.show_viewport()
    log.run()
    # log.starting_Windowss()
    # dpg.start_dearpygui()
    # dpg.destroy_context()

# Start the GUI here
if __name__ == "__main__":
   start_gui()
