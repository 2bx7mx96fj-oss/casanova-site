from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.pdfgen import canvas
from reportlab.lib import colors

W, H = A4

# ── Colours ────────────────────────────────────────────────────────────────
DARK   = colors.HexColor('#0d0d0d')
GOLD   = colors.HexColor('#c9a96e')
WHITE  = colors.HexColor('#ffffff')
LIGHT  = colors.HexColor('#f0ece4')
MUTED  = colors.HexColor('#888880')
DIM    = colors.HexColor('#555550')
DIVIDER= colors.HexColor('#2a2a2a')
ACCENT = colors.HexColor('#1a1a1a')

def base(c, page, total, title_text):
    c.setFillColor(DARK)
    c.rect(0, 0, W, H, fill=1, stroke=0)
    c.setFillColor(GOLD)
    c.rect(0, H-3*mm, W, 3*mm, fill=1, stroke=0)
    c.rect(0, 0, 2.5*mm, H, fill=1, stroke=0)
    c.setStrokeColor(DIVIDER)
    c.setLineWidth(0.5)
    c.line(20*mm, 14*mm, W-20*mm, 14*mm)
    c.setFont('Helvetica', 7)
    c.setFillColor(MUTED)
    c.drawString(20*mm, 9*mm, title_text)
    c.drawRightString(W-20*mm, 9*mm, f'Page {page} of {total}')

def gold_tag(c, x, y, text):
    c.setFont('Helvetica-Bold', 7)
    c.setFillColor(GOLD)
    c.drawString(x, y, text.upper())

def h1(c, x, y, text):
    c.setFont('Helvetica-Bold', 22)
    c.setFillColor(WHITE)
    c.drawString(x, y, text)

def h2(c, x, y, text):
    c.setFont('Helvetica-Bold', 13)
    c.setFillColor(WHITE)
    c.drawString(x, y, text)

def body(c, x, y, text, size=9, col=None):
    if col is None: col = colors.HexColor('#b0aca6')
    c.setFont('Helvetica', size)
    c.setFillColor(col)
    c.drawString(x, y, text)
    return y - size*1.8

def wrap(c, x, y, text, size=9, max_w=150*mm, col=None):
    if col is None: col = colors.HexColor('#b0aca6')
    c.setFont('Helvetica', size)
    c.setFillColor(col)
    words = text.split()
    line = ''
    for word in words:
        test = (line+' '+word).strip()
        if c.stringWidth(test,'Helvetica',size) > max_w:
            c.drawString(x, y, line)
            y -= size*1.75
            line = word
        else:
            line = test
    if line:
        c.drawString(x, y, line)
        y -= size*1.75
    return y

def step_row(c, y, num, title, detail, x=20*mm):
    # number circle bg
    c.setFillColor(colors.HexColor('#1a1a1a'))
    c.rect(x, y-3*mm, 8*mm, 8*mm, fill=1, stroke=0)
    c.setFont('Helvetica-Bold', 9)
    c.setFillColor(GOLD)
    c.drawCentredString(x+4*mm, y+0.5*mm, str(num))
    # title
    c.setFont('Helvetica-Bold', 10)
    c.setFillColor(WHITE)
    c.drawString(x+12*mm, y+1*mm, title)
    # detail
    y2 = wrap(c, x+12*mm, y-6*mm, detail, size=8.5, max_w=155*mm)
    return y2 - 5*mm

def divline(c, y):
    c.setStrokeColor(DIVIDER)
    c.setLineWidth(0.5)
    c.line(20*mm, y, W-20*mm, y)
    return y - 7*mm

# ══════════════════════════════════════════════════════════════════════════════
# DOC 1 — HANDOVER
# ══════════════════════════════════════════════════════════════════════════════
c = canvas.Canvas('/Users/alexmcmillan/casanova-site/CN_Handover.pdf', pagesize=A4)
c.setTitle('Casa Nova — Website Handover')

