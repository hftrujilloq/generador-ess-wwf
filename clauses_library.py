from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, List, Set, Iterable


CLAUSULAS: Dict[str, Dict[str, str]] = {
    "SAS-00": {
        "titulo": "SAS-00. Introducción SAS",
        "texto": """LA PARTE / LA PERSONA CONTRATADA entenderá por: (a) Salvaguardas WWF: el conjunto de políticas, estándares, guías, procedimientos y herramientas de salvaguardas ambientales y sociales declarados por WWF a nivel internacional y nacional, vigentes durante la ejecución del Contrato/Acuerdo/Convenio. (b) Actores Relevantes: comunidades, organizaciones, grupos étnicos, y demás partes que puedan verse involucradas por el Objeto Contractual. (c) Incidente SAS: cualquier evento, situación, amenaza, afectación o denuncia que implique (i) daño o riesgo de daño a los actores relevantes, (ii) vulneración de derechos, (iii) conflicto social, (iv) impacto ambiental relevante, (v) riesgo de seguridad, (vi) violencias basadas en género (VBG), acoso, explotación o abuso sexual, (vii) afectación a patrimonio cultural, o (viii) riesgo reputacional material para WWF a nivel internacional y nacional. (d) Mecanismo de Escucha y Acción (MEyA): conjunto de canales, reglas y procedimientos definidos por WWF Colombia para recibir, registrar, tramitar, responder y cerrar quejas y reclamos relacionados con el Objeto Contractual."""
    },
    "SAS-01": {
        "titulo": "SAS-01. Obligación general de cumplimiento de Salvaguardas",
        "texto": """LA PARTE / LA PERSONA CONTRATADA se obliga a ejecutar el Objeto Contractual cumpliendo con las Salvaguardas de WWF aplicables, bajo los principios de prevención del daño, debida diligencia reforzada, respeto y garantía de los derechos humanos reconocidos en la Constitución Política de Colombia, el bloque de constitucionalidad, los tratados internacionales ratificados por el Estado colombiano, el enfoque diferencial, la interculturalidad y el principio de “no causar daño”. Esta obligación constituye un estándar mínimo exigible de resultado y de conducta, verificable respecto de: (i) la conducta profesional y el relacionamiento con Actores Relevantes; (ii) el respeto de rutas, protocolos y decisiones institucionales definidas por WWF Colombia; (iii) la adopción de medidas preventivas razonables cuando el contexto lo exija; y (iv) el reporte oportuno de Incidentes ESS. El incumplimiento de esta cláusula se considerará incumplimiento grave para efectos de terminación y demás remedios contractuales."""
    },
    "ME&A-01": {
        "titulo": "ME&A-01. Mecanismo de Escucha y Acción",
        "texto": """WWF COLOMBIA, en cumplimiento de sus SAS ha establecido un procedimiento para recibir y responder quejas y reclamos presentados por grupos de interés o personas quienes consideren que sus derechos han sido afectados por acciones asociadas a la ejecución del objeto del presente Acuerdo / Contrato / Convenio.
LA PARTE / LA PERSONA CONTRATADA deberá informar de manera inmediata a WWF Colombia cualquier incidente o situación que afecte derechos sociales, ambientales, culturales o de derechos humanos y cooperar en la gestión entregando toda la información disponible de manera confidencial, absteniéndose de ejecutar acciones que afecten a las personas o comunidades involucradas, sin tener aprobación previa y escrita de WWF Colombia.
Cuando a juicio de WWF Colombia exista un riesgo para las personas, comunidades o el ambiente, podrá ordenar la suspensión temporal de actividades mientras se gestiona la queja o reclamo sin que ello implique reconocimiento de responsabilidad de WWF Colombia.
Los canales del Mecanismo de Escucha y Acción son el correo electrónico escuchayaccion@wwf.org.co, el número de Whatsapp +57 3102205625 o por correspondencia enviada a la dirección Carrera 10 A # 69 A – 44 en Bogotá, así como aquellos que sean habilitados.
En los casos en que los aliados cuenten con mecanismos propios para el manejo de estos asuntos, WWF Colombia acordará un procedimiento claro para asegurar la notificación oportuna de los reclamos."""
    },
    "IC-01": {
        "titulo": "IC-01. Estándar de conducta y relacionamiento",
        "texto": """En toda interacción con Actores Relevantes, LA PARTE / LA PERSONA CONTRATADA deberá actuar con respeto, diligencia, transparencia y sensibilidad cultural absteniéndose de: (i) prometer beneficios, compensaciones o resultados; (ii) inducir decisiones mediante presión, manipulación o aprovechamiento de situaciones de vulnerabilidad; (iii) emitir mensajes que estigmaticen, desinformen o incrementen riesgos sociales; (iv) realizar registros audiovisuales sin consentimiento previo; y (v) interferir con las estructuras de gobernanza comunitaria o de autoridades legítimas."""
    },
    "IC-02": {
        "titulo": "IC-02. Información veraz, consentimiento y gestión de expectativas",
        "texto": """LA PARTE / LA PERSONA CONTRATADA deberá comunicar de manera clara y veraz el propósito de su actividad, el alcance y límites de su rol, evitando generar expectativas indebidas. Si hace entrevistas, registros de imágenes, uso de datos personales y divulgación de información, deberá obtener el consentimiento previo conforme a las Políticas de manejo e Datos de WWF Colombia. Si por razones de seguridad o sensibilidad cultural no procede la recolección de nombres o firmas, deberá dejarse constancia de la medida adoptada y su justificación."""
    },
    "PI-01": {
        "titulo": "PI-01. Respeto a derechos colectivos y autoridades",
        "texto": """Cuando el Contrato se ejecute con participación o potencial afectación de pueblos indígenas entendidas como lo señala la Decisión 169 de la Organización Internacional del Trabajo, comunidades negras, afrocolombianas, raizales y palenqueras, y comunidades campesinas, LA PARTE / LA PERSONA CONTRATADA deberá respetar desarrollar sus actividades de manera coordinada atendiendo su autonomía, autoridades legítimas, normas propias, estructuras de representación, usos y costumbres, y abstenerse de fragmentar procesos colectivos mediante acuerdos individuales o interlocuciones no autorizadas por las autoridades."""
    },
    "PI-02": {
        "titulo": "PI-02. CLPI y límites operativos",
        "texto": """Cuando aplique el Consentimiento Libre, Previo e Informado (CLPI), conforme a los criterios definidos por la salvaguarda de pueblos indígenas de WWF Colombia, la jurisprudencia de la Corte Constitucional colombiana y las disposiciones internacionales reconocidos por el Estado colombiano, LA PARTE / LA PERSONA CONTRATADA no podrá: (i) iniciar actividades sustantivas en territorio; (ii) levantar información sensible o conocimiento tradicional; (iii) difundir información del proceso; ni (iv) promover decisiones o acuerdos, sin que WWF Colombia haya definido y aprobado por escrito la ruta CLPI y los soportes requeridos."""
    },
    "PI-03": {
        "titulo": "PI-03. Conocimiento tradicional y uso de información",
        "texto": """El uso de conocimiento tradicional o información culturalmente sensible requerirá autorización expresa según la ruta CLPI y condiciones de uso acordadas. LA PARTE / PERSONA CONTRATADA reconoce que el almacenamiento, reproducción o divulgación de este conocimiento sin autorización puede generar daños irreparables y se obliga a no hacerlo, incluso después de la terminación del Contrato."""
    },
    "SEG-01": {
        "titulo": "SEG-01. Deber de “no exposición” y gestión del riesgo",
        "texto": """LA PARTE / LA PERSONA CONTRATADA implementará medidas de “no exposición” para no incrementar riesgos de seguridad para comunidades, organizaciones, personal o para sí misma. Queda prohibido divulgar información (incluyendo ubicación, nombres, fotografías, listados o acuerdos). Ante variación del contexto, deberá solicitar instrucciones por escrito y ajustar actividades según las instrucciones impartidas por el personal de WWF Colombia."""
    },
    "SEG-02": {
        "titulo": "SEG-02. Neutralidad operacional y prohibiciones",
        "texto": """LA PARTE / LA PERSONA CONTRATADA se abstendrá de realizar acuerdos de seguridad, pagos, favores, gestiones o coordinaciones con actores que puedan comprometer la independencia, la neutralidad operacional o la seguridad de WWF, de las comunidades o de otros actores, en concordancia con los principios de neutralidad, independencia y acción sin daño aplicables a organizaciones de conservación y acción territorial. Cualquier requerimiento de “permiso”, presión o condicionamiento deberá ser reportado de inmediato como Incidente ESS."""
    },
    "VBG-01": {
        "titulo": "VBG-01. Estándar de conducta y cero tolerancia",
        "texto": """LA PARTE / LA PERSONA CONTRATADA se obliga a mantener un estándar de conducta profesional de cero tolerancia frente a acoso, hostigamiento, explotación o abuso relacionado con conductas sexuales, o cualquier forma de VbG, discriminación o trato degradante. Esta obligación aplica en interacciones relacionadas con el desarrollo del contrato/acuerdo, comunitarias y con terceros."""
    },
    "VBG-02": {
        "titulo": "VBG-02. Manejo de reportes: confidencialidad, no revictimización y remisión",
        "texto": """Ante cualquier reporte, sospecha o indicio de violencia basada en género, acoso, explotación o abuso relacionado con conductas sexuales, LA PARTE / LA PERSONA CONTRATADA deberá: (i) preservar la confidencialidad y la seguridad de la persona afectada; (ii) abstenerse de realizar indagaciones por cuenta propia; y (iii) reportar de inmediato el caso por los canales internos definidos por WWF Colombia. El incumplimiento de esta obligación se considerará falta grave."""
    },
    "PC-01": {
        "titulo": "PC-01. Cláusula de hallazgos fortuitos y respeto cultural",
        "texto": """Ante cualquier hallazgo arqueológico, funerario, o elemento de valor cultural, o ante indicios de afectación a sitios sagrados o culturalmente significativos, LA PARTE / LA PERSONA CONTRATADA deberá: (i) suspender inmediatamente la actividad relacionada; (ii) asegurar el área en la medida de lo posible sin manipulación; (iii) notificar a WWF Colombia dentro el siguiente día hábil; y (iv) acatar el procedimiento institucional definido por WWF Colombia, sin perjuicio de las obligaciones de reporte a las autoridades competentes cuando la ley lo exija."""
    },
    "MV-01": {
        "titulo": "MV-01. Prohibición de implementar restricciones sin evaluación y aprobación",
        "texto": """LA PARTE / LA PERSONA CONTRATADA no podrá diseñar, recomendar ni implementar medidas que impliquen restricciones de acceso a recursos, afectación a medios de vida, desplazamiento económico, pérdida de ingresos o cambios en reglas de uso territorial, sin que WWF Colombia haya realizado la debida diligencia social y ambiental correspondiente y lo haya aprobado por escrito, garantizando en todo caso el principio de no regresividad en materia de derechos sociales. Cualquier riesgo de este tipo deberá ser reportado como incidente relacionado con las salvaguardas sociales y ambientales."""
    },
    "GP-01": {
        "titulo": "GP-01. Manejo Integrado de Plagas y prohibiciones",
        "texto": """Si el Objeto Contractual involucra prácticas productivas con control de plagas, LA PARTE / LA PERSONA CONTRATADA aplicará Manejo Integrado de Plagas (MIP) conforme a la salvaguarda de gestión de plaguicidas de WWF a nivel internacional."""
    },
    "ED-01": {
        "titulo": "ED-01. Aplicación obligatoria del enfoque diferencial",
        "texto": """Cuando el Contrato involucre directamente a personas o comunidades indígenas, afrodescendientes y campesinas, personas en condición de vulnerabilidad, víctimas del conflicto armado, personas desplazadas, mujeres rurales, personas mayores, personas con discapacidad u otros sujetos de especial protección constitucional, LA PARTE / LA PERSONA CONTRATADA se obliga a incorporar y aplicar enfoque diferencial en la ejecución del Objeto Contractual. Dicho enfoque comprende, como mínimo: (i) trato digno y no discriminación; (ii) adecuación cultural y territorial en el desarrollo de actividades considerando las dinámicas comunitarias, autoridades legítimas y contextos locales; y (v) adopción de medidas para prevenir impactos desproporcionados o que agraven condiciones de vulnerabilidad."""
    },
    "ED-02": {
        "titulo": "ED-02. Prohibición de instrumentalización de la vulnerabilidad y deber de no agravamiento",
        "texto": """LA PARTE / LA PERSONA CONTRATADA deberá abstenerse de utilizar, aprovechar o instrumentalizar condiciones de vulnerabilidad social, económica, cultural o territorial para ejecutar el objeto Contrato."""
    },
    "ED-03": {
        "titulo": "ED-03. Ajustes metodológicos razonables, documentación y trazabilidad",
        "texto": """Cuando resulte aplicable el enfoque diferencial, LA PARTE / LA PERSONA CONTRATADA deberá implementar ajustes metodológicos razonables, tales como adaptación de lenguajes, tiempos, espacios, herramientas de participación o acompañamiento comunitario, de acuerdo con el contexto específico. La adopción de dichas medidas deberá quedar documentada en los productos contractuales."""
    },
}

