# HabitEst3D
Estimating true crystal habit from two-dimensional cut sections

Clone all files in this [HabitEst3D](https://github.com/lj201112/HabitEst3D) repository, and run main.py to start the program. The user should have Python installed or use [portable Python](https://github.com/codrsquad/portable-python). 

The program is written in Python with Numpy, Scipy, Pandas, Matplotlib, and Numba. It is in Python3.8 but only uses common functions in the libs mentioned above and maybe works with lower Python versions. The program is only tested on Win7 but should also work on other systems which support Python and its libs. 

The file "run.bat" can be used for executing portable Python. `path=%~dp0\Python\python-3.8.7.amd64` means the Python script .exe locates at `./Python\python-3.8.7.amd64`, and the current dir is where the .bat is. The user can directly run `main.py` if Python is in the system environment variables.

## About "config.ini"

This configuration file allows the user to customize how to execute the python file. The program will generate and execute the temporary Python file named `find_R_squared_shape.py` when estimating multiple crystal habits. Then the `config.ini` file is for configuring how to run the temporary file. The content of the configuration file:

```bat
[config]  
python_env = python  
python_loc =  
```
For example, when python_env is set to `python3`, the command `python3 find_R_squared_shape.py` will be executed, and the default value is `python` if left blank. `python_loc` is the location of the python .exe. If your file path is `C:\Python\python.exe`, then `python_loc = C:\Python\python.exe` , the command `C:\Python\python.exe find_R_squared_shape.py` will be executed. The priority of `python_loc` is higher than `python_env`, and `python_env` only works when `python_loc` is empty.

If you have any questions, please let me know. :)

