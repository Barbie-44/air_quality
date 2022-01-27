"""
Estos son los diccionarios estáticos y las constantes que se utilizan en
los métodos durante la ejecución de todo el programa.
"""

pollutants = {
    "CO": "CO(GT)",
    "PT08_S1": "PT08.S1(CO)",
    "NMHC": "NMHC(GT)",
    "C6H6": "C6H6(GT)",
    "PT08_S2": "PT08.S2(NMHC)",
    "NOX": "NOx(GT)",
    "PT08_S3": "PT08.S3(NOx)",
    "NO2": "NO2(GT)",
    "PT08_S4": "PT08.S4(NO2)",
    "PT08_S5": "PT08.S5(O3)",
}
numerate_dic = {
    "0": "CO",
    "1": "PT08_S1",
    "2": "NMHC",
    "3": "C6H6",
    "4": "PT08_S2",
    "5": "NOX",
    "6": "PT08_S3",
    "7": "NO2",
    "8": "PT08_S4",
    "9": "PT08_S5",
}
variables = {"T": "T", "H": "AH"}
years = [2004, 2005]

pollutant_labels = {
    "CO(GT)": "CO (Monóxido de carbono) [mg/m^3]",
    "PT08.S1(CO)": "PT08.S1 (Oxido de estaño) [mg/m^3]",
    "NMHC(GT)": "NMHC (Hidrocarburos no-metánicos) [microg/m^3]",
    "C6H6(GT)": "C6H6 (Benceno) [microg/m^3]",
    "PT08.S2(NMHC)": "PT08.S2 (Titanio) [microg/m^3]",
    "NOx(GT)": "NOx (Óxido de nitrógeno) [ppb]",
    "PT08.S3(NOx)": "PT08.S3 (Óxido de tungsteno) [microg/m^3]",
    "NO2(GT)": "NO2 (Dióxido de nitrógeno) [microg/m^3]",
    "PT08.S4(NO2)": "PT08.S4 (Óxido de tungsteno) [microg/m^3]",
    "PT08.S5(O3)": "PT08.S5 (Óxido de indio) [microg/m^3]",
}
factor_labels = {
    "T": ["Temperatura", "T [ºC]"],
    "AH": ["Humedad Absoluta", "Humedad Absoluta [g/m^3]"],
}

FRAMES = 150
FPS = 30
