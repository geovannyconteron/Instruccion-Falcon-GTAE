import streamlit as st
import streamlit.components.v1 as components
import time

# Configuración de la cabina táctica FAE
st.set_page_config(page_title="Falcon 7X Flight Deck - GTAE", page_icon="✈️", layout="wide")

# ==============================================================================
# SCRIPT DE AUDIO INSTANTÁNEO MECÁNICO (COCKPIT CLICK)
# ==============================================================================
components.html("""
    <script>
    const parentDoc = window.parent.document;
    function playCockpitClick() {
        try {
            const AudioContext = window.AudioContext || window.webkitAudioContext;
            const ctx = new AudioContext();
            const osc = ctx.createOscillator();
            const gain = ctx.createGain();
            osc.type = 'triangle';
            osc.frequency.setValueAtTime(160, ctx.currentTime);
            osc.frequency.exponentialRampToValueAtTime(40, ctx.currentTime + 0.04);
            gain.gain.setValueAtTime(0.4, ctx.currentTime);
            gain.gain.exponentialRampToValueAtTime(0.01, ctx.currentTime + 0.04);
            osc.connect(gain);
            gain.connect(ctx.destination);
            osc.start();
            osc.stop(ctx.currentTime + 0.04);
        } catch(e) {}
    }
    parentDoc.addEventListener('click', function(e) {
        const target = e.target;
        if (target && (target.tagName === 'BUTTON' || target.closest('button'))) {
            playCockpitClick();
        }
    }, true);
    </script>
""", height=0, width=0)

# ==============================================================================
# DISEÑO SKEUOMÓRFICO TRIDIMENSIONAL DE CABINA (CSS)
# ==============================================================================
st.markdown("""
    <style>
    .main { background-color: #0b0f19; color: #e2e8f0; font-family: 'Segoe UI', sans-serif; }
    .overhead-frame { background: linear-gradient(145deg, #1e2530, #131822); border: 6px solid #2d3748; border-radius: 12px; padding: 25px; box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.8); margin-bottom: 25px; }
    .subpanel-3d { background: linear-gradient(180deg, #1a202c, #11141d); border-left: 4px solid #0f1219; border-top: 4px solid #0f1219; border-right: 4px solid #2d3748; border-bottom: 4px solid #2d3748; border-radius: 8px; padding: 18px; margin-bottom: 15px; box-shadow: inset 0 4px 8px rgba(0,0,0,0.6); }
    .titulo-serigrafia { color: #94a3b8; font-family: 'Courier New', monospace; font-weight: bold; font-size: 0.9rem; text-align: center; letter-spacing: 2px; margin-bottom: 12px; text-transform: uppercase; }
    .linea-tactica { border-top: 2px solid #4a5568; border-bottom: 1px solid #1a202c; margin: 15px 0; }
    
    .stButton>button { 
        width: 100%; font-weight: bold; height: 54px; border-radius: 6px; font-size: 0.8rem; font-family: 'Courier New', monospace;
        background: linear-gradient(180deg, #334155, #1e293b) !important; color: #e2e8f0 !important;
        border-top: 2px solid #64748b !important; border-left: 2px solid #475569 !important; border-right: 2px solid #0f172a !important; border-bottom: 3px solid #0f172a !important;
        box-shadow: 0 6px 10px rgba(0,0,0,0.4); transition: all 0.1s ease;
    }
    .stButton>button:active { transform: translateY(3px); box-shadow: 0 2px 4px rgba(0,0,0,0.6); border-top: 2px solid #0f172a !important; border-bottom: 1px solid #475569 !important; }
    
    .anunciador-verde { background-color: #042f1a; color: #4ade80; border: 2px solid #22c55e; font-weight: bold; text-align: center; border-radius: 4px; font-size: 0.75rem; padding: 5px; box-shadow: 0 0 12px rgba(34, 197, 94, 0.6); }
    .anunciador-amber { background-color: #451a03; color: #fbbf24; border: 2px solid #f59e0b; font-weight: bold; text-align: center; border-radius: 4px; font-size: 0.75rem; padding: 5px; box-shadow: 0 0 12px rgba(245, 158, 11, 0.6); }
    .anunciador-apagado { background-color: #181f2a; color: #4b5563; border: 2px solid #374151; text-align: center; border-radius: 4px; font-size: 0.75rem; padding: 5px; box-shadow: inset 0 2px 4px rgba(0,0,0,0.5); }
    
    .pantalla-mfd { font-family: 'Courier New', monospace; border: 5px solid #334155; background-color: #04070e; color: #38bdf8; padding: 22px; border-radius: 8px; min-height: 520px; box-shadow: inset 0 0 30px rgba(0,0,0,0.9); white-space: pre-wrap; }
    .display-digital-principal { background-color: #020203; border: 3px solid #475569; border-radius: 6px; color: #f87171; font-family: 'Courier New', monospace; font-size: 2.4rem; font-weight: bold; text-align: center; padding: 12px; box-shadow: inset 0 0 20px rgba(239, 68, 68, 0.4); }
    .display-digital-secundario { background-color: #020203; border: 2px solid #475569; border-radius: 6px; color: #fbbf24; font-family: 'Courier New', monospace; font-size: 1.6rem; font-weight: bold; text-align: center; padding: 8px; box-shadow: inset 0 0 12px rgba(245, 158, 11, 0.3); }
    .portada-container { background: linear-gradient(rgba(15,23,42,0.85), rgba(15,23,42,0.95)); border: 2px solid #3b82f6; padding: 30px; border-radius: 10px; text-align: center; margin-bottom: 25px; }
    </style>
""", unsafe_allow_html=True)

# ==============================================================================
# SISTEMA DE LOGIN DE SEGURIDAD
# ==============================================================================
if "autenticado" not in st.session_state: st.session_state.autenticado = False

if not st.session_state.autenticado:
    st.markdown("<br><br>", unsafe_allow_html=True)
    _, col_login, _ = st.columns([1, 1.4, 1])
    with col_login:
        st.markdown("<div style='background: linear-gradient(135deg, #1e293b, #0f172a); border: 3px solid #3b82f6; padding: 35px; border-radius: 12px; text-align: center;'><h1 style='color: #ffffff; font-size: 1.6rem; font-family: monospace;'>FLIGHT DECK PANEL SIMULATOR</h1><h3 style='color: #3b82f6; font-size: 1.1rem; font-family: monospace;'>FALCON 7X - GTAE</h3></div>", unsafe_allow_html=True)
        st.image("https://images.unsplash.com/photo-1540962351504-03099e0a754b?q=80&w=1200&auto=format&fit=crop", caption="Grupo de Transporte Aéreo Especial - FAE", use_container_width=True)
        with st.form("credenciales_cabina"):
            st.markdown("<h5 style='text-align: center; color: #94a3b8;'>🔒 CONTROL DE SOBERANÍA Y ACCESO</h5>", unsafe_allow_html=True)
            txt_user = st.text_input("Identificador Técnico:", placeholder="gtae_operator")
            txt_pass = st.text_input("Clave de Bloqueo:", type="password", placeholder="••••••••")
            if st.form_submit_button("CONECTAR SISTEMAS EMBARCADOS"):
                if txt_user == "gtae" and txt_pass == "7X2026":
                    st.session_state.autenticado = True
                    st.rerun()
                else: st.error("Credenciales incorrectas.")
    st.stop()

