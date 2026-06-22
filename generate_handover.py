from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.pdfgen import canvas
from reportlab.lib import colors

W, H = A4

GOLD = colors.HexColor('#c9a96e')
DARK = colors.HexColor('#0d0d0d')
WHITE = colors.HexColor('#ffffff')
LIGHT = colors.HexColor('#f0ece4')
MUTED = colors.HexColor('#888880')
DIVIDER = colors.HexColor('#2a2a2a')

def draw_page(c, page_num, total):
    # Background
    c.setFillColor(DARK)
    c.rect(0, 0, W, H, fill=1, stroke=0)
    # Footer line
    c.setStrokeColor(DIVIDER)
    c.setLineWidth(0.5)
    c.line(20*mm, 14*mm, W - 20*mm, 14*mm)
    # Footer text
    c.setFont('Helvetica', 7)
    c.setFillColor(MUTED)
    c.drawString(20*mm, 9*mm, 'Casa Nova Global Sourcing Interiors — Confidential Handover Document')
    c.drawRightString(W - 20*mm, 9*mm, f'Page {page_num} of {total}')

def gold_label(c, x, y, text):
    c.setFont('Helvetica-Bold', 7)
    c.setFillColor(GOLD)
    c.drawString(x, y, text.upper())

def heading(c, x, y, text, size=18):
    c.setFont('Helvetica-Bold', size)
    c.setFillColor(WHITE)
    c.drawString(x, y, text)

def body(c, x, y, text, size=9.5, color=None, max_width=None):
    if color is None:
        color = colors.HexColor('#b0aca6')
    c.setFont('Helvetica', size)
    c.setFillColor(color)
    if max_width:
        # word wrap
        words = text.split()
        line = ''
        line_y = y
        for word in words:
            test = line + (' ' if line else '') + word
            if c.stringWidth(test, 'Helvetica', size) > max_width:
                c.drawString(x, line_y, line)
                line_y -= size * 1.7
                line = word
            else:
                line = test
        if line:
            c.drawString(x, line_y, line)
        return line_y - size * 1.7
    else:
        c.drawString(x, y, text)
        return y - size * 1.7

def step_block(c, y, num, title, items, x=20*mm, w=170*mm):
    # Number + gold bar
    c.setFillColor(GOLD)
    c.setFont('Helvetica-Bold', 8)
    num_str = f'0{num}'
    c.drawString(x, y, num_str)
    c.setStrokeColor(GOLD)
    c.setLineWidth(0.5)
    c.line(x + 12*mm, y + 1.5, x + w, y + 1.5)

    y -= 7*mm
    c.setFont('Helvetica-Bold', 13)
    c.setFillColor(WHITE)
    c.drawString(x, y, title)

    y -= 6*mm
    for item in items:
        # bullet
        c.setFillColor(GOLD)
        c.circle(x + 2, y + 3, 1.5, fill=1, stroke=0)
        c.setFont('Helvetica', 9)
        c.setFillColor(colors.HexColor('#b0aca6'))
        # wrap text
        max_w = w - 8*mm
        tx = x + 7*mm
        words = item.split()
        line = ''
        first = True
        for word in words:
            test = line + (' ' if line else '') + word
            if c.stringWidth(test, 'Helvetica', 9) > max_w:
                c.drawString(tx, y, line)
                if first:
                    first = False
                y -= 5*mm
                line = word
            else:
                line = test
        if line:
            c.drawString(tx, y, line)
            y -= 5*mm

    return y - 6*mm

def divider(c, y):
    c.setStrokeColor(DIVIDER)
    c.setLineWidth(0.5)
    c.line(20*mm, y, W - 20*mm, y)
    return y - 8*mm

# ── BUILD PDF ──────────────────────────────────────────────────────────────────
c = canvas.Canvas('/Users/alexmcmillan/casanova-site/Casa_Nova_Handover.pdf', pagesize=A4)
c.setTitle('Casa Nova — Website Handover Document')

