from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import mm
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, HRFlowable, Table, TableStyle
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_RIGHT

W, H = A4
GREEN = colors.HexColor('#2D6A4F')
GREEN_L = colors.HexColor('#D8F3DC')
AMBER = colors.HexColor('#F4A261')
DARK = colors.HexColor('#0D1B0F')
GRAY = colors.HexColor('#6B7A6E')
WHITE = colors.white
CREAM = colors.HexColor('#FAFAF8')

def style(name, **kw):
    base = {
        'fontName': 'Helvetica',
        'fontSize': 10,
        'leading': 14,
        'textColor': DARK,
        'spaceAfter': 0,
        'spaceBefore': 0,
    }
    base.update(kw)
    return ParagraphStyle(name, **base)

S_LABEL   = style('label', fontSize=8, fontName='Helvetica-Bold', textColor=GREEN, leading=10, spaceAfter=2)
S_H1      = style('h1', fontSize=26, fontName='Helvetica-Bold', leading=30, textColor=WHITE, spaceAfter=4)
S_H2      = style('h2', fontSize=17, fontName='Helvetica-Bold', leading=22, textColor=DARK, spaceAfter=6)
S_H3      = style('h3', fontSize=12, fontName='Helvetica-Bold', leading=16, textColor=DARK, spaceAfter=4)
S_BODY    = style('body', fontSize=10, leading=15, textColor=colors.HexColor('#374840'), spaceAfter=0)
S_SMALL   = style('small', fontSize=8.5, leading=13, textColor=GRAY)
S_PRICE   = style('price', fontSize=22, fontName='Helvetica-Bold', textColor=DARK, leading=26)
S_WHITE   = style('white', fontSize=10, textColor=WHITE, leading=14)
S_CENTER  = style('center', alignment=TA_CENTER, fontSize=9, textColor=GRAY)
S_TAG     = style('tag', fontSize=8.5, fontName='Helvetica-Bold', textColor=GREEN, leading=11)

doc = SimpleDocTemplate(
    'jungle-lodge-3days.pdf',
    pagesize=A4,
    leftMargin=18*mm, rightMargin=18*mm,
    topMargin=14*mm, bottomMargin=14*mm,
    title='Amazon Jungle Lodge — 3-Day Expedition',
    author='Amazon Eco Travellers',
)

story = []

# ── HERO BANNER ──────────────────────────────────────────────────────────────
hero_data = [[
    Paragraph('AMAZON ECO TRAVELLERS', style('logo', fontSize=8, fontName='Helvetica-Bold', textColor=colors.HexColor('#A8D5B5'), leading=10)),
    Paragraph('amazonecotravellers.com', style('url', fontSize=8, textColor=colors.HexColor('#A8D5B5'), alignment=TA_RIGHT, leading=10)),
]]
hero_top = Table(hero_data, colWidths=[85*mm, 85*mm])
hero_top.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,-1), GREEN),
    ('TOPPADDING', (0,0), (-1,-1), 6),
    ('BOTTOMPADDING', (0,0), (-1,-1), 6),
    ('LEFTPADDING', (0,0), (0,-1), 10),
    ('RIGHTPADDING', (-1,0), (-1,-1), 10),
    ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
]))
story.append(hero_top)

hero_title_data = [[
    Paragraph('3 DAYS · 2 NIGHTS  ·  LODGE IN THE AMAZON', style('badge', fontSize=8, fontName='Helvetica-Bold', textColor=AMBER, leading=10)),
]]
ht = Table(hero_title_data, colWidths=[170*mm])
ht.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,-1), DARK),
    ('TOPPADDING', (0,0), (-1,-1), 12),
    ('BOTTOMPADDING', (0,0), (-1,-1), 4),
    ('LEFTPADDING', (0,0), (-1,-1), 10),
]))
story.append(ht)

hero_main_data = [[
    Paragraph('Amazon Jungle<br/>Lodge Expedition', style('heroH', fontSize=28, fontName='Helvetica-Bold', textColor=WHITE, leading=32)),
]]
hm = Table(hero_main_data, colWidths=[170*mm])
hm.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,-1), DARK),
    ('TOPPADDING', (0,0), (-1,-1), 4),
    ('BOTTOMPADDING', (0,0), (-1,-1), 10),
    ('LEFTPADDING', (0,0), (-1,-1), 10),
]))
story.append(hm)

