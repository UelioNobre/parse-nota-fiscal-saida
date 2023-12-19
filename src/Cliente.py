from PyPDF2 import PdfReader


class Cliente:
    def __init__(self, path_pdf):
        self.path_pdf = path_pdf
        self.slowmotion = True
        self.executeParse()

    def getPages(self, reader):
        pages = []
        for page in reader.pages:
            pages.append(page)
        return pages

    def showInfo(self, page):
        text = page.extract_text()
        text_list = text.split("\n")

        row_0 = text_list[2].split(" ")
        row_1 = text_list[1].strip().split(" ")

        cnpj_cpf = row_0[1]
        incsricao_estadual = row_0[-2]

        data_emissao = row_1[8]
        contador = " ".join(row_1[9:13]).strip()
        cliente = " ".join(row_1[13:]).strip()

        data_show = [
            "",
            f"Cliente: {cliente}",
            f"CNPJ/CPF: {cnpj_cpf}",
            f"Inscrição Estadual: {incsricao_estadual}",
            f"Data Emissão: {data_emissao}",
            "",
            f"Contador: {contador}",
            "",
            "",
            "Feliz natal! Ho, ho, ho, ho!",
            "",
            "E acabou a apresentação :-)",
            "",
            "",
            "",
        ]

        for line in data_show:
            print(line)

        print("")

    def executeParse(self):
        reader = PdfReader(self.path_pdf)
        pages = self.getPages(reader)
        self.showInfo(pages[0])
