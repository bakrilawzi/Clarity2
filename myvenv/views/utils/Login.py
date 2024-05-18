import dearpygui.dearpygui as dpg
# from front import Front
import os
import sys
path = os.path.join("C:","Users","user","Desktop","Project 308","myvenv","views","utils")
sys.path.append(path)
from views.utils.Register import Register
from views.utils.front import Front
from views.utils.virtualPainter import virtualpainter as vp
# import Frame 
class Login(Register):
    def __init__(self):
        super().__init__()
        folderPath = os.path.join("../../headers", os.listdir("../headers")[0])
        self.vs = vp(folderPath)
        self.login_window_x = (1300) // 2
        self.login_window_y = (600) // 2

    def login_callback(self)->None:
         self.username = dpg.get_value(100)
         self.password = dpg.get_value(101)
         #Validating The email 
         z,res = self.checking_Validation(self.username)        
         # Check if username and password are correct
         pass_validation = self.verify_password(z["salt"],z["password"],self.password)
         if res == True and  pass_validation:
            #Show Front here
            dpg.delete_item("Login")
          #   dpg.delete_item("Register")
            front =  Front(self.vs)
            count = 0
            front.creating_window(window_name="Clarity",window_text="clarity")
            while dpg.is_dearpygui_running():
                 frame = self.vs.open_camera()
                 texture_data = front.add_camera_in_the_frame(frame)
                 if count==0:
                      with dpg.texture_registry(show=True):
                          dpg.add_raw_texture(frame.shape[1], frame.shape[0], texture_data, tag="texture_tag", format=dpg.mvFormat_Float_rgb)
                         #  print("done")
                          count+=1
                         
                 fing = self.vs.detection_fingers()
                 dpg.set_value("texture_tag", texture_data) 
               #   print("done2")        
               #   dpg.render_dearpygui_frame()
                 self.vs.selection_mode(fing)
               #   cv2.imshow("image",frame)
               #   print("done3")
                 self.vs.endin_app(frame)
                 self.vs.releasing()
               #   self.ending_app()
                      #Logic Goes Here
         else:
                with dpg.window(tag="Reg", label="Register Plz", width=1300, height=600,pos=[0,0]):
                           dpg.add_text("Unfortunately no account found! please register")
    
    def button_callback(self, sender,app_data):
          print(f"Button pressed: {sender}")
          if sender == 24:
              self.login_callback()
          elif sender == 25:
               self.starting_Windows()
          #   self.starting_Windows()
    #Overiding the window starting
    def starting_Windowss(self) -> None:
        #  self.star
     #     print("hey")
         dpg.delete_item("Register")
         with dpg.window(tag="Login", label="Login", width=1300, height=600,pos=[0,0]):
              dpg.add_input_text(tag=100,label="Email", width=200, hint="Enter Email",pos=[self.login_window_x-80,self.login_window_y])
              dpg.add_input_text(tag=101,label="Password", width=200, hint="Enter password", pos=[self.login_window_x-80,self.login_window_y+30],password=True)
              dpg.add_text("", tag="LoginStatus",pos=[self.login_window_x-80,self.login_window_y+55])
              with dpg.group(horizontal=True):
                   dpg.add_button(label="Login", callback=self.button_callback,pos=[self.login_window_x-80,self.login_window_y+80])
                    # dpg.add_same_line()
                   dpg.add_button(label="Register",callback=self.button_callback,pos=[self.login_window_x+2,self.login_window_y+80])
                  
         
    
    def ending_app(self):
         dpg.start_dearpygui()
         dpg.destroy_context()





