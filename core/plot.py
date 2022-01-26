import matplotlib.pyplot as plt
from constants import pollutant_labels, factor_labels
from matplotlib import animation
import time


def label_interpreter(pollutant: str, factor: str):
    concentration, variable = (pollutant_labels[pollutant], factor_labels[factor])
    return (concentration, variable)


def plotter(x_axys: str, y_axis: str, y_axis2: str, pollutant: str, factor: str):
    concentration, factors = label_interpreter(pollutant, factor)

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
    print("PARA CONTINUAR CIERRE LA VENTANA EMERGENTE DE LA FIGURA")
    plt.show()


class Video:
    fig = plt.figure(figsize=(20, 10))
    ax1 = fig.add_subplot(1, 1, 1)

    def __init__(self, analysis, pollutant, factor):
        self.analysis = analysis
        self.pollutant = pollutant
        self.factor = factor

    def update(self, frame: int):
        self.ax1.clear()
        self.ax1.set_title(f"Concentración de {self.pollutant} a lo largo del tiempo")
        self.ax1.set_ylabel(f"Concentración de {pollutant_labels[self.pollutant]}")
        self.ax1.set_xlabel("Tiempo")
        self.ax1.plot(
            self.analysis["Date"][:frame],
            self.analysis[self.pollutant][:frame],
        )

    # ## Esta función se encarga de hacer la animación
    def animator(self):
        start = time.time()
        anim = animation.FuncAnimation(
            self.fig,
            self.update,
            frames=300,
        )
        print(
            "ESPERE UN MOMENTO, GUARDANDO ANIMACIÓN, ESTO PUEDE TARDAR ALGUNOS SEGUNDOS..."
        )
        # Se inicia el proceso de guardado de la animación con formato mp4
        anim.save("animacion.mp4", fps=30, extra_args=["-vcodec", "libx264"])
        end = time.time()
        # Se muestra al usuario la confirmación y el tiempo de ejecución.
        # La imagen ya debe estar guardada.
        print("La animación ha sido guardada.")
        print(f"El tiempo de ejecución ha sido de {end - start} s")
        return
