from clauses_library import MAPEO_PREGUNTAS, MAPEO_CLAUSULAS, ORDEN_ACTIVADORES

class DecisionEngine:
    def __init__(self):
        self.codigos_activados = []
        self.clausulas_finales = []

    def evaluar_cuestionario(self, respuestas):
        """
        Procesa las respuestas del cuestionario.
        respuestas: dict con formato {"A1": True, "A2": False, ...}
        También acepta valores como 'sí', 'si', 'x', 1.
        """
        activados = set()

        for pregunta, valor in respuestas.items():
            pregunta = str(pregunta).upper()

            if isinstance(valor, bool):
                es_si = valor
            elif isinstance(valor, (int, float)):
                es_si = bool(valor)
            elif isinstance(valor, str):
                es_si = valor.strip().lower() in {"si", "sí", "s", "true", "1", "x", "checked"}
            else:
                es_si = False

            if es_si and pregunta in MAPEO_PREGUNTAS:
                activados.update(MAPEO_PREGUNTAS[pregunta])

        self.codigos_activados = [c for c in ORDEN_ACTIVADORES if c in activados]

        if not self.codigos_activados:
            self.clausulas_finales = []
            return []

        clausulas_ids = []
        vistos = set()

        for clausula in MAPEO_CLAUSULAS["BASE"]:
            if clausula not in vistos:
                clausulas_ids.append(clausula)
                vistos.add(clausula)

        for codigo in self.codigos_activados:
            for clausula in MAPEO_CLAUSULAS.get(codigo, []):
                if clausula not in vistos:
                    clausulas_ids.append(clausula)
                    vistos.add(clausula)

        self.clausulas_finales = clausulas_ids
        return self.clausulas_finales

    def get_codigos_activados(self):
        return self.codigos_activados

    def get_clausulas_finales(self):
        return self.clausulas_finales
