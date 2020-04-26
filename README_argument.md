# agrv
- to import sys library to agrv (argumant varaiable) use below lines in your python script
 - `from sys import argv`   
 - `script, first, second, third, fourth = argv`
 - remember **script** is the name of your python script file
- when you run your python script in terminal use: `python3.7 "your file name".py "variable1" "variable2" ... `
- remember to keep the number of variables same as the number of variables defined in `script, first, second, third, fourth = argv` => here, we defined four variables
- you can replace any four variable (string/integer) in your python script argument
  - for example:
    `python3.7 syntax_argument.py apple orange peach grape`
- You **CANNOT** call two separate argv command within one script file
- You can directly write below lines in python3.7 through terminal
 - `python3.7`
 - `txt = open("sample.txt", "r")`
 - `print(txt.read())`
 - `print(txt.close)` or `txt.close()`

# remember below commands
- `close`: closes file
-  `read`: reads the file content
- `readline`: reads just one line of the text
- `truncate`: empties the file
- `write('stuff')`: writes "stuff" to the file
- `seek(0)`: moves read/write location to the file beginning
