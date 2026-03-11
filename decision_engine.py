from clauses_library import MAPEO_PREGUNTAS, MAPEO_CLAUSULAS

class DecisionEngine:
    def __init__(self):
        self.codigos_activados = set()
        self.clausulas_finales = []
    
    def evaluar_cuestionario(self, respuestas):
        """
        Procesa las respuestas del cuestionario.
        respuestas: dict con formato {"A1": True, "A2": False, ...}
        """
        self.codigos_activados = set()
        
        # Evaluar cada pregunta
        for pregunta, activado in respuestas.items():
            if activado and pregunta in MAPEO_PREGUNTAS:
                codigos = MAPEO_PREGUNTAS[pregunta]
                self.codigos_activados.update(codigos)
        
        # Si no hay ningún código activado, no se aplica ESS
        if not self.codigos_activados:
            return []
        
        # Siempre incluir cláusulas base si hay al menos un código
        clausulas_ids = set(MAPEO_CLAUSULAS["BASE"])
        
        # Agregar cláusulas específicas por cada código activado
        for codigo in self.codigos_activados:
            if codigo in MAPEO_CLAUSULAS:
                clausulas_ids.update(MAPEO_CLAUSULAS[codigo])
        
        return sorted(list(clausulas_ids))
    
    def get_codigos_activados(self):
        return sorted(list(self.codigos_activados))