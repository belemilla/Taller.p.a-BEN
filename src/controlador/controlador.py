'''
:wx.Dialog:
'''
Created on 26-04-2022

@author: Belen

import wx 
import random 
import configparser

class Example(wx.Dialog):
    
    def _init_(self, *args, **kw):
        super(Example, self)._init_(*args, **kw)
        
        self.InitUI()
        
    def InitUI(self):
        
        images = ['../controlador/1.jpg', '../controlador/2.jpg', '../controlador/3.jpg', '../controlador/4.jpg', 
                '../controlador/5.jpg', '../controlador/6.jpg', '../controlador/7.jpg', '../controlador/8.jpg']

        self.pos = [ [0, 1, 2], [3, 4, 5], [6, 7, 8] ]

        self.sizer = wx.GridSizer(3, 3, 0, 0)

        numbers = [0, 1, 2, 3, 4, 5, 6, 7]
        random.shuffle(numbers)

        for i in numbers:
            
                btn = wx.BitmapButton(self, i, wx.Bitmap(images[i]))
                btn.Bind(wx.EVT_BUTTON, self.OnPressButton, btn)
                self.sizer.Add(btn)


        self.SetSizerAndFit(self.sizer)
        self.SetTitle('Puzzle')
        self.Centre()
        self.ShowModal()
        self.Destroy()

    def OnPressButton(self, e):
        
        btn = e.GetEventObject()
        
        width = self.empty.GetSize().x
        height = self.empty.GetSize().y

        btnX = btn.GetPosition().x
        btnY = btn.GetPosition().y
        emptyX = self.empty.GetPosition().x
        emptyY = self.empty.GetPosition().y
    
        
        if (((btnX == emptyX) and (emptyY - btnY) == height)
          or ((btnX == emptyX) and (emptyY - btnY) == -height)
          or ((btnY == emptyY) and (emptyX - btnX) == width)
          or ((btnY == emptyY) and (emptyX - btnX) == -width)):
                 
            self.ExchangeImages(btn)

            
    def ExchangeImages(self, btn):
        
        bmp1 = self.empty.GetBitmapLabel()
        bmp2 = btn.GetBitmapLabel()
        
        self.empty.SetBitmapLabel(bmp2)
        btn.SetBitmapLabel(bmp1)
        
        self.empty = btn        


def main():
    
    ex = wx.App()
    Example(None)
    ex.MainLoop()    


if __name__ == '_main_':
    main()