# Page 1 — Cover
base(c, 1, 2, 'Casa Nova Global Sourcing Interiors — Website Handover Document')
gold_tag(c, 20*mm, H-28*mm, 'Casa Nova Global Sourcing Interiors')
c.setFont('Helvetica-Bold', 38); c.setFillColor(WHITE)
c.drawString(20*mm, H-52*mm, 'Website')
c.drawString(20*mm, H-68*mm, 'Handover')
c.setFont('Helvetica', 38); c.setFillColor(GOLD)
c.drawString(20*mm, H-84*mm, 'Document.')
c.setStrokeColor(GOLD); c.setLineWidth(1)
c.line(20*mm, H-96*mm, 80*mm, H-96*mm)
c.setFont('Helvetica', 9.5); c.setFillColor(MUTED)
c.drawString(20*mm, H-108*mm, 'Step-by-step guide to transferring full ownership of the Casa Nova website.')
c.drawString(20*mm, H-119*mm, 'To be completed upon receipt of payment.')

# Info box
c.setFillColor(colors.HexColor('#111111'))
c.roundRect(20*mm, H-200*mm, 170*mm, 60*mm, 2, fill=1, stroke=0)
gold_tag(c, 28*mm, H-152*mm, 'Prepared For')
c.setFont('Helvetica-Bold', 12); c.setFillColor(WHITE)
c.drawString(28*mm, H-161*mm, 'Esther Nyambura Ngumi')
c.setFont('Helvetica', 9); c.setFillColor(MUTED)
c.drawString(28*mm, H-169*mm, 'Casa Nova Global Sourcing Interiors  ·  Karen, Nairobi, Kenya')
c.setStrokeColor(DIVIDER); c.setLineWidth(0.5)
c.line(28*mm, H-174*mm, 182*mm, H-174*mm)
gold_tag(c, 28*mm, H-181*mm, 'Live Website')
c.setFont('Helvetica', 9); c.setFillColor(MUTED)
c.drawString(28*mm, H-189*mm, 'https://2bx7mx96fj-oss.github.io/casanova-site/')

gold_tag(c, 20*mm, H-218*mm, 'Important')
c.setFont('Helvetica', 9); c.setFillColor(colors.HexColor('#b0aca6'))
c.drawString(20*mm, H-226*mm, 'Do not begin any transfer steps until payment has been confirmed in full.')
c.drawString(20*mm, H-235*mm, 'Once transferred, the website and all associated assets belong to the client.')

c.showPage()

# Page 2 — Steps
base(c, 2, 2, 'Casa Nova Global Sourcing Interiors — Website Handover Document')
gold_tag(c, 20*mm, H-25*mm, 'Step-by-Step Handover Process')
c.setFont('Helvetica-Bold', 18); c.setFillColor(WHITE)
c.drawString(20*mm, H-37*mm, 'Transferring Ownership')

y = H-58*mm

y = step_row(c, y, 1, 'Confirm Payment',
    'Ensure £350 has cleared in full to your bank account before proceeding. Do not begin transfer until funds are confirmed.')
y = divline(c, y)
y = step_row(c, y, 2, 'Esther Creates a GitHub Account',
    'Go to github.com and click Sign Up. Use a professional email. Recommended username: casanovaglobal or casanovainteriors. Complete email verification (takes 2 minutes). Share your username with the developer.')
y = divline(c, y)
y = step_row(c, y, 3, 'Esther Creates a Namecheap Account & Buys Domain',
    'Go to namecheap.com, create an account, and search for your preferred domain (e.g. casanovaglobal.com or casanovainteriors.co.ke). Purchase on your own card — this is your asset.')
y = divline(c, y)
y = step_row(c, y, 4, 'Connect Domain to Website (DNS Setup)',
    'In Namecheap: Domain List > Manage > Advanced DNS. Add 4 A Records pointing @ to: 185.199.108.153 / 185.199.109.153 / 185.199.110.153 / 185.199.111.153. Add CNAME: www pointing to 2bx7mx96fj-oss.github.io.')
y = divline(c, y)
y = step_row(c, y, 5, 'Set Custom Domain on GitHub',
    'In the GitHub repository: Settings > Pages > Custom Domain. Enter your domain and save. Tick Enforce HTTPS once available. DNS propagation takes 10–30 minutes.')
y = divline(c, y)
y = step_row(c, y, 6, 'Transfer GitHub Repository',
    'Developer goes to: github.com/2bx7mx96fj-oss/casanova-site > Settings > scroll to Danger Zone > Transfer. Enter repository name to confirm, then enter your GitHub username. You will receive an email — click Accept Transfer within 24 hours.')