MAPEO_PREGUNTAS: Dict[str, List[str]] = {
    "A1": ["A-IC"],
    "A2": ["A-IC"],
    "A3": ["A-MV"],
    "A5": ["A-GP"],
    "A6": ["A-SEG"],
    "C2": ["A-SEG"],
    "A7": ["A-PC"],
    "B1": ["A-ED"],
    "B2": ["A-VBG"],
    "C1": ["A-PI"],
}

MAPEO_CLAUSULAS: Dict[str, List[str]] = {
    "BASE": ["SAS-00", "SAS-01", "ME&A-01"],
    "A-IC": ["IC-01", "IC-02"],
    "A-PI": ["PI-01", "PI-02", "PI-03"],
    "A-SEG": ["SEG-01", "SEG-02"],
    "A-VBG": ["VBG-01", "VBG-02"],
    "A-PC": ["PC-01"],
    "A-MV": ["MV-01"],
    "A-GP": ["GP-01"],
    "A-ED": ["ED-01", "ED-02", "ED-03"],
}

ORDEN_ACTIVADORES = [
    "A-IC",
    "A-PI",
    "A-SEG",
    "A-VBG",
    "A-PC",
    "A-MV",
    "A-GP",
    "A-ED",
]


@dataclass
class ResultadoSAS:
    preguntas_si: List[str]
    activadores: List[str]
    clausulas: List[str]
    clausulas_detalle: List[Dict[str, str]]


