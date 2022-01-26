import pandas as pd
import numpy as np


class DataAnalysis:
    def __init__(self, pollutant: str, factor: str, year: int):
        self.analysis = None
        self.factor = factor
        self.pollutant = pollutant
        self.year = year

    def file_reader(self, file: str):
        return pd.read_csv(file, delimiter=";", dtype=str)

    def data_retriever(self, file):
        self.analysis = self.file_reader(file)[
            [
                "Date",
                "Time",
                self.pollutant,
                self.factor,
            ]
        ]

    def filter_year(self, year: int):
        expected = self.analysis[
            self.analysis["Date"].astype(str).str.contains(str(year))
        ]["Date"]
        self.analysis = self.analysis.drop(labels=["Date", "Time"], axis=1)
        self.analysis["Date"] = expected

    def date_formatter(self):
        self.analysis["Date"] = self.analysis["Date"] + " " + self.analysis["Time"]
        self.analysis["Date"] = pd.to_datetime(
            self.analysis["Date"], format="%d/%m/%Y %H.%M.%S"
        )

    def data_formatter(self, value: str):
        self.analysis[value] = pd.to_numeric(
            self.analysis[value].str.replace(",", ".").str.replace("-200", "")
        )
        return self.analysis

    ## Función que elimina los registros con valores NaN
    def empty_data_remover(self):
        self.analysis.replace(r"^\s*$", np.nan, regex=True, inplace=True)
        self.analysis.dropna(inplace=True)

    ## Función de correlación de Pearson para el pollutant y factor elegidos
    def pearson_correlation(self, pollutant: str, factor: str):
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
        self.data_retriever("raw_data/AirQualityUCI.csv")
        self.date_formatter()
        self.data_formatter(self.pollutant)
        self.data_formatter(self.factor)
        self.filter_year(self.year)
        self.empty_data_remover()
        self.pearson_correlation(self.pollutant, self.factor)
        return self.analysis
