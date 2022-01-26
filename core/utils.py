from typing import List, Tuple
from core.constants import pollutant_labels, factor_labels


def label_interpreter(pollutant: str, factor: str) -> Tuple[str, List[str]]:
    return (pollutant_labels[pollutant], factor_labels[factor])
