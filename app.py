import streamlit as st

st.set_page_config(page_title="Simulador Falcon 7X - GTAE", page_icon="✈️", layout="wide")

# Estilos de inmersión para calcar la cabina real oscura (Dark Cockpit & Panel Gris FAE)
st.markdown("""
    <style>
    .main { background-color: #05070c; color: #f1f5f9; }
    
    /* Botones estilo cabina gris oscuro militar */
    .stButton>button { 
        width: 100%; 
        font-weight: bold; 
        height: 52px; 
        border-radius: 4px; 
        font-size: 0.82rem;
        background-color: #2a3547 !important;
        color: #ffffff !important;
        border: 2px solid #475569 !important;
        box-shadow: 0 4px 6px rgba(0,0,0,0.3);
    }
    .stButton>button:hover {
        background-color: #3b4b61 !important;
        border: 2px solid #60a5fa !important;
    }
    
    /* Consola física gris de fondo */
    .consola-gris { background-color: #4a5568; border: 4px solid #2d3748; padding: 25px; border-radius: 8px; margin-bottom: 15px; box-shadow: inset 0 2px 5px rgba(0,0,0,0.5); }
    .seccion-dc { border: 3px solid #22c55e; padding: 15px; border-radius: 6px; background-color: #2d3748; }
    .titulo-dc { color: #ffffff; font-weight: bold; font-size: 1rem; text-align: center; font-family: monospace; letter-spacing: 1px; margin-bottom: 15px; }
    
    /* Réplica exacta de la Pantalla CRT Honeywell EASy (Totalmente Hermética) */
    .crt-easy-display { font-family: 'Courier New', Courier, monospace; border-radius: 8px; padding: 25px; min-height: 480px; box-shadow: 0 10px 15px rgba(0,0,0,0.7); }
    .crt-normal { background-color: #000000; border: 5px solid #2d3748; color: #00ff66; box-shadow: inset 0px 0px 30px rgba(0,255,102,0.15); }
    .crt-error { background-color: #450a0a; border: 5px solid #ef4444; color: #f87171; box-shadow: inset 0px 0px 40px rgba(239,68,68,0.4); animation: parpadeo 1.5s infinite; }
    
    .crt-header-line { display: flex; justify-content: space-between; border-bottom: 2px solid #064e3b; padding-bottom: 8px; margin-bottom: 20px; font-size: 0.85rem; font-weight: bold; }
    .crt-section-title { font-weight: bold; margin-bottom: 12px; font-size: 0.95rem; }
    .crt-txt-normal { font-size: 0.95rem; margin-bottom: 6px; font-weight: bold; }
    
    /* Caja de Alertas CAS interna */
    .crt-cas-container { border-top: 1px dashed #064e3b; padding-top: 15px; margin-top: 25px; }
    .crt-cas-label { font-weight: bold; font-size: 0.9rem; margin-bottom: 10px; border-bottom: 1px solid #78350f; padding-bottom: 4px; }
    .crt-cas-msg { font-size: 0.88rem; line-height: 1.5; white-space: pre-line; background-color: #050505; border: 1px solid #1f2937; padding: 15px; border-radius: 4px; }
    
    /* Anunciadores de luces integrados debajo de los botones */
    .luz-f7x-verde { background-color: #064e3b; color: #00ff66; border: 1px solid #22c55e; font-weight: bold; text-align: center; border-radius: 2px; font-size: 0.75rem; padding: 4px; margin-top: 3px; }
    .luz-f7x-amber { background-color: #78350f; color: #ffb700; border: 1px solid #d97706; font-weight: bold; text-align: center; border-radius: 2px; font-size: 0.75rem; padding: 4px; margin-top: 3px; }
    .luz-f7x-off { background-color: #1a202c; color: #4a5568; border: 1px solid #2d3748; text-align: center; border-radius: 2px; font-size: 0.75rem; padding: 4px; margin-top: 3px; }
    </style>
""", unsafe_allow_html=True)

st.title("✈️ Sistema de Instrucción Falcon 7X - GTAE")
st.subheader("Panel Avanzado ATA 24: Entrenamiento y Evaluación Operativa")
st.markdown("---")

