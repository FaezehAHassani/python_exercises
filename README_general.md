

# Some terminal tips, and how to link your local repo to your GitHub repo:
- in terminal type mkdir to make new folder as your local repo (e.g. phyton_project)
- in Atom make your README text file
- ls will list all available files in the directory
- in your local repo directory use: git init
- in your GitHub account make a new repo with "phyton_project" name
- in terminal type: git remote add origin <the url of your new GitHub repo>
- in terminal `git add` and then `git commit -m "your message"`your new README file, and type `git push --set-upstream origin master`

# Start phyton 3.7
- installed 3.7.6 version and in terminal use: `phyton3.7`
- `python+tab` will show you all the phyton versions available
- in terminal use: `quit()` to quit python
- in terminal use: `python3.7 "atom file name".py` or first type `python3.7` then you can type all your commands directly there.

# Escape sequences
| Escape (in the preview one \ is removed that is correct) |Activity                                  |
|:---------------------------------------------------------|:-----------------------------------------|
|\\\                                                       |Backslash                                 |
|\\'                                                       |single-quote                              |
|\\"                                                       |double-quote                              |
|\\a                                                       |ASCII bell (a bell sound)                 |
|\\b                                                       |ASCII backspace                           |
|\\f                                                       |ASCII formfeed                            |
|\\n                                                       |ASCII linefeed                            |
|\\N{name}                                                 |character names `name` in Unicode database|
|\\r                                                       |return                                    |
|\\t                                                       |horizontal tab                            |
|\\uxxxx                                                   |character with 16-bit hex value xxxx      |
|\\Uxxxxxxxx                                               |character with 32-bit hex value xxxxxxxx  |
|\\v                                                       |ASCII vertical tab                        |
|\\000                                                     |character with octal value 000            |
|\\xhh                                                     |character with hex value hh               |

# pydoc
- `python3.7 -m pydoc` provides a help documentation
- `python3.7 -m file/os/sys` are a few documentation
- `python3.7 -m pydoc open` gives you information on open() command
