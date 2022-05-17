'''
Created on 29-04-2022

@author: nicole
'''
import wx

def onButton(event):
    print ("Button pressed.")

app = wx.App()
frame = wx.Frame(None, -1, 'Rompecabezas Deslizante')
frame.SetDimensions(0,0,900,500)

panel = wx.Panel(frame, wx.ID_ANY)
button = wx.Button(panel, wx.ID_ANY, 'Comenzar', (600, 350))
button.Bind(wx.EVT_BUTTON, onButton)

button_2 = wx.Button(panel, wx.ID_ANY, 'Facil', (500, 300))
button_2.Bind(wx.EVT_BUTTON, onButton)

button_3 = wx.Button(panel, wx.ID_ANY, 'Medio', (600, 300))
button_3.Bind(wx.EVT_BUTTON, onButton)

button_4 = wx.Button(panel, wx.ID_ANY, 'Dificil', (700, 300))
button_4.Bind(wx.EVT_BUTTON, onButton)

frame.Show()
frame.Centre()
app.MainLoop()