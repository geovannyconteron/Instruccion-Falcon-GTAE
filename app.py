import streamlit as st
import streamlit.components.v1 as components

# Configuración estructural de la cabina táctica FAE
st.set_page_config(page_title="Falcon 7X Flight Deck - GTAE", page_icon="✈️", layout="wide")

# ==============================================================================
# SCRIPT DE AUDIO INSTANTÁNEO Y ENTORNO GLOBAL
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
        } catch(e) { console.log("Audio demorado"); }
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
# DISEÑO TRIDIMENSIONAL SKEUOMÓRFICO (CABINA REALISTA CSS)
# ==============================================================================
st.markdown("""
    <style>
    .main { 
        background-color: #0b0f19; 
        color: #e2e8f0;
        font-family: 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
    }
    .overhead-frame {
        background: linear-gradient(145deg, #1e2530, #131822);
        border: 6px solid #2d3748;
        border-radius: 12px;
        padding: 25px;
        box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.8), inset 0 2px 4px rgba(255,255,255,0.1);
        margin-bottom: 25px;
        position: relative;
    }
    .subpanel-3d {
        background: linear-gradient(180deg, #1a202c, #11141d);
        border-left: 4px solid #0f1219;
        border-top: 4px solid #0f1219;
        border-right: 4px solid #2d3748;
        border-bottom: 4px solid #2d3748;
        border-radius: 8px;
        padding: 18px;
        margin-bottom: 15px;
        box-shadow: inset 0 4px 8px rgba(0,0,0,0.6), 0 4px 6px rgba(0,0,0,0.3);
    }
    .linea-tactica {
        border-top: 2px solid #4a5568;
        border-bottom: 1px solid #1a202c;
        margin: 15px 0;
    }
    .titulo-serigrafia {
        color: #94a3b8;
        font-family: 'Courier New', Courier, monospace;
        font-weight: bold;
        font-size: 0.9rem;
        text-align: center;
        letter-spacing: 2px;
        margin-bottom: 12px;
        text-transform: uppercase;
        text-shadow: 1px 1px 2px rgba(0,0,0,0.5);
    }
    .stButton>button { 
        width: 100%; 
        font-weight: bold; 
        height: 54px; 
        border-radius: 6px; 
        font-size: 0.8rem;
        font-family: 'Courier New', Courier, monospace;
        background: linear-gradient(180deg, #334155, #1e293b) !important;
        color: #e2e8f0 !important;
        border-top: 2px solid #64748b !important;
        border-left: 2px solid #475569 !important;
        border-right: 2px solid #0f172a !important;
        border-bottom: 3px solid #0f172a !important;
        box-shadow: 0 6px 10px rgba(0,0,0,0.4);
        transition: all 0.1s ease;
    }
    .stButton>button:active {
        transform: translateY(3px);
        box-shadow: 0 2px 4px rgba(0,0,0,0.6);
        border-top: 2px solid #0f172a !important;
        border-bottom: 1px solid #475569 !important;
    }
    .anunciador-verde { 
        background-color: #042f1a; color: #4ade80; border: 2px solid #22c55e; font-weight: bold;
        text-align: center; border-radius: 4px; font-size: 0.75rem; padding: 5px; font-family: monospace;
        box-shadow: 0 0 12px rgba(34, 197, 94, 0.6);
    }
    .anunciador-amber { 
        background-color: #451a03; color: #fbbf24; border: 2px solid #f59e0b; font-weight: bold;
        text-align: center; border-radius: 4px; font-size: 0.75rem; padding: 5px; font-family: monospace;
        box-shadow: 0 0 12px rgba(245, 158, 11, 0.6);
    }
    .anunciador-apagado { 
        background-color: #181f2a; color: #4b5563; border: 2px solid #374151;
        text-align: center; border-radius: 4px; font-size: 0.75rem; padding: 5px; font-family: monospace;
        box-shadow: inset 0 2px 4px rgba(0,0,0,0.5);
    }
    .display-digital-principal {
        background-color: #020203; border: 3px solid #475569; border-radius: 6px; color: #f87171;
        font-family: 'Courier New', monospace; font-size: 2.4rem; font-weight: bold; text-align: center;
        letter-spacing: 5px; padding: 12px; box-shadow: inset 0 0 20px rgba(239, 68, 68, 0.4);
    }
    .display-digital-secundario {
        background-color: #020203; border: 2px solid #475569; border-radius: 6px; color: #fbbf24;
        font-family: 'Courier New', monospace; font-size: 1.6rem; font-weight: bold; text-align: center;
        letter-spacing: 3px; padding: 8px; box-shadow: inset 0 0 12px rgba(245, 158, 11, 0.3);
    }
    .pantalla-mfd {
        font-family: 'Courier New', monospace; border: 5px solid #334155; background-color: #04070e; 
        color: #38bdf8; padding: 22px; border-radius: 8px; min-height: 520px; box-shadow: inset 0 0 30px rgba(0,0,0,0.9); 
        white-space: pre-wrap;
    }
    </style>
""", unsafe_allow_html=True)

