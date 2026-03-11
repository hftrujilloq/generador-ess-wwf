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

# CSS personalizado
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
    .pregunta-box {
        background-color: #f8f9fa;
        padding: 0.5rem;
        border-radius: 3px;
        margin-bottom: 0.5rem;
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
    nombre_proyecto = st.text_input("Nombre del proyecto:", placeholder="Ej: Proyecto Bosques Andinos")
    objeto_contrato = st.text_area("Objeto resumido del contrato:", placeholder="Ej: Consultoría para diagnóstico participativo...", height=80)

with col2:
    territorio = st.text_input("Territorio(s) donde se ejecutará (municipio, vereda, resguardo, etc.):", placeholder="Ej: Municipio de San José, Vereda El Toldo")
    fecha = st.date_input("Fecha de generación:", datetime.now())

st.markdown("---")

# Cuestionario
st.header("❓ Cuestionario de Screening ESS")

# INSTRUCCIÓN ACTUALIZADA SEGÚN SOLICITUD
st.info("Seleccione las opciones que aplican o que se marcarían como SÍ. Cada opción seleccionada activará cláusulas específicas automáticamente según la Matriz de Decisión ESS.")

# Sección A - PREGUNTAS EXACTAS DEL DOCUMENTO
st.subheader("Sección A. Preguntas sobre el objeto del contrato (Qué se va a hacer)")

respuestas = {}

st.markdown('<div class="pregunta-box">', unsafe_allow_html=True)
respuestas["A1"] = st.checkbox("A1. ¿La persona contratada tendrá contacto directo con comunidades, asociaciones, consejos comunitarios, resguardos, organizaciones locales o autoridades territoriales?")
st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<div class="pregunta-box">', unsafe_allow_html=True)
respuestas["A2"] = st.checkbox("A2. ¿El contrato incluye actividades en territorio como visitas de campo, talleres, reuniones comunitarias, levantamiento participativo de información o acompañamiento local?")
st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<div class="pregunta-box">', unsafe_allow_html=True)
respuestas["A3"] = st.checkbox("A3. ¿Las actividades podrían afectar, directa o indirectamente, el acceso a recursos, el uso del territorio, las prácticas productivas o los medios de vida de personas o comunidades? (Ej.: restricciones, acuerdos de uso, cambios en reglas, reconversión productiva, áreas de conservación)")
st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<div class="pregunta-box">', unsafe_allow_html=True)
respuestas["A4"] = st.checkbox("A4. ¿Se recopilará o usará información sensible, como: datos personales, testimonios, fotografías, audios o videos, cartografía social, información sobre conflictos, conocimiento tradicional?")
st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<div class="pregunta-box">', unsafe_allow_html=True)
respuestas["A5"] = st.checkbox("A5. ¿El contrato incluye asesoría productiva, agrícola o ambiental que pueda involucrar manejo de plagas, control sanitario, insumos o recomendaciones técnicas en finca o sistemas productivos?")
st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<div class="pregunta-box">', unsafe_allow_html=True)
respuestas["A6"] = st.checkbox("A6. ¿Existe algún riesgo de seguridad asociado a la ejecución del contrato? (Ej.: zonas con presencia de actores armados, amenazas, estigmatización, economías ilegales, restricciones de movilidad)")
st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<div class="pregunta-box">', unsafe_allow_html=True)
respuestas["A7"] = st.checkbox("A7. ¿Las actividades podrían coincidir con sitios culturalmente sensibles, como lugares sagrados, cementerios, territorios ancestrales, o existe riesgo de hallazgos arqueológicos o culturales?")
st.markdown('</div>', unsafe_allow_html=True)

# Sección B - PREGUNTAS EXACTAS DEL DOCUMENTO
st.subheader("Sección B. Preguntas sobre la persona contratada (Quién ejecuta)")

st.markdown('<div class="pregunta-box">', unsafe_allow_html=True)
respuestas["B1"] = st.checkbox("B1. ¿La persona contratada pertenece a una comunidad indígena, afrodescendiente, campesina vulnerable o reside en zona de conflicto o alta vulnerabilidad?")
st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<div class="pregunta-box">', unsafe_allow_html=True)
respuestas["B2"] = st.checkbox("B2. ¿El rol de la persona contratada implica interacciones que puedan generar riesgos de conducta, acoso, violencia basada en género (VBG), explotación o abuso sexual (SEA/SH), especialmente con población en condición de especial vulnerabilidad (mujeres, NNA, víctimas del conflicto, líderes sociales, personas desplazadas)?")
st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<div class="pregunta-box">', unsafe_allow_html=True)
respuestas["B3"] = st.checkbox("B3. ¿La persona contratada tendrá responsabilidades de custodia, procesamiento, análisis o mediación relacionadas con información sensible o conflictos (más allá de la simple recolección)?")
st.markdown('</div>', unsafe_allow_html=True)

# Sección C - PREGUNTAS EXACTAS DEL DOCUMENTO
st.subheader("Sección C. Preguntas sobre los actores involucrados (Con quién se interactúa)")

st.markdown('<div class="pregunta-box">', unsafe_allow_html=True)
respuestas["C1"] = st.checkbox("C1. ¿Hay Pueblos Indígenas involucrados directa o indirectamente en las actividades del contrato?")
st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<div class="pregunta-box">', unsafe_allow_html=True)
respuestas["C2"] = st.checkbox("C2. ¿El territorio presenta conflicto armado activo, control territorial, disputas por tierra o presencia de economías ilegales?")
st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<div class="pregunta-box">', unsafe_allow_html=True)
respuestas["C3"] = st.checkbox("C3. ¿Existe probabilidad de que se presenten quejas, inconformidades o conflictos sociales relacionados con expectativas, beneficios, exclusiones o decisiones del proyecto?")
st.markdown('</div>', unsafe_allow_html=True)

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
                from clauses_library import CLAUSULAS
                for codigo in clausulas_a_generar:
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
