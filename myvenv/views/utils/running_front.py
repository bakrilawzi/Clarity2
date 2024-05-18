import dearpygui.dearpygui as dpg
import os ,sys 
path = os.path.join("C:","Users","user","Desktop","Project 308","myvenv","views","utils")
sys.path.append(path)
from views.utils.front import Front
from views.utils.virtualPainter import virtualpainter as vp
class Running(vp,Front):
    def __init__(self)->None:
        folderPath = os.path.join("../../headers", os.listdir("../headers")[0])
        vp().__init__()
        Front().__init__()
    def start_cams(self)->None:
            count = 0
            self.creating_window(window_name="Clarity",window_text="Exercice")
            while dpg.is_dearpygui_running():
                 
                 frame = self.open_camera()
                 print(frame)
                 texture_data = self.add_camera_in_the_frame(frame)
                 if count==0:
                      with dpg.texture_registry(show=True):
                          dpg.add_raw_texture(frame.shape[1], frame.shape[0], texture_data, tag="texture_tag", format=dpg.mvFormat_Float_rgb)
                          print("done")
                          count+=1
                         
                 fing = self.detection_fingers()
                 dpg.set_value("texture_tag", texture_data)
               #   print("done2")        
               #   dpg.render_dearpygui_frame()
                 self.selection_mode(fing)
               #   cv2.imshow("image",frame)
               #   print("done3")
                 self.endin_app(frame)
                 self.releasing()