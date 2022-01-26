from utils import DataAnalysis
from plot import Video, plotter
from constants import pollutants, variables, years


class UserInterface:
    def __init__(self):
        while True:
            try:
                ## mejor cambie este print acá porque abajo se veía feon
                print(
                    "Bienvenido al programa que te permite recuperar información gráfica acerca de algunos contaminantes"
                )
                self.pollutant = input(
                    f"Escoge un contaminante a analizar de la siguiente lista: {pollutants.keys()}\n"
                )
                self.factor = input(
                    f"Escoge una propiedad de la siguiente lista: {variables.keys()}\n"
                )
                year = int(input("Escoge un año: 2004, 2005 \n"))
                if year not in years:
                    raise Exception()
                pollutant = pollutants.get(self.pollutant.upper())
                factor = variables.get(str(self.factor).upper())
                analysis = DataAnalysis().data_retriever(
                    "raw_data/AirQualityUCI.csv", pollutant, factor
                )
                ## A continuación se invoca a otra función para darle formato a
                ## la fecha y al contaminante, su definición la pueden encontrar en
                ## el archivo de utils.py
                DataAnalysis().date_formatter(analysis)
                DataAnalysis().data_formatter(analysis, pollutant)
                DataAnalysis().data_formatter(analysis, factor)
                ## Se invoca la función que elimina los registros NaN
                ## del dataframe final
                analysis = DataAnalysis().filter_year(analysis, year)
                DataAnalysis().empty_data_remover(analysis)
                ## Esta función devuelve el coeficiente de correlación de Pearson
                ## entre el contaminante y el factor elegidos
                DataAnalysis().pearson_correlation(analysis, pollutant, factor)
                ## Moví el código que había aquí para graficar y lo metí en una función
                ## que se dedica exclusivamente al graficado y la pueden encontrar
                ## en el archivo core/plot.py
                plotter(
                    analysis["Date"],
                    analysis[pollutant],
                    analysis[factor],
                    pollutant,
                    factor,
                )

                Video(analysis, pollutant, factor).animator()

                print("El programa ha concluido.")
                return None
            except Exception as e:
                print(e)
                print(
                    "Los datos ingresados son incorrectos o hubo un error en la ejecución."
                )
                ## escriba la letra "n" en caso de no querer continuar
                retry = input("¿Quieres intentar de nuevo? s/n\n")
                if retry == "n":
                    break


# Let's give it a try!
UserInterface()
