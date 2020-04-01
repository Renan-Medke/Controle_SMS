def carregar_latitude():
        f = open('parametros.txt', 'r')
        s = f.readline()
        f.close()
        return(s)

def carregar_longitude():
        f = open('parametros.txt', 'r')
        s = f.readline()
        s = f.readline()
        f.close()
        return(s)

def salvar_coordenadas(latitude,longitude):
        f = open('parametros.txt', 'w')
        f.write(latitude)
        f.write('\n')
        f.write(longitude)
        f.close()
        return()

'''
    def carregar_latitude(self):
        f = open('parametros.txt', 'r')
        self.s = f.readline()
        f.close()
        return(self.s)

    def carregar_longitude(self):
        f = open('parametros.txt', 'r')
        self.s = f.readline()
        self.s = f.readline()
        f.close()
        return(self.s)
        -29.6914
        -53.8008
    '''   