hero_sub_data = [[
    Paragraph('Two nights in the heart of the Amazon — Meeting of the Waters, pink river dolphins, piranha fishing, night caiman search, guided jungle trails, and a riverside community. Fully guided, full board, departing from Manaus.', S_WHITE),
]]
hs = Table(hero_sub_data, colWidths=[170*mm])
hs.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#1A3020')),
    ('TOPPADDING', (0,0), (-1,-1), 8),
    ('BOTTOMPADDING', (0,0), (-1,-1), 12),
    ('LEFTPADDING', (0,0), (-1,-1), 10),
    ('RIGHTPADDING', (0,0), (-1,-1), 10),
]))
story.append(hs)
story.append(Spacer(1, 6*mm))

# ── STATS STRIP ───────────────────────────────────────────────────────────────
stats = [
    ['DURATION', 'DEPARTURE', 'LEVEL', 'MEALS'],
    ['3 Days / 2 Nights', 'Manaus, AM, Brazil', 'Easy to Moderate', 'Full Board Included'],
]
st = Table(stats, colWidths=[42.5*mm]*4)
st.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#F0F7F2')),
    ('BACKGROUND', (0,1), (-1,1), WHITE),
    ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
    ('FONTSIZE', (0,0), (-1,0), 7),
    ('TEXTCOLOR', (0,0), (-1,0), GREEN),
    ('FONTNAME', (0,1), (-1,1), 'Helvetica-Bold'),
    ('FONTSIZE', (0,1), (-1,1), 9),
    ('TEXTCOLOR', (0,1), (-1,1), DARK),
    ('ALIGN', (0,0), (-1,-1), 'CENTER'),
    ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
    ('TOPPADDING', (0,0), (-1,-1), 7),
    ('BOTTOMPADDING', (0,0), (-1,-1), 7),
    ('LINEBELOW', (0,0), (-1,-1), 0.5, colors.HexColor('#D0E8D8')),
    ('LINEAFTER', (0,0), (-2,-1), 0.5, colors.HexColor('#D0E8D8')),
    ('BOX', (0,0), (-1,-1), 0.5, colors.HexColor('#C8E0CE')),
]))
story.append(st)
story.append(Spacer(1, 6*mm))

# ── HIGHLIGHTS GRID ───────────────────────────────────────────────────────────
story.append(Paragraph('HIGHLIGHTS', S_LABEL))
story.append(Spacer(1, 2*mm))

hl_items = [
    ['Meeting of the Waters', 'Pink River Dolphins', 'Lodge in the Forest', 'Night Caiman Search'],
    ['Guided Jungle Walk', 'Piranha Fishing', 'Riverside Community', 'Full Board Meals'],
]
hl = Table(hl_items, colWidths=[42.5*mm]*4)
hl.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,-1), GREEN_L),
    ('FONTNAME', (0,0), (-1,-1), 'Helvetica-Bold'),
    ('FONTSIZE', (0,0), (-1,-1), 8.5),
    ('TEXTCOLOR', (0,0), (-1,-1), colors.HexColor('#1B4332')),
    ('ALIGN', (0,0), (-1,-1), 'CENTER'),
    ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
    ('TOPPADDING', (0,0), (-1,-1), 7),
    ('BOTTOMPADDING', (0,0), (-1,-1), 7),
    ('LINEAFTER', (0,0), (-2,-1), 0.5, WHITE),
    ('LINEBELOW', (0,0), (-1,0), 0.5, WHITE),
    ('ROUNDEDCORNERS', [4, 4, 4, 4]),
]))
story.append(hl)
story.append(Spacer(1, 6*mm))

# ── ITINERARY ─────────────────────────────────────────────────────────────────
story.append(HRFlowable(width='100%', thickness=0.5, color=colors.HexColor('#C8E0CE')))
story.append(Spacer(1, 4*mm))
story.append(Paragraph('ITINERARY', S_LABEL))
story.append(Spacer(1, 2*mm))

def day_block(day_num, label, title, desc, tags):
    num_cell = Table([[Paragraph(day_num, style('dn', fontSize=14, fontName='Helvetica-Bold', textColor=GREEN, alignment=TA_CENTER, leading=16))]],
                     colWidths=[14*mm], rowHeights=[14*mm])
    num_cell.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), GREEN_L),
        ('ALIGN', (0,0), (-1,-1), 'CENTER'),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('ROUNDEDCORNERS', [7,7,7,7]),
        ('BOX', (0,0), (-1,-1), 1, GREEN),
    ]))
    tag_str = '  ·  '.join(tags)
    content = [
        Paragraph(label.upper(), S_LABEL),
        Paragraph(title, S_H3),
        Spacer(1, 1*mm),
        Paragraph(desc, S_BODY),
        Spacer(1, 2*mm),
        Paragraph(tag_str, S_TAG),
    ]
    row = Table([[num_cell, content]], colWidths=[18*mm, 152*mm])
    row.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('TOPPADDING', (0,0), (-1,-1), 0),
        ('BOTTOMPADDING', (0,0), (-1,-1), 0),
        ('LEFTPADDING', (1,0), (1,-1), 6),
    ]))
    return row

