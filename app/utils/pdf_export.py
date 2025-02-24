"""
Module d'export en PDF pour AutoCours.
Utilise ReportLab pour générer un fichier PDF à partir du contenu du cours.
"""

from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def export_to_pdf(course_content: dict) -> str:
    """
    Exporte le contenu du cours dans un fichier PDF.

    Args:
        course_content (dict): Dictionnaire contenant le contenu du cours.

    Returns:
        str: Chemin du fichier PDF généré.
    """
    pdf_file = f"{course_content['title'].replace(' ', '_')}.pdf"
    c = canvas.Canvas(pdf_file, pagesize=letter)
    width, height = letter

    c.setFont("Helvetica-Bold", 16)
    c.drawString(100, height - 50, course_content["title"])

    c.setFont("Helvetica", 12)
    y = height - 100
    for module in course_content["modules"]:
        c.drawString(50, y, f"Module : {module['title']}")
        y -= 20
        c.drawString(70, y, module["content"])
        y -= 40
    c.save()
    return pdf_file
