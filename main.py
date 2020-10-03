# -*- coding: utf-8 -*-
"""
Created on Fri Oct  2 22:19:21 2020

@author: joedattoli
"""
"""
Created on Fri Oct  2 21:24:37 2020

@author: joedattoli
"""
import tkinter as tk
from datetime import datetime
import pandas as pd

#       print(time,self.get_player(),self.get_pos(),self.get_play(),self.get_direction(),self.get_speed(),self.get_bb(),self.get_base(),self.get_out(),get_align)
temp_df = pd.DataFrame(columns = ['Time', 'Player', 'Pos', 'Alignment', 'Base State', 'Out State', 'Batted Ball Type','Batted Ball Speed', 'Batted Ball Direction','Play Made', 'Extra Notes'])

temp_df.to_csv(r'C:\Users\joedattoli\Documents\GitHub\radialdefensivechart\temp.csv', index = False)

def submit_to_full():
    print('start')
    df_full = pd.read_csv(r"C:\Users\joedattoli\Documents\GitHub\radialdefensivechart\full_list.csv")
    df_temp = pd.read_csv(r"C:\Users\joedattoli\Documents\GitHub\radialdefensivechart\temp.csv")
    
    df_full = df_full.append(df_temp, ignore_index = True)
    df_full.to_csv(r"C:\Users\joedattoli\Documents\GitHub\radialdefensivechart\full_list.csv")
    print('finish')    

def temp_writer(time,player,pos,align,base,out,bbt,bbs,bbd,play,note):
    #print(time,player,pos,align,base,out,bbt,bbs,bbd,play,note)
    app_dict = {'Time' : time , 'Player' : player , 'Pos' : pos,
                'Alignment' : align, 'Base State' : base , 'Out State' : out,
                'Batted Ball Type' : bbt,'Batted Ball Speed' : bbs, 'Batted Ball Direction' : bbd,
                'Play Made' : play, 'Extra Notes' : note}
    app_series = pd.Series(app_dict)
    #print(app_series)
    df = pd.read_csv(r'C:\Users\joedattoli\Documents\GitHub\radialdefensivechart\temp.csv' )
    #print(df)
    df = df.append(app_series, ignore_index = True)
    df.to_csv(r'C:\Users\joedattoli\Documents\GitHub\radialdefensivechart\temp.csv', index = False)

