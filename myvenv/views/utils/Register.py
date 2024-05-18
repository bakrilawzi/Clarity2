import os
import sys
path = os.path.join("C:","Users","user","Desktop","Project 308","myvenv","views","utils")
path2 = os.path.join("C:","Users","user","Desktop","Project 308","myvenv","models","utils")
pathroot = os.path.join("C:","Users","user","Desktop","Project 308","myvenv") 
sys.path.append(pathroot)
sys.path.append(path)
sys.path.append(path2)
# sys.path.append(str(Path("models").resolve()))
# sys.path.append(str(Path("models/utils").resolve()))

# sys.path.append(path3)
import dearpygui.dearpygui as dpg
from models.utils.Database import Databases
from views.utils.running_front import Running
class Register(Databases,Running):
    def __init__(self):
        super().__init__()
        # dpg.create_context()
        # dpg.create_viewport(title="Clarity", width=1300, height=600)
        # dpg.setup_dearpygui()
        # dpg.show_viewport()
        self.login_window_x = (1300) // 2
        self.login_window_y = (600) // 2

    def starting_Windows(self) -> None:
         dpg.delete_item("Login")
         with dpg.window(tag="Register", label="Register", width=1300, height=600,pos=[0,0]):
              dpg.add_input_text(tag=104,label="Name", width=200, hint="Enter name",pos=[self.login_window_x-80,self.login_window_y+45])
              dpg.add_input_text(tag=105,label="LastName", width=200, hint="Enter LastName",pos=[self.login_window_x-80,self.login_window_y+65])
              dpg.add_input_text(tag=106,label="Email", width=200, hint="Enter Email",pos=[self.login_window_x-80,self.login_window_y+85])
              dpg.add_input_text(tag=107,label="Password", width=200, hint="Enter password", pos=[self.login_window_x-80,self.login_window_y+105],password=True,)
              dpg.add_text("", tag="LoginStatus",pos=[self.login_window_x-80,self.login_window_y+125])
              with dpg.group(horizontal=True):
                    # dpg.add_button(label="Login", callback=self.login_callback,pos=[self.login_window_x-80,self.login_window_height+80])
                    # dpg.add_same_line()
                    dpg.add_button(label="Register",callback=self.Registration_callback ,pos=[self.login_window_x+50,self.login_window_y+145])
         


    def Registration_callback(self,sender,user_data):  
          name = dpg.get_value(104)
          last_name = dpg.get_value(105)
          email = dpg.get_value(106)
          password = dpg.get_value(107)  
          if  not ( name and last_name and email and password):
            dpg.set_value( "All fields are required")
            return
          data = [name,last_name,email,password]
          result = self.sending_data(data)
          if result: 
               result2 = self.sending_emails(name,email) 
              #  print("Done")
               if result2:
                      dpg.set_value(item=104,value="") 
                      dpg.set_value(item=105,value="") 
                      dpg.set_value(item=106,value="") 
                      dpg.set_value(item=107,value="") 
                      dpg.focus_item(item=104)
                      # dpg.destroy_context()
               else: 
                        with dpg.window(label="Warning",tag="Register2",pos=[0,0]):
                                dpg.add_text("warning")
          else:
                with dpg.window(label="Error",tag="Register3",pos=[0,0]):
                          self.start_cams()
                        #   dpg.add_text("Account Already Exists,login pls")
                
               
              
                 

    def Registering_Person(self,data):
        #add them  to the database 
        pass
        #send them an email welcome

        #return them to login 
    def ending_app(self):
         dpg.start_dearpygui()
         dpg.destroy_context()
    
# if __name__ == "__main__" and __package__ is None:
#       w = Register()
#       w.starting_Windows()
#       w.ending_app()
# callback=self.register_callback,pos=[self.login_window_x+2,self.login_window_height+80]