# ══════════════════════════════════════════════════════════════════════════════
# PAGE 1 — COVER
# ══════════════════════════════════════════════════════════════════════════════
draw_page(c, 1, 3)

# Gold accent bar top
c.setFillColor(GOLD)
c.rect(0, H - 3*mm, W, 3*mm, fill=1, stroke=0)

# Side gold stripe
c.rect(0, 0, 2.5*mm, H, fill=1, stroke=0)

# Casa Nova label
gold_label(c, 20*mm, H - 28*mm, 'Casa Nova Global Sourcing Interiors')

# Title
c.setFont('Helvetica-Bold', 36)
c.setFillColor(WHITE)
c.drawString(20*mm, H - 52*mm, 'Website')
c.drawString(20*mm, H - 68*mm, 'Handover')

c.setFont('Helvetica', 36)
c.setFillColor(GOLD)
c.drawString(20*mm, H - 84*mm, 'Document.')

# Divider
c.setStrokeColor(GOLD)
c.setLineWidth(1)
c.line(20*mm, H - 96*mm, 80*mm, H - 96*mm)

# Subtitle
c.setFont('Helvetica', 10)
c.setFillColor(colors.HexColor('#888880'))
c.drawString(20*mm, H - 108*mm, 'Step-by-step guide to transferring full ownership')
c.drawString(20*mm, H - 120*mm, 'of the Casa Nova website upon payment completion.')

# Info box
c.setFillColor(colors.HexColor('#111111'))
c.roundRect(20*mm, H - 195*mm, 170*mm, 55*mm, 2, fill=1, stroke=0)

c.setFont('Helvetica-Bold', 8)
c.setFillColor(GOLD)
c.drawString(28*mm, H - 148*mm, 'PREPARED FOR')
c.setFont('Helvetica', 11)
c.setFillColor(WHITE)
c.drawString(28*mm, H - 156*mm, 'Esther Nyambura Ngumi')
c.setFont('Helvetica', 9)
c.setFillColor(colors.HexColor('#888880'))
c.drawString(28*mm, H - 163*mm, 'Casa Nova Global Sourcing Interiors · Karen, Nairobi')

c.setStrokeColor(DIVIDER)
c.setLineWidth(0.5)
c.line(28*mm, H - 168*mm, 178*mm, H - 168*mm)

c.setFont('Helvetica-Bold', 8)
c.setFillColor(GOLD)
c.drawString(28*mm, H - 175*mm, 'WEBSITE')
c.setFont('Helvetica', 9)
c.setFillColor(colors.HexColor('#888880'))
c.drawString(28*mm, H - 182*mm, 'https://2bx7mx96fj-oss.github.io/casanova-site/')

# What's included note
c.setFont('Helvetica-Bold', 9)
c.setFillColor(WHITE)
c.drawString(20*mm, H - 215*mm, "What's covered in this document:")

items = [
    'Step 1 — Confirming payment',
    'Step 2 — Creating a GitHub account',
    'Step 3 — Transferring the website repository',
    'Step 4 — Setting up a custom domain (optional)',
    'Step 5 — Final handover checklist',
]
y = H - 226*mm
for item in items:
    c.setFillColor(GOLD)
    c.circle(23*mm, y + 3, 1.5, fill=1, stroke=0)
    c.setFont('Helvetica', 9)
    c.setFillColor(colors.HexColor('#b0aca6'))
    c.drawString(27*mm, y, item)
    y -= 6.5*mm

c.showPage()

# ══════════════════════════════════════════════════════════════════════════════
# PAGE 2 — STEPS 1–3
# ══════════════════════════════════════════════════════════════════════════════
draw_page(c, 2, 3)

gold_label(c, 20*mm, H - 22*mm, 'Handover Process')
c.setFont('Helvetica-Bold', 20)
c.setFillColor(WHITE)
c.drawString(20*mm, H - 34*mm, 'Steps 1 – 3')

y = H - 52*mm

