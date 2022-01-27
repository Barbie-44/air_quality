"""
Estos son los diccionarios estáticos y las constantes que se utilizan en
los métodos durante la ejecución de todo el programa.
"""

pollutants = {
    "CO": "CO(GT)",
    "NMHC": "NMHC(GT)",
    "C6H6": "C6H6(GT)",
    "NOX": "NOx(GT)",
    "NO2": "NO2(GT)",
}
numerate_dic = {
    "0": "CO",
    "1": "NMHC",
    "2": "C6H6",
    "3": "NOX",
    "4": "NO2",
}
variables = {"T": "T", "H": "AH"}
years = [2004, 2005]

pollutant_labels = {
    "CO(GT)": "CO (Monóxido de carbono) [mg/m^3]",
    "NMHC(GT)": "NMHC (Hidrocarburos no-metánicos) [microg/m^3]",
    "C6H6(GT)": "C6H6 (Benceno) [microg/m^3]",
    "NOx(GT)": "NOx (Óxido de nitrógeno) [ppb]",
    "NO2(GT)": "NO2 (Dióxido de nitrógeno) [microg/m^3]",
}
factor_labels = {
    "T": ["Temperatura", "T [ºC]"],
    "AH": ["Humedad Absoluta", "Humedad Absoluta [g/m^3]"],
}

FRAMES = 150
FPS = 30