def normalizar_respuestas(respuestas: Dict[str, object]) -> Dict[str, bool]:
    salida: Dict[str, bool] = {}

    for pregunta, valor in respuestas.items():
        key = pregunta.upper()

        if isinstance(valor, bool):
            salida[key] = valor
        elif isinstance(valor, (int, float)):
            salida[key] = bool(valor)
        elif isinstance(valor, str):
            salida[key] = valor.strip().lower() in {"si", "sí", "s", "true", "1", "x", "checked"}
        else:
            salida[key] = False

    return salida


def obtener_activadores(respuestas: Dict[str, object]) -> List[str]:
    respuestas_norm = normalizar_respuestas(respuestas)
    activados: Set[str] = set()

    for pregunta, es_si in respuestas_norm.items():
        if es_si and pregunta in MAPEO_PREGUNTAS:
            activados.update(MAPEO_PREGUNTAS[pregunta])

    return [a for a in ORDEN_ACTIVADORES if a in activados]


def obtener_clausulas(activadores: Iterable[str]) -> List[str]:
    activadores = list(activadores)
    if not activadores:
        return []

    clausulas: List[str] = []
    vistos: Set[str] = set()

    for codigo in MAPEO_CLAUSULAS["BASE"]:
        if codigo not in vistos:
            clausulas.append(codigo)
            vistos.add(codigo)

    for activador in activadores:
        for codigo in MAPEO_CLAUSULAS.get(activador, []):
            if codigo not in vistos:
                clausulas.append(codigo)
                vistos.add(codigo)

    return clausulas


