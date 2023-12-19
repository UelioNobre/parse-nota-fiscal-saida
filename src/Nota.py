from dataclasses import dataclass


@dataclass
class Nota:
    especie: str
    serie: str
    numero: str
    fiscal: str
    emissao: str
    entrada_saida: str
    valor_contabil: float
    valor_icms: float
    valor_ipi: float
    status: str
    exp: str
