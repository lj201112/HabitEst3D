@echo off
echo Welcome...
echo.
echo This program is used for reconstructing a 3D crystal shape from a set of 2D crystal sections by statistical method.
echo.
echo Close this window to terminate the program.
echo.
set path=%~dp0\Python\python-3.8.7.amd64;%path%
python --version
python main.py

rem %~dp0\Python\python-3.8.7.amd64\python.exe main.py