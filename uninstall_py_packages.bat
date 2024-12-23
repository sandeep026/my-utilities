REM a batch script to uninstall python packages from a given environment
@echo off
pip freeze > installed_packages.txt & REM collect names of all packages installed in the environment to a text file
for /F "delims==" %%i in (installed_packages.txt) do (  & REM iteratively delete each package 
    echo Uninstalling %%i...
    pip uninstall -y %%i
)
del installed_packages.txt & REM delete the text file created