story.append(day_block(
    '1', 'Day 1 — Arrival',
    'Meeting of the Waters, Pink Dolphins & Lodge Check-In',
    'Departure from your Manaus hotel. First stop: the Encontro das Aguas — where the dark Rio Negro meets the white-water Solimoes, running side by side for ~6 km without mixing. From there, visit the pink river dolphin habitat in the Rio Negro\'s dark waters. Afternoon: boat transfer to the jungle lodge, accessible only by river, in primary Amazon forest. Evening: night caiman search by spotlight along the river margins.',
    ['Meeting of the Waters', 'Pink Dolphins', 'Lodge Check-In', 'Night Caiman Search']
))
story.append(Spacer(1, 4*mm))

story.append(day_block(
    '2', 'Day 2 — Deep Forest',
    'Jungle Walk, Piranha Fishing & Riverside Community',
    'After breakfast, a native guide leads the group into primary Amazon forest — plant identification, animal tracking, and Amazonian ecology. Afternoon: piranha fishing from a canoe in the channels adjacent to the lodge. Late afternoon: visit to a riverside ribeirinho community whose architecture, diet, and rhythm are shaped entirely by the Amazon and the forest.',
    ['Guided Jungle Walk', 'Plant ID', 'Piranha Fishing', 'Riverside Community']
))
story.append(Spacer(1, 4*mm))

story.append(day_block(
    '★', 'Optional — Night 2',
    'Jungle Camping — Sleep Under the Canopy',
    'An optional upgrade: spend the second night camping in the jungle — hammocks strung between trees, a fire, and the full nocturnal soundscape of the rainforest. Discussed and confirmed at booking.',
    ['Jungle Hammock Camp', 'Optional Add-On', 'Amazon Night Sounds']
))
story.append(Spacer(1, 4*mm))

story.append(day_block(
    '3', 'Day 3 — Return',
    'Final Morning & Return to Manaus',
    'Unhurried breakfast at the lodge. Return by boat to Manaus following the same river network. Drop-off at your hotel or directly at the international airport, depending on your onward plans.',
    ['Lodge Breakfast', 'River Return', 'Hotel or Airport Drop-off']
))
story.append(Spacer(1, 6*mm))

# ── INCLUDED / EXCLUDED + GOOD TO KNOW ───────────────────────────────────────
story.append(HRFlowable(width='100%', thickness=0.5, color=colors.HexColor('#C8E0CE')))
story.append(Spacer(1, 4*mm))

inc_yes = [
    '✓  Airport <-> Manaus hotel transfer',
    '✓  All transport (boat + vehicle)',
    '✓  Lodge accommodation (2 nights)',
    '✓  Full board — breakfast, lunch & dinner',
    '✓  Bilingual guide + native naturalist',
    '✓  All described activities',
    '✓  Mineral water throughout',
]
inc_no = [
    '✗  Manaus hotel (nights before/after)',
    '✗  Alcoholic beverages',
    '✗  Tips & personal expenses',
    '✗  Travel insurance',
]
gtk = [
    'Guides speak EN, DE, PT & ES',
    'Light clothes, long trousers & closed footwear',
    'Insect repellent & sunscreen — essential',
    'Rain poncho — always pack one',
    'Swimwear for river stops',
    'Safety kit & first aid on every activity',
    'Eco-responsible — leave no trace policy',
]

def bullet_list(items, color=DARK, bold_first_char=False):
    parts = []
    for it in items:
        c = GREEN if it.startswith('✓') else colors.HexColor('#C0392B') if it.startswith('✗') else GRAY
        parts.append(Paragraph(it, style('li', fontSize=9, textColor=c, leading=13, spaceAfter=2)))
    return parts

inc_col = [Paragraph('WHAT\'S INCLUDED', S_LABEL), Spacer(1, 2*mm)] + \
          bullet_list(inc_yes) + [Spacer(1, 2*mm)] + bullet_list(inc_no)

gtk_col = [Paragraph('GOOD TO KNOW', S_LABEL), Spacer(1, 2*mm)] + \
          bullet_list(['  ' + g for g in gtk])

