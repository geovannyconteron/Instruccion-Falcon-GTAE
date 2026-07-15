import streamlit as st
import streamlit.components.v1 as components

# Configuración estructural de la cabina táctica FAE
st.set_page_config(page_title="Falcon 7X Flight Deck - GTAE", page_icon="✈️", layout="wide")

# ==============================================================================
# SCRIPT DE AUDIO INSTANTÁNEO Y EFECTOS SONOROS DE CABINA
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
    .slot-palanca {
        background: #090c12; border: 2px solid #1a202c; border-radius: 8px; height: 140px;
        display: flex; flex-direction: column; justify-content: space-between; align-items: center; padding: 10px 0;
        box-shadow: inset 0 5px 10px rgba(0,0,0,0.9);
    }
    .korry-label {
        font-family: 'Courier New', monospace; font-weight: bold; font-size: 0.75rem; color: #94a3b8;
        text-align: center; margin-bottom: 5px;
    }
    </style>
""", unsafe_allow_html=True)

# ==============================================================================
# ALARMAS CENTRALIZADAS (MANEJADOR DE EFECTOS DE SONIDO CAS)
# ==============================================================================
if "audio_alarma" not in st.session_state: st.session_state.audio_alarma = None

if st.session_state.audio_alarma == "alarma_critica":
    components.html("""
        <script>
        try {
            const ctx = new (window.AudioContext || window.webkitAudioContext)();
            const osc = ctx.createOscillator(); const gain = ctx.createGain();
            osc.type = 'sawtooth'; osc.frequency.setValueAtTime(500, ctx.currentTime);
            gain.gain.setValueAtTime(0.25, ctx.currentTime);
            osc.connect(gain); gain.connect(ctx.destination); osc.start();
            setTimeout(() => { osc.stop(); }, 1200);
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
            osc.frequency.setValueAtTime(580, ctx.currentTime);
            osc.connect(ctx.destination); osc.start();
            setTimeout(() => { osc.stop(); }, 500);
        } catch(e){}
        </script>
    """, height=0, width=0)
    st.session_state.audio_alarma = None

# ==============================================================================
# CONTROL DE ACCESO MILITAR PRINCIPAL
# ==============================================================================
if "autenticado" not in st.session_state: st.session_state.autenticado = False

if not st.session_state.autenticado:
    st.markdown("<br><br>", unsafe_allow_html=True)
    _, col_login, _ = st.columns([1, 1.4, 1])
    with col_login:
        st.markdown("""
            <div style='background: linear-gradient(135deg, #1e293b, #090d16); border: 3px solid #3b82f6; padding: 35px; border-radius: 12px; text-align: center; box-shadow: 0 20px 25px -5px rgba(0,0,0,0.9);'>
                <h1 style='color: #ffffff; font-size: 1.6rem; margin-bottom: 5px; font-family: monospace; letter-spacing: 2px;'>FLIGHT DECK PANEL SIMULATOR</h1>
                <h3 style='color: #3b82f6; font-size: 1.0rem; margin-bottom: 25px; font-family: monospace;'>FALCON 7X - GTAE ECUADOR</h3>
            </div>
        """, unsafe_allow_html=True)
        st.image("https://images.unsplash.com/photo-1540962351504-03099e0a754b?q=80&w=1200&auto=format&fit=crop", caption="Unidad de Simulación y Sistemas Especiales - FAE", use_container_width=True)
        st.markdown("<br>", unsafe_allow_html=True)
        with st.form("credenciales_cabina"):
            st.markdown("<h5 style='text-align: center; color: #94a3b8; font-family: monospace;'>🔒 CONTROL DE ACCESO MILITAR</h5>", unsafe_allow_html=True)
            txt_user = st.text_input("Operador:", placeholder="gtae_operator")
            txt_pass = st.text_input("Código de Seguridad:", type="password", placeholder="••••••••")
            if st.form_submit_button("AUTORIZAR ENTRADA"):
                if txt_user == "gtae" and txt_pass == "7X2026":
                    st.session_state.autenticado = True
                    st.rerun()
                else: st.error("Credenciales incorrectas. Origen de datos no autorizado.")
    st.stop()

# ==============================================================================
# BARRA LATERAL - SEPARACIÓN POR ENTORNO DE EVALUACIÓN
# ==============================================================================
with st.sidebar:
    st.markdown("<h4 style='color: #38bdf8; font-family: monospace;'>✈ glycemic AVIONICS SHIELD</h4>", unsafe_allow_html=True)
    st.markdown("**Destacamento:** Grupo de Transporte Aéreo Especial")
    
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

# Inicialización de variables operacionales y persistencia de memoria
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

# Variables de estado de motores e hileras independientes de Korrys del CODDE 2
if "p_bat" not in st.session_state: st.session_state.p_bat = "OFF"
if "p_apu" not in st.session_state: st.session_state.p_apu = "OFF"
if "p_bleed" not in st.session_state: st.session_state.p_bleed = "CLOSED"
if "p_boost_pumps" not in st.session_state: st.session_state.p_boost_pumps = ["OFF", "OFF", "OFF", "OFF"]  # 1A, 2A, 2B, 3A
if "p_eng" not in st.session_state: st.session_state.p_eng = ["STBY", "STBY", "STBY"]
if "p_lever" not in st.session_state: st.session_state.p_lever = ["SHUTOFF", "SHUTOFF", "SHUTOFF"]
if "p_cas" not in st.session_state: st.session_state.p_cas = ["🟢 COLD DARK CONFIGURATION", "Avión apagado completamente. Requiere energización esencial."]

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
    st.markdown("<h2 style='text-align: center; color: #f1f5f9; font-family: monospace; letter-spacing: 1px;'>✈️ PANEL OVERHEAD DE PILOTOS (SEC. CODDE 2)</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #94a3b8; margin-top:-10px;'>Cabina Libre - Las desviaciones del procedimiento dispararán alertas en el EASy</p>", unsafe_allow_html=True)

    col_mandos_vuelo, col_display_honeywell = st.columns([1.3, 1])

    with col_mandos_vuelo:
        st.markdown("<div class='overhead-frame'>", unsafe_allow_html=True)
        
        # ATA 24 ELECTRIC DC CONTROL
        st.markdown("<div class='subpanel-3d'><div class='titulo-serigrafia'>⚡ ATA 24 ELECTRIC DC CONTROL</div>", unsafe_allow_html=True)
        col_bats = st.columns(2)
        with col_bats[0]:
            st.markdown("<div class='korry-label'>BAT 1</div>", unsafe_allow_html=True)
            if st.button("BAT 1 PUSH", key="btn_bat1"):
                st.session_state.p_bat = "ON" if st.session_state.p_bat == "OFF" else "OFF"
                if st.session_state.p_bat == "ON":
                    st.session_state.p_cas = ["🔸 28 FUEL: BOOST PUMPS OFF", "🔸 36 BLEED: APU VALVE CLOSED", "🔸 29 HYDR: PRESS LOW"]
                else:
                    st.session_state.p_cas = ["🟢 COLD DARK CONFIGURATION", "Avión apagado completamente."]
                st.rerun()
            st.markdown("<div class='anunciador-verde'>AUTO</div>" if st.session_state.p_bat == "ON" else "<div class='anunciador-apagado'>OFF</div>", unsafe_allow_html=True)
        with col_bats[1]:
            st.markdown("<div class='korry-label'>BAT 2</div>", unsafe_allow_html=True)
            if st.button("BAT 2 PUSH", key="btn_bat2"):
                st.session_state.p_bat = "ON" if st.session_state.p_bat == "OFF" else "OFF"
                st.rerun()
            st.markdown("<div class='anunciador-verde'>AUTO</div>" if st.session_state.p_bat == "ON" else "<div class='anunciador-apagado'>OFF</div>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

        # INTERFAZ EXPANDIDA CORREGIDA: LAS 4 BOMBAS INDEPENDIENTES DEL COODE 2 (1A - 2A - 2B - 3A)
        st.markdown("<div class='subpanel-3d'><div class='titulo-serigrafia'>⛽ ATA 28 FUEL OVERHEAD ROW - BOOST PUMPS (1A - 2A - 2B - 3A)</div>", unsafe_allow_html=True)
        col_boosters = st.columns(4)
        nombres_pumps = ["PUMP 1A", "PUMP 2A", "PUMP 2B", "PUMP 3A"]
        for i in range(4):
            with col_boosters[i]:
                st.markdown(f"<div class='korry-label'>{nombres_pumps[i]}</div>", unsafe_allow_html=True)
                if st.button("PUSH", key=f"btn_pump_{i}"):
                    if st.session_state.p_bat == "ON":
                        st.session_state.p_boost_pumps[i] = "ON" if st.session_state.p_boost_pumps[i] == "OFF" else "OFF"
                        # Si todas las bombas requeridas están armadas, limpiamos el mensaje global del CAS
                        if all(p == "ON" for p in st.session_state.p_boost_pumps):
                            st.session_state.p_cas = [x for x in st.session_state.p_cas if "28 FUEL" not in x]
                    st.rerun()
                st.markdown("<div class='anunciador-verde'>ON</div>" if st.session_state.p_boost_pumps[i] == "ON" else "<div class='anunciador-amber'>FAULT</div>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

        # ATA 36 / 49 APU & BLEED
        st.markdown("<div class='subpanel-3d'><div class='titulo-serigrafia'>🌬️ ATA 36 / 49 AUXILIARY POWER & BLEED AIR</div>", unsafe_allow_html=True)
        col_apubl = st.columns(2)
        with col_apubl[0]:
            st.markdown("<div class='korry-label'>APU MASTER</div>", unsafe_allow_html=True)
            if st.button("APU PUSH", key="btn_apu_mst"):
                if st.session_state.p_bat == "ON":
                    st.session_state.p_apu = "RUN" if st.session_state.p_apu == "OFF" else "OFF"
                    if st.session_state.p_apu == "OFF": st.session_state.p_bleed = "CLOSED"
                st.rerun()
            st.markdown("<div class='anunciador-verde'>ON (100%)</div>" if st.session_state.p_apu == "RUN" else "<div class='anunciador-apagado'>OFF</div>", unsafe_allow_html=True)
        with col_apubl[1]:
            st.markdown("<div class='korry-label'>APU BLEED</div>", unsafe_allow_html=True)
            if st.button("BLEED PUSH", key="btn_apu_bld"):
                if st.session_state.p_bat == "ON" and st.session_state.p_apu == "RUN":
                    st.session_state.p_bleed = "OPEN" if st.session_state.p_bleed == "CLOSED" else "CLOSED"
                    if st.session_state.p_bleed == "OPEN":
                        st.session_state.p_cas = [x for x in st.session_state.p_cas if "36 BLEED" not in x]
                    else:
                        if "🔸 36 BLEED: APU VALVE CLOSED" not in st.session_state.p_cas:
                            st.session_state.p_cas.append("🔸 36 BLEED: APU VALVE CLOSED")
                st.rerun()
            st.markdown("<div class='anunciador-amber'>OPEN</div>" if st.session_state.p_bleed == "OPEN" else "<div class='anunciador-apagado'>CLOSED</div>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

        # ATA 70 IGNITION / START PANEL
        st.markdown("<div class='subpanel-3d'><div class='titulo-serigrafia'>⚙️ ATA 70 IGNITION / CRANK PANEL</div>", unsafe_allow_html=True)
        c_motores = st.columns(3)
        for i in range(3):
            with c_motores[i]:
                st.markdown(f"<div class='korry-label'>ENG {i+1} START</div>", unsafe_allow_html=True)
                if st.button("ENGAGE", key=f"btn_start_{i}"):
                    if st.session_state.p_bat == "ON":
                        if st.session_state.p_bleed == "OPEN":
                            st.session_state.p_eng[i] = "CRANK"
                            if st.session_state.p_lever[i] == "RUN":
                                st.session_state.p_cas = [f"🚨 72 ENGINE: HOT START DETECTED ENG {i+1}", "Falla estructural crítica. Ignición prematura con N2 bajo."]
                                st.session_state.audio_alarma = "alarma_critica"
                        else:
                            st.session_state.p_cas = [f"🚨 36 BLEED: AIR FAULT ENG {i+1}", "Presión neumática insuficiente para mover la turbina del motor."]
                            st.session_state.audio_alarma = "alarma_critica"
                    st.rerun()
                st.markdown(f"<div class='anunciador-amber'>{st.session_state.p_eng[i]}</div>" if st.session_state.p_eng[i] != "STBY" else "<div class='anunciador-apagado'>STBY</div>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

        # Pedestal Central: Palancas Físicas de Combustible
        st.markdown("<div class='subpanel-3d'><div class='titulo-serigrafia'>🎮 COCKPIT CENTRAL PEDESTAL (ENG FUEL LEVERS)</div>", unsafe_allow_html=True)
        c_levers = st.columns(3)
        for i in range(3):
            with c_levers[i]:
                st.markdown(f"<div class='korry-label'>LEVER {i+1}</div>", unsafe_allow_html=True)
                st.markdown("<div class='slot-palanca'>", unsafe_allow_html=True)
                if st.button("TOGGLE", key=f"btn_lever_{i}"):
                    if st.session_state.p_bat == "ON":
                        st.session_state.p_lever[i] = "RUN" if st.session_state.p_lever[i] == "SHUTOFF" else "SHUTOFF"
                        if st.session_state.p_lever[i] == "RUN":
                            # Verificación estricta: requiere que las correspondientes bombas booster estén armadas (ON)
                            if "OFF" in st.session_state.p_boost_pumps:
                                st.session_state.p_cas = [f"🚨 28 FUEL: BOOST PUMP FAULT ENG {i+1}", "Falta de presión en el múltiple. Revise la hilera de bombas (1A-2A-2B-3A)."]
                                st.session_state.audio_alarma = "alarma_critica"
                            elif st.session_state.p_eng[i] == "CRANK":
                                st.session_state.p_eng[i] = "RUN IDLE"
                                st.session_state.p_cas = ["🟢 SYSTEMS RUNNING NOMINAL", "Flujo y presiones de combustible estables según CODDE 2."]
                            else:
                                st.session_state.p_cas = [f"🚨 72 ENGINE: HOT START DETECTED ENG {i+1}", "Palanca en RUN sin aire de rotación previo. Daño térmico severo."]
                                st.session_state.audio_alarma = "alarma_critica"
                    st.rerun()
                st.markdown("<div class='anunciador-verde'>RUN</div>" if st.session_state.p_lever[i] == "RUN" else "<div class='anunciador-amber'>SHUTOFF</div>", unsafe_allow_html=True)
                st.markdown("</div>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

        if st.button("🚨 LIMPIAR Y REINICIAR PROCEDIMIENTO CODDE 2"):
            st.session_state.p_bat = "OFF"; st.session_state.p_apu = "OFF"; st.session_state.p_bleed = "CLOSED"; st.session_state.p_boost_pumps = ["OFF", "OFF", "OFF", "OFF"]
            st.session_state.p_eng = ["STBY", "STBY", "STBY"]; st.session_state.p_lever = ["SHUTOFF", "SHUTOFF", "SHUTOFF"]
            st.session_state.p_cas = ["🟢 COLD DARK CONFIGURATION", "Avión apagado completamente. Requiere energización esencial."]
            st.rerun()
        st.markdown("</div>", unsafe_allow_html=True)

    with col_display_honeywell:
        st.markdown("### 📺 Honeywell EASy Avionics Display")
        
        # Relojes e instrumentos analógicos en tiempo real para los 3 motores
        html_clocks = ""
        for i in range(3):
            n1 = 24.5 if st.session_state.p_eng[i] == "RUN IDLE" else 0.0
            n2 = 58.2 if st.session_state.p_eng[i] == "RUN IDLE" else (22.0 if st.session_state.p_eng[i] == "CRANK" else 0.0)
            itt = 510 if st.session_state.p_eng[i] == "RUN IDLE" else 15
            html_clocks += f"""
            <div style="display:inline-block; width:30%; background:#020b1e; border:1px solid #1e293b; padding:8px; border-radius:6px; text-align:center; margin:1%;">
                <div style="font-size:0.75rem; color:#38bdf8; font-weight:bold; font-family: monospace; letter-spacing:1px; margin-bottom: 8px;">ENG {i+1}</div>
                <canvas id="n1_{i}" width="80" height="80"></canvas><div style="font-size:0.7rem; color:#4ade80; font-family: monospace; margin: 4px 0;">N1: {n1}%</div>
                <canvas id="n2_{i}" width="80" height="80"></canvas><div style="font-size:0.7rem; color:#4ade80; font-family: monospace; margin: 4px 0;">N2: {n2}%</div>
                <canvas id="itt_{i}" width="80" height="80"></canvas><div style="font-size:0.7rem; color:#fbbf24; font-family: monospace; margin: 4px 0;">ITT: {itt}°C</div>
            </div>
            <script>
                function draw(id, val, max, color) {{
                    let c = document.getElementById(id); if(!c) return;
                    let ctx = c.getContext("2d"); ctx.clearRect(0,0,80,80);
                    ctx.beginPath(); ctx.arc(40,40,32,0.75*Math.PI, 2.25*Math.PI); ctx.strokeStyle="#1a202c"; ctx.lineWidth=3; ctx.stroke();
                    let a = 0.75*Math.PI + (val/max)*(1.5*Math.PI);
                    ctx.beginPath(); ctx.arc(40,40,32,0.75*Math.PI, a); ctx.strokeStyle=color; ctx.lineWidth=3; ctx.stroke();
                }}
                setTimeout(() => {{ draw("n1_{i}", {n1}, 100, "#4ade80"); draw("n2_{i}", {n2}, 100, "#38bdf8"); draw("itt_{i}", {itt}, 800, "#fbbf24"); }}, 100);
            </script>
            """
        components.html(f"<div style='display:flex; justify-content: space-around; background: #020b1e; padding: 10px; border-radius:10px; border: 2px solid #1e293b;'>{html_clocks}</div>", height=350)

        # Configuración visual de advertencias CAS (Modo Azul Táctico Nocturno)
        contiene_alertas = any("🚨" in x or "ALERT" in x or "FAULT" in x for x in st.session_state.p_cas)
        borde_mfd = "#f87171" if contiene_alertas else "#334155"
        color_pantalla = "#1e0b0b" if contiene_alertas else "#01040a"
        color_texto_feed = "#fca5a5" if contiene_alertas else "#38bdf8"

        st.markdown(f"""
            <div class="pantalla-mfd" style="border: 5px solid {borde_mfd}; background-color: {color_pantalla}; color: {color_texto_feed};">
                <div style="border-bottom: 2px solid #1e293b; padding-bottom: 8px; margin-bottom: 25px; display: flex; justify-content: space-between; font-size: 0.8rem; font-weight: bold; color: #94a3b8;">
                    <span>MFD MONITOR: HONEYWELL PRIMUS EASy II</span>
                    <span>FLIGHT DECK SYNOPTIC</span>
                </div>
                <div style="font-size: 0.8rem; line-height: 1.6; font-family: monospace;">
                    <div>⚙️ TELEMETRÍA DE PREVALORACIÓN REAL DE SISTEMAS:</div>
                    <div style="padding-left:15px;">• DC BATERÍAS GENERAL   : {st.session_state.p_bat}</div>
                    <div style="padding-left:15px;">• APU GENERATOR CORE    : {st.session_state.p_apu}</div>
                    <div style="padding-left:15px;">• APU ISOLATION BLEED   : {st.session_state.p_bleed}</div>
                    <div style="padding-left:15px;">• BOOSTER PRESSURE (1A) : {"ONLINE" if st.session_state.p_boost_pumps[0] == "ON" else "LOW PRESS"}</div>
                    <div style="padding-left:15px;">• BOOSTER PRESSURE (2A) : {"ONLINE" if st.session_state.p_boost_pumps[1] == "ON" else "LOW PRESS"}</div>
                    <div style="padding-left:15px;">• BOOSTER PRESSURE (2B) : {"ONLINE" if st.session_state.p_boost_pumps[2] == "ON" else "LOW PRESS"}</div>
                    <div style="padding-left:15px;">• BOOSTER PRESSURE (3A) : {"ONLINE" if st.session_state.p_boost_pumps[3] == "ON" else "LOW PRESS"}</div>
                </div>
                <div style="border-top: 1px dashed #1e293b; margin: 15px 0;"></div>
                <div style="font-size: 0.82rem; font-weight: bold; margin-bottom: 8px;">🔔 CREW ALERTING SYSTEM (CAS) DISPLAY FEED:</div>
                <div style="background-color: rgba(0,0,0,0.4); padding: 10px; border-radius: 6px; border: 1px solid #1e293b;">
                    {"<br>".join([f"<div style='margin-bottom: 6px;'>{x}</div>" for x in st.session_state.p_cas])}
                </div>
            </div>
        """, unsafe_allow_html=True)

# ==============================================================================
# MÓDULOS DE MANTENIMIENTO TÉCNICO COMPLETO (RESTAURADO E INTACTO SIN ERRORES)
# ==============================================================================
else:
    st.title("🔧 Pantalla de Procedimientos de Mantenimiento (Técnicos)")
    st.markdown("---")
    
    # SE CORRIGE EL NAMEERROR DEFINIENDO EL MODULO ACTIVO DIRECTAMENTE DESDE LA NAVEGACIÓN SIDEBAR
    modulo_activo = opcion_sistema
    
    if modulo_activo == "MÓDULO I: ENERGIZACIÓN (ATA 24)":
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
                    if procedimiento == "ENERGIZACIÓN COMPLETA (COLD OPERATIONS)" and st.session_state.fase_e == 8: st.session_state.fase_e = 9
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

    elif modulo_activo == "MÓDULO II: COMBUSTIBLE (ATA 28)":
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
