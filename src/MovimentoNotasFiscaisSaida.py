import locale
from PyPDF2 import PdfReader

from src.Nota import Nota


class MovimentoNotasFiscaisSaida:
    def __init__(self, path_pdf):
        self.path_pdf = path_pdf
        self.notas = []
        self.notas_canceladas = []
        self.total = 0
        self.total_cancelada = 0
        self.slowmotion = True
        self.executeParse()

    def getPages(self, reader):
        pages = []
        for page in reader.pages:
            pages.append(page)
        return pages

    def getRawContents(self, page):
        return page.extract_text()

    def convertToFloat(self, value):
        return float(value.replace(".", "").replace(",", "."))

    def createNotaNormal(self, values):
        especie = values[0]
        serie = values[1]
        numero = values[2]
        fiscal = values[3]
        emissao = values[4]
        entrada_saida = values[5]
        valor_contabil = self.convertToFloat(values[6])
        valor_icms = self.convertToFloat(values[7])
        valor_ipi = self.convertToFloat(values[8])
        status = None
        exp = values[9]

        self.total += valor_contabil

        return Nota(
            especie,
            serie,
            numero,
            fiscal,
            emissao,
            entrada_saida,
            valor_contabil,
            valor_icms,
            valor_ipi,
            status,
            exp,
        )

    def createNotaCancelada(self, values):
        especie = values[0]
        serie = values[1]
        numero = values[2]
        fiscal = values[3]
        emissao = values[4]
        entrada_saida = values[5]
        valor_contabil = self.convertToFloat(values[6])  # ok
        valor_icms = self.convertToFloat(values[8])
        valor_ipi = self.convertToFloat(values[9])
        status = values[7]
        exp = values[10]

        self.total_cancelada += valor_contabil

        return Nota(
            especie,
            serie,
            numero,
            fiscal,
            emissao,
            entrada_saida,
            valor_contabil,
            valor_icms,
            valor_ipi,
            status,
            exp,
        )

    def createDataRow(self, value):
        whitelist_row_started = ["cfe", "nfe"]
        content_list = value.strip().split("\n")

        for row in content_list:
            split_row = row.strip().split(" ")

            if split_row[0].lower() not in whitelist_row_started:
                continue

            if len(split_row) == 11:
                nota = self.createNotaCancelada(split_row)
                self.notas_canceladas.append(nota)
                self.notas.append(nota)
            else:
                nota = self.createNotaNormal(split_row)
                self.notas.append(nota)

    def showInfo(self):
        print("")
        print("Total de notas", len(self.notas))
        print("Valor total de saída", self.moeda(self.total))
        print("Total de notas canceladas", len(self.notas_canceladas))
        print("Valor total notas cancelada", self.moeda(self.total_cancelada))

    def executeParse(self):
        reader = PdfReader(self.path_pdf)
        pages = self.getPages(reader)

        for page in pages:
            contents = self.getRawContents(page)
            self.createDataRow(contents)

    def moeda(self, value):
        locale.setlocale(locale.LC_ALL, "pt_BR.UTF-8")

        valor = locale.currency(value, grouping=True, symbol=None)
        return valor
