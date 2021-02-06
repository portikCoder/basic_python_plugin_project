# basic_python_plugin_project

#

## Useful local tests to run 
**For everything that is saved/configured is used PyCharm as the Idea!** 

### PYLINT: Setup a local macro to be used faster
Edit -> Macros -> Start macro recording -> ALT+F12 -> if you want you can press several times the *backspace* ent hit
 enter to clear up the text if was something there -> type the following into the terminal: <code>
 pylint "--msg-template='{abspath}:{line:5d},{column:2d}: {msg} ({symbol})'" --output-format=colorized src tests </code>
-> press enter -> stop recording by clicking on the red square (whereever is the icon showing the macro recording)
Then hit *CTRL+ALT+S*, search for **keymap**, and there you go, edit the shortcut for running easily this command.

### PYLINT: Setup *External tool*
Hit *CTRL+ALT+S*, search for **external tool**, make one new by hitting the add button:
 * program: python
 * arguments: -m pylint "--msg-template='{abspath}:{line:5d},{column:2d}: {msg} ({symbol})'" --output-format=colorized "src"
 * working directory: $ProjectFileDir$
 * check on the console show
 * output filter: $FILE_PATH$:\s*$LINE$\,\s*$COLUMN$: