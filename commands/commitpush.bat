::   Primary Author: Mayank Mohindra <github.com/mayankmtg>
::
::   Description: committing and pushing changes to the present branch from a user account


@echo off
git add .
if %1==mayankmtg (git -c user.name="Mayank Mohindra" -c user.email="mayank15056@iiitd.ac.in" commit -m %2) else (git commit -m %2)
git push
