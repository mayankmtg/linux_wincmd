::   Primary Author: Mayank Mohindra <github.com/mayankmtg>
::
::   Description: list the passed directory


@echo off
echo.
echo DIRECTORIES
if [%1]==[] (set direc=*) else (set direc=%1\*)
for /d %%i in (%direc%) do echo %%i
echo.
echo FILES
for %%i in (%direc%) do echo %%i
