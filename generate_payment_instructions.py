from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib.colors import HexColor
from reportlab.pdfgen import canvas

GOLD = HexColor("#c9a96e")
DARK = HexColor("#1a1a1a")
GREY = HexColor("#555555")
LIGHT = HexColor("#f4f1ec")
LINE = HexColor("#dddddd")

W, H = A4
c = canvas.Canvas("CN_Payment_Instructions.pdf", pagesize=A4)

# ---- Header band ----
c.setFillColor(DARK)
c.rect(0, H - 45*mm, W, 45*mm, fill=1, stroke=0)
c.setFillColor(GOLD)
c.setFont("Helvetica-Bold", 22)
c.drawString(25*mm, H - 25*mm, "Payment Instructions")
c.setFillColor(HexColor("#cccccc"))
c.setFont("Helvetica", 11)
c.drawString(25*mm, H - 33*mm, "Casa Nova Global Sourcing Interiors  |  Website Project")

y = H - 58*mm

# ---- Intro ----
c.setFillColor(GREY)
c.setFont("Helvetica", 10.5)
intro = [
    "Thank you. Below are the details to settle the invoice for your website",
    "design and development. Payment is by international bank transfer.",
]
for line in intro:
    c.drawString(25*mm, y, line)
    y -= 6*mm

y -= 4*mm

# ---- Amount box ----
c.setFillColor(LIGHT)
c.roundRect(25*mm, y - 20*mm, W - 50*mm, 20*mm, 3*mm, fill=1, stroke=0)
c.setFillColor(GREY)
c.setFont("Helvetica", 9)
c.drawString(32*mm, y - 7*mm, "AMOUNT DUE")
c.setFillColor(DARK)
c.setFont("Helvetica-Bold", 20)
c.drawString(32*mm, y - 16*mm, "GBP 350.00")
c.setFillColor(GREY)
c.setFont("Helvetica", 9)
c.drawRightString(W - 32*mm, y - 7*mm, "INVOICE")
c.setFillColor(DARK)
c.setFont("Helvetica-Bold", 12)
c.drawRightString(W - 32*mm, y - 16*mm, "INV-001")

y -= 32*mm

# ---- Bank details heading ----
c.setFillColor(DARK)
c.setFont("Helvetica-Bold", 13)
c.drawString(25*mm, y, "Bank Transfer Details")
y -= 4*mm
c.setStrokeColor(GOLD)
c.setLineWidth(1.5)
c.line(25*mm, y, 60*mm, y)
y -= 10*mm

rows = [
    ("Beneficiary name", "Alexander McMillan"),
    ("IBAN", "GB37 REVO 2301 2071 1572 91"),
    ("BIC / SWIFT code", "REVOGB21"),
    ("Correspondent BIC", "CHASGB2L"),
    ("Bank name", "Revolut Ltd"),
    ("Bank address", "30 South Colonnade, E14 5HX, London, United Kingdom"),
    ("Payment reference", "Casa Nova Website"),
]

c.setFont("Helvetica", 10.5)
for label, value in rows:
    c.setFillColor(GREY)
    c.setFont("Helvetica", 9.5)
    c.drawString(25*mm, y, label.upper())
    c.setFillColor(DARK)
    c.setFont("Helvetica-Bold", 11)
    c.drawString(75*mm, y, value)
    y -= 4*mm
    c.setStrokeColor(LINE)
    c.setLineWidth(0.5)
    c.line(25*mm, y, W - 25*mm, y)
    y -= 6.5*mm

y -= 4*mm

# ---- How to pay ----
c.setFillColor(DARK)
c.setFont("Helvetica-Bold", 13)
c.drawString(25*mm, y, "How to Pay")
y -= 4*mm
c.setStrokeColor(GOLD)
c.setLineWidth(1.5)
c.line(25*mm, y, 38*mm, y)
y -= 10*mm

steps = [
    "Open your bank's app or online banking, or visit your branch.",
    "Choose \"International transfer\" or \"Send money abroad\".",
    "Enter the beneficiary name, IBAN and BIC/SWIFT code exactly as shown above.",
    "Send GBP 350.00 and add \"Casa Nova Website\" as the reference.",
    "Confirm and complete the transfer.",
]
c.setFont("Helvetica", 10.5)
for i, step in enumerate(steps, 1):
    c.setFillColor(GOLD)
    c.setFont("Helvetica-Bold", 11)
    c.drawString(25*mm, y, f"{i}.")
    c.setFillColor(GREY)
    c.setFont("Helvetica", 10.5)
    c.drawString(32*mm, y, step)
    y -= 7.5*mm

# ---- Notes box (fixed position near bottom) ----
note_h = 30*mm
box_top = 50*mm                 # top edge of box, fixed
c.setFillColor(LIGHT)
c.roundRect(25*mm, box_top - note_h, W - 50*mm, note_h, 3*mm, fill=1, stroke=0)
c.setFillColor(DARK)
c.setFont("Helvetica-Bold", 10)
c.drawString(31*mm, box_top - 9*mm, "Good to know")
c.setFillColor(GREY)
c.setFont("Helvetica", 9.5)
notes = [
    "Transfers usually take 3 to 5 working days to arrive.",
    "Your bank may apply a small international transfer fee on your side.",
    "Please ensure the beneficiary name matches exactly to avoid delays.",
]
ny = box_top - 16*mm
for n in notes:
    c.drawString(31*mm, ny, "•  " + n)
    ny -= 5.5*mm

# ---- Footer (fixed, below the box) ----
c.setStrokeColor(LINE)
c.setLineWidth(0.5)
c.line(25*mm, 15*mm, W - 25*mm, 15*mm)
c.setFillColor(GREY)
c.setFont("Helvetica", 8.5)
c.drawCentredString(W/2, 10*mm, "Once payment is received you will be notified and the website handover will begin.")
c.setFillColor(GOLD)
c.setFont("Helvetica-Bold", 9)
c.drawCentredString(W/2, 5*mm, "Oakden Creative")

c.save()
print("Created CN_Payment_Instructions.pdf")
