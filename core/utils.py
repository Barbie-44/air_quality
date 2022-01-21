import pandas as pd
import numpy as np


class DataAnalysis:
    def file_reader(self, file: str):
        return pd.read_csv(file, delimiter=";", dtype=str)

    def data_retriever(self, file, data1: str, data2: str):
        return self.file_reader(file)[["Date", "Time", data1, data2]]

    def data_formatter(self, data: pd.DataFrame, pollutant: str, factor: str):
        data["Date"] = data["Date"] + " " + data["Time"]
        data["Date"] = pd.to_datetime(data["Date"], format="%d/%m/%Y %H.%M.%S")
        data[pollutant] = pd.to_numeric(
            data[pollutant].str.replace(",", ".").str.replace("-200", "")
        )
        data[factor] = pd.to_numeric(
            data[factor].str.replace(",", ".").str.replace("-200", "")
        )
        return data

    ## Aqui agregué lo que hizo Hugo, no esperé a que hiciéramos merge, lo copié y pegué en mi branch
    def empty_data_remover(self, data: pd.DataFrame):
        data.replace(r"^\s*$", np.nan, regex=True, inplace=True)
        data.dropna(inplace=True)
        return None
     def filter_year(self,data:pd.DataFrame,year:int,column:str):
       df=data[data[column].str.contains(str(year))]
       return df

    ## Función de correlación de Pearson para el pollutant y factor elegidos
    def Pearson_correlation(self, data: pd.DataFrame, pollutant: str, factor: str):
        Xi_Xm = data[pollutant] - data[pollutant].mean()
        Yi_Ym = data[factor] - data[factor].mean()
        Mult = Xi_Xm * Yi_Ym
        Numerator = Mult.sum()
        Xi_Xm2 = Xi_Xm * Xi_Xm
        Yi_Ym2 = Yi_Ym * Yi_Ym
        Denominator = np.sqrt(Xi_Xm2.sum()) * np.sqrt(Yi_Ym2.sum())
        r_coeficient = Numerator / Denominator
        print(
            "El coeficiente de correlación entre",
            pollutant,
            "y",
            factor,
            "es:",
            r_coeficient,
        )
        ##No se si vale la pena dar un return dado que ya está el print.
        return r_coeficient
