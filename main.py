from core.constants import pollutants, variables, years, numerate
from core.data_analysis import DataAnalysis
from core.plot import Video, Plotter
from core.utils import label_interpreter

if __name__ == "__main__":
    while True:
        try:
            print(
                "Bienvenido al programa que te permite recuperar información gráfica acerca de algunos contaminantes"
            )
            pollutant = input(f"Escoge un contaminante a analizar: {numerate}\n")
            factor = input(
                f"Escoge una propiedad de la siguiente lista: {variables.keys()}\n"
            )
            year = int(input("Escoge un año: 2004, 2005 \n"))

            pollutant = pollutants[numerate[str(pollutant)]]
            factor = variables[str(factor).upper()]

            if year not in years:
                raise Exception()

            analysis = DataAnalysis(pollutant, factor, year)
            analysis = analysis.run_analysis()
            concentration, factors = label_interpreter(pollutant, factor)

            plotter = Plotter()
            plotter.add_subplot(211)
            plotter.add_subplot(212)
            plotter.subplot(
                plotter.plots[0],
                analysis["Date"],
                analysis[pollutant],
                f"Concentración de {pollutant} a lo largo del tiempo",
                concentration,
            )
            plotter.subplot(
                plotter.plots[1],
                analysis["Date"],
                analysis[factor],
                f"Medición de {factors[0]} a lo largo del tiempo",
                factors[1],
                color="r",
            )
            plotter.draw("animacion.png")

            Video(analysis, pollutant, factor).animator("animacion")
            print("El programa ha concluido.")
            break
        except Exception as e:
            print(e)
            print(
                "Los datos ingresados son incorrectos o hubo un error en la ejecución."
            )
            retry = input("¿Quieres intentar de nuevo? s/n\n")
            if retry.lower() == "n":
                break