# ==============================================================================
# MEMORIAS OPERACIONALES E INICIALIZACIONES GLOBALES
# ==============================================================================
if "audio_alarma" not in st.session_state: st.session_state.audio_alarma = None
if "fase_e" not in st.session_state: st.session_state.fase_e = 0
if "fase_d" not in st.session_state: st.session_state.fase_d = 0
if "falla_procedimiento" not in st.session_state: st.session_state.falla_procedimiento = False
if "descripcion_falla" not in st.session_state: st.session_state.descripcion_falla = ""

if "apu_status" not in st.session_state: st.session_state.apu_status = "OFF"
if "apu_rpm" not in st.session_state: st.session_state.apu_rpm = 0
if "bleed_valve" not in st.session_state: st.session_state.bleed_valve = "CLOSED"
if "eng_selected" not in st.session_state: st.session_state.eng_selected = None
if "eng_phase" not in st.session_state: st.session_state.eng_phase = "STBY"
if "motor_n1" not in st.session_state: st.session_state.motor_n1 = [0.0, 0.0, 0.0]
if "motor_n2" not in st.session_state: st.session_state.motor_n2 = [0.0, 0.0, 0.0]
if "motor_itt" not in st.session_state: st.session_state.motor_itt = [15, 15, 15]
if "lever_run" not in st.session_state: st.session_state.lever_run = [False, False, False]
if "start_error" not in st.session_state: st.session_state.start_error = None

if "combustible_actual" not in st.session_state: st.session_state.combustible_actual = 1150
if "combustible_objetivo" not in st.session_state: st.session_state.combustible_objetivo = 10500
if "valvula_izq" not in st.session_state: st.session_state.valvula_izq = "OFF"
if "valvula_ctr" not in st.session_state: st.session_state.valvula_ctr = "OFF"
if "valvula_der" not in st.session_state: st.session_state.valvula_der = "OFF"
if "bombeo_activo" not in st.session_state: st.session_state.bombeo_activo = False

# Ejecución de alarmas sonoras transitorias
if st.session_state.audio_alarma == "alarma_critica":
    components.html("<script>try{const ctx=new(window.AudioContext||window.webkitAudioContext)();const osc=ctx.createOscillator();const gain=ctx.createGain();osc.type='sawtooth';osc.frequency.setValueAtTime(380,ctx.currentTime);gain.gain.setValueAtTime(0.3,ctx.currentTime);osc.connect(gain);gain.connect(ctx.destination);osc.start();setTimeout(()=>{osc.stop();},1000);}catch(e){}</script>", height=0, width=0)
    st.session_state.audio_alarma = None
elif st.session_state.audio_alarma == "carga_completa":
    components.html("<script>try{const ctx=new(window.AudioContext||window.webkitAudioContext)();const osc=ctx.createOscillator();osc.type='sine';osc.frequency.setValueAtTime(520,ctx.currentTime);osc.connect(ctx.destination);osc.start();setTimeout(()=>{osc.stop();},400);}catch(e){}</script>", height=0, width=0)
    st.session_state.audio_alarma = None

# Lógica del motor APU (Módulo III)
if st.session_state.apu_status == "STARTING":
    st.session_state.apu_rpm += 20
    if st.session_state.apu_rpm >= 100:
        st.session_state.apu_rpm = 100
        st.session_state.apu_status = "RUN"
    time.sleep(0.1)
    st.rerun()

# Lógica de rotación neumática de motores (Módulo III)
if st.session_state.eng_selected is not None and st.session_state.start_error is None:
    idx = st.session_state.eng_selected - 1
    if st.session_state.eng_phase == "CRANK":
        st.session_state.motor_n2[idx] += 2.5
        if st.session_state.motor_n2[idx] >= 18.0:
            if st.session_state.lever_run[idx]: st.session_state.eng_phase = "IGN"
            elif st.session_state.motor_n2[idx] >= 25.0: st.session_state.motor_n2[idx] = 25.0
        time.sleep(0.1)
        st.rerun()
    elif st.session_state.eng_phase == "IGN":
        st.session_state.motor_n2[idx] += 3.0
        st.session_state.motor_itt[idx] += 45
        if st.session_state.motor_itt[idx] >= 520: st.session_state.eng_phase = "RUN"
        time.sleep(0.1)
        st.rerun()
    elif st.session_state.eng_phase == "RUN":
        if st.session_state.motor_n2[idx] < 57.4: st.session_state.motor_n2[idx] += 2.0
        else: st.session_state.motor_n2[idx] = 57.4
        if st.session_state.motor_n1[idx] < 24.0: st.session_state.motor_n1[idx] += 1.5
        else: st.session_state.motor_n1[idx] = 24.2
        if st.session_state.motor_itt[idx] > 490: st.session_state.motor_itt[idx] -= 10
        else: st.session_state.motor_itt[idx] = 490
        time.sleep(0.1)
        st.rerun()

# Lógica del camión cisterna (Módulo II)
if st.session_state.bombeo_activo and st.session_state.combustible_actual < st.session_state.combustible_objetivo:
    st.session_state.combustible_actual += 400
    if st.session_state.combustible_actual >= st.session_state.combustible_objetivo:
        st.session_state.combustible_actual = st.session_state.combustible_objetivo
        st.session_state.bombeo_activo = False
        st.session_state.audio_alarma = "carga_completa"
    st.rerun()

# ==============================================================================
# NAVEGACIÓN EN BARRA LATERAL (SEPARACIÓN POR ENTORNO RESTRINGIDO)
# ==============================================================================
with st.sidebar:
    st.markdown("<h3 style='color: #38bdf8; font-family: monospace;'>🖥️ CONSOLA DE CONFIGURACIÓN FAE</h3>", unsafe_allow_html=True)
    entorno_activo = st.radio(
        "SELECCIONE EL TIPO DE PROCEDIMIENTO:",
        ["✈️ PANTALLAS DE PROCEDIMIENTOS OPERATIVOS", "🔧 PANTALLAS DE MANTENIMIENTO"]
    )
    st.markdown("---")
    
    if entorno_activo == "✈️ PANTALLAS DE PROCEDIMIENTOS OPERATIVOS":
        modulo_activo = st.radio("MÓDULOS DE VUELO DISPONIBLES:", ["MÓDULO III: ARRANCADO DE MOTORES (PW307A)"])
    else:
        modulo_activo = st.radio("MÓDULOS MECÁNICOS DISPONIBLES:", ["MÓDULO I: DISTRIBUCIÓN ELÉCTRICA (ATA 24)", "MÓDULO II: PRESIÓN DE COMBUSTIBLE (ATA 28)"])

