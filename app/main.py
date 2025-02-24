#!/usr/bin/env python
"""
Point d'entrée pour la logique backend en mode CLI.
Ce script prend un sujet en argument, génère un cours et l'exporte en PDF et PPT.
"""

import sys
from app.prompts.generate_course import generate_course
from app.utils.pdf_export import export_to_pdf
from app.utils.ppt_export import export_to_ppt

def main() -> None:
    if len(sys.argv) < 2:
        print("Usage: python main.py <sujet>")
        sys.exit(1)
    subject = sys.argv[1]
    course = generate_course(subject)
    print("Cours généré :")
    print(course)
    pdf_file = export_to_pdf(course)
    ppt_file = export_to_ppt(course)
    print(f"PDF généré: {pdf_file}")
    print(f"PPT généré: {ppt_file}")

if __name__ == '__main__':
    main()
