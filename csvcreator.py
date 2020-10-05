# -*- coding: utf-8 -*-
"""
Created on Fri Oct  2 22:19:21 2020

@author: joedattoli
"""
"""
Created on Fri Oct  2 21:24:37 2020

@author: joedattoli
"""

import pandas as pd

#       print(time,self.get_player(),self.get_pos(),self.get_play(),self.get_direction(),self.get_speed(),self.get_bb(),self.get_base(),self.get_out(),get_align)
temp_df = pd.DataFrame(columns = ['Time', 'Player', 'Pos', 'Alignment', 'Base State', 'Out State', 'Batted Ball Type','Batted Ball Speed', 'Batted Ball Direction','Play Made', 'Extra Notes'])

temp_df.to_csv(r'C:\Users\joedattoli\Documents\GitHub\radialdefensivechart\full_list_test.csv', index = False)