# ==============================================================================
# ALARMAS Y ADVERTENCIAS SONORAS TRAS RECARGA DE SEGURIDAD
# ==============================================================================
if "audio_alarma" not in st.session_state: st.session_state.audio_alarma = None

if st.session_state.audio_alarma == "alarma_critica":
    components.html("""
        <script>
        try {
            const ctx = new (window.AudioContext || window.webkitAudioContext)();
            const osc = ctx.createOscillator(); const gain = ctx.createGain();
            osc.type = 'sawtooth'; osc.frequency.setValueAtTime(380, ctx.currentTime);
            gain.gain.setValueAtTime(0.3, ctx.currentTime);
            osc.connect(gain); gain.connect(ctx.destination); osc.start();
            setTimeout(() => { osc.stop(); }, 1000);
        } catch(e){}
        </script>
    """, height=0, width=0)
    st.session_state.audio_alarma = None

elif st.session_state.audio_alarma == "carga_completa":
    components.html("""
        <script>
        try {
            const ctx = new (window.AudioContext || window.webkitAudioContext)();
            const osc = ctx.createOscillator(); osc.type = 'sine';
            osc.frequency.setValueAtTime(520, ctx.currentTime);
            osc.connect(ctx.destination); osc.start();
            setTimeout(() => { osc.stop(); }, 400);
        } catch(e){}
        </script>
    """, height=0, width=0)
    st.session_state.audio_alarma = None

# ==============================================================================
# CONTROL DE ACCESO MILITAR PRINCIPAL (EVALUADO EN PRIMERA INSTANCIA)
# ==============================================================================
if "autenticado" not in st.session_state: st.session_state.autenticado = False

if not st.session_state.autenticado:
    st.markdown("<br><br>", unsafe_allow_html=True)
    _, col_login, _ = st.columns([1, 1.4, 1])
    with col_login:
        st.markdown("""
            <div style='background: linear-gradient(135deg, #1e293b, #0f172a); border: 3px solid #3b82f6; padding: 35px; border-radius: 12px; text-align: center; box-shadow: 0 20px 25px -5px rgba(0,0,0,0.7);'>
                <h1 style='color: #ffffff; font-size: 1.6rem; margin-bottom: 5px; font-family: monospace;'>FLIGHT DECK PANEL SIMULATOR</h1>
                <h3 style='color: #3b82f6; font-size: 1.1rem; margin-bottom: 25px; font-family: monospace;'>FALCON 7X - GTAE</h3>
            </div>
        """, unsafe_allow_html=True)
        st.image("https://images.unsplash.com/photo-1540962351504-03099e0a754b?q=80&w=1200&auto=format&fit=crop", caption="Grupo de Transporte Aéreo Especial - FAE", use_container_width=True)
        st.markdown("<br>", unsafe_allow_html=True)
        with st.form("credenciales_cabina"):
            st.markdown("<h5 style='text-align: center; color: #94a3b8;'>🔒 CONTROL DE ACCESO MILITAR</h5>", unsafe_allow_html=True)
            txt_user = st.text_input("Identificador Técnico:", placeholder="gtae_operator")
            txt_pass = st.text_input("Clave de Bloqueo:", type="password", placeholder="••••••••")
            if st.form_submit_button("INGRESAR A LOS SISTEMAS"):
                if txt_user == "gtae" and txt_pass == "7X2026":
                    st.session_state.autenticado = True
                    st.rerun()
                else: st.error("Credenciales incorrectas. Origen de datos no autorizado.")
    st.stop()

# ==============================================================================
# SEPARACIÓN POR ENTORNO DE LA BARRA LATERAL (PILOTOS VS TÉCNICOS)
# ==============================================================================
with st.sidebar:
    st.markdown("<h4 style='color: #38bdf8; font-family: monospace;'>✈️ AVIONICS SIDEBAR</h4>", unsafe_allow_html=True)
    st.markdown("**Destacamento:** Grupo de Transporte Aéreo Especial")
    
    # El cambio a False detiene inmediatamente la ejecución gracias al st.stop() superior
    if st.button("🔒 DESCONECTAR CABINA"):
        st.session_state.autenticado = False
        st.rerun()
    st.markdown("---")
    
    tipo_procedimiento = st.radio(
        "PERFIL DE EVALUACIÓN:",
        ["✈️ PROCEDIMIENTOS OPERATIVOS (PILOTOS)", "🔧 PROCEDIMIENTOS DE MANTENIMIENTO (TÉCNICOS)"]
    )

    if tipo_procedimiento == "🔧 PROCEDIMIENTOS DE MANTENIMIENTO (TÉCNICOS)":
        opcion_sistema = st.radio(
            "CONSOLA INTERACTIVA TÉCNICA:",
            ["MÓDULO I: ENERGIZACIÓN (ATA 24)", "MÓDULO II: COMBUSTIBLE (ATA 28)"]
        )
    else:
        opcion_sistema = "MÓDULO III: ENCENDIDO DE MOTORES"