y = divline(c, y)
y = step_row(c, y, 7, 'Confirm Everything is Working',
    'Visit your custom domain in a browser. Confirm the site loads correctly. Confirm HTTPS padlock is visible. The website is now fully yours.')

c.save()
print('Saved: CN_Handover.pdf')


# ══════════════════════════════════════════════════════════════════════════════
# DOC 2 — INVOICE
# ══════════════════════════════════════════════════════════════════════════════
c = canvas.Canvas('/Users/alexmcmillan/casanova-site/CN_Invoice.pdf', pagesize=A4)
c.setTitle('Invoice — Casa Nova Website')

base(c, 1, 1, 'Invoice — Confidential')

# Header
gold_tag(c, 20*mm, H-28*mm, 'Invoice')
c.setFont('Helvetica-Bold', 34); c.setFillColor(WHITE)
c.drawString(20*mm, H-48*mm, 'INV-001')
c.setFont('Helvetica', 10); c.setFillColor(MUTED)
c.drawString(20*mm, H-59*mm, 'Date: 23 June 2026')
c.drawString(20*mm, H-69*mm, 'Due: Within 7 days (by 30 June 2026)')

# From / To boxes
c.setFillColor(colors.HexColor('#111111'))
c.roundRect(20*mm, H-140*mm, 78*mm, 55*mm, 2, fill=1, stroke=0)
c.roundRect(102*mm, H-140*mm, 88*mm, 55*mm, 2, fill=1, stroke=0)

gold_tag(c, 27*mm, H-95*mm, 'From')
c.setFont('Helvetica-Bold', 10); c.setFillColor(WHITE)
c.drawString(27*mm, H-104*mm, 'Alex McMillan')
c.setFont('Helvetica', 8.5); c.setFillColor(MUTED)
c.drawString(27*mm, H-112*mm, 'Web Design & Development')
c.drawString(27*mm, H-120*mm, 'mcmillan_alex@icloud.com')

gold_tag(c, 109*mm, H-95*mm, 'Bill To')
c.setFont('Helvetica-Bold', 10); c.setFillColor(WHITE)
c.drawString(109*mm, H-104*mm, 'Esther Nyambura Ngumi')
c.setFont('Helvetica', 8.5); c.setFillColor(MUTED)
c.drawString(109*mm, H-112*mm, 'Casa Nova Global Sourcing Interiors')
c.drawString(109*mm, H-120*mm, 'Karen, Nairobi, Kenya')
c.drawString(109*mm, H-128*mm, 'casanovaglobalsourcingltd@gmail.com')

# Line items header
y = H - 160*mm
c.setFillColor(colors.HexColor('#1a1a1a'))
c.rect(20*mm, y, 170*mm, 9*mm, fill=1, stroke=0)
c.setFont('Helvetica-Bold', 8); c.setFillColor(GOLD)
c.drawString(25*mm, y+2.5*mm, 'DESCRIPTION')
c.drawRightString(W-20*mm, y+2.5*mm, 'AMOUNT')

# Items
y -= 12*mm
items = [
    ('Website Design & Development — One-Time Fee',
     'Complete premium website including: multi-page design (Home, About, Services,\nPortfolio, Mission, Founder, FAQs), video hero, contact form, chatbot widget,\nWhatsApp integration, mobile optimisation, and full deployment on GitHub Pages.',
     '£350.00'),
]

for title, desc, amount in items:
    c.setFont('Helvetica-Bold', 9.5); c.setFillColor(WHITE)
    c.drawString(25*mm, y, title)
    y -= 6*mm
    for line in desc.split('\n'):
        c.setFont('Helvetica', 8.5); c.setFillColor(MUTED)
        c.drawString(25*mm, y, line)
        y -= 5*mm
    c.setFont('Helvetica-Bold', 10); c.setFillColor(LIGHT)
    c.drawRightString(W-20*mm, y+5*mm, amount)
    c.setStrokeColor(DIVIDER); c.setLineWidth(0.5)
    y -= 4*mm
    c.line(20*mm, y, W-20*mm, y)
    y -= 8*mm