# Selección del Modo Operativo (Energización o Desenergización)
modo_operacion = st.radio(
    "📋 SELECCIONE EL PROCEDIMIENTO TÉCNICO A EVALUAR:",
    ["ENERGIZACIÓN COMPLETA (COLD OPERATIONS)", "DESENERGIZACIÓN COMPLETA (SHUTDOWN)"],
    horizontal=True
)

# Inicialización de estados de simulación
if "step_e" not in st.session_state: st.session_state.step_e = 0
if "step_d" not in st.session_state: st.session_state.step_d = 0
if "error_activo" not in st.session_state: st.session_state.error_activo = False
if "msg_error" not in st.session_state: st.session_state.msg_error = ""

# Lógica de reinicio automático al cambiar de modo
if "modo_previo" not in st.session_state:
    st.session_state.modo_previo = modo_operacion
elif st.session_state.modo_previo != modo_operacion:
    st.session_state.step_e = 0
    st.session_state.step_d = 0
    st.session_state.error_activo = False
    st.session_state.msg_error = ""
    st.session_state.modo_previo = modo_operacion

# Función para registrar errores procedimentales
def registrar_error(mensaje):
    st.session_state.error_activo = True
    st.session_state.msg_error = mensaje

col_left, col_right = st.columns([1.3, 1])

