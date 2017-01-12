py_win_keyboard_layout
========

Interaction with keyboard layout on windows


## Usage

Install the [PyPI package](https://pypi.python.org/pypi/py_win_keyboard_layout/):

    $ sudo pip install py_win_keyboard_layout

or clone the repository (no installation required, source files are sufficient):

    $ git clone https://github.com/Lex98/py_win_keyboard_layout

Then check the [API docs](https://github.com/Lex98/py_win_keyboard_layout#api) to see what features are available.

## Example


```
import py_win_keyboard_layout

# change foreground window keyboard layout to russian
py_win_keyboard_layout.change_foreground_window_keyboard_layout(0x04190419)
```


# API
#### Table of Contents

- [py\_win\_keyboard\_layout.**get\_foreground\_window\_keyboard\_layout**](#py_win_keyboard_layout.get_foreground_window_keyboard_layout)
- [py\_win\_keyboard\_layout.**change_foreground_window_keyboard_layout**](#py_win_keyboard_layout.change_foreground_window_keyboard_layout)
- [py\_win\_keyboard\_layout.**get_keyboard_layout_list**](#py_win_keyboard_layout.get_keyboard_layout_list)
- [py\_win\_keyboard\_layout.**load_keyboard_layout**](#py_win_keyboard_layout.load_keyboard_layout)


<a name="py_win_keyboard_layout.get_foreground_window_keyboard_layout"/>
## py_win_keyboard_layout.**get\_foreground\_window\_keyboard\_layout**


<a name="py_win_keyboard_layout.change_foreground_window_keyboard_layout"/>
## py_win_keyboard_layout.**change\_foreground\_window\_keyboard\_layout**


<a name="py_win_keyboard_layout.get_keyboard_layout_list"/>
## py_win_keyboard_layout.**get\_keyboard\_layout\_list**




<a name="py_win_keyboard_layout.load_keyboard_layout"/>
### py_win_keyboard_layout.**load\_keyboard\_layout**