def construir_resultado(respuestas: Dict[str, object]) -> ResultadoSAS:
    respuestas_norm = normalizar_respuestas(respuestas)
    preguntas_si = sorted([k for k, v in respuestas_norm.items() if v])
    activadores = obtener_activadores(respuestas_norm)
    clausulas = obtener_clausulas(activadores)

    detalle = []
    for codigo in clausulas:
        detalle.append({
            "codigo": codigo,
            "titulo": CLAUSULAS[codigo]["titulo"],
            "texto": CLAUSULAS[codigo]["texto"],
        })

    return ResultadoSAS(
        preguntas_si=preguntas_si,
        activadores=activadores,
        clausulas=clausulas,
        clausulas_detalle=detalle,
    )


def render_markdown(resultado: ResultadoSAS, incluir_texto_completo: bool = True) -> str:
    partes: List[str] = []
    partes.append("# Resultado de la Matriz de Decisión SAS\n")

    partes.append("## Preguntas con respuesta afirmativa")
    partes.extend([f"- {p}" for p in resultado.preguntas_si] or ["- Ninguna"])
    partes.append("")

    partes.append("## Activadores SAS aplicables")
    partes.extend([f"- {a}" for a in resultado.activadores] or ["- Ninguno"])
    partes.append("")

    partes.append("## Cláusulas a incorporar")
    partes.extend([f"- {c}" for c in resultado.clausulas] or ["- Ninguna"])
    partes.append("")

    if incluir_texto_completo and resultado.clausulas_detalle:
        partes.append("## Texto de cláusulas\n")
        for item in resultado.clausulas_detalle:
            partes.append(f"### {item['titulo']}")
            partes.append(item["texto"])
            partes.append("")

    return "\n".join(partes).strip()