with col_left:
    st.markdown("<div class='consola-gris'><div class='seccion-dc'><div class='titulo-dc'>⚡ DC SUPPLY PANEL ⚡</div>", unsafe_allow_html=True)
    
    # --- FILA SUPERIOR DEL OVERHEAD ---
    fs = st.columns(8)
    
    with fs[0]:
        st.button("GALLEY MASTER", disabled=True, key="galley")
        st.markdown("<div class='luz-f7x-off'>OFF</div>", unsafe_allow_html=True)
        
    with fs[1]:
        if st.button("LH MASTER", key="lhmstr"):
            if modo_operacion == "ENERGIZACIÓN COMPLETA (COLD OPERATIONS)":
                if st.session_state.step_e == 10: st.session_state.step_e = 11
                else: registrar_error("LH MASTER accionado fuera de secuencia de O.T.")
            else:
                if st.session_state.step_d == 0: st.session_state.step_d = 1
                else: registrar_error("Corte de LH MASTER fuera de secuencia.")
            st.rerun()
        
        # Luces de estado dinámicas
        if modo_operacion == "ENERGIZACIÓN COMPLETA (COLD OPERATIONS)":
            luz = "<div class='luz-f7x-verde'>ON</div>" if st.session_state.step_e >= 11 else "<div class='luz-f7x-amber'>OFF</div>"
        else:
            luz = "<div class='luz-f7x-amber'>OFF</div>" if st.session_state.step_d >= 1 else "<div class='luz-f7x-verde'>ON</div>"
        st.markdown(luz, unsafe_allow_html=True)
        
    with fs[2]:
        if st.button("LH INIT", key="lhinit"):
            if modo_operacion == "ENERGIZACIÓN COMPLETA (COLD OPERATIONS)":
                if st.session_state.step_e == 7: st.session_state.step_e = 8
                else: registrar_error("LH INIT accionado sin acoplamiento de BUS TIE.")
            else:
                if st.session_state.step_d == 4: st.session_state.step_d = 5
                else: registrar_error("Corte de LH INIT fuera de secuencia.")
            st.rerun()
            
        if modo_operacion == "ENERGIZACIÓN COMPLETA (COLD OPERATIONS)":
            luz = "<div class='luz-f7x-off'>RUN</div>" if st.session_state.step_e >= 8 else "<div class='luz-f7x-amber'>OFF</div>"
        else:
            luz = "<div class='luz-f7x-amber'>OFF</div>" if st.session_state.step_d >= 5 else "<div class='luz-f7x-off'>RUN</div>"
        st.markdown(luz, unsafe_allow_html=True)
        
    with fs[3]:
        if st.button("BUS TIE", key="bustie"):
            if modo_operacion == "ENERGIZACIÓN COMPLETA (COLD OPERATIONS)":
                if st.session_state.step_e == 6: st.session_state.step_e = 7
                else: registrar_error("BUS TIE presionado antes de la protección de la RAT.")
            else:
                if st.session_state.step_d == 3: st.session_state.step_d = 4
                else: registrar_error("Desacoplamiento de BUS TIE fuera de secuencia.")
            st.rerun()
            
        if modo_operacion == "ENERGIZACIÓN COMPLETA (COLD OPERATIONS)":
            luz = "<div class='luz-f7x-amber'>TIED</div>" if st.session_state.step_e >= 7 else "<div class='luz-f7x-off'>AUTO</div>"
        else:
            luz = "<div class='luz-f7x-off'>AUTO</div>" if st.session_state.step_d >= 4 else "<div class='luz-f7x-amber'>TIED</div>"
        st.markdown(luz, unsafe_allow_html=True)
        
    with fs[4]:
        if st.button("RH INIT", key="rhinit"):
            if modo_operacion == "ENERGIZACIÓN COMPLETA (COLD OPERATIONS)":
                if st.session_state.step_e == 7: st.session_state.step_e = 8
                else: registrar_error("RH INIT accionado sin acoplamiento de BUS TIE.")
            else:
                if st.session_state.step_d == 4: st.session_state.step_d = 5
                else: registrar_error("Corte de RH INIT fuera de secuencia.")
            st.rerun()
            
        if modo_operacion == "ENERGIZACIÓN COMPLETA (COLD OPERATIONS)":
            luz = "<div class='luz-f7x-off'>RUN</div>" if st.session_state.step_e >= 8 else "<div class='luz-f7x-amber'>OFF</div>"
        else:
            luz = "<div class='luz-f7x-amber'>OFF</div>" if st.session_state.step_d >= 5 else "<div class='luz-f7x-off'>RUN</div>"
        st.markdown(luz, unsafe_allow_html=True)
        
    with fs[5]:
        if st.button("RH MASTER", key="rhmstr"):
            if modo_operacion == "ENERGIZACIÓN COMPLETA (COLD OPERATIONS)":
                if st.session_state.step_e == 10: st.session_state.step_e = 11
                else: registrar_error("RH MASTER accionado fuera de secuencia de O.T.")
            else:
                if st.session_state.step_d == 0: st.session_state.step_d = 1
                else: registrar_error("Corte de RH MASTER fuera de secuencia.")
            st.rerun()
            
        if modo_operacion == "ENERGIZACIÓN COMPLETA (COLD OPERATIONS)":
            luz = "<div class='luz-f7x-verde'>ON</div>" if st.session_state.step_e >= 11 else "<div class='luz-f7x-amber'>OFF</div>"
        else:
            luz = "<div class='luz-f7x-amber'>OFF</div>" if st.session_state.step_d >= 1 else "<div class='luz-f7x-verde'>ON</div>"
        st.markdown(luz, unsafe_allow_html=True)
        
    with fs[6]:
        if st.button("CABIN MASTER", key="cabin"):
            if modo_operacion == "ENERGIZACIÓN COMPLETA (COLD OPERATIONS)":
                if st.session_state.step_e == 9: st.session_state.step_e = 10
                else: registrar_error("CABIN MASTER accionado sin alimentación principal estable.")
            else:
                if st.session_state.step_d == 1: st.session_state.step_d = 2
                else: registrar_error("CABIN MASTER accionado fuera de secuencia de desenergización.")
            st.rerun()
            
        if modo_operacion == "ENERGIZACIÓN COMPLETA (COLD OPERATIONS)":
            luz = "<div class='luz-f7x-amber'>OFF</div>" if st.session_state.step_e >= 10 else "<div class='luz-f7x-verde'>ON</div>"
        else:
            luz = "<div class='luz-f7x-verde'>ON</div>" if st.session_state.step_d >= 2 else "<div class='luz-f7x-amber'>OFF</div>"
        st.markdown(luz, unsafe_allow_html=True)
        
    with fs[7]:
        if st.button("EXT POWER", key="extpwr"):
            if modo_operacion == "ENERGIZACIÓN COMPLETA (COLD OPERATIONS)":
                if st.session_state.step_e == 8: st.session_state.step_e = 9
                else: registrar_error("EXT POWER presionado sin inicialización previa de barras esenciales.")
            else:
                if st.session_state.step_d == 2: st.session_state.step_d = 3
                else: registrar_error("Desconexión de EXT POWER fuera de secuencia.")
            st.rerun()
            
        if modo_operacion == "ENERGIZACIÓN COMPLETA (COLD OPERATIONS)":
            luz = "<div class='luz-f7x-verde'>ONLINE</div>" if st.session_state.step_e >= 9 else "<div class='luz-f7x-off'>OFF</div>"
        else:
            luz = "<div class='luz-f7x-off'>OFF</div>" if st.session_state.step_d >= 3 else "<div class='luz-f7x-verde'>ONLINE</div>"
        st.markdown(luz, unsafe_allow_html=True)

    st.markdown("<div style='border-top: 4px solid #ffffff; margin-top: 25px; margin-bottom: 25px;'></div>", unsafe_allow_html=True)

    # --- FILA INFERIOR DEL OVERHEAD ---
    fi = st.columns(8)
    
    with fi[0]:
        st.button("GEN 1", disabled=True, key="gen1")
        st.markdown("<div class='luz-f7x-off'>OFF</div>", unsafe_allow_html=True)
        
    with fi[1]:
        if st.button("LH ISOL", key="lhisol"):
            if modo_operacion == "ENERGIZACIÓN COMPLETA (COLD OPERATIONS)":
                if st.session_state.step_e == 9: st.session_state.step_e = 10
                else: registrar_error("Aislamiento LH accionado antes de establecer la carga comercial.")
            else:
                if st.session_state.step_d == 1: st.session_state.step_d = 2
                else: registrar_error("Acoplamiento LH ISOL fuera de secuencia.")
            st.rerun()
            
        if modo_operacion == "ENERGIZACIÓN COMPLETA (COLD OPERATIONS)":
            luz = "<div class='luz-f7x-off'>TIED</div>" if st.session_state.step_e >= 10 else "<div class='luz-f7x-amber'>ISOL</div>"
        else:
            luz = "<div class='luz-f7x-amber'>ISOL</div>" if st.session_state.step_d >= 2 else "<div class='luz-f7x-off'>TIED</div>"
        st.markdown(luz, unsafe_allow_html=True)
        
    with fi[2]:
        if st.button("BAT 1", key="bat1"):
            if modo_operacion == "ENERGIZACIÓN COMPLETA (COLD OPERATIONS)":
                if st.session_state.step_e == 4: st.session_state.step_e = 5
                else: registrar_error("BAT 1 accionada sin parámetros estables en la planta externa.")
            else:
                if st.session_state.step_d == 6: st.session_state.step_d = 7
                else: registrar_error("Corte de BAT 1 fuera de secuencia final.")
            st.rerun()
            
        if modo_operacion == "ENERGIZACIÓN COMPLETA (COLD OPERATIONS)":
            luz = "<div class='luz-f7x-verde'>AUTO</div>" if st.session_state.step_e >= 5 else "<div class='luz-f7x-off'>OFF</div>"
        else:
            luz = "<div class='luz-f7x-off'>OFF</div>" if st.session_state.step_d >= 7 else "<div class='luz-f7x-verde'>AUTO</div>"
        st.markdown(luz, unsafe_allow_html=True)
        
    with fi[3]:
        if st.button("BAT 2", key="bat2"):
            if modo_operacion == "ENERGIZACIÓN COMPLETA (COLD OPERATIONS)":
                if st.session_state.step_e == 4: st.session_state.step_e = 5
                else: registrar_error("BAT 2 accionada sin parámetros estables en la planta externa.")
            else:
                if st.session_state.step_d == 6: st.session_state.step_d = 7
                else: registrar_error("Corte de BAT 2 fuera de secuencia final.")
            st.rerun()
            
        if modo_operacion == "ENERGIZACIÓN COMPLETA (COLD OPERATIONS)":
            luz = "<div class='luz-f7x-verde'>AUTO</div>" if st.session_state.step_e >= 5 else "<div class='luz-f7x-off'>OFF</div>"
        else:
            luz = "<div class='luz-f7x-off'>OFF</div>" if st.session_state.step_d >= 7 else "<div class='luz-f7x-verde'>AUTO</div>"
        st.markdown(luz, unsafe_allow_html=True)
        
    with fi[4]:
        st.button("RAT RESET", disabled=True, key="rat_res")
        st.markdown("<div class='luz-f7x-off'>OFF</div>", unsafe_allow_html=True)
        
    with fi[5]:
        if st.button("RH ISOL", key="rhisol"):
            if modo_operacion == "ENERGIZACIÓN COMPLETA (COLD OPERATIONS)":
                if st.session_state.step_e == 9: st.session_state.step_e = 10
                else: registrar_error("Aislamiento RH accionado antes de establecer la carga comercial.")
            else:
                if st.session_state.step_d == 1: st.session_state.step_d = 2
                else: registrar_error("Acoplamiento RH ISOL fuera de secuencia.")
            st.rerun()
            
        if modo_operacion == "ENERGIZACIÓN COMPLETA (COLD OPERATIONS)":
            luz = "<div class='luz-f7x-off'>TIED</div>" if st.session_state.step_e >= 10 else "<div class='luz-f7x-amber'>ISOL</div>"
        else:
            luz = "<div class='luz-f7x-amber'>ISOL</div>" if st.session_state.step_d >= 2 else "<div class='luz-f7x-off'>TIED</div>"
        st.markdown(luz, unsafe_allow_html=True)
        
    with fi[6]:
        st.button("GEN 2", disabled=True, key="gen2")
        st.markdown("<div class='luz-f7x-off'>OFF</div>", unsafe_allow_html=True)
        
    with fi[7]:
        st.button("GEN 3", disabled=True, key="gen3")
        st.markdown("<div class='luz-f7x-off'>OFF</div>", unsafe_allow_html=True)

    st.markdown("</div></div>", unsafe_allow_html=True)

    # --- CONTROLES AUXILIARES DE COUPLING EN TIERRA ---
    st.markdown("<div class='consola-gris' style='background-color: #2d3748;'><div class='titulo-overhead'>🔧 SECCIÓN DE CONFIGURACIÓN Y ACOPLE DE PLANTA EXTERNA</div>", unsafe_allow_html=True)
    cx1, cx2, cx3, cx4 = st.columns(4)
    with cx1:
        if st.button("🔌 ACOPLAR RECEPTÁCULO GPU", key="con_gpu"):
            if modo_operacion == "ENERGIZACIÓN COMPLETA (COLD OPERATIONS)":
                if st.session_state.step_e == 0: st.session_state.step_e = 1
                else: registrar_error("Planta externa acoplada fuera de secuencia.")
            else:
                if st.session_state.step_d == 8: st.session_state.step_d = 9
                else: registrar_error("Desconexión prematura de la línea física de tierra.")
            st.rerun()
            
        if modo_operacion == "ENERGIZACIÓN COMPLETA (COLD OPERATIONS)":
            luz = "<div class='luz-f7x-verde'>CONECTADO</div>" if st.session_state.step_e >= 1 else "<div class='luz-f7x-off'>DESCONECTADO</div>"
        else:
            luz = "<div class='luz-f7x-off'>DESCONECTADO</div>" if st.session_state.step_d >= 9 else "<div class='luz-f7x-verde'>CONECTADO</div>"
        st.markdown(luz, unsafe_allow_html=True)
        
    with cx2:
        if st.button("⚡ REGULAR TENSIÓN A 28.0 VDC", key="set_volt"):
            if modo_operacion == "ENERGIZACIÓN COMPLETA (COLD OPERATIONS)":
                if st.session_state.step_e == 1: st.session_state.step_e = 2
                else: registrar_error("Ajuste de tensión modificado sin cableado de entrada.")
            else:
                if st.session_state.step_d == 8: st.session_state.step_d = 9
                else: registrar_error("Modificación de tensión fuera de secuencia final.")
            st.rerun()
            
        if modo_operacion == "ENERGIZACIÓN COMPLETA (COLD OPERATIONS)":
            luz = "<div class='luz-f7x-verde'>28.0 VDC OK</div>" if st.session_state.step_e >= 2 else "<div class='luz-f7x-off'>0.0 VDC</div>"
        else:
            luz = "<div class='luz-f7x-off'>0.0 VDC</div>" if st.session_state.step_d >= 9 else "<div class='luz-f7x-verde'>28.0 VDC OK</div>"
        st.markdown(luz, unsafe_allow_html=True)
        
    with cx3:
        if st.button("🎛️ CONTROLADOR SWITCH GPU TO ON", key="sw_gpu"):
            if modo_operacion == "ENERGIZACIÓN COMPLETA (COLD OPERATIONS)":
                if st.session_state.step_e == 2: st.session_state.step_e = 3
                else: registrar_error("Switch GPU colocado en ON sin regulación de voltaje nominal.")
            else:
                if st.session_state.step_d == 7: st.session_state.step_d = 8
                else: registrar_error("Corte de Switch de control de planta fuera de orden.")
            st.rerun()
            
        if modo_operacion == "ENERGIZACIÓN COMPLETA (COLD OPERATIONS)":
            luz = "<div class='luz-f7x-verde'>LÍNEA ONLINE</div>" if st.session_state.step_e >= 3 else "<div class='luz-f7x-off'>LÍNEA OFF</div>"
        else:
            luz = "<div class='luz-f7x-off'>LÍNEA OFF</div>" if st.session_state.step_d >= 8 else "<div class='luz-f7x-verde'>LÍNEA ONLINE</div>"
        st.markdown(luz, unsafe_allow_html=True)
        
    with cx4:
        if st.button("⚙️ DIENTE FRENO DE PARQUEO", key="park_brake"):
            if modo_operacion == "ENERGIZACIÓN COMPLETA (COLD OPERATIONS)":
                if st.session_state.step_e == 3: st.session_state.step_e = 4
                else: registrar_error("Freno de parqueo omitido antes de la entrada de barras.")
            else:
                if st.session_state.step_d == 7: st.session_state.step_d = 8
                else: registrar_error("Liberación del freno de seguridad fuera de secuencia.")
            st.rerun()
            
        if modo_operacion == "ENERGIZACIÓN COMPLETA (COLD OPERATIONS)":
            luz = "<div class='luz-f7x-verde'>ENGANCHADO</div>" if st.session_state.step_e >= 4 else "<div class='luz-f7x-off'>LIBERADO</div>"
        else:
            luz = "<div class='luz-f7x-off'>LIBERADO</div>" if st.session_state.step_d >= 8 else "<div class='luz-f7x-verde'>ENGANCHADO</div>"
        st.markdown(luz, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("🚨 CORREGIR / REINICIAR EVALUACIÓN", key="reset_sim"):
        st.session_state.step_e = 0
        st.session_state.step_d = 0
        st.session_state.error_activo = False
        st.session_state.msg_error = ""
        st.rerun()
    st.markdown("</div>", unsafe_allow_html=True)

with col_right:
    st.markdown("### 📺 Honeywell EASy Display & Emergencias")
    
    # --- BOTÓN INDEPENDIENTE DE LA RAT (Ubicación real en caja de emergencias) ---
    st.markdown("<div class='consola-gris' style='padding: 15px; margin-bottom: 15px;'>", unsafe_allow_html=True)
    st.markdown("<div style='color: #f87171; font-weight: bold; font-size: 0.85rem; margin-bottom: 8px; text-align: center;'>EMERGENCY BOX (MANDO SEPARADO)</div>", unsafe_allow_html=True)
    
    if st.button("🔘 RAT AUTO", key="ratauto"):
        if modo_operacion == "ENERGIZACIÓN COMPLETA (COLD OPERATIONS)":
            if st.session_state.step_e == 5: st.session_state.step_e = 6
            else: registrar_error("RAT AUTO accionada fuera del orden estipulado de O.T.")
        else:
            if st.session_state.step_d == 5: st.session_state.step_d = 6
            else: registrar_error("Corte de protección de RAT fuera de secuencia.")
        st.rerun()
        
    if modo_operacion == "ENERGIZACIÓN COMPLETA (COLD OPERATIONS)":
        luz_rat = "<div class='luz-f7x-amber'>INHIBIT</div>" if st.session_state.step_e >= 6 else "<div class='luz-f7x-off'>OFF</div>"
    else:
        luz_rat = "<div class='luz-f7x-off'>OFF</div>" if st.session_state.step_d >= 6 else "<div class='luz-f7x-amber'>INHIBIT</div>"
    st.markdown(luz_rat, unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

    # --- PANTALLA INTELIGENTE CRT ---
    estado_pantalla = "crt-error" if st.session_state.error_activo else "crt-normal"
    st.markdown(f"<div class='crt-easy-display {estado_pantalla}'>", unsafe_allow_html=True)
    
    # Configuración de variables eléctricas en tiempo real
    if modo_operacion == "ENERGIZACIÓN COMPLETA (COLD OPERATIONS)":
        v_gpu = "28.0 VDC" if st.session_state.step_e >= 2 else "0.0 VDC"
        v_ess = "28.1 V" if st.session_state.step_e >= 9 else "0.0 V"
        s_isol = "CONECTADO [── GREEN ──]" if st.session_state.step_e >= 10 else "AISLADO [| AMBER |]"
        pasos_completados = st.session_state.step_e == 12
    else:
        v_gpu = "0.0 VDC" if st.session_state.step_d >= 9 else "28.0 VDC"
        v_ess = "0.0 V" if st.session_state.step_d >= 3 else "28.1 V"
        s_isol = "AISLADO [| AMBER |]" if st.session_state.step_d >= 2 else "CONECTADO [── GREEN ──]"
        pasos_completados = st.session_state.step_d == 9

    # Renderizado interno de aviónica
    st.markdown(f"""
        <div class='crt-header-line'>
            <span>SISTEMA: HONEYWELL EASY PDU</span>
            <span>MODO: MDU ELEC SYNOPTIC</span>
        </div>
        <div class='crt-section-title'>⚙️ LÍNEAS DE FLUJO DE CORRIENTE CONTINUA (DC)</div>
        <div class='crt-txt-normal'>• ENTRADA FEEDER GPU TIERRA : {v_gpu}</div>
        <div class='crt-txt-normal'>• LH ESSENTIAL BUS LINE     : {v_ess}</div>
        <div class='crt-txt-normal'>• RH ESSENTIAL BUS LINE     : {v_ess}</div>
        <div class='crt-txt-normal'>• CONTACTOR DE AISLAMIENTO  : {s_isol}</div>
        
        <div class='crt-cas-container'>
            <div class='crt-cas-label'>🔔 CREW ALERTING SYSTEM (CAS) STATUS</div>
    """, unsafe_allow_html=True)
    
    # Lógica de mensajes para el display de aviónica (Sin revelar los siguientes pasos)
    if st.session_state.error_activo:
        st.markdown(f"""
            <div class='crt-cas-msg' style='color: #f87171; border: 2px solid #ef4444; background-color: #2d0000;'>
                🚨 CAS ALERT: ERROR PROCEDIMENTAL INDEBIDO\n
                {st.session_state.msg_error}\n\n
                [PRESIONE EL BOTÓN ROJO DE ABAJO PARA REINICIAR EL PASO]
            </div>
        """, unsafe_allow_html=True)
    elif pasos_completados:
        st.markdown(f"""
            <div class='crt-cas-msg' style='color: #00ff66; border: 2px solid #22c55e;'>
                ⚡ SECUENCIA CONCLUIDA CON ÉXITO\n
                El procedimiento de {'energización' if modo_operacion.startswith('ENERG') else 'desenergización'} cumple al 100% las normativas técnicas del GTAE.
            </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown(f"""
            <div class='crt-cas-msg' style='color: #ffb700;'>
                📲 MODO EVALUACIÓN ACTIVO\n
                Ejecute la secuencia en los interruptores físicos siguiendo el orden establecido en su Orden Técnica (O.T.). La pantalla registrará la telemetría automáticamente.
            </div>
        """, unsafe_allow_html=True)
        
    st.markdown("</div></div>", unsafe_allow_html=True)
