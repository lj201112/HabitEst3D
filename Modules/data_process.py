"""
Copyright (C) 2022, Jie Li

This file is part of ShapeEst3D

ShapeEst3D is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

ShapeEst3D is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with ShapeEst3D.  If not, see <https://www.gnu.org/licenses/>.
    
Author: Jie Li <lj201112@163.com>, Feb. 2019, modefied on March 2021.
License: GPL v 3
"""

class data_process():
    def __init__(self):
        pass
       
    def open_fdialog(self):
        from tkinter import filedialog
        string_var = ''
        fpath_temp = filedialog.askopenfilename(title = "Select Data File",filetypes = (("excel files",["*.xls","*.xlsx"]),("all files","*.*")))
        if fpath_temp != '':
            if fpath_temp.split('.')[-1].lower() == 'xlsx' or fpath_temp.split('.')[-1].lower() == 'xls':
                self.fpath = fpath_temp
                string_var += ('Data File {0} is loaded.'.format(''.join(self.fpath.split('/')[-1])))
            elif fpath_temp.split('.')[-1].lower() == 'csv':
                self.fpath = fpath_temp
                string_var += 'Data File {0} is loaded.'.format(''.join(self.fpath.split('/')[-1]))
            else:
                string_var += ('Please select an EXCEL or a CSV file.')
                self.fpath = None
        else:
            string_var += ('The data file has NOT been selected.')
            self.fpath = None
            
        self.open_fdialog_message = string_var
        return self.open_fdialog_message,self.fpath
        
    def processing_data(self):
        import pandas as pd
        import numpy as np
        string_var = ''
        if self.fpath == None:
            return string_var,None
        elif self.fpath.split('.')[-1] == 'xlsx' or self.fpath.split('.')[-1] == 'xls':
            try:
                df = pd.read_excel(self.fpath)
                columns = df.columns.str.lower()
            except:
                df = pd.read_csv(self.fpath, sep='\t')
                columns = df.columns.str.lower()

        elif self.fpath.split('.')[-1] == 'csv':
            df = pd.read_csv(self.fpath, sep='\t')
            columns = df.columns.str.lower()
        else:
            string_var += "Input the data file with xls or csv"

        if 'ar' in columns:
            df_new = df[df.columns[columns.get_loc('ar')]].dropna()
            temp = df_new.astype(str).str.replace(' ','',regex=True).str.replace('.','',regex=False)
            new_data_list = df_new.astype(str).str.replace(' ','',regex=True)[temp.str.isdigit()].astype(float)
            string_var += ('{0} is selected. {1} data avaliable.'.format(df.columns[columns.get_loc('ar')],len(new_data_list)))
            self.processing_data_message = string_var            
            return self.processing_data_message,np.log(np.array(list(new_data_list)))
        elif 'ratio' in columns:
            df_new = df[df.columns[columns.get_loc('ratio')]].dropna()
            temp = df_new.astype(str).str.replace(' ','',regex=True).str.replace('.','',regex=False)
            new_data_list = 1/(df_new.astype(str).str.replace(' ','',regex=True)[temp.str.isdigit()].astype(float))
            string_var += ('{0} is selected. {1} data avaliable.'.format(df.columns[columns.get_loc('ratio')],len(new_data_list)))
            self.processing_data_message = string_var
            return self.processing_data_message,np.log(np.array(list(new_data_list)))
        elif 'major' in columns and 'minor' in columns:
            df_new = df[[df.columns[columns.get_loc('major')],df.columns[columns.get_loc('minor')]]].dropna(axis=0, how='any').astype(str).replace(' ','',regex=True)
            major = df_new[df.columns[columns.get_loc('major')]]
            minor = df_new[df.columns[columns.get_loc('minor')]]
            temp_major = major.astype(str).str.replace(' ','',regex=False).str.replace('.','',regex=False).str.isdigit()
            temp_minor = minor.astype(str).str.replace(' ','',regex=False).str.replace('.','',regex=False).str.isdigit()
            new_data_df = df_new[pd.DataFrame({df.columns[columns.get_loc('major')]:temp_major, df.columns[columns.get_loc('minor')]:temp_minor})].dropna(axis=0, how='any').astype(float)
            new_data_list = new_data_df[df.columns[columns.get_loc('major')]] / new_data_df[df.columns[columns.get_loc('minor')]]
            string_var += ('{0} and {1} are selected. {2} data avaliable.'.format(df.columns[columns.get_loc('major')],df.columns[columns.get_loc('minor')],len(new_data_list)))
            self.processing_data_message = string_var
            return self.processing_data_message,np.log(np.array(list(new_data_list)))
        else:
            string_var += ('Attention: "Major" and "Minor" or "AR" or "Ratio" are ALL NOT in the Data File, Please check the data and reload the file.')
            self.processing_data_message = string_var
            return self.processing_data_message,None
            
    # def main(self):
    #     self.open_file()
    #     return self.processing_data()
        
        