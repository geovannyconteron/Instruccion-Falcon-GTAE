import streamlit as st

# Configuración inicial de la página
st.set_page_config(page_title="Simulador Falcon 7X - GTAE", page_icon="✈️", layout="wide")

# Estilos globales de inmersión técnica (Dark Cockpit & FAE Panel)
st.markdown("""
    <style>
    .main { background-color: #05070c; color: #f1f5f9; }
    
    /* Botones estilo cabina militar */
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
    
    /* Consolas fijas grises */
    .consola-gris { background-color: #4a5568; border: 4px solid #2d3748; padding: 25px; border-radius: 8px; margin-bottom: 15px; box-shadow: inset 0 2px 5px rgba(0,0,0,0.5); }
    .seccion-dc { border: 3px solid #22c55e; padding: 15px; border-radius: 6px; background-color: #2d3748; }
    .titulo-dc { color: #ffffff; font-weight: bold; font-size: 1rem; text-align: center; font-family: monospace; letter-spacing: 1px; margin-bottom: 15px; }
    
    /* Pantalla CRT Honeywell EASy */
    .crt-easy-display { 
        font-family: 'Courier New', Courier, monospace; 
        border-radius: 8px; 
        padding: 25px; 
        min-height: 520px; 
        box-shadow: 0 10px 25px rgba(0,0,0,0.7); 
        white-space: pre-wrap;
    }
    .crt-normal { background-color: #000000 !important; border: 5px solid #374151 !important; color: #00ff66 !important; }
    .crt-error { 
        background-color: #7f1d1d !important; border: 5px solid #ef4444 !important; color: #fca5a5 !important;
        animation: alarma-parpadeo 1s infinite alternate;
    }
    @keyframes alarma-parpadeo {
        0% { background-color: #7f1d1d; border-color: #ef4444; }
        100% { background-color: #b91c1c; border-color: #f87171; }
    }
    .crt-header { display: flex; justify-content: space-between; border-bottom: 2px solid #064e3b; padding-bottom: 8px; margin-bottom: 20px; font-size: 0.85rem; font-weight: bold; }
    
    /* Luces de anunciadores */
    .luz-f7x-verde { background-color: #064e3b; color: #00ff66; border: 1px solid #22c55e; font-weight: bold; text-align: center; border-radius: 2px; font-size: 0.75rem; padding: 4px; margin-top: 3px; }
    .luz-f7x-amber { background-color: #78350f; color: #ffb700; border: 1px solid #d97706; font-weight: bold; text-align: center; border-radius: 2px; font-size: 0.75rem; padding: 4px; margin-top: 3px; }
    .luz-f7x-off { background-color: #1a202c; color: #4a5568; border: 1px solid #2d3748; text-align: center; border-radius: 2px; font-size: 0.75rem; padding: 4px; margin-top: 3px; }
    
    /* Estilo de la portada */
    .portada-container { background: linear-gradient(rgba(15,23,42,0.85), rgba(15,23,42,0.95)); border: 2px solid #3b82f6; padding: 30px; border-radius: 10px; text-align: center; margin-bottom: 25px; }
    </style>
""", unsafe_allow_html=True)

# ==========================================
# SISTEMA DE CONTROL DE ACCESO (LOGIN)
# ==========================================
if "autenticado" not in st.session_state:
    st.session_state.autenticado = False

