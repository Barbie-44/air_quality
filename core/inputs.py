from utils import DataAnalysis
from plot import plotter
from plot import VIDEO
from constants import pollutants, variables

class UserInterface:
    def input_retriever(self):
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
                pollutant = pollutants.get(self.pollutant.upper())
                factor = variables.get(str(self.factor).upper())
                
                analysis = DataAnalysis().data_retriever(
                    "raw_data/AirQualityUCI.csv", pollutant, factor
                )
                ## A continuación invoco a otra función para darle formato a
                ## la fecha y al contaminante, su definición la pueden encontrar en
                ## el archivo de utils.py
                DataAnalysis().data_formatter(analysis, pollutant, factor)
                ## Moví aquí la función que elimina los registros NaN para que borre
                ## los registros del dataframe final
                print(analysis)
                DataAnalysis().empty_data_remover(analysis)
                ## Esta función devuelve el coeficiente de correlación de Pearson
                ## entre el contaminante y el factor elegidos
                DataAnalysis().Pearson_correlation(analysis, pollutant, factor)
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
                
                VIDEO(analysis,pollutant,factor).animator()

                print("El programa ha concluido.")

                return analysis
            except:
                print("Los datos ingresados son incorrectos o hubo un error en la ejecución.")
                ## Creo que me parece más conveniente que el usuario solo
                ## escriba la letra "n" en caso de no querer continuar
                retry = input("¿Quieres intentar de nuevo? s/n\n")
                if retry == "n":
                    break


UserInterface().input_retriever()