# ------------------------------------------------------------------------------
# PANTALLA 1: PROCEDIMIENTOS OPERATIVOS (PILOTOS)
# ------------------------------------------------------------------------------
if entorno_activo == "✈️ PANTALLAS DE PROCEDIMIENTOS OPERATIVOS":
    st.title("✈️ Pantalla de Procedimientos Operativos (Pilotos)")
    st.subheader("Entrenamiento de Vuelo - Engine Start Panel System")
    st.markdown("---")
    
    col_panels, col_easy_engine = st.columns([1.2, 1])
    
    with col_panels:
        st.markdown("<div class='overhead-frame'>", unsafe_allow_html=True)
        st.markdown("<div class='subpanel-3d'><div class='titulo-serigrafia'>Auxiliary Power Unit (APU)</div>", unsafe_allow_html=True)
        c_apu = st.columns(3)
        with c_apu[0]:
            if st.button("APU MASTER"):
                if st.session_state.apu_status == "OFF": st.session_state.apu_status = "STARTING"
                else:
                    st.session_state.apu_status = "OFF"
                    st.session_state.apu_rpm = 0
                    st.session_state.bleed_valve = "CLOSED"
                st.rerun()
            st.markdown(f"<div class='anunciador-verde'>{'ON' if st.session_state.apu_status != 'OFF' else 'OFF'}</div>", unsafe_allow_html=True)
        with c_apu[1]:
            st.markdown(f"<div class='display-digital-secundario' style='font-size:1.2rem; padding:15px;'>RPM: {st.session_state.apu_rpm}%</div>", unsafe_allow_html=True)
        with c_apu[2]:
            if st.button("APU BLEED VALVE"):
                if st.session_state.apu_status == "RUN":
                    st.session_state.bleed_valve = "OPEN" if st.session_state.bleed_valve == "CLOSED" else "CLOSED"
                else: st.error("No hay presión neumática. Inicialice la APU.")
                st.rerun()
            st.markdown(f"<div class='anunciador-amber'>BLEED: {st.session_state.bleed_valve}</div>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)
        
        st.markdown("<div class='subpanel-3d'><div class='titulo-serigrafia'>MAN START PANEL</div>", unsafe_allow_html=True)
        c_eng = st.columns(3)
        for i in range(3):
            with c_eng[i]:
                st.markdown(f"<div style='text-align:center; font-weight:bold; margin-bottom:5px;'>ENGINE {i+1}</div>", unsafe_allow_html=True)
                if st.button(f"ENG {i+1} START"):
                    if st.session_state.bleed_valve == "OPEN":
                        st.session_state.eng_selected = i + 1
                        st.session_state.eng_phase = "CRANK"
                        st.session_state.start_error = None
                    else: st.session_state.start_error = f"FALLO DE ARRANQUE EN MOTOR {i+1}: Presión neumática insuficiente (APU BLEED CLOSED)."
                    st.rerun()
                if st.session_state.eng_selected == (i + 1):
                    lbl_anz = st.session_state.eng_phase
                    clase_anz = "anunciador-verde" if lbl_anz == "RUN" else "anunciador-amber"
                else:
                    lbl_anz = "STBY"
                    clase_anz = "anunciador-apagado"
                st.markdown(f"<div class='{clase_anz}'>{lbl_anz}</div>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)
        
        st.markdown("<div class='subpanel-3d'><div class='titulo-serigrafia'>Pedestal Fuel Control Levers</div>", unsafe_allow_html=True)
        c_levers = st.columns(3)
        for i in range(3):
            with c_levers[i]:
                lbl_lever = "🔥 RUN (FUEL ON)" if st.session_state.lever_run[i] else "❄️ SHUT OFF"
                if st.button(lbl_lever, key=f"lev_{i}"):
                    st.session_state.lever_run[i] = not st.session_state.lever_run[i]
                    if st.session_state.lever_run[i] and st.session_state.eng_selected == (i+1) and st.session_state.motor_n2[i] < 15.0:
                        st.session_state.start_error = f"🚨 ALERT CAS: HOT START IN ENGINE {i+1}!\n Combustible inyectado con rotación N2 inferior al límite mínimo de ignición."
                    st.rerun()
        st.markdown("</div>", unsafe_allow_html=True)
        
        if st.button("🚨 RESTABLECER SIMULACIÓN DE ARRANQUE"):
            st.session_state.apu_status = "OFF"
            st.session_state.apu_rpm = 0
            st.session_state.bleed_valve = "CLOSED"
            st.session_state.eng_selected = None
            st.session_state.eng_phase = "STBY"
            st.session_state.motor_n1 = [0.0, 0.0, 0.0]
            st.session_state.motor_n2 = [0.0, 0.0, 0.0]
            st.session_state.motor_itt = [15, 15, 15]
            st.session_state.lever_run = [False, False, False]
            st.session_state.start_error = None
            st.rerun()
        st.markdown("</div>", unsafe_allow_html=True)

    with col_easy_engine:
        st.markdown("### 📺 Honeywell EASy - Engine Synoptic Display")
        color_b = "#ef4444" if st.session_state.start_error is not None else "#475569"
        fondo_b = "#2d1a1a" if st.session_state.start_error is not None else "#04070e"
        texto_b = "#fca5a5" if st.session_state.start_error is not None else "#38bdf8"
        
        st.markdown(f"""
            <div class="pantalla-mfd" style="border-color: {color_b}; background-color: {fondo_b}; color: {texto_b}; font-size:0.82rem;">
<div style="display: flex; justify-content: space-between; border-bottom: 2px solid #334155; padding-bottom: 5px; margin-bottom: 15px; font-weight: bold;"><span>HONEYWELL EASy: ENGINE SYNOPTIC</span><span>ATA: 70/72</span></div>
📊 PARÁMETROS CRÍTICOS EN TIEMPO REAL:

 ENGINE 1 (LH MOTOR)  |  ENGINE 2 (CENTER)     |  ENGINE 3 (RH MOTOR)
 ---------------------|------------------------|---------------------
 • N1: {st.session_state.motor_n1[0]:04.1f}%          | • N1: {st.session_state.motor_n1[1]:04.1f}%           | • N1: {st.session_state.motor_n1[2]:04.1f}%
 • N2: {st.session_state.motor_n2[0]:04.1f}%          | • N2: {st.session_state.motor_n2[1]:04.1f}%           | • N2: {st.session_state.motor_n2[2]:04.1f}%
 • ITT: {st.session_state.motor_itt[0]} °C          | • ITT: {st.session_state.motor_itt[1]} °C           | • ITT: {st.session_state.motor_itt[2]} °C
 • LEVER: {'RUN' if st.session_state.lever_run[0] else 'SHUTOFF'}     | • LEVER: {'RUN' if st.session_state.lever_run[1] else 'SHUTOFF'}      | • LEVER: {'RUN' if st.session_state.lever_run[2] else 'SHUTOFF'}

 ──────────────────────── STATUS DE COMPRESIÓN ────────────────────────
 
 APU AIR PRESSURE STATUS: [ {'DISPONIBLE' if st.session_state.bleed_valve == 'OPEN' else 'NO DETECTADA'} ]
 ENG IGNITION STATUS    : [ {'ACTIVE (IGN)' if st.session_state.eng_phase == 'IGN' else 'STBY/NOMINAL'} ]

----------------------------------------------------------------------
🔔 CREW ALERTING SYSTEM (CAS) - ALARMAS DE MOTOR:

{st.session_state.start_error if st.session_state.start_error is not None else '🟢 SYSTEMS GENERAL RUN NOMINAL\n Parámetros operacionales dentro de los límites estipulados por el fabricante.'}
            </div>
        """, unsafe_allow_html=True)

# ------------------------------------------------------------------------------
# PANTALLA 2: PROCEDIMIENTOS DE MANTENIMIENTO (TÉCNICOS)
# ------------------------------------------------------------------------------
else:
    st.title("🔧 Pantalla de Procedimientos de Mantenimiento (Técnicos)")
    st.markdown("---")
    
    if modulo_activo == "MÓDULO I: DISTRIBUCIÓN ELÉCTRICA (ATA 24)":
        st.subheader("Módulo I: Distribución Eléctrica y Gestión de Barras en Cabina Completa")
        procedimiento = st.radio("⚙️ SELECCIONE PROCEDIMIENTO DE EVALUACIÓN:", ["ENERGIZACIÓN COMPLETA (COLD OPERATIONS)", "DESENERGIZACIÓN COMPLETA (SHUTDOWN)"], horizontal=True)
        
        if "procedimiento_previo" not in st.session_state:
            st.session_state.procedimiento_previo = procedimiento
        elif st.session_state.procedimiento_previo != procedimiento:
            st.session_state.fase_e = 0
            st.session_state.fase_d = 0
            st.session_state.falla_procedimiento = False
            st.session_state.descripcion_falla = ""
            st.session_state.procedimiento_previo = procedimiento

        def forzar_alarma(texto):
            st.session_state.falla_procedimiento = True
            st.session_state.descripcion_falla = text
            st.session_state.audio_alarma = "alarma_critica"

        col_fisica_panel, col_telemetria_pdu = st.columns([1.3, 1])
        with col_fisica_panel:
            st.markdown("<div class='overhead-frame'>", unsafe_allow_html=True)
            
            # FILA SUPERIOR DEL OVERHEAD
            st.markdown("<div class='subpanel-3d'><div class='titulo-serigrafia'>⚡ DC SUPPLY PANEL ⚡</div>", unsafe_allow_html=True)
            grid_sup = st.columns(8)
            with grid_sup[0]:
                st.button("GALLEY MSTR", disabled=True, key="mstr_g")
                st.markdown("<div class='anunciador-apagado'>OFF</div>", unsafe_allow_html=True)
            with grid_sup[1]:
                if st.button("LH MSTR", key="l_mstr_24"):
                    if procedimiento == "ENERGIZACIÓN COMPLETA (COLD OPERATIONS)":
                        if st.session_state.fase_e == 11: st.session_state.fase_e = 12
                        else: forzar_alarma("LH MASTER activado de forma prematura fuera de la secuencia técnica.")
                    else: forzar_alarma("LH MASTER se mantiene enclavado automáticamente.")
                    st.rerun()
                luz = "<div class='anunciador-verde'>ON</div>" if (procedimiento == "ENERGIZACIÓN COMPLETA (COLD OPERATIONS)" and st.session_state.fase_e >= 12) or procedimiento == "DESENERGIZACIÓN COMPLETA (SHUTDOWN)" else "<div class='anunciador-amber'>OFF</div>"
                st.markdown(luz, unsafe_allow_html=True)
            with grid_sup[2]:
                if st.button("LH INIT", key="lh_init_24"):
                    if procedimiento == "ENERGIZACIÓN COMPLETA (COLD OPERATIONS)":
                        if st.session_state.fase_e == 7: st.session_state.fase_e = 8
                        else: forzar_alarma("LH INIT accionado sin acoplamiento estructural del BUS TIE.")
                    else: forzar_alarma("LH INIT protegido por solenoide de retención.")
                    st.rerun()
                luz = "<div class='anunciador-apagado'>RUN</div>" if (procedimiento == "ENERGIZACIÓN COMPLETA (COLD OPERATIONS)" and st.session_state.fase_e >= 8) or procedimiento == "DESENERGIZACIÓN COMPLETA (SHUTDOWN)" else "<div class='anunciador-amber'>OFF</div>"
                st.markdown(luz, unsafe_allow_html=True)
            with grid_sup[3]:
                if st.button("BUS TIE", key="bt_24"):
                    if procedimiento == "ENERGIZACIÓN COMPLETA (COLD OPERATIONS)":
                        if st.session_state.fase_e == 6: st.session_state.fase_e = 7
                        else: forzar_alarma("BUS TIE accionado previo al armado de seguridad de la RAT.")
                    else: forzar_alarma("Corte directo inhabilitado de barras.")
                    st.rerun()
                luz = "<div class='anunciador-amber'>TIED</div>" if (procedimiento == "ENERGIZACIÓN COMPLETA (COLD OPERATIONS)" and st.session_state.fase_e >= 7) or procedimiento == "DESENERGIZACIÓN COMPLETA (SHUTDOWN)" else "<div class='anunciador-apagado'>AUTO</div>"
                st.markdown(luz, unsafe_allow_html=True)
            with grid_sup[4]:
                if st.button("RH INIT", key="rh_init_24"):
                    if procedimiento == "ENERGIZACIÓN COMPLETA (COLD OPERATIONS)":
                        if st.session_state.fase_e == 7: st.session_state.fase_e = 8
                        else: forzar_alarma("RH INIT accionado sin acoplamiento estructural del BUS TIE.")
                    else: forzar_alarma("RH INIT protegido por solenoide de retención.")
                    st.rerun()
                luz = "<div class='anunciador-apagado'>RUN</div>" if (procedimiento == "ENERGIZACIÓN COMPLETA (COLD OPERATIONS)" and st.session_state.fase_e >= 8) or procedimiento == "DESENERGIZACIÓN COMPLETA (SHUTDOWN)" else "<div class='anunciador-amber'>OFF</div>"
                st.markdown(luz, unsafe_allow_html=True)
            with grid_sup[5]:
                if st.button("RH MSTR", key="rh_mstr_24"):
                    if procedimiento == "ENERGIZACIÓN COMPLETA (COLD OPERATIONS)":
                        if st.session_state.fase_e == 11: st.session_state.fase_e = 12
                        else: forzar_alarma("RH MASTER activado de forma prematura.")
                    else: forzar_alarma("RH MASTER se mantiene enclavado automáticamente.")
                    st.rerun()
                luz = "<div class='anunciador-verde'>ON</div>" if (procedimiento == "ENERGIZACIÓN COMPLETA (COLD OPERATIONS)" and st.session_state.fase_e >= 12) or procedimiento == "DESENERGIZACIÓN COMPLETA (SHUTDOWN)" else "<div class='anunciador-amber'>OFF</div>"
                st.markdown(luz, unsafe_allow_html=True)
            with grid_sup[6]:
                if st.button("CABIN MSTR", key="cabin_24"):
                    if procedimiento == "ENERGIZACIÓN COMPLETA (COLD OPERATIONS)":
                        if st.session_state.fase_e == 9: st.session_state.fase_e = 10
                        else: forzar_alarma("CABIN MASTER accionado sin alimentación estable.")
                    else: forzar_alarma("El disyuntor comercial se drena automáticamente.")
                    st.rerun()
                luz = "<div class='anunciador-amber'>OFF</div>" if (procedimiento == "ENERGIZACIÓN COMPLETA (COLD OPERATIONS)" and st.session_state.fase_e >= 10) or procedimiento == "DESENERGIZACIÓN COMPLETA (SHUTDOWN)" else "<div class='anunciador-verde'>ON</div>"
                st.markdown(luz, unsafe_allow_html=True)
            with grid_sup[7]:
                if st.button("EXT PWR", key="ext_pwr_24"):
                    if procedimiento == "ENERGIZACIÓN COMPLETA (COLD OPERATIONS)":
                        if st.session_state.fase_e == 8: st.session_state.fase_e = 9
                        else: forzar_alarma("EXT POWER conectado sin configurar parámetros nominales de la GPU.")
                    else:
                        if st.session_state.fase_d == 0: st.session_state.fase_d = 1
                        else: forzar_alarma("EXT POWER debe ser deprimido en primera instancia.")
                    st.rerun()
                luz = "<div class='anunciador-verde'>ONLINE</div>" if (procedimiento == "ENERGIZACIÓN COMPLETA (COLD OPERATIONS)" and st.session_state.fase_e >= 9) or (procedimiento == "DESENERGIZACIÓN COMPLETA (SHUTDOWN)" and st.session_state.fase_d < 1) else "<div class='anunciador-apagado'>OFF</div>"
                st.markdown(luz, unsafe_allow_html=True)
            st.markdown("</div>", unsafe_allow_html=True)
            
            st.markdown("<div class='linea-tactica'></div>", unsafe_allow_html=True)
            
            # FILA INFERIOR DEL OVERHEAD
            st.markdown("<div class='subpanel-3d'>", unsafe_allow_html=True)
            grid_inf = st.columns(8)
            with grid_inf[0]: st.button("GEN 1", disabled=True, key="g1_24"); st.markdown("<div class='anunciador-apagado'>OFF</div>", unsafe_allow_html=True)
            with grid_inf[1]:
                if st.button("LH ISOL", key="l_isol_24"):
                    if procedimiento == "ENERGIZACIÓN COMPLETA (COLD OPERATIONS)":
                        if st.session_state.fase_e == 10: st.session_state.fase_e = 11
                        else: forzar_alarma("Válvula de aislamiento accionada antes de la carga comercial.")
                    else: forzar_alarma("El aislamiento ISOL se autoprotege.")
                    st.rerun()
                luz = "<div class='anunciador-apagado'>TIED</div>" if (procedimiento == "ENERGIZACIÓN COMPLETA (COLD OPERATIONS)" and st.session_state.fase_e >= 11) or procedimiento == "DESENERGIZACIÓN COMPLETA (SHUTDOWN)" else "<div class='anunciador-amber'>ISOL</div>"
                st.markdown(luz, unsafe_allow_html=True)
            with grid_inf[2]:
                if st.button("BAT 1", key="b1_24"):
                    if procedimiento == "ENERGIZACIÓN COMPLETA (COLD OPERATIONS)":
                        if st.session_state.fase_e == 4: st.session_state.fase_e = 5
                        else: forzar_alarma("BAT 1 activada sin comprobar el freno de rampa.")
                    else:
                        if st.session_state.fase_d == 1: st.session_state.fase_d = 2
                        else: forzar_alarma("BAT 1 debe apagarse tras deponer el EXT POWER.")
                    st.rerun()
                luz = "<div class='anunciador-verde'>AUTO</div>" if (procedimiento == "ENERGIZACIÓN COMPLETA (COLD OPERATIONS)" and st.session_state.fase_e >= 5) or (procedimiento == "DESENERGIZACIÓN COMPLETA (SHUTDOWN)" and st.session_state.fase_d < 2) else "<div class='anunciador-apagado'>OFF</div>"
                st.markdown(luz, unsafe_allow_html=True)
            with grid_inf[3]:
                if st.button("BAT 2", key="b2_24"):
                    if procedimiento == "ENERGIZACIÓN COMPLETA (COLD OPERATIONS)":
                        if st.session_state.fase_e == 4: st.session_state.fase_e = 5
                        else: forzar_alarma("BAT 2 activada sin comprobar el freno de rampa.")
                    else:
                        if st.session_state.fase_d == 1: st.session_state.fase_d = 2
                        else: forzar_alarma("BAT 2 debe apagarse tras deponer el EXT POWER.")
                    st.rerun()
                luz = "<div class='anunciador-verde'>AUTO</div>" if (procedimiento == "ENERGIZACIÓN COMPLETA (COLD OPERATIONS)" and st.session_state.fase_e >= 5) or (procedimiento == "DESENERGIZACIÓN COMPLETA (SHUTDOWN)" and st.session_state.fase_d < 2) else "<div class='anunciador-apagado'>OFF</div>"
                st.markdown(luz, unsafe_allow_html=True)
            with grid_inf[4]: st.button("RAT RSET", disabled=True, key="rat_24"); st.markdown("<div class='anunciador-apagado'>OFF</div>", unsafe_allow_html=True)
            with grid_inf[5]:
                if st.button("RH ISOL", key="r_isol_24"):
                    if procedimiento == "ENERGIZACIÓN COMPLETA (COLD OPERATIONS)":
                        if st.session_state.fase_e == 10: st.session_state.fase_e = 11
                        else: forzar_alarma("Válvula de aislamiento accionada antes de la carga comercial.")
                    else: forzar_alarma("El aislamiento ISOL se autoprotege.")
                    st.rerun()
                luz = "<div class='anunciador-apagado'>TIED</div>" if (procedimiento == "ENERGIZACIÓN COMPLETA (COLD OPERATIONS)" and st.session_state.fase_e >= 11) or procedimiento == "DESENERGIZACIÓN COMPLETA (SHUTDOWN)" else "<div class='anunciador-amber'>ISOL</div>"
                st.markdown(luz, unsafe_allow_html=True)
            with grid_inf[6]: st.button("GEN 2", disabled=True, key="g2_24"); st.markdown("<div class='anunciador-apagado'>OFF</div>", unsafe_allow_html=True)
            with grid_inf[7]: st.button("GEN 3", disabled=True, key="g3_24"); st.markdown("<div class='anunciador-apagado'>OFF</div>", unsafe_allow_html=True)
            st.markdown("</div>", unsafe_allow_html=True)
            
            st.markdown("<div class='linea-tactica'></div>", unsafe_allow_html=True)
            
            # CONTROL DE ENTRADA EN TIERRA (GPU COUPLING)
            st.markdown("<div class='subpanel-3d'><div class='titulo-serigrafia'>🔌 EXTERNAL GROUND POWER UNIT CONFIGURATION</div>", unsafe_allow_html=True)
            grid_rampa = st.columns(5)
            with grid_rampa[0]:
                if st.button("🔌 RECEPTÁCULO GPU", key="rec_24"):
                    if procedimiento == "ENERGIZACIÓN COMPLETA (COLD OPERATIONS)":
                        if st.session_state.fase_e == 0: st.session_state.fase_e = 1
                        else: forzar_alarma("Línea física acoplada fuera de secuencia.")
                    else:
                        if st.session_state.fase_d == 5: st.session_state.fase_d = 6
                        else: forzar_alarma("Desconexión física del mazo de cables sin deponer la planta eléctrica.")
                    st.rerun()
                luz = "<div class='anunciador-verde'>CONECTADO</div>" if (procedimiento == "ENERGIZACIÓN COMPLETA (COLD OPERATIONS)" and st.session_state.fase_e >= 1) or (procedimiento == "DESENERGIZACIÓN COMPLETA (SHUTDOWN)" and st.session_state.fase_d < 6) else "<div class='anunciador-apagado'>DESCONECTADO</div>"
                st.markdown(luz, unsafe_allow_html=True)
            with grid_rampa[1]:
                if st.button("⚡ POTENCIÓMETRO", key="pot_24"):
                    if procedimiento == "ENERGIZACIÓN COMPLETA (COLD OPERATIONS)":
                        if st.session_state.fase_e == 1: st.session_state.fase_e = 2
                        else: forzar_alarma("Regulación de voltaje modificada sin alimentación base de rampa.")
                    else: forzar_alarma("El reóstato permanece bloqueado.")
                    st.rerun()
                luz = "<div class='anunciador-verde'>28.0 VDC OK</div>" if (procedimiento == "ENERGIZACIÓN COMPLETA (COLD OPERATIONS)" and st.session_state.fase_e >= 2) or (procedimiento == "DESENERGIZACIÓN COMPLETA (SHUTDOWN)" and st.session_state.fase_d < 6) else "<div class='anunciador-apagado'>0.0 VDC</div>"
                st.markdown(luz, unsafe_allow_html=True)
            with grid_rampa[2]:
                if st.button("🎛️ BREAK SW GPU", key="brk_24"):
                    if procedimiento == "ENERGIZACIÓN COMPLETA (COLD OPERATIONS)":
                        if st.session_state.fase_e == 2: st.session_state.fase_e = 3
                        else: forzar_alarma("Breaker de protección cerrado sin tensión nominal.")
                    else:
                        if st.session_state.fase_d == 3: st.session_state.fase_d = 4
                        else: forzar_alarma("El breaker de protección debe desactivarse tras la RAT.")
                    st.rerun()
                luz = "<div class='anunciador-verde'>LÍNEA ONLINE</div>" if (procedimiento == "ENERGIZACIÓN COMPLETA (COLD OPERATIONS)" and st.session_state.fase_e >= 3) or (procedimiento == "DESENERGIZACIÓN COMPLETA (SHUTDOWN)" and st.session_state.fase_d < 4) else "<div class='anunciador-apagado'>LÍNEA OFF</div>"
                st.markdown(luz, unsafe_allow_html=True)
            with grid_rampa[3]:
                if st.button("⚙️ FRENO PARQUEO", key="frn_24"):
                    if procedimiento == "ENERGIZACIÓN COMPLETA (COLD OPERATIONS)":
                        if st.session_state.fase_e == 3: st.session_state.fase_e = 4
                        else: forzar_alarma("Freno de estacionamiento ignorado; riesgo de desplazamiento estructural.")
                    else: forzar_alarma("El freno permanece bloqueado.")
                    st.rerun()
                luz = "<div class='anunciador-verde'>ENGANCHADO</div>" if (procedimiento == "ENERGIZACIÓN COMPLETA (COLD OPERATIONS)" and st.session_state.fase_e >= 4) or procedimiento == "DESENERGIZACIÓN COMPLETA (SHUTDOWN)" else "<div class='anunciador-apagado'>LIBERADO</div>"
                st.markdown(luz, unsafe_allow_html=True)
            with grid_rampa[4]:
                if st.button("🚪 COMPUERTA RECEPT", key="door_24"):
                    if procedimiento == "DESENERGIZACIÓN COMPLETA (SHUTDOWN)":
                        if st.session_state.fase_d == 6: st.session_state.fase_d = 7
                        else: forzar_alarma("Intento de cierre con el mazo de cables acoplado.")
                    else: forzar_alarma("La compuerta estructural debe mantenerse abierta.")
                    st.rerun()
                luz_c = "<div class='anunciador-apagado'>CERRADA</div>" if procedimiento == "DESENERGIZACIÓN COMPLETA (SHUTDOWN)" and st.session_state.fase_d >= 7 else "<div class='anunciador-verde'>ABIERTA</div>"
                st.markdown(luz_c, unsafe_allow_html=True)
            st.markdown("</div>", unsafe_allow_html=True)
            
            st.markdown("<br>", unsafe_allow_html=True)
            if st.button("🚨 RESTABLECER PARÁMETROS DEL OVERHEAD"):
                st.session_state.fase_e = 0
                st.session_state.fase_d = 0
                st.session_state.falla_procedimiento = False
                st.session_state.descripcion_falla = ""
                st.rerun()
            st.markdown("</div>", unsafe_allow_html=True)

        with col_telemetria_pdu:
            st.markdown("### 📺 Honeywell EASy Avionics Display")
            st.markdown("<div class='subpanel-3d'>", unsafe_allow_html=True)
            if st.button("🔘 RAT AUTO SELECTOR", key="rat_auto_24"):
                if procedimiento == "ENERGIZACIÓN COMPLETA (COLD OPERATIONS)":
                    if st.session_state.fase_e == 5: st.session_state.fase_e = 6
                    else: forzar_alarma("RAT AUTO accionada fuera de secuencia.")
                else:
                    if st.session_state.fase_d == 2: st.session_state.fase_d = 3
                    else: forzar_alarma("La salvaguarda RAT AUTO debe normalizarse tras las baterías.")
                st.rerun()
            luz_rat_box = "<div class='anunciador-amber'>INHIBIT</div>" if (procedimiento == "ENERGIZACIÓN COMPLETA (COLD OPERATIONS)" and st.session_state.fase_e >= 6) or (procedimiento == "DESENERGIZACIÓN COMPLETA (SHUTDOWN)" and st.session_state.fase_d < 3) else "<div class='anunciador-apagado'>OFF (NORMAL POSITION)</div>"
            st.markdown(luz_rat_box, unsafe_allow_html=True)
            st.markdown("</div>", unsafe_allow_html=True)
            
            st.markdown("<div class='subpanel-3d' style='background-color:#111827;'>", unsafe_allow_html=True)
            if st.button("🛑 DETENER MOTOR GPU", key="stop_gpu_24"):
                if procedimiento == "DESENERGIZACIÓN COMPLETA (SHUTDOWN)":
                    if st.session_state.fase_d == 4: st.session_state.fase_d = 5
                    else: forzar_alarma("Corte de combustión ejecutado sin deponer la protección.")
                else: forzar_alarma("El motor de rampa debe suministrar energía continua.")
                st.rerun()
            luz_motor = "<div class='anunciador-apagado'>MOTOR APAGADO</div>" if (procedimiento == "DESENERGIZACIÓN COMPLETA (SHUTDOWN)" and st.session_state.fase_d >= 5) or (procedimiento == "ENERGIZACIÓN COMPLETA (COLD OPERATIONS)" and st.session_state.fase_e == 0) else "<div class='anunciador-verde'>MOTOR RUNNING (GENERANDO)</div>"
            st.markdown(luz_motor, unsafe_allow_html=True)
            st.markdown("</div>", unsafe_allow_html=True)
            
            if procedimiento == "ENERGIZACIÓN COMPLETA (COLD OPERATIONS)":
                val_gpu = "28.0 VDC" if st.session_state.fase_e >= 2 else "0.0 VDC"
                val_bus = "28.1 V" if st.session_state.fase_e >= 9 else "0.0 V"
                val_isol = "CONECTADO [── EN LÍNEA ──]" if st.session_state.fase_e >= 11 else "AISLADO [| OPEN |]"
                finalizado = st.session_state.fase_e == 12
            else:
                val_gpu = "0.0 VDC" if st.session_state.fase_d >= 5 else "28.0 VDC"
                val_bus = "0.0 V" if st.session_state.fase_d >= 1 else "28.1 V"
                val_isol = "AISLADO [| OPEN |]" if st.session_state.fase_d >= 1 else "CONECTADO [── EN LÍNEA ──]"
                finalizado = st.session_state.fase_d == 7

            if st.session_state.falla_procedimiento:
                borde_crt = "#ef4444"; fondo_crt = "#200d0d"; texto_crt = "#fca5a5"
                status_easydisplay = f"🚨 CAS ALERT: ERROR PROCEDIMENTAL DETECTADO\n\n  REPORTE CRÍTICO: {st.session_state.descripcion_falla}\n\n  [SECUENCIA QUEBRADA]: Violación de la directiva Dassault."
            elif finalizado:
                borde_crt = "#22c55e"; fondo_crt = "#06130b"; texto_crt = "#4ade80"
                status_easydisplay = "⚡ SYSTEMS STATUS: ENTORNO INTEGRADO CORRECTAMENTE\n\n  Fase concluida satisfactoriamente para el Grupo de Transporte Aéreo Especial."
            else:
                borde_crt = "#475569"; fondo_crt = "#030712"; texto_crt = "#38bdf8"
                status_easydisplay = "📲 MONITOR DE EVALUACIÓN TÁCTICA ACTIVO\n\n  Sistemas de telemetría a la espera de conmutación física en el overhead."

            st.markdown(f"""
                <div class="pantalla-mfd" style="border: 5px solid {borde_crt}; background-color: {fondo_crt}; color: {texto_crt};">
<div style="display: flex; justify-content: space-between; border-bottom: 2px solid #334155; padding-bottom: 8px; margin-bottom: 25px; font-size: 0.8rem; font-weight: bold;"><span>HONEYWELL PDU: AVIONICS SHIELD</span><span>MODO: TÁCTICO</span></div>
⚙️ TELEMETRÍA DE RED DE DISTRIBUCIÓN EN TIEMPO REAL (ATA 24):
 • SENSOR BUS GPU EXTERNO       : {val_gpu}
 • LH ESSENTIAL BUS DE CABINA   : {val_bus}
 • RH ESSENTIAL BUS DE CABINA   : {val_bus}
 • DISYUNTOR DE INTERCONEXIÓN   : {val_isol}
----------------------------------------------------------------------
🔔 CREW ALERTING SYSTEM (CAS) LIVE DATA FEED:

{status_easydisplay}
                </div>
            """, unsafe_allow_html=True)

    elif modulo_activo == "MÓDULO II: PRESIÓN DE COMBUSTIBLE (ATA 28)":
        st.subheader("Módulo II: Panel de Abastecimiento de Combustible por Presión en Rampa")
        col_panel_comb, col_monitor_comb = st.columns([1.3, 1])
        
        with col_panel_comb:
            st.markdown("<div class='overhead-frame'>", unsafe_allow_html=True)
            st.markdown("<div class='subpanel-3d' style='background: linear-gradient(180deg, #242b35, #161b22); border: 3px solid #0f172a;'>", unsafe_allow_html=True)
            
            st.markdown(f"<div class='display-digital-principal'>{st.session_state.combustible_actual:05d}</div>", unsafe_allow_html=True)
            st.markdown("<div style='text-align: center; font-weight: bold; font-size: 0.75rem; color: #94a3b8; margin-bottom: 25px; font-family: monospace;'>TOTAL QUANTITY (Lbs)</div>", unsafe_allow_html=True)
            
            grid_valvulas = st.columns(3)
            with grid_valvulas[0]:
                st.markdown("<div style='text-align: center; font-weight: bold; font-size: 0.8rem; font-family: monospace;'>LEFT VALVE</div>", unsafe_allow_html=True)
                est_l = "<div class='anunciador-verde'>FULL</div>" if st.session_state.combustible_actual >= (st.session_state.combustible_objetivo * 0.3) else "<div class='anunciador-apagado'>OFF</div>"
                st.markdown(est_l, unsafe_allow_html=True)
                st.session_state.valvula_izq = st.radio("V_Izq:", ["ON", "OFF"], index=1 if st.session_state.valvula_izq == "OFF" else 0, key="sel_v_izq_28", label_visibility="collapsed")
            with grid_valvulas[1]:
                st.markdown("<div style='text-align: center; font-weight: bold; font-size: 0.8rem; font-family: monospace;'>CENTER VALVE</div>", unsafe_allow_html=True)
                est_c = "<div class='anunciador-verde'>FULL</div>" if st.session_state.combustible_actual >= (st.session_state.combustible_objetivo * 0.8) else "<div class='anunciador-apagado'>OFF</div>"
                st.markdown(est_c, unsafe_allow_html=True)
                st.session_state.valvula_ctr = st.radio("V_Ctr:", ["ON", "OFF"], index=1 if st.session_state.valvula_ctr == "OFF" else 0, key="sel_v_ctr_28", label_visibility="collapsed")
            with grid_valvulas[2]:
                st.markdown("<div style='text-align: center; font-weight: bold; font-size: 0.8rem; font-family: monospace;'>RIGHT VALVE</div>", unsafe_allow_html=True)
                est_r = "<div class='anunciador-verde'>FULL</div>" if st.session_state.combustible_actual >= st.session_state.combustible_objetivo else "<div class='anunciador-apagado'>OFF</div>"
                st.markdown(est_r, unsafe_allow_html=True)
                st.session_state.valvula_der = st.radio("V_Der:", ["ON", "OFF"], index=1 if st.session_state.valvula_der == "OFF" else 0, key="sel_v_der_28", label_visibility="collapsed")
            
            st.markdown("<div class='linea-tactica'></div>", unsafe_allow_html=True)
            
            grid_controles_inf = st.columns(4)
            with grid_controles_inf[0]:
                if st.button("🧪 HIGH LEVEL"): st.toast("Líneas hidráulicas sometidas a prueba de estanqueidad...")
                if st.button("💡 ANNUN TEST"): st.toast("Filtros dicroicos verificados.")
            with grid_controles_inf[1]:
                st.markdown(f"<div class='display-digital-secundario'>{st.session_state.combustible_objetivo:05d}</div>", unsafe_allow_html=True)
                st.markdown("<div style='text-align: center; font-weight: bold; font-size: 0.65rem; color: #94a3b8; font-family: monospace;'>QTY SELECT</div>", unsafe_allow_html=True)
            with grid_controles_inf[2]:
                if st.button("🔼 INC QUANTITY"):
                    if st.session_state.combustible_objetivo < 24000: st.session_state.combustible_objetivo += 100; st.rerun()
                if st.button("🔽 DEC QUANTITY"):
                    if st.session_state.combustible_objetivo > 1000: st.session_state.combustible_objetivo -= 100; st.rerun()
            with grid_controles_inf[3]:
                sel_modo = st.radio("Modo Suministro:", ["MÁXIMO", "PRESELECCIÓN"], index=1, key="sel_modo_28")
                if sel_modo == "MÁXIMO": st.session_state.combustible_objetivo = 24000

            st.markdown("</div>", unsafe_allow_html=True)
            
            st.markdown("<div class='subpanel-3d' style='background-color: #1a202c;'>", unsafe_allow_html=True)
            grid_botones_camion = st.columns(3)
            with grid_botones_camion[0]:
                if st.button("🚀 INICIAR BOMBEO"):
                    if "ON" in [st.session_state.valvula_izq, st.session_state.valvula_ctr, st.session_state.valvula_der]:
                        st.session_state.bombeo_activo = True
                        st.rerun()
                    else: st.error("Abra al menos un selector de válvula (ON).")
            with grid_botones_camion[1]:
                if st.button("⏹️ PAUSAR PRESIÓN"):
                    st.session_state.bombeo_activo = False
                    st.rerun()
            with grid_botones_camion[2]:
                if st.button("🚨 PURGAR LÍNEAS / RESET"):
                    st.session_state.combustible_actual = 1150
                    st.session_state.bombeo_activo = False
                    st.rerun()
            st.markdown("</div></div></div>", unsafe_allow_html=True)

        with col_monitor_comb:
            st.markdown("### 📋 Flight Deck Verification Unit")
            if st.session_state.bombeo_activo: inf_comb = "⚡ SUCCIÓN DE ALTA PRESIÓN EN CURSO ⚡\n\n Transfiriendo masa de carburante hacia los depósitos alares."
            elif st.session_state.combustible_actual == st.session_state.combustible_objetivo: inf_comb = "🟢 CARGA DE COMBUSTIBLE NOMINAL CONCLUIDA\n\n Boquilla de rampa autorizada para desconexión."
            else: inf_comb = "📲 CIRCUITO DE ALIMENTACIÓN ENGANCHADO\n\n Configure el dial 'QTY SELECT' y sitúe las compuertas en ON."

            st.markdown(f"""
                <div class="pantalla-mfd" style="border: 5px solid #d97706; background-color: #0c0702; color: #fbbf24;">
<div style="display: flex; justify-content: space-between; border-bottom: 2px solid #78350f; padding-bottom: 8px; margin-bottom: 25px; font-size: 0.8rem; font-weight: bold;"><span>MONITOR: FUEL SYSTEM DATA</span><span>RAMPA: FAE-QUITO</span></div>
📊 PARÁMETROS HIDRÁULICOS Y MECÁNICOS DEL SISTEMA ATA 28:

 • VÁLVULA DE ENTRADA ALA IZQUIERDA : {st.session_state.valvula_izq}
 • VÁLVULA DE ENTRADA TANQUE CENTRAL: {st.session_state.valvula_ctr}
 • VÁLVULA DE ENTRADA ALA DERECHA   : {st.session_state.valvula_der}
 
 • COMBUSTIBLE PROGRAMADO EN DIAL   : {st.session_state.combustible_objetivo} Lbs
 • COMBUSTIBLE REAL EN INTERIOR     : {st.session_state.combustible_actual} Lbs

----------------------------------------------------------------------
🔔 CONTROL ALERTING SYSTEM (RAMPA) - REPORT:

{inf_comb}
                </div>
            """, unsafe_allow_html=True)