if not st.session_state.autenticado:
    st.markdown("<br><br>", unsafe_allow_html=True)
    col_l1, col_l2, col_l3 = st.columns([1, 1.5, 1])
    
    with col_l2:
        st.markdown("""
            <div class='portada-container'>
                <h1 style='color: #ffffff; font-size: 1.8rem; margin-bottom: 5px;'>SISTEMA DE INSTRUCCIÓN TÉCNICA</h1>
                <h3 style='color: #3b82f6; font-size: 1.2rem; margin-bottom: 20px;'>FALCON 7X - GTAE</h3>
            </div>
        """, unsafe_allow_html=True)
        
        # Imagen representativa de portada (puedes cambiar la URL por una foto específica si lo deseas)
        st.image("https://images.unsplash.com/photo-1540962351504-03099e0a754b?q=80&w=1200&auto=format&fit=crop", 
                 caption="Grupo de Transporte Aéreo Especial - Fuerza Aérea Ecuatoriana", use_container_width=True)
        
        st.markdown("<br>", unsafe_allow_html=True)
        with st.form("form_login"):
            st.markdown("<h4 style='text-align: center; color: #f1f5f9;'>🔑 Control de Seguridad Militar</h4>", unsafe_allow_html=True)
            usuario = st.text_input("Usuario Operativo:", placeholder="Ej: gtae_maintenance")
            contrasena = st.text_input("Contraseña de Acceso:", type="password", placeholder="••••••••")
            boton_login = st.form_submit_button("INGRESAR AL ENTORNO TÁCTICO")
            
            if boton_login:
                # Credenciales operativas básicas (Cámbialas a tu gusto)
                if usuario == "gtae" and contrasena == "7X2026":
                    st.session_state.autenticado = True
                    st.rerun()
                else:
                    st.error("❌ Credenciales incorrectas. Acceso denegado para personal no autorizado.")
    st.stop()

# ==========================================
# ENTORNO PROTEGIDO - NAVEGACIÓN MÚLTIPLES MÓDULOS
# ==========================================

# Botón de cierre de sesión en la barra lateral
with st.sidebar:
    st.markdown("### 👤 OPERADOR ACTIVO")
    st.markdown("**Unidad:** Grupo de Transporte Aéreo Especial")
    if st.button("🔒 Cerrar Sesión"):
        st.session_state.autenticado = False
        st.rerun()
    st.markdown("---")
    
    # Selector de módulos de entrenamiento
    st.markdown("### 📂 MÓDULOS DE ENTRENAMIENTO")
    modulo_seleccionado = st.radio(
        "Seleccione el sistema a evaluar:",
        ["MÓDULO I: SISTEMA ELÉCTRICO (ATA 24)", "MÓDULO II: SISTEMA DE COMBUSTIBLE (ATA 28)"]
    )

