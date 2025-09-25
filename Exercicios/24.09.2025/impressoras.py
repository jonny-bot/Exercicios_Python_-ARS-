from fpdf import FPDF

# Criar classe PDF personalizada
class PDF(FPDF):
    def header(self):
        self.set_font("Arial", "B", 14)
        self.cell(0, 10, "Modelos de Impressoras Equivalentes ou Melhores que a Lexmark X466", 0, 1, "C")
        self.ln(5)

    def chapter_title(self, title):
        self.set_font("Arial", "B", 12)
        self.cell(0, 10, title, 0, 1, "L")
        self.ln(2)

    def chapter_body(self, body):
        self.set_font("Arial", "", 11)
        self.multi_cell(0, 8, body)
        self.ln()

# Criar o conteúdo
modelos = [
    {
        "Modelo": "Pantum BP5100DW",
        "Descrição": "Mono, duplex automático, 40 ppm, USB/Rede/WiFi",
        "Preço e Loja": "R$ 1.626,57 (ImpressoraJato)"
    },
    {
        "Modelo": "Pantum BM5100FDW",
        "Descrição": "Multifuncional, duplex, WiFi, 40 ppm, scanner/fax",
        "Preço e Loja": "R$ 2.315,00 (DigitalCopy)"
    },
    {
        "Modelo": "HP 4103FDW",
        "Descrição": "Multifuncional robusta, 40 ppm, rede, duplex, painel moderno",
        "Preço e Loja": "R$ 2.967,72 (TotalForce)"
    },
    {
        "Modelo": "HP Pro E42540F",
        "Descrição": "Alta performance, 42 ppm, ciclo mensal elevado",
        "Preço e Loja": "R$ 3.161,07 (ImpressoraJato)"
    },
    {
        "Modelo": "Kyocera Ecosys M2640idw",
        "Descrição": "Multifuncional, 40 ppm, WiFi, duplex, robusta",
        "Preço e Loja": "R$ 5.268,00 (DigitalCopy)"
    },
    {
        "Modelo": "Brother DCP-L2540DW",
        "Descrição": "Mono, multifuncional, ADF, WiFi, duplex",
        "Preço e Loja": "R$ 1.100,00 (Mercado Livre)"
    },
    {
        "Modelo": "HP Laser M432FDN",
        "Descrição": "Mono, rede, duplex, 40 ppm",
        "Preço e Loja": "R$ 1.901,01 (Mercado Livre)"
    },
    {
        "Modelo": "Brother DCPL3560CDW",
        "Descrição": "Colorida, duplex, ADF, WiFi",
        "Preço e Loja": "R$ 4.139,41 (Amazon)"
    },
    {
        "Modelo": "HP Laser 135W",
        "Descrição": "Mono, WiFi, básica",
        "Preço e Loja": "R$ 1.592,10 (Magazine Luiza)"
    },
    {
        "Modelo": "HP Laser 135A",
        "Descrição": "Mono, multifuncional básica",
        "Preço e Loja": "R$ 1.349,10 (HP Store Brasil)"
    }
]

# Gerar PDF
pdf = PDF()
pdf.add_page()
pdf.set_auto_page_break(auto=True, margin=15)

pdf.chapter_title("Lista de Impressoras Recomendadas")

for m in modelos:
    content = f"Modelo: {m['Modelo']}\nDescrição: {m['Descrição']}\nPreço e Loja: {m['Preço e Loja']}"
    pdf.chapter_body(content)

# Salvar o PDF
pdf.output("Modelos_Impressoras_Alternativas_Lexmark_X466.pdf")