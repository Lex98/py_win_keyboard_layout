"""
Interaction with keyboard layout on windows
"""


import win32gui
import win32api
import win32process

WM_INPUTLANGCHANGEREQUEST = 0x0050  # win32api const


def get_foreground_window_keyboard_layout():
    """
    Returns foreground window keyboard layout as integer

    Examples:
    68748313 - 0x04190419 - russian
    67699721 - 0x04090409 - english
    """
    window_handle = win32gui.GetForegroundWindow()
    thread_id = win32process.GetWindowThreadProcessId(window_handle)[0]
    layout_id = win32api.GetKeyboardLayout(thread_id)
    return layout_id


def change_foreground_window_keyboard_layout(layout_id=0):
    """
    Change foreground window keyboard layout

    Parameter

        layout_id=0 : integer

        Integer containing a locale id, eg 68748313 - 0x04190419 - 0x419 - russian

        By default change layout like Ctrl+Shift or Alt+Shift

    Return Value

    Returns True if layout is changed and win32api.SendMessage() output if not
    """
    if not isinstance(layout_id, int):
        raise TypeError('parameter must be integer')

    window_handle = win32gui.GetForegroundWindow()
    result = win32api.SendMessage(window_handle,
                                  WM_INPUTLANGCHANGEREQUEST,
                                  0,
                                  layout_id)
    if result == 0:
        return True
    else:
        return result



def get_keyboard_layout_list():
    """
    Returns a tuple of all locale ids currently loaded

    Example

    (68748313, 67699721)
    """
    return win32api.GetKeyboardLayoutList()


def load_keyboard_layout(string_layout_id, flags=0):
    """
    Loads a new locale id

    Parameters

        string_layout_id : string

        Hex string containing a locale id, eg "00000409"

        Flags=0 : int

        Combination of win32con.KLF_* constants

        Examples

        KLF_ACTIVATE|KLF_SETFORPROCESS|KLF_REORDER == 0x109 == 265

    Return Value

    Returns the integer locale id that was loaded

    Example

    load_keyboard_layout("00000409") == 67699721 for english
    """
    if not isinstance(string_layout_id, str) or not isinstance(flags, int):
        raise TypeError('first parameter must be string and second must be int')

    return win32api.LoadKeyboardLayout(string_layout_id, flags)


__all__ = ["get_foreground_window_keyboard_layout",
           "change_foreground_window_keyboard_layout",
           "get_keyboard_layout_list",
           "load_keyboard_layout"]
