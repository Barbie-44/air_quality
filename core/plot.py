from typing import List
import matplotlib.pyplot as plt
from core.constants import pollutant_labels, FRAMES, FPS
from matplotlib import animation
import time


class Plotter:
    def __init__(self):
        """
        Al inicializar la clase se crea un objeto que corresponde
        a la figura y otro que corresponde a una lista vacía
        """
        self.fig = plt.figure()
        self.plots = []

    def add_subplot(self, coordinates: int):
        """
        Se encarga de agregar las coordenadas de las gráficas que se crean
        """
        self.plots.append(self.fig.add_subplot(coordinates))

    def subplot(self, plot, x: List, y: List, title, message_y, color: str = "b"):
        """
        Se encarga de establecer los límites a cada gráfica
        que se crea, se establece el título del gráfico y el
        nombre específico para el eje y
        """
        plot.plot(x[:1000], y[:1000], "-", color=color)
        plot.set_title(title)
        plot.set_ylabel(message_y)
        plot.set_xlabel("Tiempo")

    def draw(self, name: str):
        """La función que se ejecuta en main y se guarda la figura"""
        self.fig.set_size_inches(20, 10)
        self.fig.savefig(name, dpi=100)
        print("LA IMAGEN SE HA GUARDADO...")


class Video:
    def __init__(self, analysis, pollutant, factor):
        """
        Al inicializar la clase se crea un objeto analysis correspondiente al dataframe,
        el contaminante, el factor, se inicializa la creación de una figura y se especifican
        los nombres de la figura y los ejes de acuerdo al tipo de contaminante y factor
        elegido por el usuario.
        """
        self.analysis = analysis
        self.pollutant = pollutant
        self.factor = factor
        self.fig = plt.figure(figsize=(20, 10))
        self.ax1 = self.fig.add_subplot(1, 1, 1)
        self.ax1.set_title(f"Concentración de {self.pollutant} a lo largo del tiempo")
        self.ax1.set_ylabel(f"Concentración de {pollutant_labels[self.pollutant]}")
        self.ax1.set_xlabel("Tiempo")

    def update(self, frame: int):
        """
        Esta función se iterará un limitado número de veces, se encarga de graficar
        cada punto del dataframe hasta cierto punto especificado
        """
        self.ax1.plot(
            self.analysis["Date"][:frame],
            self.analysis[self.pollutant][:frame],
            "b-",
        )

    def animator(self, name: str):
        """
        Se encarga de hacer una animación al llamar de manera iteratiba a la función
        update. Se guarda la animación con formato .mp4. De manera adicional, se
        muestra al usuario el tiempo de ejecución
        """
        start = time.time()
        anim = animation.FuncAnimation(
            self.fig,
            self.update,
            frames=FRAMES,
        )
        print(
            "ESPERE UN MOMENTO, GUARDANDO ANIMACIÓN, ESTO PUEDE TARDAR ALGUNOS SEGUNDOS..."
        )
        anim.save(f"{name}.mp4", fps=FPS, extra_args=["-vcodec", "libx264"])
        end = time.time()
        print("La animación ha sido guardada.")
        print(f"El tiempo de ejecución ha sido de {end - start} s")
