# List of Lists
dadoscabecalhos = [
    
    ['ID', 'TIPO', 'Histórico', 'R$ Compet', 'C. Custo', 'Doc.', 'Valor', 'Vcto', 'Pagto', 'F. Pagto.', 'Status', 'Saldo']
    
]

listatest = [
    
    ['€200/', '€100/Month', '€20/', '€50/', 'C. Custo', 'Doc.', 'Valor', 'Vcto', 'Pagto', 'F. Pagto.', 'Status', 'Saldo'],
    ['Free ', 'Free ', 'Free Domain', 'Free ', 'C. Custo', 'Doc.', 'Valor', 'Vcto', 'Pagto', 'F. Pagto.', 'Status', 'Saldo'],
    ['2GB ', '20GB ', 'Unlimited Email', 'Unlimi', 'C. Custo', 'Doc.', 'Valor', 'Vcto', 'Pagto', 'F. Pagto.', 'Status', 'Saldo']
]

for linh    in listatest:
    dadoscabecalhos.append(linh)

fileName = 'Relatório.pdf'
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.pagesizes import letter, landscape
from reportlab.lib.styles import getSampleStyleSheet
pdf = SimpleDocTemplate(
    fileName,
    pagesize=landscape(letter)

)

from reportlab.platypus import Table

#table2 = Table(listatest)
table = Table(dadoscabecalhos)

# add style
from reportlab.platypus import TableStyle
from reportlab.lib import colors

style = TableStyle([
    ('BACKGROUND', (0,0), (11,0), colors.silver),
    ('TEXTCOLOR',(0,0),(-1,0),colors.black),

    ('ALIGN',(0,0),(-1,-1),'CENTER'),

    ('FONTNAME', (0,0), (-1,0), 'Courier-Bold'),
    ('FONTSIZE', (0,0), (-1,0), 14),

    ('BOTTOMPADDING', (0,0), (-1,0), 12),

    ('BACKGROUND',(0,1),(-1,-1),colors.silver),
])
table.setStyle(style)
#table2.setStyle(style)

# 2) Alternate backgroud color
rowNumb = len(dadoscabecalhos)
for i in range(1, rowNumb):
    if i % 2 == 0:
        bc = colors.silver
    else:
        bc = colors.white
    
    ts = TableStyle(
        [('BACKGROUND', (0,i),(-1,i), bc)]
    )
    table.setStyle(ts)
    #table2.setStyle(ts)
    

# 3) Add borders
ts = TableStyle(
    [
    ('BOX',(0,0),(-1,-1),2,colors.black),

    ('LINEBEFORE',(2,1),(2,-1),2,colors.red),
    ('LINEABOVE',(0,2),(-1,2),2,colors.green),

    ('GRID',(0,0),(-1,-1),2,colors.black),
    ]
)
table.setStyle(ts)
#table2.setStyle(ts)



elems = []
styles = getSampleStyleSheet()
styleH = styles['Heading1']
elems.append(Paragraph("Meu cabeçalho",styleH))
elems.append(table)

#elems.append(table2)


pdf.build(elems)

import webbrowser
webbrowser.open('Relatório.pdf')