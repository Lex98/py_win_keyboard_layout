from unittest import TestCase

import py_win_keyboard_layout as pwkl


class TestKeyboardLayoutPackage(TestCase):

    def test_change_foreground_window_keyboard_layout_wrong_type(self):
        self.assertRaises(TypeError,
                          pwkl.change_foreground_window_keyboard_layout, '409')

    def test_load_keyboard_layout_wrong_type_first_arg(self):
        self.assertRaises(TypeError,
                          pwkl.load_keyboard_layout, 0x409, 0)

    def test_load_keyboard_layout_wrong_type_second_arg(self):
        self.assertRaises(TypeError,
                          pwkl.load_keyboard_layout, '00000409', '0')

    def test_load_keyboard_layout_wrong_type_both_arg(self):
        self.assertRaises(TypeError,
                          pwkl.load_keyboard_layout, 0x409, '0')