# Inicialización de memorias operacionales e historial de pasos técnicos
if "fase_e" not in st.session_state: st.session_state.fase_e = 0
if "fase_d" not in st.session_state: st.session_state.fase_d = 0
if "falla_procedimiento" not in st.session_state: st.session_state.falla_procedimiento = False
if "descripcion_falla" not in st.session_state: st.session_state.descripcion_falla = ""
if "combustible_actual" not in st.session_state: st.session_state.combustible_actual = 1150
if "combustible_objetivo" not in st.session_state: st.session_state.combustible_objetivo = 10500
if "valvula_izq" not in st.session_state: st.session_state.valvula_izq = "OFF"
if "valvula_ctr" not in st.session_state: st.session_state.valvula_ctr = "OFF"
if "valvula_der" not in st.session_state: st.session_state.valvula_der = "OFF"
if "bombeo_activo" not in st.session_state: st.session_state.bombeo_activo = False

# Variables de estado de motores para el perfil CODDE 2
if "p_apu" not in st.session_state: st.session_state.p_apu = "OFF"
if "p_bleed" not in st.session_state: st.session_state.p_bleed = "CLOSED"
if "p_boost" not in st.session_state: st.session_state.p_boost = "OFF"
if "p_eng" not in st.session_state: st.session_state.p_eng = ["STBY", "STBY", "STBY"]
if "p_lever" not in st.session_state: st.session_state.p_lever = ["SHUTOFF", "SHUTOFF", "SHUTOFF"]
if "p_cas" not in st.session_state: st.session_state.p_cas = "🟢 SYSTEMS GENERAL RUN NOMINAL\nMotores y líneas de presión monitoreados según el perfil Dassault EASy."

# Simulación de recarga de rampa (Módulo II)
if st.session_state.bombeo_activo and st.session_state.combustible_actual < st.session_state.combustible_objetivo:
    st.session_state.combustible_actual += 400
    if st.session_state.combustible_actual >= st.session_state.combustible_objetivo:
        st.session_state.combustible_actual = st.session_state.combustible_objetivo
        st.session_state.bombeo_activo = False
        st.session_state.audio_alarma = "carga_completa"
    st.rerun()

