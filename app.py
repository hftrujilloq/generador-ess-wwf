import streamlit as st
from decision_engine import DecisionEngine
from document_generator import DocumentGenerator
from datetime import datetime

# Configuración de la página
st.set_page_config(
    page_title="Generador de Cláusulas ESS - WWF",
    page_icon="🛡️",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# CSS personalizado para mejor apariencia
st.markdown("""
<style>
    .main {
        background-color: #f5f5f5;
    }
    .stButton>button {
        background-color: #2e7d32;
        color: white;
        font-weight: bold;
        padding: 0.5rem 1rem;
        border-radius: 5px;
    }
    .stButton>button:hover {
        background-color: #1b5e20;
    }
    .riesgo-box {
        background-color: #fff3cd;
        padding: 1rem;
        border-radius: 5px;
        border-left: 5px solid #ffc107;
    }
    .success-box {
        background-color: #d4edda;
        padding: 1rem;
        border-radius: 5px;
        border-left: 5px solid #28a745;
    }
</style>
""", unsafe_allow_html=True)

# Header
st.title("🛡️ Sistema de Generación de Cláusulas ESS")
st.subheader("Matriz de Decisión de Salvaguardas Sociales y Ambientales")
st.markdown("---")

# Información básica del contrato
st.header("📋 Sección 0: Información Básica del Contrato")
col1, col2 = st.columns(2)

with col1:
    nombre_proyecto = st.text_input("Nombre del Proyecto:", placeholder="Ej: Proyecto Bosques Andinos")
    objeto_contrato = st.text_area("Objeto resumido del contrato:", placeholder="Ej: Consultoría para diagnóstico participativo...", height=80)

with col2:
    territorio = st.text_input("Territorio(s) de ejecución:", placeholder="Ej: Municipio de San José, Vereda El Toldo")
    fecha = st.date_input("Fecha de generación:", datetime.now())

st.markdown("---")

# Cuestionario
st.header("❓ Cuestionario de Screening ESS")

st.info("Responda 'SÍ' solo si aplica a su contrato. Cada 'SÍ' activará cláusulas específicas automáticamente.")

# Sección A
st.subheader("Sección A: Sobre el Objeto del Contrato (Qué se va a hacer)")
respuestas = {}

col_a1, col_a2 = st.columns(2)
with col_a1:
    respuestas["A1"] = st.checkbox("A1. ¿Contacto directo con comunidades, asociaciones o autoridades territoriales?")
    respuestas["A3"] = st.checkbox("A3. ¿Afectación potencial a acceso a recursos o medios de vida?")
    respuestas["A5"] = st.checkbox("A5. ¿Asesoría productiva con manejo de plagas o insumos?")
    respuestas["A7"] = st.checkbox("A7. ¿Posible coincidencia con sitios culturalmente sensibles?")

with col_a2:
    respuestas["A2"] = st.checkbox("A2. ¿Actividades en territorio (talleres, reuniones, campo)?")
    respuestas["A4"] = st.checkbox("A4. ¿Recopilación de información sensible (datos, testimonios, audios)?")
    respuestas["A6"] = st.checkbox("A6. ¿Riesgo de seguridad (conflicto, estigmatización, economías ilegales)?")

# Sección B
st.subheader("Sección B: Sobre la Persona Contratada (Quién ejecuta)")
col_b1, col_b2 = st.columns(2)
with col_b1:
    respuestas["B1"] = st.checkbox("B1. ¿La persona pertenece a comunidad indígena, afro o vulnerable?")
    respuestas["B3"] = st.checkbox("B3. ¿Responsabilidades de custodia de información sensible?")

with col_b2:
    respuestas["B2"] = st.checkbox("B2. ¿Riesgos de conducta/VBG/SEA con población vulnerable?")

# Sección C
st.subheader("Sección C: Sobre los Actores Involucrados (Con quién se interactúa)")
col_c1, col_c2, col_c3 = st.columns(3)
with col_c1:
    respuestas["C1"] = st.checkbox("C1. ¿Involucra Pueblos Indígenas?")
with col_c2:
    respuestas["C2"] = st.checkbox("C2. ¿Territorio con conflicto armado o economías ilegales?")
with col_c3:
    respuestas["C3"] = st.checkbox("C3. ¿Probabilidad de quejas o conflictos sociales?")

st.markdown("---")

# Procesamiento
if st.button("🚀 PROCESAR Y GENERAR ANEXO ESS", type="primary", use_container_width=True):
    
    if not nombre_proyecto or not objeto_contrato:
        st.error("⚠️ Por favor complete al menos el nombre del proyecto y el objeto del contrato.")
    else:
        # Procesar respuestas
        engine = DecisionEngine()
        clausulas_a_generar = engine.evaluar_cuestionario(respuestas)
        codigos_detectados = engine.get_codigos_activados()
        
        # Mostrar resultados del análisis
        st.header("📊 Resultado del Análisis de Riesgos")
        
        if not clausulas_a_generar:
            st.success("✅ No se detectaron riesgos que requieran cláusulas ESS especiales.")
            st.info("Según el principio preventivo, si tiene dudas, consulte con el área de Salvaguardas.")
        else:
            col_res1, col_res2 = st.columns([1, 2])
            
            with col_res1:
                st.metric("Códigos Activados", len(codigos_detectados))
                st.metric("Cláusulas a Incluir", len(clausulas_a_generar))
            
            with col_res2:
                st.markdown('<div class="riesgo-box">', unsafe_allow_html=True)
                st.write("**Códigos de Riesgo Identificados:**")
                for codigo in codigos_detectados:
                    descripcion = {
                        "A-SE": "Interacción con comunidades",
                        "A-LH": "Medios de vida",
                        "A-DATA": "Datos sensibles",
                        "A-PM": "Plagas",
                        "A-CHSS": "Seguridad / conflicto",
                        "A-CH": "Patrimonio cultural",
                        "A-VD": "Enfoque diferencial",
                        "A-GBV": "VBG / población vulnerable",
                        "A-IP": "Pueblos Indígenas / CLPI",
                        "A-GM": "Riesgo de quejas"
                    }.get(codigo, codigo)
                    st.write(f"• **{codigo}**: {descripcion}")
                st.markdown('</div>', unsafe_allow_html=True)
            
            # Generar documento
            with st.spinner("Generando documento Word..."):
                gen = DocumentGenerator(nombre_proyecto, objeto_contrato, territorio)
                doc = gen.generar_anexo(clausulas_a_generar, codigos_detectados)
                buffer = gen.descargar_word()
            
            # Mostrar preview de cláusulas
            with st.expander("👁️ Ver preview de cláusulas incluidas"):
                for codigo in clausulas_a_generar:
                    from clauses_library import CLAUSULAS
                    if codigo in CLAUSULAS:
                        st.write(f"**{CLAUSULAS[codigo]['titulo']}**")
            
            # Botón de descarga
            st.success("✅ Documento generado exitosamente")
            st.download_button(
                label="📥 DESCARGAR ANEXO ESS (Word)",
                data=buffer,
                file_name=f"Anexo_ESS_{nombre_proyecto.replace(' ', '_')}_{fecha.strftime('%Y%m%d')}.docx",
                mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
                use_container_width=True
            )
            
            st.info("💡 **Instrucciones:** El documento descargado debe adjuntarse al contrato como Anexo ESS. Revise que los códigos correspondan a la realidad del proyecto.")

# Footer
st.markdown("---")
st.caption("Sistema de automatización contractual ESS - WWF Colombia | Basado en la Matriz de Decisión oficial")