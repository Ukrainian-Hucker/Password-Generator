import wx
import string
import random
import pyperclip


class PasswordGenerator(wx.Frame):
    def __init__(self):
        super().__init__(None, title='Генератор паролів', size=(400, 300), style=wx.DEFAULT_FRAME_STYLE & ~(wx.RESIZE_BORDER | wx.MAXIMIZE_BOX))
        self.panel = wx.Panel(self)

        # Створення елементів на формі
        self.lbl_length = wx.StaticText(self.panel, label='Довжина паролю:', pos=(20, 20))
        self.txt_length = wx.SpinCtrl(self.panel, value='8', pos=(150, 20), min=6, max=20)

        self.lbl_chars = wx.StaticText(self.panel, label='Символи:', pos=(20, 60))
        self.chk_lowercase = wx.CheckBox(self.panel, label='a-z', pos=(150, 60))
        self.chk_uppercase = wx.CheckBox(self.panel, label='A-Z', pos=(200, 60))
        self.chk_digits = wx.CheckBox(self.panel, label='0-9', pos=(250, 60))
        self.chk_symbols = wx.CheckBox(self.panel, label='!@#$%^&*', pos=(300, 60))

        self.btn_generate = wx.Button(self.panel, label='Згенерувати', pos=(20, 100))
        self.btn_copy = wx.Button(self.panel, label='Копіювати', pos=(150, 100))
        self.btn_clear = wx.Button(self.panel, label='Очистити', pos=(250, 100))

        self.txt_password = wx.TextCtrl(self.panel, pos=(20, 150), size=(350, 30), style=wx.TE_READONLY)

        # Події
        self.btn_generate.Bind(wx.EVT_BUTTON, self.on_generate)
        self.btn_copy.Bind(wx.EVT_BUTTON, self.on_copy)
        self.btn_clear.Bind(wx.EVT_BUTTON, self.on_clear)

        # Центрування форми на екрані
        self.Centre()

    def on_generate(self, event):
        # Перевірка, чи хоча б один параметр вибраний
        if not self.chk_lowercase.GetValue() and not self.chk_uppercase.GetValue() and not self.chk_digits.GetValue() and not self.chk_symbols.GetValue():
            wx.MessageBox('Ви повинні вибрати хоча б один параметр', 'Помилка', wx.OK | wx.ICON_ERROR)
            return

        # Створення списку дозволених символів
        chars = ''
        if self.chk_lowercase.GetValue():
            chars += string.ascii_lowercase
        if self.chk_uppercase.GetValue():
            chars += string.ascii_uppercase
        if self.chk_digits.GetValue():
            chars += string.digits
        if self.chk_symbols.GetValue():
            chars += string.punctuation

        # Генерація паролю
        length = self.txt_length.GetValue()
        password = ''.join(random.choice(chars) for _ in range(length))

        # Виведення паролю
        self.txt_password.SetValue(password)

    def on_copy(self, event):
        # Копіювання паролю в буфер обміну
        password = self.txt_password.GetValue()
        pyperclip.copy(password)

    def on_clear(self, event):
        # Очищення полів форми
        self.chk_lowercase.SetValue(False)
        self.chk_uppercase.SetValue(False)
        self.chk_digits.SetValue(False)
        self.chk_symbols.SetValue(False)
        self.txt_password.SetValue('')


app = wx.App()
PasswordGenerator().Show()
app.MainLoop()
