# wincmd

Package contains very helpful cmd command examples

Creating a new command:

```
python create.py -n <command_name> -d <command-description> [-e] "example string for command" [-t] <headr-file.txt>
```

## Table of contents
[Touch](#touch)<br>
[Commitpush](#commitpush)<br>
[Ls](#ls)<br>
[Cvenv](#cvenv)<br>
[Avenv](#avenv)<br>
[Lvenv](#lvenv)<br>
[Forloop](#forloop)<br>
[Home](#home)<br>


## Commands
### touch
create new blank files with filename
```
touch <filename>
```


### commitpush
committing and pushing changes to the present branch from a user account
```
commitpush <username>[mayankmtg, mayank.mohindra] "message"
```


### ls
list the passed directory
```
ls <directory_name>
```


### cvenv
create virtual environment
```
cvenv <environment_name>
```


### avenv
activate existing virtual environment
```
avenv <venv-folder>
```


### lvenv
list existing venvs
```
lvenv
```


### forloop
forloop counter to execture a command 'n' times
```
forloop n
```
There will be a prompt for the command
'%i' can be used to access the counter for the loop


### home
command to redirect me to a custom home directory
```
home
```


