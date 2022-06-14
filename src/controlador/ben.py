'''
Created on 29-04-2022

@author: Belen
'''
import wx

listaInputsTxtCtrl=[]


class InterfazGrafica(wx.Frame):

    def _init_(self,parent,id):
        wx.Frame._init_(self,parent,id,"ventana")
        panel=wx.Panel(self)
        boton1=wx.Button(panel,label="Ingresar",pos=(130,30))
        boton2=wx.Button(panel,label="Buscar",pos=(130,60))
        boton3=wx.Button(panel,label="Eliminar",pos=(130,90))
        boton4=wx.Button(panel,label="Actualizar",pos=(130,120))
        
        self.Bind(wx.EVT_BUTTON,self.ingresarUsuario,boton1)
        self.Bind(wx.EVT_BUTTON,self.buscarUsuario,boton2)
        self.Bind(wx.EVT_BUTTON,self.eliminarUsuario,boton3)
        self.Bind(wx.EVT_BUTTON,self.actualizarUsuario,boton4)
        
        self.dlg1=wx.TextCtrl(panel,pos=(10,30))
        self.dlg1_1 = wx.TextCtrl(panel, pos=(10, 150))
        self.dlg2=wx.TextCtrl(panel,pos=(10,60))
        self.dlg3=wx.TextCtrl(panel,pos=(10,90))
        self.dlg4=wx.TextCtrl(panel,pos=(10,120))

        self.lista = wx.ListBox(panel,choices=listaInputsTxtCtrl,pos=(240,30))
        
        self.Show()

    def ingresarUsuario(self,event):
        dniUs=str(self.dlg1.GetValue())+"-"+str(self.dlg1_1.GetValue())
        if dniUs != (""):
            listaInputsTxtCtrl.append(dniUs)
            print(listaInputsTxtCtrl)
            print("Usuario Ingresado")
        else:
            print("Completar casilla requerida")
        self.dlg1.SetValue('')

    def buscarUsuario(self,event):
        dniUs2 = self.dlg2.GetValue()
        for i in range(0,len(listaInputsTxtCtrl),1):
            if dniUs2 == listaInputsTxtCtrl[i]:
                print("Se ha encontrado el usuario en la posicion "+str(i))
            else:
                print("Usuario no encontrado")
        self.dlg2.SetValue('')
    def eliminarUsuario(self,event):
        dniUs3 = self.dlg3.GetValue()
        for i in range(0, len(listaInputsTxtCtrl),1):
            if dniUs3 == listaInputsTxtCtrl[i]:
                listaInputsTxtCtrl.pop(i)
        print("Usuario eliminado")
        self.dlg3.SetValue('')
        print(listaInputsTxtCtrl)
    def actualizarUsuario(self,event):
        dniUs2 = self.dlg2.GetValue()
        dniUs4 = self.dlg4.GetValue()
        for i in range(0, len(listaInputsTxtCtrl), 1):
            if dniUs2 == listaInputsTxtCtrl[i]:
                listaInputsTxtCtrl[i]= dniUs4
                print("Usuario Actualizado")
            else:
                print("Usuario no encontrado")
        self.dlg4.SetValue('')
        self.dlg2.SetValue('')
        print(listaInputsTxtCtrl)

app=wx.App()
ventana=InterfazGrafica(None,-1)
app.MainLoop()