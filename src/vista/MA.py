import wx
import random

class Example(wx.Frame):
    def __init__(self, parent, title):
        super(Example, self).__init__(parent, title = title,size = (300,200))            
        self.InitUI() 
        
    def InitUI(self):
        
        images = ['img/1.jpeg', 'img/2.jpeg', 'img/3.jpeg', 'img/4.jpeg', 
            'img/5.jpeg', 'img/6.jpeg', 'img/7.jpeg', 'img/8.jpeg']

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
        self.SetSizer
        self.Show(True)
   
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
    Example(None,"Test")
    ex.MainLoop()    

if __name__ == '__main__':
    main()