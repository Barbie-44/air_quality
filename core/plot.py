from lib2to3.pgen2.pgen import DFAState
import matplotlib.pyplot as plt
from constants import pollutant_labels, factor_labels
from matplotlib import animation
from IPython.display import HTML
from IPython import display

## AQUI EN CUANTO ESTÉ HECHO LO DE FILTRAR POR AÑOS DEBEMOS AGREGAR UN ARGUMENTO A plotter
## QUE PIDA EL AÑO SOLICITADO Y CAMBIAR EL X LABEL DE LOS PLOTS PARA QUE CORRESPONDA AL AÑO


def label_interpreter(pollutant: str, factor: str):
    concentration, variable = (pollutant_labels[pollutant], factor_labels[factor])
    return (concentration, variable)


def plotter(x_axys: str, y_axis: str, y_axis2: str, pollutant: str, factor: str):
    concentration, factors = label_interpreter(pollutant, factor)
    
    # NOTA, CORREGIR LOS LIMITES DE PLOTEO
    plt.figure()
    plt.subplot(211)
    plt.plot(x_axys[0:1000], y_axis[0:1000], "-")
    plt.title(f"Concentración de {pollutant} a lo largo del tiempo")
    plt.ylabel(f"{concentration}")
    plt.xlabel("Tiempo")
    plt.subplot(212)
    plt.plot(x_axys[0:1000], y_axis2[0:1000], "-", color="r")
    plt.title(f"Medición de {factors[0]} a lo largo del tiempo")
    plt.ylabel(f"{factors[1]}")
    plt.xlabel("Tiempo")
    fig = plt.gcf()
    fig.set_size_inches(20, 10)
    fig.savefig("Grafica.png", dpi=100)
    print("PARA CONTINUAR CIERRE LA FIGURA")
    return plt.show()

class VIDEO:
    def __init__(self, analysis, pollutant, factor):
        self.analysis=analysis
        self.pollutant=pollutant
        self.factor=factor
        #self.fig=plt.figure(figsize=(20,10))
#Refrescamiento de cuadros.
#Ploteamos el punto i+1 con todos los anteriores para cada i que nos dará self.animate()
    def update(self,frame):
        ## NO PUDIMOS HACER QUE LA ANIMACION MUESTRE LABELS
        plt.title(f"Concentración de {self.pollutant} a lo largo del tiempo")
        plt.ylabel(f"Concentración")
        plt.xlabel("Tiempo")
        pl=plt.plot(self.analysis["Date"][0:frame],self.analysis[self.pollutant][0:frame],"b-")
        pl2=plt.plot(self.analysis["Date"][0:frame],self.analysis[self.pollutant][0:frame],"b-")
        
        return pl

## Esta función se encarga de hacer la animación
    def animator(self):
        fig=plt.figure(figsize=(20,10))
        anim = animation.FuncAnimation(fig,self.update,frames=300,repeat=True,interval=20,blit=True)
        #plt.show()
        print("ESPERE UN MOMENTO, guardando animación...")
        ## ESTA ES LA PARTE QUE NO FUNCIONA PORQUE VISUAL STUDIO CODE NO TIENE SOPORTE PARA ffmpeg
        anim.save('Animación.gif', writer='pillow',fps=30)
        print("La animación ha sido guardada.")
        return 

                






#########################################################################
                

    
#########################################################################
                