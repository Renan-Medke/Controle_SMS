import get_parameters
from tkinter import *
from time import *
import math
#import smtplib
        
class Tela:

    def __init__(self,root):
        self.font = ("verdana",'16','bold')
        self.font2 = ("verdana",'14','bold')
       
        self.coordenadas = Frame(root,bd = 4, relief = "raise")
        self.editar = Frame(root,bd = 4, relief = "raise")
        

    #CRIA O FRAME PARA MOSTRAR UM RELÓGIO
        self.atualizar = Frame(root,bd = 4, relief = "raise")
        self.relogio = Frame(self.atualizar,bd = 4, relief = "raise")

        self.clock = Frame(self.relogio,bd = 4, relief = "raise")
        self.data = Label(self.clock,text = "DATA",font=self.font2)
        self.data.pack(side=TOP)

        self.relogio_layout = Label(self.clock,font=self.font2)
        self.relogio_layout.pack()
        self.clock.pack()
        
        self.nome_relogio = Label(self.clock,text = "Horário de Brasília",font=self.font2)
        self.nome_relogio.pack(side=TOP)
 
        self.Nascer = Frame(self.relogio,bd = 4, relief = "raise")
        self.nascer_do_sol = Label(self.Nascer,text = "Nascer do Sol:",font=self.font2)
        self.nascer_do_sol.pack()
        self.hora_nascer_do_sol = Label(self.Nascer,text = "teste:",font=self.font2)
        self.hora_nascer_do_sol.pack()
        self.Nascer.pack()

        self.Por = Frame(self.relogio,bd = 4, relief = "raise")       
        self.por_do_sol = Label(self.Por,text = "Pôr do Sol:",font=self.font2)
        self.por_do_sol.pack()
        self.hora_por_do_sol = Label(self.Por,text='teste',font=self.font2)
        self.hora_por_do_sol.pack()
        self.Por.pack()
        
        self.foto = Frame(self.atualizar)
        self.photo = PhotoImage(file = "dia_convertido.png")
        self.label_foto = Label(self.foto, image = self.photo)
        self.label_foto.pack()
        

    # EMPACOTAR FRAMES
        self.coordenadas.pack()
        self.editar.pack(side=TOP)
        self.Nascer.pack()
        self.foto.pack(side= RIGHT)
        self.relogio.pack(side=LEFT)
        self.atualizar.pack()

    #Cria button_automatico
        self.automatic = True
        print(self.automatic)
        self.button_automatico = Button(self.coordenadas,bd = 4,relief = "raise",text = "Funcionamento Automático",command= self.TrocaModo,font=self.font2)
        self.button_automatico.pack(side=LEFT)

    #Cria botão OK
        self.button_ok = Button(self.editar,bd = 4,relief = "raise", text = "OK",font= self.font2,command= self.Mudar_valores)
                
    #Cria botão EDIT
        self.edit = False
        self.button_editar = Button(self.editar,bd = 4,relief = "raise", text = "Editar Coordenadas",font= self.font2,command= self.Editar_coordenadas)
        self.button_editar.pack(side = LEFT)

    #Cria entradas das coordenadas
        self.t11 = Label(self.editar,text="Latitude ",font= self.font2)
        self.e11 = Entry(self.editar,font= self.font2)
        self.t22 = Label(self.editar,text="Longitude ",font= self.font2)
        self.e22 = Entry(self.editar,font= self.font2)


    #CRIA NOTIFICAÇÃO DE ENTRADA INVÁLIDA
        self.entrada_invalida = Label(self.editar, text = "ENTRADA INVÁLIDA",font= self.font2)

    #CRIA UM LOOP INFINITO PARA VERIFICAÇÃO DE MUDANÇAS
        self.dia_anterior = int(strftime('%j'))
        self.calculo_solar()
        self.hora_now = round(float(float(strftime('%M'))/60)+float(strftime('%H')),2) 

       
        if self.por_sol_h > self.hora_now:
            if self.hora_now > self.nascer_sol_h:
                self.dia = True
        else:
             self.dia = False

    # Cria botões de abrir e fechar para o modo automático
        self.construir_ccd1()

        if self.automatic == True:
            #self.informacoes()
            self.Apagar_entradas()
            self.destruir_ccd1()
            self.automatic = True
                        
        else:
            
            self.informacoes()
            self.Apagar_informacoes()
            self.automatic = False
        
        self.tac()
        
    def tac(self):
        self.teste()           
        root.after(1000,self.tac)
        
    #trabalhadno aqui
    def teste(self):
       
        if self.dia_anterior != int(strftime('%j')):
            self.calculo_solar()
            print("mudou o dia, mais uma oportunidade pra fazer cagada!")
            self.calculo_solar()
        self.data['text'] = strftime('%d/%m/%Y')
        self.relogio_layout['text'] = strftime('%H:%M:%S')
        self.dia_anterior = int(strftime('%j'))
        self.hora_now = round(float(float(strftime('%M'))/60)+float(strftime('%H')),5) 

        if self.por_sol_h > self.hora_now:
            self.teste1 = True
        else:
            self.teste1 = False

        if self.hora_now > self.nascer_sol_h:
            self.teste2 = True
        else:
            self.teste2=False

        if self.teste1 == True & self.teste2 == True:
            self.dia = True
            print(self.dia)
            self.foto_dia()
        else:
            self.dia = False
            print(self.dia)
            self.foto_noite()
            
        if self.automatic == True:
            self.estado_automatico()
        else:
            self.estado_manual()
    #trabalhadno até aqui
        
    def estado_automatico(self):
        print("chama função automatica")
        #print(get_parameters.carregar_estado())
        return()

    def estado_manual(self):
        print("chama função manual")
        #print(get_parameters.carregar_estado())
        return()

    def construir_ccd1(self):
        #Cria botão abrir ccd1 ccd2 e photômetro
        self.ccd1 = Label(self.foto, text = "CCD 1",font= self.font2,width = 10,height=2)
        self.ccd1.pack()
        self.ccd1.place(x = 10, y = 10)
        self.ccd1 = Label(self.foto, text = "Aberto",font= self.font2,width = 7,height=2)
        self.ccd1.pack()
        self.ccd1.place(x = 150, y = 10)
        self.button_abrir = Button(self.foto, text = "ABRIR",font= self.font2,width = 6,height=1,bd = 4,relief = "raise",) 
        self.button_abrir.pack()
        self.button_abrir.place(x = 250, y = 13)

        self.ccd2 = Label(self.foto, text = "CCD 2",font= self.font2,width = 10,height=2)
        self.ccd2.pack()
        self.ccd2.place(x = 10, y = 80)
        self.ccd2 = Label(self.foto, text = "Aberto",font= self.font2,width = 7,height=2)
        self.ccd2.pack()
        self.ccd2.place(x = 150, y = 80)
        self.button_abrir2 = Button(self.foto, text = "ABRIR",font= self.font2,width = 6,height=1,bd = 4,relief = "raise",) 
        self.button_abrir2.pack()
        self.button_abrir2.place(x = 250, y = 83)

        self.photometer = Label(self.foto, text = "FOTÔMETRO",font= self.font2,width = 10,height=2)
        self.photometer.pack()
        self.photometer.place(x = 10, y = 150)
        self.photometer = Label(self.foto, text = "Aberto",font= self.font2,width = 7,height=2)
        self.photometer.pack()
        self.photometer.place(x = 150, y = 150)
        self.button_abrir3 = Button(self.foto, text = "ABRIR",font= self.font2,width = 6,height=1,bd = 4,relief = "raise",) 
        self.button_abrir3.pack()
        self.button_abrir3.place(x = 250, y = 153)
        return()

     
    def destruir_ccd1(self):
        self.button_abrir.destroy()
        self.button_abrir2.destroy()
        self.button_abrir3.destroy()
   
    
    def calculo_solar(self):
        #cálculo de duração do dia
        self.ltt = float(get_parameters.carregar_latitude())
        self.n = int(strftime('%j'))
        self.fi = 23.45*math.sin(math.radians((360/365)*(284+self.n)))
        self.Td = (2/15)*math.degrees(math.acos( -math.tan(math.radians(self.ltt))*math.tan(math.radians(self.fi))))
        self.correcao = (((abs(float(get_parameters.carregar_longitude())) - int(abs(float(get_parameters.carregar_longitude()))/15)*15) * 60)/15)/60
        #calculo do pôr do sol
        self.por_sol_h = 12 + (self.Td/2) + self.correcao
        self.por_sol_min = (self.por_sol_h - int(self.por_sol_h))*60
        self.por_sol_seg = (self.por_sol_min - int(self.por_sol_min))*60
        self.hora_por_do_sol['text'] = str(int(self.por_sol_h)) + str(":") + str(round(int(self.por_sol_min),2))+ str(":") + str(round(int(self.por_sol_seg),2))#atualiza hora por dol sol
        #calculo nasce do sol
        self.nascer_sol_h = (12 - (self.Td/2)) + self.correcao
        self.nascer_sol_min = (self.nascer_sol_h - int(self.nascer_sol_h))*60
        self.nascer_sol_seg = (self.nascer_sol_min - int(self.nascer_sol_min))*60 
        self.hora_nascer_do_sol['text'] = str(int(self.nascer_sol_h)) + str(":") + str(int(self.nascer_sol_min)) + str(":") + str(int(self.nascer_sol_seg))
        return()
                       
    def foto_dia(self):
        self.photo = PhotoImage(file = "dia_convertido.png")
        self.label_foto['image'] = self.photo
        self.label_foto.pack()
        return()

    def foto_noite(self):
        self.photo = PhotoImage(file = "noite_convertido.png")
        self.label_foto['image'] = self.photo
        self.label_foto.pack()
        return()
        
    def informacoes(self):
        self.lat = float(get_parameters.carregar_latitude())
        self.long= float(get_parameters.carregar_longitude())
        self.latitude1 = Frame(self.coordenadas)
        self.t1 = Label(self.latitude1,text="    Latitude :",font= self.font2)
        self.t1.pack(side=LEFT)
        self.lat = Label(self.latitude1,text=self.lat,font= self.font2)
        self.lat.pack(side=RIGHT)
        self.latitude1.pack(side=RIGHT)

        self.longitude1 = Frame(self.coordenadas)
        self.t2 = Label(self.longitude1,text="   Longitude :",font= self.font2)
        self.t2.pack(side=LEFT)
        self.long = Label(self.longitude1,text=[self.long],font= self.font2)
        self.long.pack(side=RIGHT)
        self.longitude1.pack(side=RIGHT)
        self.label_foto.pack()

    def Apagar_informacoes(self):
        self.latitude1.pack_forget()
        self.longitude1.pack_forget()
        self.entrada_invalida.pack_forget()
   
        
    def isnumber(self,value):
        self.value = value
        try:
            float(self.value)
        except ValueError:
            return False
        return True
        
        
    def Mudar_valores(self):
        if self.automatic == False:
            if self.isnumber(self.e11.get())== True & self.isnumber(self.e22.get())== True:
                get_parameters.salvar_coordenadas(str(float(self.e11.get())),str(float(self.e22.get())))
                self.Editar_coordenadas()
                self.entrada_invalida.pack_forget()
            else:
                self.entrada_invalida.pack()
            
    def Entrada_coordenadas(self):
        self.t22.pack(side = LEFT)
        self.e22.pack(side= LEFT)
        self.t11.pack(side = LEFT)
        self.e11.pack(side= LEFT)
        self.button_ok.pack(side = RIGHT)
        return()

    def Apagar_entradas(self):
        self.e11.pack_forget()
        self.t11.pack_forget()
        self.e22.pack_forget()
        self.t22.pack_forget()
        self.button_ok.pack_forget()
        self.entrada_invalida.pack_forget()
        return()
        
    def Editar_coordenadas(self):
         if self.automatic == False:
            if self.edit:
                self.Entrada_coordenadas() 
            else:
                self.Apagar_entradas() 

         self.edit = not self.edit
     
    def TrocaModo(self):
        if self.automatic == True:
            self.Apagar_entradas()
            self.destruir_ccd1()
            self.informacoes()
            self.automatic = False
            get_parameters.salvar_estado(str(self.automatic))
                        
        else:
            self.construir_ccd1()
            self.Apagar_informacoes()
            self.automatic = True
            get_parameters.salvar_estado(str(self.automatic))
            
root = Tk()
root.geometry("1280x720+0+0")        
root.configure(background='#04E669')
root.title("Controle do Observatório Espacial do Sul")
Tela(root)
root.mainloop()
