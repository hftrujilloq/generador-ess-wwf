from docx import Document
from docx.shared import Pt, RGBColor, Inches
from docx.enum.text import WD_ALIGN_PARAGRAPH
from io import BytesIO
from clauses_library import CLAUSULAS

class DocumentGenerator:
    def __init__(self, nombre_proyecto, objeto_contrato, territorio):
        self.nombre_proyecto = nombre_proyecto
        self.objeto_contrato = objeto_contrato
        self.territorio = territorio
        self.doc = Document()
    
    def generar_anexo(self, lista_clausulas, codigos_activados):
        # Título
        titulo = self.doc.add_heading('ANEXO DE SALVAGUARDAS SOCIALES Y AMBIENTALES (ESS)', 0)
        titulo.alignment = WD_ALIGN_PARAGRAPH.CENTER
        
        # Información general
        self.doc.add_paragraph(f"Proyecto: {self.nombre_proyecto}")
        self.doc.add_paragraph(f"Objeto Contractual: {self.objeto_contrato}")
        self.doc.add_paragraph(f"Territorio: {self.territorio}")
        self.doc.add_paragraph(f"Códigos de Riesgo Identificados: {', '.join(codigos_activados)}")
        self.doc.add_paragraph()
        
        # Introducción
        intro = self.doc.add_paragraph()
        intro.add_run("Este anexo forma parte integral del contrato y contiene las obligaciones de salvaguardas sociales y ambientales derivadas del análisis de riesgos realizado mediante el Cuestionario de Screening ESS. ")
        intro.add_run("Las cláusulas aquí incluidas son de obligatorio cumplimiento y prevalecerán sobre instrucciones informales contradictorias.")
        
        self.doc.add_paragraph()
        
        # Cláusulas
        for codigo in lista_clausulas:
            if codigo in CLAUSULAS:
                clausula = CLAUSULAS[codigo]
                
                # Título de cláusula
                heading = self.doc.add_heading(clausula["titulo"], level=2)
                
                # Texto
                parrafo = self.doc.add_paragraph(clausula["texto"])
                parrafo.paragraph_format.space_after = Pt(12)
                parrafo.paragraph_format.first_line_indent = Inches(0.25)
        
        # Pie de página
        self.doc.add_paragraph()
        self.doc.add_paragraph("— Fin del Anexo ESS —").alignment = WD_ALIGN_PARAGRAPH.CENTER
        
        return self.doc
    
    def descargar_word(self):
        buffer = BytesIO()
        self.doc.save(buffer)
        buffer.seek(0)
        return buffer
    
    def guardar_local(self, filename):
        self.doc.save(filename)