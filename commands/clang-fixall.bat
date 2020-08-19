::   Primary Author: Mayank Mohindra <github.com/mayankmtg>
::
::   Description: Apply clang-format fixes for all files changed from a branch


@echo off
if [%1] == [] (GOTO completed)
for /f %%i in ('git diff --name-only %1 ^| findstr ".cpp .h"') do clang-format -i %%i
GOTO :EOF
:completed
echo "command line argument missing"