# ------------------------------------------------------------------
# DESARROLLO DEL MÓDULO I: SISTEMA ELÉCTRICO (ATA 24)
# ------------------------------------------------------------------
if modulo_seleccionado == "MÓDULO I: SISTEMA ELÉCTRICO (ATA 24)":
    st.title("⚡ Módulo I: Distribución Eléctrica ATA 24")
    st.subheader("Entrenamiento de Energizado y Desenergizado en Cabina Completa")
    st.markdown("---")

    modo_operacion = st.radio(
        "📋 SELECCIONE EL PROCEDIMIENTO TÉCNICO A EVALUAR:",
        ["ENERGIZACIÓN COMPLETA (COLD OPERATIONS)", "DESENERGIZACIÓN COMPLETA (SHUTDOWN)"],
        horizontal=True
    )

    if "step_e" not in st.session_state: st.session_state.step_e = 0
    if "step_d" not in st.session_state: st.session_state.step_d = 0
    if "error_activo" not in st.session_state: st.session_state.error_activo = False
    if "msg_error" not in st.session_state: st.session_state.msg_error = ""

    if "modo_previo" not in st.session_state:
        st.session_state.modo_previo = modo_operacion
    elif st.session_state.modo_previo != modo_operacion:
        st.session_state.step_e = 0
        st.session_state.step_d = 0
        st.session_state.error_activo = False
        st.session_state.msg_error = ""
        st.session_state.modo_previo = modo_operacion

    def registrar_error(mensaje):
        st.session_state.error_activo = True
        st.session_state.msg_error = mensaje

    col_left, col_right = st.columns([1.2, 1])

    with col_left:
        st.markdown("<div class='consola-gris'><div class='seccion-dc'><div class='titulo-dc'>⚡ DC SUPPLY PANEL ⚡</div>", unsafe_allow_html=True)
        fs = st.columns(8)
        
        with fs[0]:
            st.button("GALLEY MASTER", disabled=True, key="galley")
            st.markdown("<div class='luz-f7x-off'>OFF</div>", unsafe_allow_html=True)
            
        with fs[1]:
            if st.button("LH MASTER", key="lhmstr"):
                if modo_operacion == "ENERGIZACIÓN COMPLETA (COLD OPERATIONS)":
                    if st.session_state.step_e == 11: st.session_state.step_e = 12
                    else: registrar_error("LH MASTER accionado fuera de secuencia de O.T.")
                else: registrar_error("LH MASTER no requiere ser ciclado en esta fase de desenergización.")
                st.rerun()
            luz = "<div class='luz-f7x-verde'>ON</div>" if (modo_operacion == "ENERGIZACIÓN COMPLETA (COLD OPERATIONS)" and st.session_state.step_e >= 12) or modo_operacion == "DESENERGIZACIÓN COMPLETA (SHUTDOWN)" else "<div class='luz-f7x-amber'>OFF</div>"
            st.markdown(luz, unsafe_allow_html=True)
            
        with fs[2]:
            if st.button("LH INIT", key="lhinit"):
                if modo_operacion == "ENERGIZACIÓN COMPLETA (COLD OPERATIONS)":
                    if st.session_state.step_e == 7: st.session_state.step_e = 8
                    else: registrar_error("LH INIT accionado sin acoplamiento de BUS TIE.")
                else: registrar_error("LH INIT permanece enganchado en modo RUN automático durante el corte manual.")
                st.rerun()
            luz = "<div class='luz-f7x-off'>RUN</div>" if (modo_operacion == "ENERGIZACIÓN COMPLETA (COLD OPERATIONS)" and st.session_state.step_e >= 8) or modo_operacion == "DESENERGIZACIÓN COMPLETA (SHUTDOWN)" else "<div class='luz-f7x-amber'>OFF</div>"
            st.markdown(luz, unsafe_allow_html=True)
            
        with fs[3]:
            if st.button("BUS TIE", key="bustie"):
                if modo_operacion == "ENERGIZACIÓN COMPLETA (COLD OPERATIONS)":
                    if st.session_state.step_e == 6: st.session_state.step_e = 7
                    else: registrar_error("BUS TIE presionado antes de la protección de la RAT.")
                else: registrar_error("BUS TIE se autoprotege; corte directo por switch maestro según O.T.")
                st.rerun()
            luz = "<div class='luz-f7x-amber'>TIED</div>" if (modo_operacion == "ENERGIZACIÓN COMPLETA (COLD OPERATIONS)" and st.session_state.step_e >= 7) or modo_operacion == "DESENERGIZACIÓN COMPLETA (SHUTDOWN)" else "<div class='luz-f7x-off'>AUTO</div>"
            st.markdown(luz, unsafe_allow_html=True)
            
        with fs[4]:
            if st.button("RH INIT", key="rhinit"):
                if modo_operacion == "ENERGIZACIÓN COMPLETA (COLD OPERATIONS)":
                    if st.session_state.step_e == 7: st.session_state.step_e = 8
                    else: registrar_error("RH INIT accionado sin acoplamiento de BUS TIE.")
                else: registrar_error("RH INIT permanece enganchado en modo RUN automático durante el corte manual.")
                st.rerun()
            luz = "<div class='luz-f7x-off'>RUN</div>" if (modo_operacion == "ENERGIZACIÓN COMPLETA (COLD OPERATIONS)" and st.session_state.step_e >= 8) or modo_operacion == "DESENERGIZACIÓN COMPLETA (SHUTDOWN)" else "<div class='luz-f7x-amber'>OFF</div>"
            st.markdown(luz, unsafe_allow_html=True)
            
        with fs[5]:
            if st.button("RH MASTER", key="rhmstr"):
                if modo_operacion == "ENERGIZACIÓN COMPLETA (COLD OPERATIONS)":
                    if st.session_state.step_e == 11: st.session_state.step_e = 12
                    else: registrar_error("RH MASTER accionado fuera de secuencia de O.T.")
                else: registrar_error("RH MASTER no requiere ser ciclado en esta fase de desenergización.")
                st.rerun()
            luz = "<div class='luz-f7x-verde'>ON</div>" if (modo_operacion == "ENERGIZACIÓN COMPLETA (COLD OPERATIONS)" and st.session_state.step_e >= 12) or modo_operacion == "DESENERGIZACIÓN COMPLETA (SHUTDOWN)" else "<div class='luz-f7x-amber'>OFF</div>"
            st.markdown(luz, unsafe_allow_html=True)
            
        with fs[6]:
            if st.button("CABIN MASTER", key="cabin"):
                if modo_operacion == "ENERGIZACIÓN COMPLETA (COLD OPERATIONS)":
                    if st.session_state.step_e == 9: st.session_state.step_e = 10
                    else: registrar_error("CABIN MASTER accionado sin alimentación principal estable.")
                else: registrar_error("CABIN MASTER se desactiva mediante corte maestro de línea.")
                st.rerun()
            luz = "<div class='luz-f7x-amber'>OFF</div>" if (modo_operacion == "ENERGIZACIÓN COMPLETA (COLD OPERATIONS)" and st.session_state.step_e >= 10) or modo_operacion == "DESENERGIZACIÓN COMPLETA (SHUTDOWN)" else "<div class='luz-f7x-verde'>ON</div>"
            st.markdown(luz, unsafe_allow_html=True)
            
        with fs[7]:
            if st.button("EXT POWER", key="extpwr"):
                if modo_operacion == "ENERGIZACIÓN COMPLETA (COLD OPERATIONS)":
                    if st.session_state.step_e == 8: st.session_state.step_e = 9
                    else: registrar_error("EXT POWER presionado sin inicialización previa de barras esenciales.")
                else:
                    if st.session_state.step_d == 0: st.session_state.step_d = 1
                    else: registrar_error("EXT POWER debe ser el primer interruptor presionado para iniciar el corte.")
                st.rerun()
            luz = "<div class='luz-f7x-verde'>ONLINE</div>" if (modo_operacion == "ENERGIZACIÓN COMPLETA (COLD OPERATIONS)" and st.session_state.step_e >= 9) or (modo_operacion == "DESENERGIZACIÓN COMPLETA (SHUTDOWN)" and st.session_state.step_d < 1) else "<div class='luz-f7x-off'>OFF</div>"
            st.markdown(luz, unsafe_allow_html=True)

        st.markdown("<div style='border-top: 4px solid #ffffff; margin-top: 25px; margin-bottom: 25px;'></div>", unsafe_allow_html=True)

        fi = st.columns(8)
        with fi[0]:
            st.button("GEN 1", disabled=True, key="gen1")
            st.markdown("<div class='luz-f7x-off'>OFF</div>", unsafe_allow_html=True)
        with fi[1]:
            if st.button("LH ISOL", key="lhisol"):
                if modo_operacion == "ENERGIZACIÓN COMPLETA (COLD OPERATIONS)":
                    if st.session_state.step_e == 10: st.session_state.step_e = 11
                    else: registrar_error("Aislamiento LH accionado antes de establecer la carga comercial.")
                else: registrar_error("El contactor ISOL se drena automáticamente tras remover la excitación principal.")
                st.rerun()
            luz = "<div class='luz-f7x-off'>TIED</div>" if (modo_operacion == "ENERGIZACIÓN COMPLETA (COLD OPERATIONS)" and st.session_state.step_e >= 11) or modo_operacion == "DESENERGIZACIÓN COMPLETA (SHUTDOWN)" else "<div class='luz-f7x-amber'>ISOL</div>"
            st.markdown(luz, unsafe_allow_html=True)
        with fi[2]:
            if st.button("BAT 1", key="bat1"):
                if modo_operacion == "ENERGIZACIÓN COMPLETA (COLD OPERATIONS)":
                    if st.session_state.step_e == 4: st.session_state.step_e = 5
                    else: registrar_error("BAT 1 accionada sin parámetros estables en la planta externa.")
                else:
                    if st.session_state.step_d == 1: st.session_state.step_d = 2
                    else: registrar_error("BAT 1 debe cortarse a la posición OFF inmediatamente después del EXT POWER.")
                st.rerun()
            luz = "<div class='luz-f7x-verde'>AUTO</div>" if (modo_operacion == "ENERGIZACIÓN COMPLETA (COLD OPERATIONS)" and st.session_state.step_e >= 5) or (modo_operacion == "DESENERGIZACIÓN COMPLETA (SHUTDOWN)" and st.session_state.step_d < 2) else "<div class='luz-f7x-off'>OFF</div>"
            st.markdown(luz, unsafe_allow_html=True)
        with fi[3]:
            if st.button("BAT 2", key="bat2"):
                if modo_operacion == "ENERGIZACIÓN COMPLETA (COLD OPERATIONS)":
                    if st.session_state.step_e == 4: st.session_state.step_e = 5
                    else: registrar_error("BAT 2 accionada sin parámetros estables en la planta externa.")
                else:
                    if st.session_state.step_d == 1: st.session_state.step_d = 2
                    else: registrar_error("BAT 2 debe cortarse a la posición OFF inmediatamente después del EXT POWER.")
                st.rerun()
            luz = "<div class='luz-f7x-verde'>AUTO</div>" if (modo_operacion == "ENERGIZACIÓN COMPLETA (COLD OPERATIONS)" and st.session_state.step_e >= 5) or (modo_operacion == "DESENERGIZACIÓN COMPLETA (SHUTDOWN)" and st.session_state.step_d < 2) else "<div class='luz-f7x-off'>OFF</div>"
            st.markdown(luz, unsafe_allow_html=True)
        with fi[4]:
            st.button("RAT RESET", disabled=True, key="rat_res")
            st.markdown("<div class='luz-f7x-off'>OFF</div>", unsafe_allow_html=True)
        with fi[5]:
            if st.button("RH ISOL", key="rhisol"):
                if modo_operacion == "ENERGIZACIÓN COMPLETA (COLD OPERATIONS)":
                    if st.session_state.step_e == 10: st.session_state.step_e = 11
                    else: registrar_error("Aislamiento RH accionado antes de establecer la carga comercial.")
                else: registrar_error("El contactor ISOL se drena automáticamente tras remover la excitación principal.")
                st.rerun()
            luz = "<div class='luz-f7x-off'>TIED</div>" if (modo_operacion == "ENERGIZACIÓN COMPLETA (COLD OPERATIONS)" and st.session_state.step_e >= 11) or modo_operacion == "DESENERGIZACIÓN COMPLETA (SHUTDOWN)" else "<div class='luz-f7x-amber'>ISOL</div>"
            st.markdown(luz, unsafe_allow_html=True)
        with fi[6]: st.button("GEN 2", disabled=True, key="gen2"); st.markdown("<div class='luz-f7x-off'>OFF</div>", unsafe_allow_html=True)
        with fi[7]: st.button("GEN 3", disabled=True, key="gen3"); st.markdown("<div class='luz-f7x-off'>OFF</div>", unsafe_allow_html=True)

        st.markdown("</div></div>", unsafe_allow_html=True)

        st.markdown("<div class='consola-gris' style='background-color: #2d3748;'><div class='titulo-overhead'>🔧 SECCIÓN DE CONFIGURACIÓN Y ACOPLE DE PLANTA EXTERNA</div>", unsafe_allow_html=True)
        cx1, cx2, cx3, cx4, cx5 = st.columns(5)
        with cx1:
            if st.button("🔌 ACOPLAR/REMOVER RECEPTÁCULO", key="con_gpu"):
                if modo_operacion == "ENERGIZACIÓN COMPLETA (COLD OPERATIONS)":
                    if st.session_state.step_e == 0: st.session_state.step_e = 1
                    else: registrar_error("Planta externa acoplada fuera de secuencia.")
                else:
                    if st.session_state.step_d == 5: st.session_state.step_d = 6
                    else: registrar_error("Desconexión física del receptáculo ejecutada antes de apagar la planta.")
                st.rerun()
            luz = "<div class='luz-f7x-verde'>CONECTADO</div>" if (modo_operacion == "ENERGIZACIÓN COMPLETA (COLD OPERATIONS)" and st.session_state.step_e >= 1) or (modo_operacion == "DESENERGIZACIÓN COMPLETA (SHUTDOWN)" and st.session_state.step_d < 6) else "<div class='luz-f7x-off'>DESCONECTADO</div>"
            st.markdown(luz, unsafe_allow_html=True)
        with cx2:
            if st.button("⚡ REGULADOR TENSIÓN TIERRA", key="set_volt"):
                if modo_operacion == "ENERGIZACIÓN COMPLETA (COLD OPERATIONS)":
                    if st.session_state.step_e == 1: st.session_state.step_e = 2
                    else: registrar_error("Ajuste de tensión modificado sin cableado de entrada.")
                else: registrar_error("El potenciómetro de voltaje de rampa no requiere manipulación durante el resguardo térmico.")
                st.rerun()
            luz = "<div class='luz-f7x-verde'>28.0 VDC OK</div>" if (modo_operacion == "ENERGIZACIÓN COMPLETA (COLD OPERATIONS)" and st.session_state.step_e >= 2) or (modo_operacion == "DESENERGIZACIÓN COMPLETA (SHUTDOWN)" and st.session_state.step_d < 6) else "<div class='luz-f7x-off'>0.0 VDC</div>"
            st.markdown(luz, unsafe_allow_html=True)
        with cx3:
            if st.button("🎛️ SWITCH EXTERNO GPU", key="sw_gpu"):
                if modo_operacion == "ENERGIZACIÓN COMPLETA (COLD OPERATIONS)":
                    if st.session_state.step_e == 2: st.session_state.step_e = 3
                    else: registrar_error("Switch GPU colocado en ON sin regulación de voltaje nominal.")
                else:
                    if st.session_state.step_d == 3: st.session_state.step_d = 4
                    else: registrar_error("El interruptor físico exterior de la planta debe pasarse a OFF después de liberar la RAT.")
                st.rerun()
            luz = "<div class='luz-f7x-verde'>LÍNEA ONLINE</div>" if (modo_operacion == "ENERGIZACIÓN COMPLETA (COLD OPERATIONS)" and st.session_state.step_e >= 3) or (modo_operacion == "DESENERGIZACIÓN COMPLETA (SHUTDOWN)" and st.session_state.step_d < 4) else "<div class='luz-f7x-off'>LÍNEA OFF</div>"
            st.markdown(luz, unsafe_allow_html=True)
        with cx4:
            if st.button("⚙️ CONTROL FRENO PARQUEO", key="park_brake"):
                if modo_operacion == "ENERGIZACIÓN COMPLETA (COLD OPERATIONS)":
                    if st.session_state.step_e == 3: st.session_state.step_e = 4
                    else: registrar_error("Freno de parqueo omitido antes de la entrada de barras.")
                else: registrar_error("El freno de parqueo permanece ENGANCHADO en rampa por seguridad de calzos.")
                st.rerun()
            luz = "<div class='luz-f7x-verde'>ENGANCHADO</div>" if (modo_operacion == "ENERGIZACIÓN COMPLETA (COLD OPERATIONS)" and st.session_state.step_e >= 4) or modo_operacion == "DESENERGIZACIÓN COMPLETA (SHUTDOWN)" else "<div class='luz-f7x-off'>LIBERADO</div>"
            st.markdown(luz, unsafe_allow_html=True)
        with cx5:
            if st.button("🚪 COMPUERTA EXTERIOR F7X", key="close_door_f7x"):
                if modo_operacion == "DESENERGIZACIÓN COMPLETA (SHUTDOWN)":
                    if st.session_state.step_d == 6: st.session_state.step_d = 7
                    else: registrar_error("No se puede cerrar la compuerta exterior antes de desconectar físicamente el receptáculo de rampa.")
                else: registrar_error("La compuerta permanece abierta durante el suministro activo de planta.")
                st.rerun()
            luz_door = "<div class='luz-f7x-off'>COMPUERTA CERRADA</div>" if modo_operacion == "DESENERGIZACIÓN COMPLETA (SHUTDOWN)" and st.session_state.step_d >= 7 else "<div class='luz-f7x-verde'>COMPUERTA ABIERTA</div>"
            st.markdown(luz_door, unsafe_allow_html=True)

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
        st.markdown("<div class='consola-gris' style='padding: 15px; margin-bottom: 15px;'>", unsafe_allow_html=True)
        st.markdown("<div style='color: #f87171; font-weight: bold; font-size: 0.85rem; margin-bottom: 8px; text-align: center;'>EMERGENCY BOX (MANDO SEPARADO)</div>", unsafe_allow_html=True)
        
        if st.button("🔘 RAT AUTO", key="ratauto"):
            if modo_operacion == "ENERGIZACIÓN COMPLETA (COLD OPERATIONS)":
                if st.session_state.step_e == 5: st.session_state.step_e = 6
                else: registrar_error("RAT AUTO accionada fuera del orden estipulado de O.T.")
            else:
                if st.session_state.step_d == 2: st.session_state.step_d = 3
                else: registrar_error("La protección RAT AUTO debe ser liberada a su posición normal inmediatamente después de pasar las baterías a OFF.")
            st.rerun()
        luz_rat = "<div class='luz-f7x-amber'>INHIBIT</div>" if (modo_operacion == "ENERGIZACIÓN COMPLETA (COLD OPERATIONS)" and st.session_state.step_e >= 6) or (modo_operacion == "DESENERGIZACIÓN COMPLETA (SHUTDOWN)" and st.session_state.step_d < 3) else "<div class='luz-f7x-off'>OFF (NORMAL POSITION)</div>"
        st.markdown(luz_rat, unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

        st.markdown("<div class='consola-gris' style='padding: 15px; margin-bottom: 15px; background-color: #1e293b;'>", unsafe_allow_html=True)
        st.markdown("<div style='color: #38bdf8; font-weight: bold; font-size: 0.85rem; margin-bottom: 8px; text-align: center;'>⚙️ CONTROL DE COMBUSTIBLE Y MOTOR DE LA GPU</div>", unsafe_allow_html=True)
        
        if st.button("🛑 DETENER MOTOR GPU", key="stop_gpu_engine"):
            if modo_operacion == "DESENERGIZACIÓN COMPLETA (SHUTDOWN)":
                if st.session_state.step_d == 4: st.session_state.step_d = 5
                else: registrar_error("No se puede detener el motor de la planta sin antes pasar el Switch Externo GPU a la posición OFF.")
            else: registrar_error("Acción inválida en fase de suministro continuo.")
            st.rerun()
        luz_engine = "<div class='luz-f7x-off'>MOTOR APAGADO</div>" if (modo_operacion == "DESENERGIZACIÓN COMPLETA (SHUTDOWN)" and st.session_state.step_d >= 5) or (modo_operacion == "ENERGIZACIÓN COMPLETA (COLD OPERATIONS)" and st.session_state.step_e == 0) else "<div class='luz-f7x-verde'>MOTOR RUNNING</div>"
        st.markdown(luz_engine, unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

        # Telemetría CRT
        if modo_operacion == "ENERGIZACIÓN COMPLETA (COLD OPERATIONS)":
            v_gpu = "28.0 VDC" if st.session_state.step_e >= 2 else "0.0 VDC"
            v_ess = "28.1 V" if st.session_state.step_e >= 9 else "0.0 V"
            s_isol = "CONECTADO [── GREEN ──]" if st.session_state.step_e >= 11 else "AISLADO [| AMBER |]"
            pasos_completados = st.session_state.step_e == 12
        else:
            v_gpu = "0.0 VDC" if st.session_state.step_d >= 5 else "28.0 VDC"
            v_ess = "0.0 V" if st.session_state.step_d >= 1 else "28.1 V"
            s_isol = "AISLADO [| AMBER |]" if st.session_state.step_d >= 1 else "CONECTADO [── GREEN ──]"
            pasos_completados = st.session_state.step_d == 7

        if st.session_state.error_activo:
            clase_pantalla = "crt-error"
            status_cas = f"🚨 CAS ALERT: ERROR PROCEDIMENTAL INDEBIDO\n\n  DETALLE: {st.session_state.msg_error}\n\n  [O.T. QUEBRADA]: Operador militar rompió la secuencia.\n  Presione el botón rojo de corrección para reiniciar."
        elif pasos_completados:
            clase_pantalla = "crt-normal"
            status_cas = "⚡ SYSTEMS STATUS: SECUENCIA CONCLUIDA CON ÉXITO\n\n  El procedimiento cumple al 100% las normativas técnicas e instrucciones\n  del manual Dassault para el Grupo de Transporte Aéreo Especial."
        else:
            clase_pantalla = "crt-normal"
            status_cas = "📲 MODO EVALUACIÓN COMPLETA ACTIVO\n\n  Las instrucciones visuales han sido removidas de la pantalla CRT.\n  El operador militar debe accionar los interruptores guiándose por su O.T."

        pantalla_html = f"""
        <div class='crt-easy-display {clase_pantalla}'>
<div class='crt-header'><span>SISTEMA: HONEYWELL EASY PDU 1</span><span>MODO: EVALUACIÓN</span></div>
⚙️ TELEMETRÍA DE RED DE BARRAS EN TIEMPO REAL (ATA 24):
 • FEEDER DE ENTRADA GPU TIERRA : {v_gpu}
 • LH ESSENTIAL BUS RED LINE    : {v_ess}
 • RH ESSENTIAL BUS RED LINE    : {v_ess}
 • CONTACTOR DE AISLAMIENTO ISOL: {s_isol}
----------------------------------------------------------------------
🔔 CREW ALERTING SYSTEM (CAS) & MONITOR:
{status_cas}
        </div>
        """
        st.markdown(pantalla_html, unsafe_allow_html=True)

# ------------------------------------------------------------------
# DESARROLLO DEL MÓDULO II: SISTEMA DE COMBUSTIBLE (ATA 28)
# ------------------------------------------------------------------
elif modulo_seleccionado == "MÓDULO II: SISTEMA DE COMBUSTIBLE (ATA 28)":
    st.title("⛽ Módulo II: Gestión de Combustible ATA 28")
    st.subheader("Simulación de Tanques de la Aeronave y Panel de Control de Válvulas / Bombas")
    st.markdown("---")
    
    st.warning("🚧 MÓDULO EN DESARROLLO ARQUITECTÓNICO 🚧")
    st.markdown("""
        ### Próximos pasos operativos para este panel:
        Este espacio está listo para mapear la cabina de combustible del Falcon 7X. Aquí podremos simular:
        * **Tanques de Combustible:** Tanque Izquierdo (LH), Tanque Central (Center) y Tanque Derecho (RH).
        * **Interconexión de Barras e Inter-Crossfeed:** Válvulas de transferencia Cruzada y alimentación cruzada.
        * **Boost Pumps:** Activación y control de las bombas principales y auxiliares de inyección a los motores.
        * **Monitoreo de Telemetría (EASy Display):** Cantidad de combustible en libras/kilogramos, estado de flujo y presiones de línea en tiempo real.
    """)
    
    # Contenedor gráfico simulado para el panel de combustible
    st.markdown("<div class='consola-gris'><div class='titulo-dc'>⛽ REPLICA PANEL DE COMBUSTIBLE OVERHEAD (PRÓXIMAMENTE)</div>", unsafe_allow_html=True)
    c_fuel = st.columns(3)
    with c_fuel[0]:
        st.button("TANK LH PUMPS", disabled=True)
        st.markdown("<div class='luz-f7x-off'>INOP</div>", unsafe_allow_html=True)
    with c_fuel[1]:
        st.button("X-FEED VALVE", disabled=True)
        st.markdown("<div class='luz-f7x-off'>INOP</div>", unsafe_allow_html=True)
    with c_fuel[2]:
        st.button("TANK RH PUMPS", disabled=True)
        st.markdown("<div class='luz-f7x-off'>INOP</div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)
