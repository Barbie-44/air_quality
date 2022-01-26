from asyncio.proactor_events import constants
import pandas as pd
import numpy as np
from constants import years


class DataAnalysis:
    def file_reader(self, file: str):
        return pd.read_csv(file, delimiter=";", dtype=str)

    def data_retriever(self, file, data1: str, data2: str):
        return self.file_reader(file)[["Date", "Time", data1, data2]]

    def filter_year(self, data: pd.DataFrame, year: int):
        expected = data[data["Date"].astype(str).str.contains(str(year))]["Date"]
        data = data.drop(labels=["Date", "Time"], axis=1)
        data["Date"] = expected
        return data

    def date_formatter(self, data: pd.DataFrame):
        data["Date"] = data["Date"] + " " + data["Time"]
        data["Date"] = pd.to_datetime(data["Date"], format="%d/%m/%Y %H.%M.%S")
        return data

    def data_formatter(self, data: pd.DataFrame, value: str):
        data[value] = pd.to_numeric(
            data[value].str.replace(",", ".").str.replace("-200", "")
        )
        return data

    ## Función que elimina los registros con valores NaN
    def empty_data_remover(self, data: pd.DataFrame):
        data.replace(r"^\s*$", np.nan, regex=True, inplace=True)
        data.dropna(inplace=True)
        pass

    ## Función de correlación de Pearson para el pollutant y factor elegidos
    def pearson_correlation(self, data: pd.DataFrame, pollutant: str, factor: str):
        Xi_Xm = data[pollutant] - data[pollutant].mean()
        Yi_Ym = data[factor] - data[factor].mean()
        Mult = Xi_Xm * Yi_Ym
        Numerator = Mult.sum()
        Xi_Xm2 = Xi_Xm * Xi_Xm
        Yi_Ym2 = Yi_Ym * Yi_Ym
        Denominator = np.sqrt(Xi_Xm2.sum()) * np.sqrt(Yi_Ym2.sum())
        r_coeficient = Numerator / Denominator
        print(
            f"El coeficiente de correlación entre {pollutant} y {factor} es {r_coeficient}"
        )
