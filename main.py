# -*- coding: utf-8 -*-

import tkinter as tk

class directional(tk.Frame):
    def __init__(self,parent,direction):
        super(directional, self).__init__(parent)
        
        
        self.label = tk.Label(self, text = direction)
        self.label.grid(row = 0, column =2)
        self.button1 = tk.Button(self, text = 'Error Field' )
        self.button1.grid(row = 1, column = 1, padx= 5)
        self.button2 = tk.Button(self, text = 'Error Throw' )
        self.button2.grid(row = 1, column = 2, padx= 5)
        #self.button3 = tk.Button(self, text = '' )
        #self.button4 = tk.Button(self, text = 'Error Field' )
    
    
    


if __name__ == "__main__":
    
    root = tk.Tk()
    east = directional(root, 'East')
    east.grid(row = 3, column = 4)
    
    west = directional(root, 'West')
    west.grid(row = 3, column = 1)
    
    root.mainloop()