# Total box
y -= 4*mm
c.setFillColor(GOLD)
c.rect(20*mm, y-8*mm, 170*mm, 16*mm, fill=1, stroke=0)
c.setFont('Helvetica-Bold', 13); c.setFillColor(DARK)
c.drawString(25*mm, y-2*mm, 'TOTAL DUE')
c.drawRightString(W-25*mm, y-2*mm, '\xa3350.00')

# Payment details
y -= 28*mm
gold_tag(c, 20*mm, y, 'Payment Details')
y -= 8*mm
details = [
    ('Beneficiary',  'Alexander McMillan'),
    ('IBAN',         'GB37 REVO 2301 2071 1572 91'),
    ('BIC / SWIFT',  'REVOGB21'),
    ('Reference',    'Casa Nova Website'),
]
for label, val in details:
    c.setFont('Helvetica-Bold', 8.5); c.setFillColor(MUTED)
    c.drawString(20*mm, y, label)
    c.setFont('Helvetica', 8.5); c.setFillColor(WHITE)
    c.drawString(65*mm, y, val)
    y -= 6.5*mm

y -= 6*mm
c.setFont('Helvetica', 8); c.setFillColor(DIM)
c.drawString(20*mm, y, 'Payment is due within 7 days of this invoice (by 30 June 2026). Thank you for your business.')

c.save()
print('Saved: CN_Invoice.pdf')


# ══════════════════════════════════════════════════════════════════════════════
# DOC 3 — SERVICE AGREEMENT
# ══════════════════════════════════════════════════════════════════════════════
c = canvas.Canvas('/Users/alexmcmillan/casanova-site/CN_Agreement.pdf', pagesize=A4)
c.setTitle('Service Agreement — Casa Nova Website')

base(c, 1, 2, 'Service Agreement — Casa Nova Global Sourcing Interiors')

gold_tag(c, 20*mm, H-28*mm, 'Service Agreement')
c.setFont('Helvetica-Bold', 30); c.setFillColor(WHITE)
c.drawString(20*mm, H-46*mm, 'Website Design &')
c.drawString(20*mm, H-62*mm, 'Development')
c.setFont('Helvetica', 30); c.setFillColor(GOLD)
c.drawString(20*mm, H-78*mm, 'Agreement.')
c.setStrokeColor(GOLD); c.setLineWidth(1)
c.line(20*mm, H-88*mm, 80*mm, H-88*mm)

# Parties box
c.setFillColor(colors.HexColor('#111111'))
c.roundRect(20*mm, H-168*mm, 170*mm, 65*mm, 2, fill=1, stroke=0)
gold_tag(c, 28*mm, H-100*mm, 'Parties to This Agreement')
c.setFont('Helvetica-Bold', 9); c.setFillColor(WHITE)
c.drawString(28*mm, H-110*mm, 'Service Provider:')
c.setFont('Helvetica', 9); c.setFillColor(MUTED)
c.drawString(80*mm, H-110*mm, 'Alex McMillan  |  mcmillan_alex@icloud.com')
c.setFont('Helvetica-Bold', 9); c.setFillColor(WHITE)
c.drawString(28*mm, H-121*mm, 'Client:')
c.setFont('Helvetica', 9); c.setFillColor(MUTED)
c.drawString(80*mm, H-121*mm, 'Esther Nyambura Ngumi  |  Casa Nova Global Sourcing Interiors')
c.setFont('Helvetica-Bold', 9); c.setFillColor(WHITE)
c.drawString(28*mm, H-132*mm, 'Date:')
c.setFont('Helvetica', 9); c.setFillColor(MUTED)
c.drawString(80*mm, H-132*mm, '23 June 2026')
c.setFont('Helvetica-Bold', 9); c.setFillColor(WHITE)
c.drawString(28*mm, H-143*mm, 'Project:')
c.setFont('Helvetica', 9); c.setFillColor(MUTED)
c.drawString(80*mm, H-143*mm, 'Casa Nova Interiors — Full Website Design & Development')
c.setFont('Helvetica-Bold', 9); c.setFillColor(WHITE)
c.drawString(28*mm, H-154*mm, 'Total Fee:')
c.setFont('Helvetica', 9); c.setFillColor(GOLD)
c.drawString(80*mm, H-154*mm, '\xa3350.00 GBP — One-time payment')

