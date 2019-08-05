::   Primary Author: Mayank Mohindra <github.com/mayankmtg>
::
::   Description: forloop counter to execture a command 'n' times

@echo off

echo %*
set /p "command=command: "
for /l %%i in (1,1,%1) do (%command%)
