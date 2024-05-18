import dearpygui.dearpygui as dpg
import os
import sys
path = os.path.join("C:","Users","user","Desktop","Project 308","myvenv","views","utils")
path2 = os.path.join("C:","Users","user","Desktop","Project 308","myvenv","models","utils")
pathroot = os.path.join("C:","Users","user","Desktop","Project 308","myvenv") 
sys.path.append(pathroot)
sys.path.append(path)
sys.path.append(path2)
# from views.utils.virtualPainter import virtualpainter as vp
import cv2
import numpy as np
# from views.utils.Login import Login
class Front:
    def __init__(self,vs):
        self.vs = vs

        # self().__init__()
        

    def add_camera_in_the_frame(self, frame)->list:
        data = np.flip(frame, 2)
        data = data.flatten()
        data = np.asfarray(data, dtype="f")
        texture_data = np.true_divide(data, 255.0)
        # print(texture_data)
        return texture_data
    def creating_window(self,window_name,window_text)->None:
        # print("Hello1")
        with dpg.window(tag = window_name,label=window_name,width=1300,height=600):
            dpg.add_text(window_text)
            self.add_Button()
        # print("Hello2")
        dpg.set_primary_window(window_name,True)
        # dpg.add_image("texture_tag")
    def add_Button(self) -> None:
        b0 = dpg.add_button(tag=100,label="Exit",callback=self.b0_callback)
        b1 = dpg.add_button(tag=101,label="Erase",callback = self.b1_callback)
        b2 = dpg.add_button(tag=102,label="Analytics",callback = self.b2_callback)
    
    def b0_callback(self,sender,app_data,user_data):
         print(sender)
         dpg.stop_dearpygui()
    
    def b1_callback(self,sender,app_data,user_data):
         pass
         
         
    def b2_callback(self,sender,app_data,user_data):
         dpg.show_metrics()
         
    


# if __name__ == "__main__":
#     # print(os.getcwd())
#     print(os.path.join("../../headers", os.listdir("../../headers")[0]))
#     folderPath = os.path.join("../../headers", os.listdir("../../headers")[0])
#     vs = vp(folderPath=folderPath)
#     front = Front() 
#     count = 0
#     front.creating_window(window_name="Clarity",window_text="Exercice")
#     while dpg.is_dearpygui_running():
#         frame = vs.open_camera()
#         texture_data = front.add_camera_in_the_frame(frame)
#         if count==0:
#              with dpg.texture_registry(show=True):
#                  dpg.add_raw_texture(frame.shape[1], frame.shape[0], texture_data, tag="texture_tag", format=dpg.mvFormat_Float_rgb)
#                  count+=1
#         fing = vs.detection_fingers()
#         dpg.set_value("texture_tag", texture_data)        
#         dpg.render_dearpygui_frame()
#         vs.selection_mode(fing)
#         # cv2.imshow("image",frame)
#         vs.endin_app(frame)
#         # vs.releasing()

#     dpg.destroy_context()