# ------------------------------------------------------------------------------
# MÓDULO III: PROCEDIMIENTOS OPERATIVOS CON CONTROL INTEGRAL DEL CODDE 2
# ------------------------------------------------------------------------------
if opcion_sistema == "MÓDULO III: ENCENDIDO DE MOTORES":
    st.markdown("<h2 style='text-align: center; color: #f1f5f9; font-family: monospace;'>PANTALLA DE PROCEDIMIENTOS OPERATIVOS (CODDE 2)</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #94a3b8;'>Flujo de Cabina Completa de los 3 Motores Pratt & Whitney PW307A</p>", unsafe_allow_html=True)

    col_mandos_vuelo, col_display_honeywell = st.columns([1.2, 1])

    with col_mandos_vuelo:
        st.markdown("<div class='overhead-frame'>", unsafe_allow_html=True)
        st.markdown("<div class='subpanel-3d'><div class='titulo-serigrafia'>Auxiliary Power Unit & Bleed Air (ATA 36 / 49)</div>", unsafe_allow_html=True)
        c_apu = st.columns(2)
        with c_apu[0]:
            if st.button("APU MASTER SWITCH"):
                st.session_state.p_apu = "RUN" if st.session_state.p_apu == "OFF" else "OFF"
                if st.session_state.p_apu == "OFF": st.session_state.p_bleed = "CLOSED"
                st.rerun()
            st.markdown("<div class='anunciador-verde'>ON (100%)</div>" if st.session_state.p_apu == "RUN" else "<div class='anunciador-apagado'>OFF</div>", unsafe_allow_html=True)
        with c_apu[1]:
            if st.button("APU BLEED VALVE"):
                if st.session_state.p_apu == "RUN":
                    st.session_state.p_bleed = "OPEN" if st.session_state.p_bleed == "CLOSED" else "CLOSED"
                st.rerun()
            st.markdown("<div class='anunciador-amber'>BLEED OPEN</div>" if st.session_state.p_bleed == "OPEN" else "<div class='anunciador-apagado'>CLOSED</div>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

        st.markdown("<div class='subpanel-3d'><div class='titulo-serigrafia'>Overhead Fuel Panel (ATA 28 Boost Pumps)</div>", unsafe_allow_html=True)
        if st.button(f"FUEL MAIN BOOST PUMPS INTERRUPTOR: {st.session_state.p_boost}"):
            st.session_state.p_boost = "ON" if st.session_state.p_boost == "OFF" else "OFF"
            st.rerun()
        st.markdown("<div class='anunciador-verde'>BOOSTER EN LÍNEA</div>" if st.session_state.p_boost == "ON" else "<div class='anunciador-apagado'>PUMPS OFF</div>", unsafe_allow_html=True)

        st.markdown("<div class='subpanel-3d'><div class='titulo-serigrafia'>Engine Ignition & Motoring (Overhead Panel)</div>", unsafe_allow_html=True)
        c_motores = st.columns(3)
        for i in range(3):
            with c_motores[i]:
                st.markdown(f"<div style='text-align:center; font-weight:bold; font-size:0.8rem; margin-bottom:5px;'>MOTOR {i+1}</div>", unsafe_allow_html=True)
                if st.button(f"ENG {i+1} START"):
                    if st.session_state.p_bleed == "OPEN":
                        st.session_state.p_eng[i] = "CRANK"
                        if st.session_state.p_lever[i] == "RUN":
                            st.session_state.p_cas = f"🚨 ALERT CAS: HOT START IN ENGINE {i+1}!\n Combustible inyectado de forma prematura con rotación N2 inferior al 15%."
                            st.session_state.audio_alarma = "alarma_critica"
                    else:
                        st.session_state.p_cas = f"🚨 ALERT CAS: BLEED AIR FAULT ENGINE {i+1}!\n No hay presión neumática en las líneas de sangrado (APU BLEED CLOSED)."
                        st.session_state.audio_alarma = "alarma_critica"
                    st.rerun()
                st.markdown(f"<div class='anunciador-amber'>{st.session_state.p_eng[i]}</div>" if st.session_state.p_eng[i] != "STBY" else "<div class='anunciador-apagado'>STBY</div>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

        st.markdown("<div class='subpanel-3d'><div class='titulo-serigrafia'>Pedestal Fuel Control Levers (Run/Shutoff)</div>", unsafe_allow_html=True)
        c_levers = st.columns(3)
        for i in range(3):
            with c_levers[i]:
                if st.button(f"LEVER {i+1}: {st.session_state.p_lever[i]}"):
                    st.session_state.p_lever[i] = "RUN" if st.session_state.p_lever[i] == "SHUTOFF" else "SHUTOFF"
                    if st.session_state.p_lever[i] == "RUN":
                        if st.session_state.p_boost == "OFF":
                            st.session_state.p_cas = f"🚨 ALERT CAS: FUEL PUMP FAULT ENGINE {i+1}!\n Intento de inyección de mezcla sin activar las Boost Pumps (ATA 28)."
                            st.session_state.audio_alarma = "alarma_critica"
                        elif st.session_state.p_eng[i] == "CRANK":
                            st.session_state.p_eng[i] = "RUN IDLE"
                            st.session_state.p_cas = f"🟩 SYSTEMS STATUS: ENGINE {i+1} ENGAGED IN IDLE RANGES NOMINAL."
                        else:
                            st.session_state.p_cas = f"🚨 ALERT CAS: HOT START IN ENGINE {i+1}!\n Válvula de corte abierta sin flujo ni rotación neumática previa."
                            st.session_state.audio_alarma = "alarma_critica"
                    st.rerun()
        st.markdown("</div>", unsafe_allow_html=True)

        if st.button("🚨 REINICIAR PROCEDIMIENTO OPERATIVO COMPLETO"):
            st.session_state.p_apu = "OFF"; st.session_state.p_bleed = "CLOSED"; st.session_state.p_boost = "OFF"
            st.session_state.p_eng = ["STBY", "STBY", "STBY"]; st.session_state.p_lever = ["SHUTOFF", "SHUTOFF", "SHUTOFF"]
            st.session_state.p_cas = "🟢 SYSTEMS GENERAL RUN NOMINAL\nMotores monitoreados dentro de límites estructurales."
            st.rerun()
        st.markdown("</div>", unsafe_allow_html=True)

    with col_display_honeywell:
        st.markdown("### 📺 Honeywell EASy Avionics Display")
        
        html_clocks = ""
        for i in range(3):
            n1 = 24.2 if st.session_state.p_eng[i] == "RUN IDLE" else 0.0
            n2 = 57.4 if st.session_state.p_eng[i] == "RUN IDLE" else (25.0 if st.session_state.p_eng[i] == "CRANK" else 0.0)
            itt = 490 if st.session_state.p_eng[i] == "RUN IDLE" else 15
            html_clocks += f"""
            <div style="display:inline-block; width:30%; background:#04070e; border:1px solid #1e293b; padding:5px; border-radius:4px; text-align:center; margin:1%;">
                <div style="font-size:0.75rem; color:#38bdf8; font-weight:bold;">ENG {i+1}</div>
                <canvas id="n1_{i}" width="80" height="80"></canvas><div style="font-size:0.7rem; color:#4ade80;">N1: {n1}%</div>
                <canvas id="n2_{i}" width="80" height="80"></canvas><div style="font-size:0.7rem; color:#4ade80;">N2: {n2}%</div>
                <canvas id="itt_{i}" width="80" height="80"></canvas><div style="font-size:0.7rem; color:#f59e0b;">ITT: {itt}°C</div>
            </div>
            <script>
                function draw(id, val, max) {{
                    let c = document.getElementById(id); if(!c) return;
                    let ctx = c.getContext("2d"); ctx.clearRect(0,0,80,80);
                    ctx.beginPath(); ctx.arc(40,40,35,0,2*Math.PI); ctx.strokeStyle="#1e293b"; ctx.lineWidth=2; ctx.stroke();
                    let a = 0.75*Math.PI + (val/max)*(1.5*Math.PI);
                    ctx.beginPath(); ctx.moveTo(40,40); ctx.lineTo(40+25*Math.cos(a), 40+25*Math.sin(a));
                    ctx.strokeStyle="#4ade80"; ctx.lineWidth=2; ctx.stroke();
                }}
                setTimeout(() => {{ draw("n1_{i}", {n1}, 100); draw("n2_{i}", {n2}, 100); draw("itt_{i}", {itt}, 800); }}, 50);
            </script>
            """
        components.html(f"<div style='display:flex;'>{html_clocks}</div>", height=320)

        borde_crt = "#ef4444" if "🚨" in st.session_state.p_cas else "#475569"
        fondo_crt = "#200d0d" if "🚨" in st.session_state.p_cas else "#000000"
        texto_crt = "#fca5a5" if "🚨" in st.session_state.p_cas else "#38bdf8"

        st.markdown(f"""
            <div class="pantalla-mfd" style="border: 5px solid {borde_crt}; background-color: {fondo_crt}; color: {texto_crt}; min-height:220px; padding:15px;">
<div style="border-bottom: 2px solid #334155; padding-bottom: 5px; margin-bottom: 15px; font-weight: bold;"><span>HONEYWELL PDU: DISPLAY DE CABINA</span><span>FLIGHT FEED</span></div>
📋 ESCANEO DE SISTEMAS EN TIEMPO REAL (ATA 70 / 36 / 28):
 • UNIDAD DE POTENCIA APU      : {st.session_state.p_apu}
 • VÁLVULA SANGRADO APU BLEED  : {st.session_state.p_bleed}
 • BOMBAS COMBUSTIBLE BOOST    : {st.session_state.p_boost}
----------------------------------------------------------------------
🔔 CREW ALERTING SYSTEM (CAS) LIVE DATA FEED:

{st.session_state.p_cas}
            </div>
        """, unsafe_allow_html=True)

# ------------------------------------------------------------------------------
# MÓDULOS DE MANTENIMIENTO TÉCNICO COMPLETO RESTAURADOS AL 100%
# ------------------------------------------------------------------------------
else:
    st.title("🔧 Pantalla de Procedimientos de Mantenimiento (Técnicos)")
    st.markdown("---")
    
    if modulo_activo == "MÓDULO I: DISTRIBUCIÓN ELÉCTRICA (ATA 24)":
        st.subheader("Módulo I: Distribución Eléctrica y Secuenciación Avanzada de Barras")
        procedimiento = st.radio("⚙️ SELECCIONE PROCEDIMIENTO DE EVALUACIÓN:", ["ENERGIZACIÓN COMPLETA (COLD OPERATIONS)", "DESENERGIZACIÓN COMPLETA (SHUTDOWN)"], horizontal=True)
        
        if "procedimiento_previo" not in st.session_state: st.session_state.procedimiento_previo = procedimiento
        elif st.session_state.procedimiento_previo != procedimiento:
            st.session_state.fase_e = 0; st.session_state.fase_d = 0
            st.session_state.falla_procedimiento = False; st.session_state.descripcion_falla = ""
            st.session_state.procedimiento_previo = procedimiento

        def forzar_alarma(texto):
            st.session_state.falla_procedimiento = True
            st.session_state.descripcion_falla = texto
            st.session_state.audio_alarma = "alarma_critica"

        col_fisica_panel, col_telemetria_pdu = st.columns([1.3, 1])
        with col_fisica_panel:
            st.markdown("<div class='overhead-frame'>", unsafe_allow_html=True)
            st.markdown("<div class='subpanel-3d'><div class='titulo-serigrafia'>⚡ DC SUPPLY PANEL (OVERHEAD UPPER ROW) ⚡</div>", unsafe_allow_html=True)
            
            grid_sup = st.columns(8)
            with grid_sup[0]:
                st.button("GALLEY MSTR", disabled=True, key="gm_m")
                st.markdown("<div class='anunciador-apagado'>OFF</div>", unsafe_allow_html=True)
            with grid_sup[1]:
                if st.button("LH MSTR", key="lm_m"):
                    if procedimiento == "ENERGIZACIÓN COMPLETA (COLD OPERATIONS)":
                        if st.session_state.fase_e == 11: st.session_state.fase_e = 12
                        else: forzar_alarma("LH MASTER activado de forma prematura fuera de la secuencia técnica.")
                    st.rerun()
                st.markdown("<div class='anunciador-verde'>ON</div>" if st.session_state.fase_e >= 12 else "<div class='anunciador-amber'>OFF</div>", unsafe_allow_html=True)
            with grid_sup[2]:
                if st.button("LH INIT", key="lh_m"):
                    if procedimiento == "ENERGIZACIÓN COMPLETA (COLD OPERATIONS)":
                        if st.session_state.fase_e == 7: st.session_state.fase_e = 8
                        else: forzar_alarma("LH INIT accionado de forma prematura sin acoplamiento del BUS TIE.")
                    st.rerun()
                st.markdown("<div class='anunciador-apagado'>RUN</div>" if st.session_state.fase_e >= 8 else "<div class='anunciador-amber'>OFF</div>", unsafe_allow_html=True)
            with grid_sup[3]:
                if st.button("BUS TIE", key="bt_m"):
                    if procedimiento == "ENERGIZACIÓN COMPLETA (COLD OPERATIONS)":
                        if st.session_state.fase_e == 6: st.session_state.fase_e = 7
                        else: forzar_alarma("BUS TIE accionado previo al acoplamiento de seguridad de la RAT.")
                    st.rerun()
                st.markdown("<div class='anunciador-amber'>TIED</div>" if st.session_state.fase_e >= 7 else "<div class='anunciador-apagado'>AUTO</div>", unsafe_allow_html=True)
            with grid_sup[4]:
                if st.button("RH INIT", key="rh_m"):
                    if procedimiento == "ENERGIZACIÓN COMPLETA (COLD OPERATIONS)":
                        if st.session_state.fase_e == 7: st.session_state.fase_e = 8
                        else: forzar_alarma("RH INIT accionado de forma prematura sin acoplamiento del BUS TIE.")
                    st.rerun()
                st.markdown("<div class='anunciador-apagado'>RUN</div>" if st.session_state.fase_e >= 8 else "<div class='anunciador-amber'>OFF</div>", unsafe_allow_html=True)
            with grid_sup[5]:
                if st.button("RH MSTR", key="rhm_m"):
                    if procedimiento == "ENERGIZACIÓN COMPLETA (COLD OPERATIONS)":
                        if st.session_state.fase_e == 11: st.session_state.fase_e = 12
                        else: forzar_alarma("RH MASTER activado fuera de secuencia reglamentaria.")
                    st.rerun()
                st.markdown("<div class='anunciador-verde'>ON</div>" if st.session_state.fase_e >= 12 else "<div class='anunciador-amber'>OFF</div>", unsafe_allow_html=True)
            with grid_sup[6]:
                if st.button("CABIN MSTR", key="cb_m"):
                    if procedimiento == "ENERGIZACIÓN COMPLETA (COLD OPERATIONS)":
                        if st.session_state.fase_e == 9: st.session_state.fase_e = 10
                        else: forzar_alarma("CABIN MASTER accionado de forma prematura sin la GPU online.")
                    st.rerun()
                st.markdown("<div class='anunciador-amber'>OFF</div>" if st.session_state.fase_e >= 10 else "<div class='anunciador-verde'>ON</div>", unsafe_allow_html=True)
            with grid_sup[7]:
                if st.button("EXT PWR", key="ep_m"):
                    if procedimiento == "ENERGIZACIÓN COMPLETA (COLD OPERATIONS)":
                        if st.session_state.fase_e == 8: st.session_state.fase_e = 9
                        else: forzar_alarma("EXT POWER conectado sin configurar los parámetros nominales de la planta externa.")
                    st.rerun()
                st.markdown("<div class='anunciador-verde'>ONLINE</div>" if st.session_state.fase_e >= 9 else "<div class='anunciador-apagado'>OFF</div>", unsafe_allow_html=True)
            st.markdown("</div>", unsafe_allow_html=True)

            st.markdown("<div class='linea-tactica'></div>", unsafe_allow_html=True)
            
            st.markdown("<div class='subpanel-3d'><div class='titulo-serigrafia'>🔋 GENERATION & BATTERIES</div>", unsafe_allow_html=True)
            grid_inf = st.columns(8)
            with grid_inf[0]: st.button("GEN 1", disabled=True, key="g1"); st.markdown("<div class='anunciador-apagado'>OFF</div>", unsafe_allow_html=True)
            with grid_inf[1]:
                if st.button("LH ISOL", key="lhi"):
                    if procedimiento == "ENERGIZACIÓN COMPLETA (COLD OPERATIONS)":
                        if st.session_state.fase_e == 10: st.session_state.fase_e = 11
                        else: forzar_alarma("LH ISOL accionado de forma prematura.")
                    st.rerun()
                st.markdown("<div class='anunciador-apagado'>TIED</div>" if st.session_state.fase_e >= 11 else "<div class='anunciador-amber'>ISOL</div>", unsafe_allow_html=True)
            with grid_inf[2]:
                if st.button("BAT 1", key="b1"):
                    if procedimiento == "ENERGIZACIÓN COMPLETA (COLD OPERATIONS)":
                        if st.session_state.fase_e == 4: st.session_state.fase_e = 5
                        else: forzar_alarma("BAT 1 activada sin comprobar el freno hidráulico de estacionamiento.")
                    st.rerun()
                st.markdown("<div class='anunciador-verde'>AUTO</div>" if st.session_state.fase_e >= 5 else "<div class='anunciador-apagado'>OFF</div>", unsafe_allow_html=True)
            with grid_inf[3]:
                if st.button("BAT 2", key="b2"):
                    if procedimiento == "ENERGIZACIÓN COMPLETA (COLD OPERATIONS)":
                        if st.session_state.fase_e == 4: st.session_state.fase_e = 5
                        else: forzar_alarma("BAT 2 activada sin comprobar el freno hidráulico de estacionamiento.")
                    st.rerun()
                st.markdown("<div class='anunciador-verde'>AUTO</div>" if st.session_state.fase_e >= 5 else "<div class='anunciador-apagado'>OFF</div>", unsafe_allow_html=True)
            st.markdown("</div>", unsafe_allow_html=True)

            st.markdown("<div class='linea-tactica'></div>", unsafe_allow_html=True)
            
            st.markdown("<div class='subpanel-3d'><div class='titulo-serigrafia'>🔧 CONFIGURACIÓN Y ACOPLE DE PLANTA EXTERNA</div>", unsafe_allow_html=True)
            grid_rampa = st.columns(5)
            with grid_rampa[0]:
                if st.button("🔌 RECEPTÁCULO GPU", key="rec"):
                    if procedimiento == "ENERGIZACIÓN COMPLETA (COLD OPERATIONS)":
                        if st.session_state.fase_e == 0: st.session_state.fase_e = 1
                        else: forzar_alarma("Línea física acoplada fuera de secuencia.")
                    st.rerun()
                st.markdown("<div class='anunciador-verde'>CONECTADO</div>" if st.session_state.fase_e >= 1 else "<div class='anunciador-apagado'>DESCONECTADO</div>", unsafe_allow_html=True)
            with grid_rampa[1]:
                if st.button("⚡ REGULADOR TENSIÓN TIERRA", key="pot"):
                    if procedimiento == "ENERGIZACIÓN COMPLETA (COLD OPERATIONS)":
                        if st.session_state.fase_e == 1: st.session_state.fase_e = 2
                        else: forzar_alarma("Regulación de voltaje modificada sin alimentación base.")
                    st.rerun()
                st.markdown("<div class='anunciador-verde'>28.0 VDC OK</div>" if st.session_state.fase_e >= 2 else "<div class='anunciador-apagado'>0.0 VDC</div>", unsafe_allow_html=True)
            with grid_rampa[2]:
                if st.button("🎛️ SWITCH EXTERNO GPU", key="sw"):
                    if procedimiento == "ENERGIZACIÓN COMPLETA (COLD OPERATIONS)":
                        if st.session_state.fase_e == 2: st.session_state.fase_e = 3
                        else: forzar_alarma("Switch GPU colocado en ON sin estabilización de voltaje nominal.")
                    st.rerun()
                st.markdown("<div class='anunciador-verde'>LÍNEA ONLINE</div>" if st.session_state.fase_e >= 3 else "<div class='anunciador-apagado'>LÍNEA OFF</div>", unsafe_allow_html=True)
            with grid_rampa[3]:
                if st.button("⚙️ CONTROL FRENO PARQUEO", key="fr"):
                    if procedimiento == "ENERGIZACIÓN COMPLETA (COLD OPERATIONS)":
                        if st.session_state.fase_e == 3: st.session_state.fase_e = 4
                        else: forzar_alarma("Freno de estacionamiento ignorado; riesgo de desplazamiento estructural.")
                    st.rerun()
                st.markdown("<div class='anunciador-verde'>ENGANCHADO</div>" if st.session_state.fase_e >= 4 else "<div class='anunciador-apagado'>LIBERADO</div>", unsafe_allow_html=True)
            with grid_rampa[4]:
                if st.button("🚪 COMPUERTA RECEPT", key="compuerta_maint_ext"):
                    if procedimiento == "DESENERGIZACIÓN COMPLETA (SHUTDOWN)" and st.session_state.fase_d == 6: st.session_state.fase_d = 7
                    st.rerun()
                luz_c = "<div class='anunciador-apagado'>CERRADA</div>" if procedimiento == "DESENERGIZACIÓN COMPLETA (SHUTDOWN)" and st.session_state.fase_d >= 7 else "<div class='anunciador-verde'>ABIERTA</div>"
                st.markdown(luz_c, unsafe_allow_html=True)
            st.markdown("</div>", unsafe_allow_html=True)
            
            st.markdown("<br>", unsafe_allow_html=True)
            if st.button("🚨 CORREGIR / REINICIAR EVALUACIÓN", key="btn_reset_maint"):
                st.session_state.fase_e = 0; st.session_state.fase_d = 0
                st.session_state.falla_procedimiento = False; st.session_state.descripcion_falla = ""
                st.rerun()
            st.markdown("</div>", unsafe_allow_html=True)

        with col_telemetria_pdu:
            st.markdown("### 📺 Honeywell EASy Avionics Display")
            borde_crt = "#ef4444" if st.session_state.falla_procedimiento else "#475569"
            fondo_crt = "#200d0d" if st.session_state.falla_procedimiento else "#000000"
            texto_crt = "#fca5a5" if st.session_state.falla_procedimiento else "#38bdf8"
            status_easydisplay = f"🚨 CAS ALERT: ERROR PROCEDIMENTAL DETECTADO\n\n  REPORTE CRÍTICO: {st.session_state.descripcion_falla}\n\n  Utilice el botón de reinicio para purgar las líneas alares." if st.session_state.falla_procedimiento else f"📲 MODO EVALUACIÓN ACTIVO\n\nFase Eléctrica Actual: Paso {st.session_state.fase_e}/12"

            st.markdown(f"""
                <div class="pantalla-mfd" style="border: 5px solid {borde_crt}; background-color: {fondo_crt}; color: {texto_crt};">
                    <div style="border-bottom: 2px solid #334155; padding-bottom: 8px; margin-bottom: 25px; font-weight: bold;"><span>HONEYWELL PDU: AVIONICS SHIELD</span></div>
                    {status_easydisplay}
                </div>
            """, unsafe_allow_html=True)

    elif modulo_activo == "MÓDULO II: PRESIÓN DE COMBUSTIBLE (ATA 28)":
        st.subheader("Módulo II: Panel de Abastecimiento de Combustible por Presión (Rampa)")
        col_panel_comb, col_monitor_comb = st.columns([1.3, 1])
        with col_panel_comb:
            st.markdown("<div class='overhead-frame'>", unsafe_allow_html=True)
            st.markdown("<div class='subpanel-3d' style='background: linear-gradient(180deg, #242b35, #161b22); border: 3px solid #0f172a;'>", unsafe_allow_html=True)
            st.markdown(f"<div class='display-digital-principal'>{st.session_state.combustible_actual:05d}</div>", unsafe_allow_html=True)
            
            grid_valvulas = st.columns(3)
            with grid_valvulas[0]:
                st.markdown("<div style='font-family: monospace; font-weight:bold;'>LEFT VALVE</div>", unsafe_allow_html=True)
                st.session_state.valvula_izq = st.radio("V_Izq:", ["ON", "OFF"], index=1 if st.session_state.valvula_izq == "OFF" else 0, key="v1_r", label_visibility="collapsed")
            with grid_valvulas[1]:
                st.markdown("<div style='font-family: monospace; font-weight:bold;'>CENTER VALVE</div>", unsafe_allow_html=True)
                st.session_state.valvula_ctr = st.radio("V_Ctr:", ["ON", "OFF"], index=1 if st.session_state.valvula_ctr == "OFF" else 0, key="v2_r", label_visibility="collapsed")
            with grid_valvulas[2]:
                st.markdown("<div style='font-family: monospace; font-weight:bold;'>RIGHT VALVE</div>", unsafe_allow_html=True)
                st.session_state.valvula_der = st.radio("V_Der:", ["ON", "OFF"], index=1 if st.session_state.valvula_der == "OFF" else 0, key="v3_r", label_visibility="collapsed")
            
            st.markdown("<br>", unsafe_allow_html=True)
            cx_f1, cx_f2, _ = st.columns(3)
            with cx_f1:
                if st.button("🚀 INICIAR SUCCIÓN / REFUELING"):
                    if "ON" in [st.session_state.valvula_izq, st.session_state.valvula_ctr, st.session_state.valvula_der]:
                        st.session_state.bombeo_activo = True
                        st.rerun()
            with cx_f2:
                if st.button("⏹️ STOP FUELING (PAUSA)"):
                    st.session_state.bombeo_activo = False
                    st.rerun()
            st.markdown("</div></div></div>", unsafe_allow_html=True)

    with col_monitor_comb:
        st.markdown("### 📋 Flight Deck Verification Unit")
        st.markdown(f"<div class='pantalla-mfd' style='border-color: #d97706; background-color: #0c0702; color: #fbbf24;'>REAL TIME TOTAL COMBUSTIBLE: {st.session_state.combustible_actual} Lbs</div>", unsafe_allow_html=True)