# Clauses
y = H-182*mm
clauses = [
    ('1. Scope of Work',
     'The Service Provider agrees to design, develop and deliver a fully functional multi-page website for the Client. Deliverables include: homepage, services page, portfolio page, about page, mission page, founder page and FAQ page. Additional features include a custom chatbot widget, WhatsApp integration, contact form, and full mobile responsiveness across all devices.'),
    ('2. Payment Terms',
     'The total fee of \xa3350.00 (three hundred and fifty pounds sterling) is payable in full upon agreement of this contract. Payment is to be made via bank transfer to the details provided on the accompanying invoice (INV-001). Work and asset transfer will be completed upon receipt of cleared funds.'),
    ('3. Ownership & Intellectual Property',
     'Upon receipt of full payment, the Client shall own all rights to the website, its design, content and code. The Service Provider will transfer the GitHub repository to the Client\'s GitHub account and assist with domain setup. The Service Provider retains the right to reference the project in their portfolio unless otherwise agreed in writing.'),
    ('4. Domain & Hosting',
     'The website is hosted on GitHub Pages at no ongoing cost to the Client. The Client is responsible for purchasing and maintaining their own domain name. The Service Provider will assist in connecting the domain to the website during the handover session at no additional charge.'),
    ('5. Revisions',
     'This agreement covers the website as delivered. Any additional pages, features or significant design changes requested after delivery are not included and will be quoted separately. Minor corrections identified within 7 days of delivery will be addressed at no extra charge.'),
    ('6. Limitation of Liability',
     'The Service Provider shall not be liable for any loss of business, data or revenue arising from use of the website. The Client accepts the website is delivered as a static site hosted on a third-party platform (GitHub Pages) and agrees to the terms of that platform independently.'),
    ('7. Governing Law',
     'This agreement shall be governed by the laws of England and Wales. Any disputes shall first be addressed through direct negotiation between the parties.'),
]

for title, text in clauses:
    if y < 40*mm:
        c.showPage()
        base(c, 2, 2, 'Service Agreement — Casa Nova Global Sourcing Interiors')
        y = H - 30*mm
    c.setFont('Helvetica-Bold', 9.5); c.setFillColor(WHITE)
    c.drawString(20*mm, y, title)
    y -= 6*mm
    y = wrap(c, 20*mm, y, text, size=8.5, max_w=170*mm)
    y -= 5*mm

# Signatures
if y < 70*mm:
    c.showPage()
    base(c, 2, 2, 'Service Agreement — Casa Nova Global Sourcing Interiors')
    y = H - 30*mm

y -= 5*mm
c.setStrokeColor(DIVIDER); c.setLineWidth(0.5)
c.line(20*mm, y, W-20*mm, y)
y -= 12*mm
gold_tag(c, 20*mm, y, 'Signatures')
y -= 14*mm

# Sig boxes
c.setFillColor(colors.HexColor('#111111'))
c.roundRect(20*mm, y-22*mm, 78*mm, 28*mm, 2, fill=1, stroke=0)
c.roundRect(102*mm, y-22*mm, 88*mm, 28*mm, 2, fill=1, stroke=0)

c.setFont('Helvetica-Bold', 8); c.setFillColor(WHITE)
c.drawString(25*mm, y-4*mm, 'Service Provider')
c.setFont('Helvetica', 8); c.setFillColor(MUTED)
c.drawString(25*mm, y-10*mm, 'Alex McMillan')
c.setStrokeColor(DIM); c.setLineWidth(0.5)
c.line(25*mm, y-17*mm, 92*mm, y-17*mm)
c.setFont('Helvetica', 7); c.setFillColor(DIM)
c.drawString(25*mm, y-21*mm, 'Signature & Date')

c.setFont('Helvetica-Bold', 8); c.setFillColor(WHITE)
c.drawString(107*mm, y-4*mm, 'Client')
c.setFont('Helvetica', 8); c.setFillColor(MUTED)
c.drawString(107*mm, y-10*mm, 'Esther Nyambura Ngumi')
c.setStrokeColor(DIM); c.setLineWidth(0.5)
c.line(107*mm, y-17*mm, 184*mm, y-17*mm)
c.setFont('Helvetica', 7); c.setFillColor(DIM)
c.drawString(107*mm, y-21*mm, 'Signature & Date')

c.save()
print('Saved: CN_Agreement.pdf')
print('\nAll 3 documents generated.')
