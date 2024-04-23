from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.utils import simpleSplit
from datetime import datetime 

def generate_pdf(comments, total_comments, youtube_title):
   
    pdf = SimpleDocTemplate("output.pdf", pagesize=letter)
    elements = []

    styles = getSampleStyleSheet()
    title_style = styles["Title"]
    normal_style = styles["Normal"]
    heading3_style = styles["Heading3"]

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    timestamp_style = ParagraphStyle(name='TimestampStyle', fontSize=10, alignment=2) 
    
    elements.append(Paragraph(f"Report generated on: {timestamp}", timestamp_style))
    elements.append(Paragraph(f"{youtube_title}", title_style))
    elements.append(Paragraph(f"Total Comments Analyzed: {total_comments}", heading3_style))
   
    header = ["Comment", "Prediction", "Accuracy"]
    data = [header] 

    for comment, prediction, accuracy in comments:
        wrapped_comment = "\n".join(simpleSplit(comment, normal_style.fontName, normal_style.fontSize, 300))
        data.append([Paragraph(wrapped_comment, normal_style), prediction, f"{accuracy:.2f}%"])
   
    table = Table(data, repeatRows=1)   

    style = TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), (0.7, 0.7, 0.7)), 
        ('TEXTCOLOR', (0, 0), (-1, 0), (1, 1, 1)), 
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'), 
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'), 
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12), 
        ('BACKGROUND', (0, 1), (-1, -1), (0.9, 0.9, 0.9)), 
        ('GRID', (0, 0), (-1, -1), 1, (0, 0, 0)), 
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'), 
        ('LINEBELOW', (0, 0), (-1, -1), 1, colors.black), 
        ('TOPPADDING', (0, 0), (-1, -1), 6), 
        ('BOTTOMPADDING', (0, 0), (-1, -1), 6), 
        ('LEFTPADDING', (0, 0), (-1, -1), 6), 
        ('RIGHTPADDING', (0, 0), (-1, -1), 6), 
        ('FONTNAME', (0, 0), (-1, -1), 'Helvetica'), 
        ('TEXTCOLOR', (0, 0), (-1, -1), colors.black), 
    ])

    table.setStyle(style)
    elements.append(table)   
    pdf.build(elements)
