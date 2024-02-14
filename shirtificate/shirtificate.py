from fpdf import FPDF

name = input("Enter name: ")
# an obj of fpdf
pdf = FPDF(orientation="P", unit="mm", format="A4")
# manually add page and font
pdf.add_page()
pdf.set_font("Times", "B", size=55)
pdf.cell(0, 60, txt="CS50 Shirtificate", align="C")
# using imges
pdf.image("shirtificate.png", keep_aspect_ratio=True, w=190, h=190, x=10, y=60)
pdf.set_text_color(255, 255, 255)
pdf.set_font_size(35)
pdf.text(55, 125, txt=name + " took CS50")

pdf.output("shirtificate.pdf")
