from typing import List, Tuple
from core.constants import pollutant_labels, factor_labels


def label_interpreter(pollutant: str, factor: str) -> Tuple[str, List[str]]:
    """
    Devuelve una tupla de strinf y lista de strings, con los nombres
    adecuados para rotular los ejes y para cada gráfico.
    """
    return (pollutant_labels[pollutant], factor_labels[factor])
