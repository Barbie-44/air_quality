from core.constants import pollutants, variables, years, numerate_dic
from core.data_analysis import DataAnalysis
from core.plot import Video, Plotter
from core.utils import label_interpreter


"""
Es desde este punto donde ocurre la ejecución del flujo completo del código, ya que
hace la llamada a cada una de las clases y a sus respectivas funciones.
Comienza solicitando al usuario tres inputs que posteriormente son usados para el
análisis de la información.
"""
if __name__ == "__main__":
    while True:
        try:
            print(
                "Bienvenido al programa que te permite recuperar información gráfica acerca de algunos contaminantes"
            )
            pollutant = input(f"Escoge un contaminante a analizar: {numerate_dic}\n")
            factor = input(
                f"Escoge una propiedad de la siguiente lista: {variables.keys()}\n"
            )
            year = int(input("Escoge un año: 2004, 2005 \n"))

            """
            Con base en la información correcta del usuario, se busca la llave en un diccionario
            que contiene los valores disponibles y se asignan a una variable. En caso de que el
            usuario no introduzca los valores adecuados, se termina levanta una excepción.
            """
            pollutant = pollutants[numerate_dic[str(pollutant)]]
            factor = variables[str(factor).upper()]

            if year not in years:
                raise Exception()

            """
            Se asigna a una variable la llamada a la clase DataAnalysis y se le pasan
            los valores (ya validados) introducidos por el usuario y se llama a la
            a la función run_analysis() para comenzar el análisis del dataset.
            """
            analysis = DataAnalysis(pollutant, factor, year)
            analysis = analysis.run_analysis()

            """
            A partir de este punto comienza el proceso de graficado.
            Se llama a la función label_interpreter con la única intención de rotular
            al eje y con el string adecuado para cada contaminante y factor.
            Posteriormente se inicializa la clase Plotter y se asigna a una variable
            con el propósito de llamar a cada una de sus funciones y establecer
            parámetros específicos en su ejecución.
            """
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
            plotter.draw("grafica_bonita.png")

            """
            Finalmente se invoca a la clase Video, se le pasan los parámetros
            de interés para el usuario y se invoca a su función animator que
            como parámetro recibe el nombre con el que se guarda la animación.
            El programa finaliza.
            """
            Video(analysis, pollutant, factor).animator("animacion")
            print("El programa ha concluido.")
            break

            """
            Si el flujo en la ejecución del programa se ve interrumpido, se
            ve interrumpido, se levanta una excepcion, se muestra en dónde fue
            la falla y se pregunta al usuario si desea iniciar la ejecución
            nuevamente.
            """
        except Exception as e:
            print(e)
            print(
                "Los datos ingresados son incorrectos o hubo un error en la ejecución."
            )
            retry = input("¿Quieres intentar de nuevo? s/n\n")
            if retry.lower() == "n":
                break
