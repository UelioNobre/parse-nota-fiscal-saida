from src.Cliente import Cliente
from src.MovimentoNotasFiscaisSaida import MovimentoNotasFiscaisSaida


file_pdf = "docs/23-11-movimento-de-notas-fiscais.pdf"

movimentoNotasFiscaisSaida = MovimentoNotasFiscaisSaida(file_pdf)
movimentoNotasFiscaisSaida.showInfo()
cliente = Cliente(file_pdf)
