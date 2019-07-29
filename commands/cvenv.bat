::   Primary Author: Mayank Mohindra <github.com/mayankmtg>
::
::   Description: create virtual environment


@echo off
if [%1] == [] (GOTO completed)
python -m venv %systemdrive%%homepath%\virtual_environments\%1
%systemdrive%%homepath%\virtual_environments\%1\Scripts\activate.bat

:completed
echo "command line argument missing"