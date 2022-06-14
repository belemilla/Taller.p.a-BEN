import wx
import random
import configparser
import numpy as np

'''
Esto es Docu
'''


class Example(wx.Dialog):
    
    def __init__(self, *args, **kw):
        super(Example, self).__init__(*args, **kw)
        
        self.InitUI()
        
    def InitUI(self):
        
        
        images = ['../img/1.jpg', '../img/2.jpg', '../img/3.jpg', '../img/4.jpg', 
                '../img/5.jpg', '../img/6.jpg', '../img/7.jpg', '../img/8.jpg']

        self.pos = [ [0, 1, 2], [3, 4, 5], [6, 7, 8] ]

        config = configparser.ConfigParser()
        config.read('../../../config.ini')
        fila = int(config['DEFAULT']['Fila'])
        columna = int(config['DEFAULT']['Columna'])
        self.sizer = wx.GridSizer(fila, columna, 0, 0)
        

        numbers = [0, 1, 2, 3, 4, 5, 6, 7]
        random.shuffle(numbers)

        for i in numbers:
            
                btn = wx.BitmapButton(self, i, wx.Bitmap(images[i]))
                btn.Bind(wx.EVT_BUTTON, self.OnPressButton, btn)
                self.sizer.Add(btn)


        self.SetSizerAndFit(self.sizer)
        self.SetTitle('Rompecabezas Deslizante')
        self.Centre()
        self.ShowModal()
        self.Destroy()

    def OnPressButton(self, e, np):
        
        '''
            Esto sirve para presionar un boton
        '''
        
        btn = e.GetEventObject()
        
        width = self.np.empty.GetSize().x
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


if __name__ == '__main__':
    main()  