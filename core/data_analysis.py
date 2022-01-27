import pandas as pd
import numpy as np


class DataAnalysis:
    """
    Esta clase se encarga de analizar y darle formato a la información contenida
    en el dataset. Se inicializa desde main al ser llamada con los valores otorgados
    por el usuario.
    """

    def __init__(self, pollutant: str, factor: str, year: int):
        self.analysis = None
        self.factor = factor
        self.pollutant = pollutant
        self.year = year

    def file_reader(self, file: str):
        """
        Esta función se encarga de leer el archivo csv
        """
        return pd.read_csv(file, delimiter=";", dtype=str)

    def data_retriever(self, file):
        """
        Se encarga de recuperar algunas de las columnas del dataframe
        """
        self.analysis = self.file_reader(file)[
            [
                "Date",
                "Time",
                self.pollutant,
                self.factor,
            ]
        ]

    def filter_year(self, year: int):
        """
        A partir del input dado por el usuario, esta función hace un
        filtrado por fecha en el dataframe y solo recupera la información
        de ese año en específico.
        """
        expected = self.analysis[
            self.analysis["Date"].astype(str).str.contains(str(year))
        ]["Date"]
        self.analysis = self.analysis.drop(labels=["Date", "Time"], axis=1)
        self.analysis["Date"] = expected

    def date_formatter(self):
        """
        Hace modificación al dataframe para que tenga un formato de
        día-mes-año hora-minuto-segundo.
        """
        self.analysis["Date"] = self.analysis["Date"] + " " + self.analysis["Time"]
        self.analysis["Date"] = pd.to_datetime(
            self.analysis["Date"], format="%d/%m/%Y %H.%M.%S"
        )

    def data_formatter(self, value: str):
        """
        Da formato a la información almacenada en el dataframe para su
        análisis y graficación.
        """
        self.analysis[value] = pd.to_numeric(
            self.analysis[value].str.replace(",", ".").str.replace("-200", "")
        )
        return self.analysis

    def empty_data_remover(self):
        """
        Se encarga de eliminar todas las filas que contengan valores NaN
        en el dataframe.
        """
        self.analysis.replace(r"^\s*$", np.nan, regex=True, inplace=True)
        self.analysis.dropna(inplace=True)

    def pearson_correlation(self, pollutant: str, factor: str):
        """
        Calcula la correlación de pearson entre contaminante y factor ambiental,
        por ejemplo CO vs Temperatura. Lo imprime en la terminal.
        """
        Xi_Xm = self.analysis[pollutant] - self.analysis[pollutant].mean()
        Yi_Ym = self.analysis[factor] - self.analysis[factor].mean()
        Mult = Xi_Xm * Yi_Ym
        Numerator = Mult.sum()
        Xi_Xm2 = Xi_Xm * Xi_Xm
        Yi_Ym2 = Yi_Ym * Yi_Ym
        Denominator = np.sqrt(Xi_Xm2.sum()) * np.sqrt(Yi_Ym2.sum())
        r_coeficient = Numerator / Denominator
        print(
            f"El coeficiente de correlación entre {pollutant} y {factor} es {r_coeficient}"
        )

    def run_analysis(self):
        """
        Al ser invocada, da paso a la ejecución de todas las funciones
        anteriores de esta clase. Regresa un dataframe listo para ser
        graficado.
        """
        self.data_retriever("raw_data/AirQualityUCI.csv")
        self.date_formatter()
        self.data_formatter(self.pollutant)
        self.data_formatter(self.factor)
        self.filter_year(self.year)
        self.empty_data_remover()
        self.pearson_correlation(self.pollutant, self.factor)
        return self.analysis
