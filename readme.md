(s)ession (m)anager

setup:
- clone repo
- `export SM_PATH=<path/to/directory>` variable in `.bash_profile` (or equivalent)
	- make sure this points to the *directory* not a file
- `export SM_LOG=<path/to/directory>`, directory where `sm` will store log files
	- `1`: stdout of last run
	- `2`: stderr of last run
- copy `sm` entry script onto `PATH`
	- this will use `$SM_PATH` to find and run `sm.py`

to run:
- `source ~/.bash_profile` (or equivalent) or logout/login
- run the `sm` command

to autorun on login:
- always autorun on tty1:
```
[[ ! $DISPLAY && $XDG_VTNR -eq 1 ]] && sm
```