class App(tk.Frame):

    def __init__(self,parent):
        super(App, self).__init__(parent)
        # player and position select
        self.label_pos = tk.Label(self,text = 'Select Pos')
        self.label_pos.grid(row=0 , column =1, padx =5)
        
        self.pos_list = ['C','1B','2B','SS','3B','LF','CF','RF']
        self.pos_var = tk.StringVar()
        self.pos_menu = tk.OptionMenu(self,self.pos_var,*self.pos_list)
        self.pos_menu.grid(row = 1 , column = 1 )
        self.pos_choice = self.pos_var.get()
        
        self.label_player = tk.Label(self,text = 'Select Player')
        self.label_player.grid(row=0 , column =0, padx =5)
        
        self.player_list = ['Wilbur', 'Thompson', 'Hendricks','Burgos']
        self.player_var = tk.StringVar()
        self.player_menu = tk.OptionMenu(self,self.player_var,*self.player_list)
        self.player_menu.grid(row = 1 , column = 0 )
        self.player_choice = self.player_var.get()
    
        #submit button
        self.label_submit = tk.Label(self, text = 'Submit Choices Here:')
        self.label_submit.grid(row =0, column =10 )
        
        self.button_submit = tk.Button(self, text = 'Submit' , command = self.submit_choices)
        self.button_submit.grid(row = 1, column = 10, padx= 5)
        
        #play and direction stuff

        self.label_play = tk.Label(self, text = "Play")
        self.label_play.grid(row = 0, column =2)
        
        self.label_dir = tk.Label(self, text = "Direction")
        self.label_dir.grid(row = 0, column =3)
        
        self.label_speed = tk.Label(self, text = "Speed of Batted Ball")
        self.label_speed.grid(row = 0, column =4)
        
        self.label_bbt = tk.Label(self, text = "Batted Ball Type")
        self.label_bbt.grid(row = 0, column =5)
        
        self.play_var = tk.StringVar()
        self.direction_var = tk.StringVar()
        self.speed_var = tk.StringVar()
        self.bb_var = tk.StringVar()
        
        
        self.options_play = ['Error Front Field', 'Error Directional Field', 'Error Throw', 'Field Front','Field Directional']
        self.play_menu = tk.OptionMenu(self,self.play_var,*self.options_play)
        self.play_menu.grid(row = 1, column = 2, padx = 15)
        
        self.options_direction = ['North','NE''East','SE','South','SW','West','NW']
        self.direction_menu = tk.OptionMenu(self,self.direction_var,*self.options_direction)
        self.direction_menu.grid(row = 1, column = 3, padx = 15)
        
        self.options_speed = ['Soft','Med','Hard']
        self.speed_menu = tk.OptionMenu(self,self.speed_var,*self.options_speed)
        self.speed_menu.grid(row = 1, column = 4, padx = 15)
        
        self.options_bb = ['Bunt','Chop','GB','LD','Flare','FB','PU']
        self.bb_menu = tk.OptionMenu(self,self.bb_var,*self.options_bb)
        self.bb_menu.grid(row = 1, column = 5, padx = 15)

        ## Situation
        self.options_base = ['---','1--','-2-','--3','12-','1-3','-23','123']
        self.options_out = ['0','1','2']
        self.base_var = tk.StringVar()
        self.out_var = tk.StringVar()       
        
        
        self.label_base = tk.Label(self, text = 'Base State')
        self.label_base.grid(row =0, column = 6)
        self.label_out = tk.Label(self, text = 'Out State')
        self.label_out.grid(row =0, column = 7)
        
        self.base_menu = tk.OptionMenu(self,self.base_var,*self.options_base)
        self.base_menu.grid(row = 1, column = 6, padx = 15)
        
        self.out_menu = tk.OptionMenu(self,self.out_var,*self.options_out)
        self.out_menu.grid(row = 1, column = 7, padx = 15)
        
        self.options_align = ['Straight UP','In','Left Pull','Left Shade', 'Right Pull', 'Right Shade', 'DP']
        self.align_var = tk.StringVar()
        
        self.label_align = tk.Label(self, text = 'Def Align')
        self.label_align.grid(row =0, column = 8)

        
        self.align_menu = tk.OptionMenu(self,self.align_var,*self.options_align)
        self.align_menu.grid(row = 1, column = 8, padx = 15)
        
        #notes
        self.label_note = tk.Label(self, text = 'Notes:')
        self.label_note.grid(row = 0, column = 9)

        self.note_entry = tk.Entry(self)
        self.note_entry.grid(row = 1, column = 9)
        
        ##submit to full csv
        self.label_final = tk.Label(self,text='SUBMIT TO FULL LIST')
        self.label_final.grid(row = 6, column = 5)
        
        
        self.button_final = tk.Button(self, text = 'Submit' , command = self.submit_all)
        self.button_final.grid(row = 7, column = 5, padx= 5)
        
        
    #(time,player,pos,align,base,out,bbt,bbs,bbd):
        
    def submit_all(self):
        submit_to_full()
        
    def submit_choices(self):
        time = datetime.now()
        temp_writer(time,self.get_player(),self.get_pos(), self.get_align(),self.get_base(),self.get_out(),self.get_bb(),self.get_speed(),self.get_direction() ,self.get_play(),self.get_note())
         
    def get_player(self):
        return self.player_var.get()
    
    def get_pos(self):
        return self.pos_var.get()  
    
    def get_play(self):
        return self.play_var.get()
    
    def get_direction(self):
        return self.direction_var.get()
    
    def get_speed(self):
        return self.speed_var.get()  
    
    def get_bb(self):
        return self.bb_var.get()

    def get_base(self):
        return self.base_var.get()  
    
    def get_out(self):
        return self.out_var.get()    
    
    def get_align(self):
        return self.align_var.get()
    
    def get_note(self):
        return self.note_entry.get()   
    

if __name__ == "__main__":
    
    root = tk.Tk()
    root.title("Defensive Chart")
    app = App(root)
    app.pack()

    
   
    

    root.mainloop()



