import glob
from fpdf import FPDF
from pathlib import Path

filepaths = glob.glob("data/*.txt")

pdf = FPDF(orientation="P", unit="mm", format="A4")

for filepath in filepaths:
    fp = open(filepath, "r")

    pdf.add_page()
    filename = Path(filepath).stem
    capital = filename.title()
    pdf.set_font(family="Times", style="B", size=21)
    pdf.cell(w=50, h=11, txt=capital, ln=1)

    content = fp.read() + "\n"

    pdf.set_font(family="Times", style="", size=16)
    pdf.multi_cell(0,6, txt=f"{content}")
    fp.close()

pdf.output(f"pdfs/project.pdf")
