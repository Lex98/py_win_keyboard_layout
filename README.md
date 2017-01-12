py_win_keyboard_layout
========

Interaction with keyboard layout on windows
Tested only on windows 7 x64 with pywin32 build 220

## Dependency

[pywin32](https://sourceforge.net/projects/pywin32/?source=directory)

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

Returns foreground window keyboard layout as integer

Examples:

    py_win_keyboard_layout.get_foreground_window_keyboard_layout() -> 68748313 - 0x04190419 - russian
    py_win_keyboard_layout.get_foreground_window_keyboard_layout() -> 67699721 - 0x04090409 - english


<a name="py_win_keyboard_layout.change_foreground_window_keyboard_layout"/>
## py_win_keyboard_layout.**change\_foreground\_window\_keyboard\_layout**
Change foreground window keyboard layout

Parameter:

- layout_id=0 : integer
Integer containing a locale id, eg 68748313 - 0x04190419 - 0x419 - russian
Default change layout like Ctrl+Shift or Alt+Shift

Return Value:

- Returns True if layout is changed

<a name="py_win_keyboard_layout.get_keyboard_layout_list"/>
## py_win_keyboard_layout.**get\_keyboard\_layout\_list**

Returns a tuple of all locale ids currently loaded

Example:

    py_win_keyboard_layout.get_keyboard_layout_list() -> (68748313, 67699721)



<a name="py_win_keyboard_layout.load_keyboard_layout"/>
### py_win_keyboard_layout.**load\_keyboard\_layout**

Loads a new locale id

Parameters:

- string_layout_id : string
Hex string containing a locale id, eg "00000409"

- Flags=0 : int
Combination of win32con.KLF_* constants.
See more information in [msdn](https://msdn.microsoft.com/ru-ru/library/windows/desktop/ms646305(v=vs.85).aspx)

Example:

    KLF_ACTIVATE|KLF_SETFORPROCESS|KLF_REORDER == 0x109 == 265

Return Value:

- Returns the integer locale id that was loaded

Example:

    py_win_keyboard_layout.load_keyboard_layout("00000409") -> 67699721 for english