def render_anexo_contractual(resultado: ResultadoSAS) -> str:
    if not resultado.clausulas_detalle:
        return "No se activaron salvaguardas SAS con base en las respuestas suministradas."

    bloques: List[str] = ["ANEXO SAS – CLÁUSULAS CONTRACTUALES APLICABLES", ""]

    for item in resultado.clausulas_detalle:
        bloques.append(item["titulo"])
        bloques.append(item["texto"])
        bloques.append("")

    return "\n".join(bloques).strip()


def validar_configuracion() -> List[str]:
    errores: List[str] = []

    for activador, clausulas in MAPEO_CLAUSULAS.items():
        for codigo in clausulas:
            if codigo not in CLAUSULAS:
                errores.append(f"MAPEO_CLAUSULAS referencia {codigo}, pero no existe en CLAUSULAS.")

    for pregunta, activadores in MAPEO_PREGUNTAS.items():
        for activador in activadores:
            if activador not in MAPEO_CLAUSULAS:
                errores.append(f"MAPEO_PREGUNTAS referencia {activador}, pero no existe en MAPEO_CLAUSULAS.")

    return errores


if __name__ == "__main__":
    ejemplo = {
        "A1": "sí",
        "A3": True,
        "A6": False,
        "A7": False,
        "B1": "sí",
        "B2": False,
        "C1": True,
        "C2": False,
    }

    errores = validar_configuracion()
    if errores:
        print("Se encontraron errores de configuración:")
        for e in errores:
            print("-", e)
    else:
        resultado = construir_resultado(ejemplo)
        print(render_markdown(resultado, incluir_texto_completo=False))
        print("\n" + "=" * 80 + "\n")
        print(render_anexo_contractual(resultado))
