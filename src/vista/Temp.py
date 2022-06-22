'''
Created on 20-06-2022

@author: Belen
'''
import datetime
import wx

class TimerFrame(wx.Frame):
    
    def __init__(self):
        #CONSTRUCTOR
        wx.Frame.__init__(self, None, title='Temporizador')
        panel = wx.Panel(self)
        #CONTADOR INICIALIZADO EN 0
        self.counter = 0 
        #DEFINICION DE ESTILO DE LA LETRA Y TEXTO ABAJO DEL LABEL
        font = wx.Font(24, wx.FONTFAMILY_ROMAN,
                       wx.FONTSTYLE_NORMAL,
                       wx.FONTWEIGHT_BOLD)

        #SE A�ADE EL TIMPO POR DEFECTO QUE ES 0, ES SOLO VISUAL
        self.lbl = wx.StaticText(panel, label='0:00:00')
        self.lbl.SetFont(font)

        #BOTON PARA INICIAR SE SETEA "START" QUE COMIENZA EL TIMER
        btnI = wx.Button(panel, label='INICIAR')
        btnI.Bind(wx.EVT_BUTTON, self.start)

        #BOTON DE PAUSA LLAMA A LA FUNCION PAUSE
        btnP = wx.Button(panel, label='PAUSAR')
        btnP.Bind(wx.EVT_BUTTON, self.pause)
        
        #BOTON DE PAUSA LLAMA A LA FUNCION UPDATE
        self.timer = wx.Timer(self)
        self.Bind(wx.EVT_TIMER, self.update, self.timer)

        #SE CONFIGURAN LAS POCICISONES DE LOS BOTONES Y TIMER
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.lbl, 0, wx.ALL|wx.CENTER, 5)
        sizer.Add(btnI, 0, wx.ALL|wx.CENTER, 5)
        sizer.Add(btnP, 0, wx.ALL|wx.CENTER, 5)
        panel.SetSizer(sizer)

        self.Show()

    #INICIA Y DEFINE EL LOOP POR 1500MILISEG APROX 1 SEG
    def start(self, event):
        self.timer.Start(1500)
        
    #PAUSA EL LOOP
    def pause(self, event):
        self.timer.Stop()
        
    #CUANDO CORRE EL LOOP ACTUALIZA +1
    def update(self, event):
        self.counter += 1
        self.lbl.SetLabel(str(datetime.timedelta(seconds=self.counter)))
        

app = wx.App(False)
frame = TimerFrame()
app.MainLoop()