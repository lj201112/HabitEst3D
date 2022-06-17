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
    
Author: Jie Li <lj201112@163.com>, Feb. 2019, modefied on March 2021, July 2021, March 2022.
License: GPL v 3
"""

class ShapeFit():
    def __init__(self,data_src,shape_num,method='gaussian_kde',top_R=10):
        import numpy as np
        self.data_src = np.array(list(data_src)) # logarithmically sectional data
        self.shape_num = shape_num
        self.method = method
        self.data_length = len(data_src)
        self.top_r = top_R
    
    def get_database(self):
        import pickle
        import numpy as np
        with open('./Database/Database_LogAR_Hist.pickle','rb') as f:
            self.database_hist = pickle.load(f)
        with open('./Database/Database_LogAR_KDE.pickle','rb') as f:
            self.database_kde = pickle.load(f)
            
        if self.method == 'histogram':
            self.index = np.array(list(self.database_hist.keys()))
        elif self.method == 'gaussian_kde':
            self.index = np.array(list(self.database_kde.keys()))
        
    def R(self,x,y):
        import numpy as np
        return np.sqrt(1/len(x)*np.sum((x-y)**2))
                
    def shape_one(self):
        import numpy as np
        from scipy.stats import gaussian_kde        
        shape_dict = {}
        if self.method == 'histogram':
            hist_src = np.histogram(self.data_src,bins=30,range=(0,3),density=True)[0]
            for i in self.index:
                shape_dict[i] = self.R(self.database_hist[i],hist_src)
                
        elif self.method == 'gaussian_kde':
            x_ = np.linspace(0,3,150)
            kde_src = gaussian_kde(self.data_src)(x_)
            for i in self.index:
                shape_dict[i] = self.R(self.database_kde[i],kde_src)
        return sorted(shape_dict.items(), key=lambda x:x[1], reverse=False)[0:self.top_r]
                
    def shape_multi(self):
        with open('find_R_squared_shape.py','w') as f:
            f.write('import numpy as np\n')
            f.write('import pickle\n')
            f.write('from numba import jit\n')
            f.write('import time\n')
            f.write('\n')

            '''
            open pickle
            '''
            if self.method == 'histogram':
                f.write("with open('./Database/Database_LogAR_Hist.pickle','rb') as f:\n")
                f.write(' '*4+'database = pickle.load(f)\n')
            elif self.method == 'gaussian_kde':
                f.write("with open('./Database/Database_LogAR_KDE.pickle','rb') as f:\n")
                f.write(' '*4+'database = pickle.load(f)\n')
            f.write('index = np.array(list(database.keys()))\n')
            f.write('\n')
            f.write("with open('DataSrc_temp.pickle','rb') as f:\n")
            f.write(' '*4+'data_load = pickle.load(f)\n')
            f.write('\n')            
            
            '''
            get shapes tuple
            '''
            f.write('def get_shapes_index():\n')
            get_shapes_tuple_str = ' '*4 + 'for a{0} in range(len(index)-{1}+1):\n'.format(0,self.shape_num)
            for i in range(1,self.shape_num):
                get_shapes_tuple_str += ' '*4*(i+1)+'for a{0} in range(a{1}+1,len(index)-{2}+1):\n'.format(i,i-1,self.shape_num-i)
            yield_str = ' '*4*(self.shape_num+1)+'yield ('
            for i in range(0,self.shape_num):
                yield_str += 'a{0}'.format(i)+','
            yield_str = yield_str[0:-1] + ')\n'
            f.write(get_shapes_tuple_str)
            f.write(yield_str)
            f.write('\n')
            
            '''
            R
            '''
            f.write('@jit(nopython=True)\n')
            f.write('def R(x,y): # RMSE\n')
            f.write(' '*4+'return np.sqrt(1/len(x)*np.sum((x-y)**2))\n')
            f.write('\n')
            
            '''
            get_coef
            '''
            f.write('@jit(nopython=True)\n')
            f.write('def get_coef(sim_stack):\n')
            f.write(' '*4+'beta = np.linalg.solve(np.dot(np.transpose(sim_stack),sim_stack),np.dot(np.transpose(sim_stack),data_load))\n')
            f.write(' '*4+'beta[beta < 0] = 1E-8\n')
            f.write(' '*4+'coef = beta / np.sum(beta)\n')
            f.write(' '*4+'return coef\n')
            f.write('\n')
            
            '''
            match
            '''
            f.write('def match(w):\n')
            sim_array_str = ' '*4+'sim_array = np.array(['
            sim_str = ' '*4+'sim = np.sum(['
            return_str = ' '*4+'return ('
            for i in range(self.shape_num):
                sim_array_str += 'database[index[w[{0}]]]'.format(i) +','
                sim_str += 'sim_array[{0}] * coef_s[{0}]'.format(i) +','
                return_str += "'{{0:.4f}}'.format(coef_s[{0}])+'*'+ index[w[{0}]]".format(i) + '+"+"+'
            sim_array_str = sim_array_str[0:-1]+'])\n'
            sim_str = sim_str[0:-1]+'],axis=0)\n'
            return_str = return_str[0:-5]+',R(sim,data_load))\n'
            f.write(sim_array_str)
            f.write(' '*4+'sim_stack = np.column_stack(sim_array)\n')
            f.write(' '*4+'coef_s = get_coef(sim_stack)\n')
            f.write(sim_str)
            f.write(return_str)
            f.write('\n')
            
            '''
            main
            '''
            f.write('if __name__ == "__main__":\n')
            f.write(' '*4+'result_match = get_shapes_index()\n')
            f.write(' '*4+'n={0}\n'.format(self.shape_num))
            f.write(' '*4+'N = len(index)\n')
            f.write(' '*4+'total_times = int(np.prod([(N-i+1)/i for i in range(1,n+1)]))\n')
            f.write(' '*4+'top_R_result = []\n')
            #f.write(' '*4+'top_R_result_appened = top_R_result.append\n')
            f.write(' '*4+"print('Shape num = {0}'.format(n))\n")
            f.write(' '*4+'print("Num of loops required = {0}".format(total_times))\n')
            f.write(' '*4+'print()\n')
            f.write(' '*4+'count = 0\n')
            f.write(' '*4+'for result in result_match:\n')
            f.write(' '*8+'top_R = match(result)\n')
            f.write(' '*8+'top_R_result.append(top_R)\n')
            f.write(' '*8+'count += 1\n')
            f.write(' '*8+'if count >= 1E6:\n')
            f.write(' '*12+'top_R_result.sort(key=lambda x:x[1], reverse=False)\n')
            f.write(' '*12+'top_R_result = top_R_result[0:{0}]\n'.format(int(self.top_r)))
            f.write(' '*12+'count=0\n')
            f.write('\n')
            f.write(' '*4+'top_R_result.sort(key=lambda x:x[1], reverse=False)\n')
            f.write(' '*4+'top_R_result = top_R_result[0:{0}]\n'.format(int(self.top_r)))
            f.write(' '*4+'print("Done..")\n')
            f.write(' '*4+"with open('DataShapeMatch.pickle','wb') as f:\n")
            f.write(' '*8+'pickle.dump(top_R_result,f,pickle.HIGHEST_PROTOCOL)\n')

    def shape_multi_MultiPool(self,pool_num):
        with open('find_R_squared_shape.py','w') as f:
            f.write('import numpy as np\n')
            f.write('import pickle\n')
            f.write('from multiprocessing import Pool\n')
            f.write('from numba import jit\n')
            f.write('import time\n')
            f.write('\n')

            '''
            open pickle
            '''
            if self.method == 'histogram':
                f.write("with open('./Database/Database_LogAR_Hist.pickle','rb') as f:\n")
                f.write(' '*4+'database = pickle.load(f)\n')
            elif self.method == 'gaussian_kde':
                f.write("with open('./Database/Database_LogAR_KDE.pickle','rb') as f:\n")
                f.write(' '*4+'database = pickle.load(f)\n')
            f.write('index = np.array(list(database.keys()))\n')
            f.write('\n')
            f.write("with open('DataSrc_temp.pickle','rb') as f:\n")
            f.write(' '*4+'data_load = pickle.load(f)\n')
            f.write('\n')            
            
            '''
            get shapes tuple
            '''
            f.write('def get_shapes_index():\n')
            get_shapes_tuple_str = ' '*4 + 'for a{0} in range(len(index)-{1}+1):\n'.format(0,self.shape_num)
            for i in range(1,self.shape_num):
                get_shapes_tuple_str += ' '*4*(i+1)+'for a{0} in range(a{1}+1,len(index)-{2}+1):\n'.format(i,i-1,self.shape_num-i)
            yield_str = ' '*4*(self.shape_num+1)+'yield ('
            for i in range(0,self.shape_num):
                yield_str += 'a{0}'.format(i)+','
            yield_str = yield_str[0:-1] + ')\n'
            f.write(get_shapes_tuple_str)
            f.write(yield_str)
            f.write('\n')
            
            '''
            RMSE
            '''
            f.write('@jit(nopython=True)\n')
            f.write('def R(x,y): #RMSE\n')
            f.write(' '*4+'return np.sqrt(1/len(x)*np.sum((x-y)**2))\n')
            f.write('\n')
            
            '''
            get_coef
            '''
            f.write('@jit(nopython=True)\n')
            f.write('def get_coef(sim_stack):\n')
            f.write(' '*4+'beta = np.linalg.solve(np.dot(np.transpose(sim_stack),sim_stack),np.dot(np.transpose(sim_stack),data_load))\n')
            f.write(' '*4+'beta[beta < 0] = 1E-8\n')
            f.write(' '*4+'coef = beta / np.sum(beta)\n')
            f.write(' '*4+'return coef\n')
            f.write('\n')
            
            '''
            match
            '''
            f.write('def match(w):\n')
            sim_array_str = ' '*4+'sim_array = np.array(['
            sim_str = ' '*4+'sim = np.sum(['
            return_str = ' '*4+'return ('
            for i in range(self.shape_num):
                sim_array_str += 'database[index[w[{0}]]]'.format(i) +','
                sim_str += 'sim_array[{0}] * coef_s[{0}]'.format(i) +','
                return_str += "'{{0:.4f}}'.format(coef_s[{0}])+'*'+ index[w[{0}]]".format(i) + '+"+"+'
            sim_array_str = sim_array_str[0:-1]+'])\n'
            sim_str = sim_str[0:-1]+'],axis=0)\n'
            return_str = return_str[0:-5]+',R(sim,data_load))\n'
            f.write(sim_array_str)
            f.write(' '*4+'sim_stack = np.column_stack(sim_array)\n')
            f.write(' '*4+'coef_s = get_coef(sim_stack)\n')
            f.write(sim_str)
            f.write(return_str)
            f.write('\n')
            
            '''
            main
            '''
            f.write('if __name__ == "__main__":\n')
            f.write(' '*4+'result_match = get_shapes_index()\n')
            f.write(' '*4+'n={0}\n'.format(self.shape_num))
            f.write(' '*4+'N = len(index)\n')
            f.write(' '*4+'total_times = int(np.prod([(N-i+1)/i for i in range(1,n+1)]))\n')
            f.write(' '*4+'chunk_size = 1E6\n') # chunk size
            f.write(' '*4+'top_R_result = []\n')
            f.write(' '*4+'result_list = []\n')
            f.write(' '*4+'result_append = result_list.append\n')
            f.write(' '*4+"print('Shape num = {0}'.format(n))\n")
            f.write(' '*4+"print('Loop times required = {0}'.format(total_times))\n")
            f.write(' '*4+"print()\n")
            f.write(' '*4+'count = 0\n')
            f.write(' '*4+'loop_times = 0\n')
            f.write('\n')
            f.write(' '*4+'if total_times <= chunk_size:\n')
            f.write(' '*8+'with Pool(processes={0}) as pool:\n'.format(pool_num))          
            f.write(' '*12+'top_R = pool.map(match, result_match)\n')
            f.write(' '*12+'top_R_result.extend(top_R)\n')
            f.write(' '*4+'else:\n')
            f.write(' '*8+'for result in result_match:\n')
            f.write(' '*12+'result_append(result)\n')
            f.write(' '*12+'count += 1\n')
            f.write(' '*12+'if count >= chunk_size:\n')
            f.write(' '*16+'start_time = time.time()\n')
            f.write(' '*16+'with Pool(processes={0}) as pool:\n'.format(pool_num))          
            f.write(' '*20+'top_R = pool.map(match, result_list)\n')
            f.write(' '*16+'top_R_result.extend(top_R)\n')
            f.write(' '*16+'top_R_result.sort(key=lambda x:x[1], reverse=False)\n')
            f.write(' '*16+'top_R_result = top_R_result[0:{0}]\n'.format(int(self.top_r)))
            f.write(' '*16+'loop_times += 1\n')
            f.write(' '*16+"print('{0:.1e} loops took {1:.1f} minutes. {2:.2e} loops left'.format(chunk_size,(time.time() - start_time)/60,total_times-chunk_size*loop_times))\n")
            f.write(' '*16+'print()\n')
            f.write(' '*16+'result_list = []\n')
            f.write(' '*16+'result_append = result_list.append\n')
            f.write(' '*16+'count = 0\n')
            f.write('\n')
            f.write(' '*4+'top_R_result.sort(key=lambda x:x[1], reverse=False)\n')
            f.write(' '*4+'top_R_result = top_R_result[0:{0}]\n'.format(int(self.top_r)))
            f.write(' '*4+'print("Done..")\n')
            f.write(' '*4+"with open('DataShapeMatch.pickle','wb') as f:\n")
            f.write(' '*8+'pickle.dump(top_R_result,f,pickle.HIGHEST_PROTOCOL)\n')

    def main(self,pool_num=None,python_env='python',idp_loc=''):
        import os
        import datetime
        import time
        import pickle
        import numpy as np
        from scipy.stats import gaussian_kde
        # import numpy as np
        # from scipy.cluster.vq import kmeans2
        total_start_time = datetime.datetime.now()
        self.get_database()
        #print('The number of shapes that need to be calculated: %i' % self.shape_num)
        os.remove('DataShapeMatch.pickle') if os.path.exists('DataShapeMatch.pickle') else None
        string_var = ''
        if self.shape_num == 1:
            result_sorted = self.shape_one()
            shape_b,shape_c = [],[]
            for result in result_sorted:
                shape_b.append(float(eval(result[0].split(',')[1].split('=')[1])))
                shape_c.append(float(eval(result[0].split(',')[2].split('=')[1])))
            # shape_b_kmeans = kmeans2(shape_b,1,iter=10, thresh=1e-04, minit='random', missing='warn', check_finite=True)[0]
            # shape_c_kmeans = kmeans2(shape_c,1,iter=10, thresh=1e-04, minit='random', missing='warn', check_finite=True)[0]     
            # print('='*int(round((84-len('RESULTS'))/2))+'RESULTS'+'='*int((round(84-len('RESULTS'))/2)))
            string_var += ('R-squared range from %.2f to %.2f\n' % (result_sorted[0][1],result_sorted[-1][1])) 
            string_var += ('Total time spent: %s\n' % str(datetime.datetime.now()-total_start_time)[:-3])
        elif self.shape_num >= 2:
            with open('DataSrc_temp.pickle','wb') as f:
                if self.method == 'histogram':
                    hist_src = np.histogram(self.data_src,bins=30,range=(0,3),density=True)[0]
                    pickle.dump(hist_src,f,pickle.HIGHEST_PROTOCOL)
                elif self.method == 'gaussian_kde':
                    x_ = np.linspace(0,3,150)
                    kde_src = gaussian_kde(self.data_src)(x_)
                    pickle.dump(kde_src,f,pickle.HIGHEST_PROTOCOL)
            if pool_num == None:
                self.shape_multi()
                if idp_loc != '':
                    os.system(idp_loc+' find_R_squared_shape.py')
                else:
                    os.system(python_env+' find_R_squared_shape.py')
                    # exec(open('find_R_squared_shape.py').read(), globals())
            elif type(pool_num) == int:
                #print('Enable multiprocessing. Processing speed increases, but memory usage also increases. processes = %i' % pool_num)
                self.shape_multi_MultiPool(pool_num)
                if idp_loc != '':
                    os.system(idp_loc+' find_R_squared_shape.py')
                else:
                    os.system(python_env+' find_R_squared_shape.py')
    
            while not os.path.exists('DataShapeMatch.pickle'): time.sleep(0.5)
            with open('DataShapeMatch.pickle','rb') as f:
                result_sorted = pickle.load(f)       
            os.remove('find_R_squared_shape.py')
            os.remove('DataShapeMatch.pickle')
            os.remove('DataSrc_temp.pickle')
            string_var += ('RMSE-values range from %.4f to %.4f\n' % (result_sorted[0][1],result_sorted[-1][1])) 
            string_var += ('Total time spent: %s\n' % str(datetime.datetime.now()-total_start_time)[:-3])
    
        return string_var,result_sorted  