y = step_block(c, y, 1, 'Confirm Payment Received', [
    'Agree the final invoice amount and send it to Esther before or during the review call.',
    'Request payment via bank transfer (preferred) or PayPal. Do not begin the transfer until funds are cleared.',
    'Once payment is confirmed in your account, proceed to Step 2.',
    'Keep a copy of the payment confirmation for your records.',
])

y = divider(c, y)

y = step_block(c, y, 2, 'Esther Creates a GitHub Account', [
    'Ask Esther to go to github.com and click "Sign up".',
    'She should use a professional email address (e.g. her business email).',
    'Recommended username: casanovaglobal or casanovainteriors.',
    'She completes email verification — this takes less than 2 minutes.',
    'She sends you her GitHub username once done.',
])

y = divider(c, y)

y = step_block(c, y, 3, 'Transfer the Website Repository', [
    'You go to: github.com/2bx7mx96fj-oss/casanova-site',
    'Click "Settings" (top menu of the repository).',
    'Scroll to the bottom — find the "Danger Zone" section.',
    'Click "Transfer" — type the repository name to confirm.',
    'Enter Esther\'s GitHub username as the new owner.',
    'Click "I understand, transfer this repository."',
    'Esther will receive an email — she must click "Accept Transfer" within 24 hours.',
    'Once accepted, the site is fully under her GitHub account.',
])

c.showPage()

# ══════════════════════════════════════════════════════════════════════════════
# PAGE 3 — STEPS 4–5 + CHECKLIST
# ══════════════════════════════════════════════════════════════════════════════
draw_page(c, 3, 3)

gold_label(c, 20*mm, H - 22*mm, 'Handover Process')
c.setFont('Helvetica-Bold', 20)
c.setFillColor(WHITE)
c.drawString(20*mm, H - 34*mm, 'Steps 4 – 5')

y = H - 52*mm

y = step_block(c, y, 4, 'Custom Domain (Optional but Recommended)', [
    'Currently the site lives on a free GitHub Pages URL. A custom domain (e.g. casanovaglobal.com) looks far more professional.',
    'Esther purchases a domain via Namecheap, GoDaddy, or Google Domains (~$12–15/year).',
    'In her GitHub repo: Settings → Pages → Custom Domain → enter the domain.',
    'In her domain registrar: add a CNAME record pointing to her GitHub Pages URL.',
    'GitHub will issue a free SSL certificate automatically (takes ~10 minutes).',
    'This step is optional — the site works without it.',
])

y = divider(c, y)

y = step_block(c, y, 5, 'Final Handover Checklist', [
    '[ ]  Payment confirmed in your account',
    '[ ]  Esther\'s GitHub account created and username received',
    '[ ]  Repository transferred and Esther has accepted',
    '[ ]  Confirm the live site still loads correctly after transfer',
    '[ ]  Share login credentials for any third-party tools (if applicable)',
    '[ ]  Walk Esther through how to update the contact number or text if needed',
    '[ ]  Agree on any post-launch support terms (e.g. 30-day minor fixes)',
])

y = divider(c, y)

# Note box
c.setFillColor(colors.HexColor('#0f0f0f'))
c.roundRect(20*mm, y - 28*mm, 170*mm, 24*mm, 2, fill=1, stroke=0)
c.setStrokeColor(GOLD)
c.setLineWidth(1)
c.line(20*mm, y - 4*mm, 20*mm, y - 28*mm)

c.setFont('Helvetica-Bold', 8)
c.setFillColor(GOLD)
c.drawString(25*mm, y - 10*mm, 'IMPORTANT NOTE')
c.setFont('Helvetica', 8.5)
c.setFillColor(colors.HexColor('#b0aca6'))
c.drawString(25*mm, y - 17*mm, 'Do not transfer the repository until payment has fully cleared. Once transferred,')
c.drawString(25*mm, y - 23*mm, 'you no longer control the site. Keep a local backup of all files before transferring.')

c.save()
print('PDF created: Casa_Nova_Handover.pdf')
