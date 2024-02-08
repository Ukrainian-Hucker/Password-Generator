import wx
import string
import random
import pyperclip


class PasswordGenerator(wx.Frame):
    def __init__(self):
        super().__init__(None, title='Password Generator', size=(400, 300), style=wx.DEFAULT_FRAME_STYLE & ~(wx.RESIZE_BORDER | wx.MAXIMIZE_BOX))
        self.panel = wx.Panel(self)

        # Creating elements on the form
        self.lbl_length = wx.StaticText(self.panel, label='Password Length:', pos=(20, 20))
        self.txt_length = wx.SpinCtrl(self.panel, value='8', pos=(150, 20), min=6, max=20)

        self.lbl_chars = wx.StaticText(self.panel, label='Characters:', pos=(20, 60))
        self.chk_lowercase = wx.CheckBox(self.panel, label='a-z', pos=(150, 60))
        self.chk_uppercase = wx.CheckBox(self.panel, label='A-Z', pos=(200, 60))
        self.chk_digits = wx.CheckBox(self.panel, label='0-9', pos=(250, 60))
        self.chk_symbols = wx.CheckBox(self.panel, label='!@#$%^&*', pos=(300, 60))

        self.btn_generate = wx.Button(self.panel, label='Generate', pos=(20, 100))
        self.btn_copy = wx.Button(self.panel, label='Copy', pos=(150, 100))
        self.btn_clear = wx.Button(self.panel, label='Clear', pos=(250, 100))

        self.txt_password = wx.TextCtrl(self.panel, pos=(20, 150), size=(350, 30), style=wx.TE_READONLY)

        # Events
        self.btn_generate.Bind(wx.EVT_BUTTON, self.on_generate)
        self.btn_copy.Bind(wx.EVT_BUTTON, self.on_copy)
        self.btn_clear.Bind(wx.EVT_BUTTON, self.on_clear)

        # Centering the form on the screen
        self.Centre()

    def on_generate(self, event):
        # Checking if at least one parameter is selected
        if not self.chk_lowercase.GetValue() and not self.chk_uppercase.GetValue() and not self.chk_digits.GetValue() and not self.chk_symbols.GetValue():
            wx.MessageBox('You must select at least one parameter', 'Error', wx.OK | wx.ICON_ERROR)
            return

        # Creating a list of allowed characters
        chars = ''
        if self.chk_lowercase.GetValue():
            chars += string.ascii_lowercase
        if self.chk_uppercase.GetValue():
            chars += string.ascii_uppercase
        if self.chk_digits.GetValue():
            chars += string.digits
        if self.chk_symbols.GetValue():
            chars += string.punctuation

        # Generating a password
        length = self.txt_length.GetValue()
        password = ''.join(random.choice(chars) for _ in range(length))

        # Displaying the password
        self.txt_password.SetValue(password)

    def on_copy(self, event):
        # Copying the password to the clipboard
        password = self.txt_password.GetValue()
        pyperclip.copy(password)

    def on_clear(self, event):
        # Clearing the form fields
        self.chk_lowercase.SetValue(False)
        self.chk_uppercase.SetValue(False)
        self.chk_digits.SetValue(False)
        self.chk_symbols.SetValue(False)
        self.txt_password.SetValue('')


app = wx.App()
PasswordGenerator().Show()
app.MainLoop()