"""

"""


import win32gui
import win32api
import win32process

WM_INPUTLANGCHANGEREQUEST = 0x0050


def get_foreground_window_keyboard_layout():
    window_handle = win32gui.GetForegroundWindow()
    thread_id = win32process.GetWindowThreadProcessId(window_handle)[0]
    layout_id = win32api.GetKeyboardLayout(thread_id)
    return layout_id


def change_foreground_window_keyboard_layout(layout_id=0):
    window_handle = win32gui.GetForegroundWindow()
    return not win32api.SendMessage(window_handle,
                                    WM_INPUTLANGCHANGEREQUEST,
                                    0,
                                    layout_id)


def get_keyboard_layout_list():
    return win32api.GetKeyboardLayoutList()


def load_keyboard_layout(layout_id, flags=0):
    return win32api.LoadKeyboardLayout(layout_id, flags)
