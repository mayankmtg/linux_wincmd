::   Primary Author: Mayank Mohindra <github.com/mayankmtg>
::
::   Description: activate existing virtual environment


@echo off
if [%1] == [] (GOTO completed)
%systemdrive%%homepath%\virtual_environments\%1\Scripts\activate.bat

:completed
echo "command line argument missing"