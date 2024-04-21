from fpdf import FPDF
from datetime import datetime

def generate_pdf(comments, total_comments, youtube_title):
    # Create instance of FPDF class
    pdf = FPDF()

    # Add a page
    pdf.add_page()

    # Set font for the PDF
    pdf.set_font("Arial", size=12)

    # Add creation timestamp
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    pdf.cell(200, 10, txt=f"Report generated on: {timestamp}", ln=True, align='C')

    # Add YouTube title
    pdf.cell(200, 10, txt=f"YouTube Title: {youtube_title}", ln=True, align='C')

    # Add total comments
    pdf.cell(200, 10, txt=f"Total Comments Analyzed: {total_comments}", ln=True, align='C')

    # Add a line break
    pdf.ln(10)

    # Add table for comments analysis
    col_widths = [90, 50, 50]
    header = ["Comment", "Prediction", "Accuracy"]
    
    # Add table headers
    for col, col_width in zip(header, col_widths):
        pdf.cell(col_width, 10, txt=col, ln=False, align='C')
    
    pdf.ln()

    # Add table content
    for comment, prediction, accuracy in comments:
        # Encode comment to UTF-8
        comment = comment.encode('latin-1', 'replace').decode('latin-1')
        lines = pdf.multi_cell(col_widths[0], 10, txt=comment)
        cell_height = pdf.font_size * len(lines) + 2  # Add 2 for padding
        pdf.cell(col_widths[0], cell_height, txt='', ln=False)  # Empty cell for comment
        pdf.cell(col_widths[1], cell_height, txt=prediction, ln=False, align='C')  # Prediction
        pdf.cell(col_widths[2], cell_height, txt=f"{accuracy:.2f}%", ln=True, align='C')  # Accuracy

    # Output the PDF using UTF-8 encoding
    pdf.output("output.pdf", 'F')

# Example usage
comments = [("This is a comment.", "Not Spam", 75.5),
            ("Another comment.", "Spam", 90.2),
            ("Yet another comment.", "Not Spam", 82.1)]
total_comments = len(comments)
youtube_title = "Example YouTube Title"
generate_pdf(comments, total_comments, youtube_title)