bottom_table = Table([[inc_col, gtk_col]], colWidths=[85*mm, 85*mm])
bottom_table.setStyle(TableStyle([
    ('VALIGN', (0,0), (-1,-1), 'TOP'),
    ('LEFTPADDING', (1,0), (1,-1), 8),
    ('LINEAFTER', (0,0), (0,-1), 0.5, colors.HexColor('#D0E8D8')),
    ('TOPPADDING', (0,0), (-1,-1), 0),
    ('BOTTOMPADDING', (0,0), (-1,-1), 0),
]))
story.append(bottom_table)
story.append(Spacer(1, 6*mm))

# ── PRICE + CTA ───────────────────────────────────────────────────────────────
story.append(HRFlowable(width='100%', thickness=0.5, color=colors.HexColor('#C8E0CE')))
story.append(Spacer(1, 4*mm))

price_data = [[
    [
        Paragraph('PRICING', S_LABEL),
        Spacer(1, 1*mm),
        Paragraph('R$ 1.500 / per person', S_PRICE),
        Paragraph('Private room (en-suite + AC) · min. 2 guests', S_SMALL),
        Paragraph('R$ 1.900 / single occupancy', style('so', fontSize=11, fontName='Helvetica-Bold', textColor=DARK, leading=14)),
        Spacer(1, 1*mm),
        Paragraph('Spots are limited — contact us for open dates', style('note', fontSize=8.5, textColor=GRAY, leading=12)),
    ],
    [
        Paragraph('BOOK NOW', S_LABEL),
        Spacer(1, 2*mm),
        Paragraph('WhatsApp: +55 92 99132-1047', style('cta1', fontSize=11, fontName='Helvetica-Bold', textColor=colors.HexColor('#1dbb58'), leading=14)),
        Spacer(1, 1*mm),
        Paragraph('wa.me/5592991321047', style('cta2', fontSize=9, textColor=GRAY, leading=12)),
        Spacer(1, 3*mm),
        Paragraph('Email: info@amazonecotravellers.com', style('cta3', fontSize=9, textColor=GREEN, leading=12)),
        Spacer(1, 3*mm),
        Paragraph('No commitment required. We reply within 24 hours.', style('cta4', fontSize=8, textColor=GRAY, leading=11)),
    ],
]]
pt = Table(price_data, colWidths=[95*mm, 75*mm])
pt.setStyle(TableStyle([
    ('VALIGN', (0,0), (-1,-1), 'TOP'),
    ('BACKGROUND', (0,0), (0,-1), colors.HexColor('#F0F7F2')),
    ('BACKGROUND', (1,0), (1,-1), DARK),
    ('LEFTPADDING', (0,0), (-1,-1), 10),
    ('RIGHTPADDING', (0,0), (-1,-1), 10),
    ('TOPPADDING', (0,0), (-1,-1), 10),
    ('BOTTOMPADDING', (0,0), (-1,-1), 10),
    ('ROUNDEDCORNERS', [6,6,6,6]),
]))

# Recolor BOOK NOW label in dark bg
price_data[0][1][0] = Paragraph('BOOK NOW', style('label_w', fontSize=8, fontName='Helvetica-Bold', textColor=AMBER, leading=10))
price_data[0][1][2] = Paragraph('WhatsApp: +55 92 99132-1047', style('cta1w', fontSize=11, fontName='Helvetica-Bold', textColor=colors.HexColor('#25D366'), leading=14))
price_data[0][1][4] = Paragraph('wa.me/5592991321047', style('cta2w', fontSize=9, textColor=colors.HexColor('#A8D5B5'), leading=12))
price_data[0][1][6] = Paragraph('Email: info@amazonecotravellers.com', style('cta3w', fontSize=9, textColor=colors.HexColor('#A8D5B5'), leading=12))
price_data[0][1][8] = Paragraph('No commitment required. We reply within 24 hours.', style('cta4w', fontSize=8, textColor=colors.HexColor('#6B9C7A'), leading=11))

story.append(pt)
story.append(Spacer(1, 4*mm))

# ── FOOTER ────────────────────────────────────────────────────────────────────
foot_data = [[
    Paragraph('Amazon Eco Travellers · Manaus, Amazonas, Brazil', S_CENTER),
    Paragraph('amazonecotravellers.com · +55 92 99132-1047', S_CENTER),
]]
ft = Table(foot_data, colWidths=[85*mm, 85*mm])
ft.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#F0F7F2')),
    ('TOPPADDING', (0,0), (-1,-1), 6),
    ('BOTTOMPADDING', (0,0), (-1,-1), 6),
    ('LINEABOVE', (0,0), (-1,0), 0.5, colors.HexColor('#C8E0CE')),
]))
story.append(ft)

doc.build(story)
print('PDF gerado: jungle-lodge-3days.pdf')
