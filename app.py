import streamlit as st
import streamlit.components.v1 as components

# Configuración táctica de pantalla ancha optimizada para simulador
st.set_page_config(page_title="Falcon 7X Overhead Panel", page_icon="✈️", layout="wide")

# ==============================================================================
# SCRIPT DE AUDIO INSTANTÁNEO PARA BOTONES (SIN RETARDO)
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
            osc.connect(gain); gain.connect(ctx.destination);
            osc.start(); osc.stop(ctx.currentTime + 0.04);
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
# CSS ULTRACOMPACTO: SIN RELLENOS, SIN DISTRACCIONES, MAXIMIZACIÓN DE ESPACIO
# ==============================================================================
st.markdown("""
    <style>
    /* Fondo oscuro de cabina nocturna */
    .main { background-color: #0b0e14; color: #f1f5f9; font-family: sans-serif; padding: 5px !important; }
    .block-container { padding-top: 5px !important; padding-bottom: 5px !important; }
    
    /* Módulos de chasis negro mate integrados sin bordes gigantes */
    .subpanel-overhead-real {
        background: #12161f;
        border: 2px solid #232d3d;
        border-radius: 4px;
        padding: 10px;
        margin-bottom: 8px;
        box-shadow: inset 0 1px 3px rgba(0,0,0,0.8);
    }
    
    /* Serigrafía técnica minimalista del Falcon 7X */
    .serigrafia-cabina {
        color: #64748b;
        font-family: 'Courier New', monospace;
        font-weight: bold;
        font-size: 0.7rem;
        text-align: center;
        letter-spacing: 2px;
        margin-bottom: 8px;
        text-transform: uppercase;
    }

    /* Korry Switches Reales del Falcon 7X */
    .korry-switch-frame {
        background: linear-gradient(180deg, #1f2633, #11151e);
        border: 1.5px solid #334155;
        border-bottom: 3px solid #090d14;
        border-radius: 3px;
        padding: 4px;
        text-align: center;
        min-height: 70px;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        box-shadow: 0 2px 4px rgba(0,0,0,0.6);
    }
    
    .korry-label {
        font-family: 'Courier New', monospace;
        font-size: 0.6rem;
        font-weight: bold;
        color: #94a3b8;
        line-height: 1.1;
    }

    .capa-luz {
        height: 14px; border-radius: 1px; font-size: 0.55rem; font-weight: 900; line-height: 14px; margin-top: 2px;
    }

    /* Brillo de lámparas dicroicas */
    .glow-green { background-color: #022c22; color: #34d399; border: 1px solid #10b981; box-shadow: 0 0 6px #10b981; }
    .glow-amber { background-color: #451a03; color: #fbbf24; border: 1px solid #f59e0b; box-shadow: 0 0 6px #f59e0b; }
    .glow-red { background-color: #450a0a; color: #f87171; border: 1px solid #ef4444; box-shadow: 0 0 8px #ef4444; }
    .glow-off { background-color: #090d16; color: #1e293b; border: 1px solid #0f172a; }

    /* Estilo del display integrado de aviónica */
    .mfd-integrated-screen {
        font-family: 'Courier New', monospace; background-color: #020612; border: 3px solid #1e293b;
        color: #38bdf8; padding: 12px; border-radius: 4px; min-height: 480px; box-shadow: inset 0 0 20px rgba(0,0,0,0.9);
    }
    </style>
""", unsafe_allow_html=True)

# ==============================================================================
# MEMORIA DE ESTADO DE DISPOSITIVOS DE CABINA
# ==============================================================================
if "p_bat" not in st.session_state: st.session_state.p_bat = "OFF"
if "p_fire_test" not in st.session_state: st.session_state.p_fire_test = False
if "p_apu" not in st.session_state: st.session_state.p_apu = "OFF"
if "p_bleed" not in st.session_state: st.session_state.p_bleed = "CLOSED"
if "p_boost_1a" not in st.session_state: st.session_state.p_boost_1a = "OFF"
if "p_boost_2a" not in st.session_state: st.session_state.p_boost_2a = "OFF"
if "p_boost_2b" not in st.session_state: st.session_state.p_boost_2b = "OFF"
if "p_boost_3a" not in st.session_state: st.session_state.p_boost_3a = "OFF"
if "p_eng" not in st.session_state: st.session_state.p_eng = ["STBY", "STBY", "STBY"]
if "p_lever" not in st.session_state: st.session_state.p_lever = ["SHUTOFF", "SHUTOFF", "SHUTOFF"]
if "p_cas" not in st.session_state: st.session_state.p_cas = ["🟢 COLD DARK CONFIGURATION", "Presione baterías para iniciar."]

# ==============================================================================
# OVERHEAD PANEL DIRECTO Y RECTILÍNEO (SIN MARCOS RELLENOS)
# ==============================================================================
col_overhead, col_mfd = st.columns([1.4, 1])

with col_overhead:
    # --- SUBPANEL 1: FIRE PROTECTION ---
    st.markdown("<div class='subpanel-overhead-real'><div class='serigrafia-cabina'>FIRE PROTECTION</div>", unsafe_allow_html=True)
    c_fire = st.columns(5)
    with c_fire[0]:
        st.markdown("<div class='korry-switch-frame'><span class='korry-label'>ENG 1</span>", unsafe_allow_html=True)
        st.markdown("<div class='capa-luz glow-red'>FIRE</div>" if st.session_state.p_fire_test else "<div class='capa-luz glow-off'>FIRE</div>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)
    with c_fire[1]:
        st.markdown("<div class='korry-switch-frame'><span class='korry-label'>APU</span>", unsafe_allow_html=True)
        st.markdown("<div class='capa-luz glow-red'>FIRE</div>" if st.session_state.p_fire_test else "<div class='capa-luz glow-off'>FIRE</div>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)
    with c_fire[2]:
        st.markdown("<div class='korry-switch-frame'><span class='korry-label'>FIRE TEST</span>", unsafe_allow_html=True)
        if st.button("TEST", key="btn_f_test", use_container_width=True):
            if st.session_state.p_bat == "ON":
                st.session_state.p_fire_test = not st.session_state.p_fire_test
                st.session_state.p_cas = ["🟩 FIRE TEST ACTIVE", "Sistemas de lazo de alarma OK."] if st.session_state.p_fire_test else ["🔸 Lámparas apagadas."]
            st.rerun()
        st.markdown("<div class='capa-luz glow-green'>TEST</div>" if st.session_state.p_fire_test else "<div class='capa-luz glow-off'>TEST</div>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)
    with c_fire[3]:
        st.markdown("<div class='korry-switch-frame'><span class='korry-label'>ENG 2</span>", unsafe_allow_html=True)
        st.markdown("<div class='capa-luz glow-red'>FIRE</div>" if st.session_state.p_fire_test else "<div class='capa-luz glow-off'>FIRE</div>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)
    with c_fire[4]:
        st.markdown("<div class='korry-switch-frame'><span class='korry-label'>ENG 3</span>", unsafe_allow_html=True)
        st.markdown("<div class='capa-luz glow-red'>FIRE</div>" if st.session_state.p_fire_test else "<div class='capa-luz glow-off'>FIRE</div>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

    # --- SUBPANEL 2: ELECTRICO (BATERÍAS Y CORRIENTE CONTINUA) ---
    st.markdown("<div class='subpanel-overhead-real'><div class='serigrafia-cabina'>DC ELECTRICAL</div>", unsafe_allow_html=True)
    c_elec = st.columns(2)
    with c_elec[0]:
        st.markdown("<div class='korry-switch-frame'><span class='korry-label'>BAT 1</span>", unsafe_allow_html=True)
        if st.button("BAT 1", key="btn_bat1", use_container_width=True):
            st.session_state.p_bat = "ON" if st.session_state.p_bat == "OFF" else "OFF"
            st.session_state.p_cas = ["🔸 ALERTA SANGRE APU", "Bomba booster desactivada."] if st.session_state.p_bat == "ON" else ["🟢 APAGADO COMPLETO"]
            st.rerun()
        st.markdown("<div class='capa-luz glow-green'>AUTO</div>" if st.session_state.p_bat == "ON" else "<div class='capa-luz glow-off'>OFF</div>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)
    with c_elec[1]:
        st.markdown("<div class='korry-switch-frame'><span class='korry-label'>BAT 2</span>", unsafe_allow_html=True)
        if st.button("BAT 2", key="btn_bat2", use_container_width=True):
            st.session_state.p_bat = "ON" if st.session_state.p_bat == "OFF" else "OFF"
            st.rerun()
        st.markdown("<div class='capa-luz glow-green'>AUTO</div>" if st.session_state.p_bat == "ON" else "<div class='capa-luz glow-off'>OFF</div>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

    # --- SUBPANEL 3: COMBUSTIBLE (BOMBAS DE COMBUSTIBLE EN ARREGLO GEOMÉTRICO) ---
    st.markdown("<div class='subpanel-overhead-real'><div class='serigrafia-cabina'>FUEL CONTROL SYSTEM</div>", unsafe_allow_html=True)
    
    # Fila superior de bombas (Bombas Exteriores 1A y 3A)
    c_fuel_ala = st.columns(2)
    with c_fuel_ala[0]:
        st.markdown("<div class='korry-switch-frame'><span class='korry-label'>LH BOOST 1A</span>", unsafe_allow_html=True)
        if st.button("1A", key="btn_1a", use_container_width=True):
            if st.session_state.p_bat == "ON": st.session_state.p_boost_1a = "ON" if st.session_state.p_boost_1a == "OFF" else "OFF"
            st.rerun()
        st.markdown("<div class='capa-luz glow-green'>ON</div>" if st.session_state.p_boost_1a == "ON" else "<div class='capa-luz glow-amber'>OFF</div>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)
    with c_fuel_ala[1]:
        st.markdown("<div class='korry-switch-frame'><span class='korry-label'>RH BOOST 3A</span>", unsafe_allow_html=True)
        if st.button("3A", key="btn_3a", use_container_width=True):
            if st.session_state.p_bat == "ON": st.session_state.p_boost_3a = "ON" if st.session_state.p_boost_3a == "OFF" else "OFF"
            st.rerun()
        st.markdown("<div class='capa-luz glow-green'>ON</div>" if st.session_state.p_boost_3a == "ON" else "<div class='capa-luz glow-amber'>OFF</div>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)
        
    st.markdown("<div style='margin: 8px 0;'></div>", unsafe_allow_html=True)
    
    # Fila inferior de bombas (Bombas de Presión Central 2A y 2B)
    c_fuel_ctr = st.columns(2)
    with c_fuel_ctr[0]:
        st.markdown("<div class='korry-switch-frame'><span class='korry-label'>CTR BOOST 2A</span>", unsafe_allow_html=True)
        if st.button("2A", key="btn_2a", use_container_width=True):
            if st.session_state.p_bat == "ON": st.session_state.p_boost_2a = "ON" if st.session_state.p_boost_2a == "OFF" else "OFF"
            st.rerun()
        st.markdown("<div class='capa-luz glow-green'>ON</div>" if st.session_state.p_boost_2a == "ON" else "<div class='capa-luz glow-amber'>OFF</div>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)
    with c_fuel_ctr[1]:
        st.markdown("<div class='korry-switch-frame'><span class='korry-label'>CTR BOOST 2B</span>", unsafe_allow_html=True)
        if st.button("2B", key="btn_2b", use_container_width=True):
            if st.session_state.p_bat == "ON": st.session_state.p_boost_2b = "ON" if st.session_state.p_boost_2b == "OFF" else "OFF"
            st.rerun()
        st.markdown("<div class='capa-luz glow-green'>ON</div>" if st.session_state.p_boost_2b == "ON" else "<div class='capa-luz glow-amber'>OFF</div>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

    # --- SUBPANEL 4: APU NEUMÁTICA ---
    st.markdown("<div class='subpanel-overhead-real'><div class='serigrafia-cabina'>APU CONTROL</div>", unsafe_allow_html=True)
    c_apu = st.columns(2)
    with c_apu[0]:
        st.markdown("<div class='korry-switch-frame'><span class='korry-label'>APU MASTER</span>", unsafe_allow_html=True)
        if st.button("RUN", key="btn_apu_m", use_container_width=True):
            if st.session_state.p_bat == "ON":
                st.session_state.p_apu = "RUN" if st.session_state.p_apu == "OFF" else "OFF"
                if st.session_state.p_apu == "OFF": st.session_state.p_bleed = "CLOSED"
            st.rerun()
        st.markdown("<div class='capa-luz glow-green'>RUN</div>" if st.session_state.p_apu == "RUN" else "<div class='capa-luz glow-off'>OFF</div>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)
    with c_apu[1]:
        st.markdown("<div class='korry-switch-frame'><span class='korry-label'>APU BLEED</span>", unsafe_allow_html=True)
        if st.button("BLEED", key="btn_apu_b", use_container_width=True):
            if st.session_state.p_bat == "ON" and st.session_state.p_apu == "RUN":
                st.session_state.p_bleed = "OPEN" if st.session_state.p_bleed == "CLOSED" else "CLOSED"
            st.rerun()
        st.markdown("<div class='capa-luz glow-amber'>OPEN</div>" if st.session_state.p_bleed == "OPEN" else "<div class='capa-luz glow-off'>CLOSED</div>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

# ==============================================================================
# COLUMNA DERECHA: DISPLAY INTEGRADO DE AVIONICA (PANTALLA MFD REAL)
# ==============================================================================
with col_mfd:
    st.markdown("<div class='mfd-integrated-screen'>", unsafe_allow_html=True)
    st.markdown("""
        <div style="border-bottom: 1.5px solid #1e293b; padding-bottom: 4px; margin-bottom: 12px; font-size: 0.75rem; font-weight: bold; color: #475569; display: flex; justify-content: space-between;">
            <span>MFD MONITOR: HONEYWELL PRIMUS EASy</span>
            <span>SYSTEM DIRECT SYNOPTIC</span>
        </div>
    """, unsafe_allow_html=True)
    
    # Telemetría síncrona compacta
    status_v = "BAT AUTO (28.2 VDC)" if st.session_state.p_bat == "ON" else "0.0 VDC - COLD SHIELD"
    status_p1 = "HIGH" if st.session_state.p_boost_1a == "ON" else "0 PSI"
    status_p2a = "HIGH" if st.session_state.p_boost_2a == "ON" else "0 PSI"
    status_p2b = "HIGH" if st.session_state.p_boost_2b == "ON" else "0 PSI"
    status_p3 = "HIGH" if st.session_state.p_boost_3a == "ON" else "0 PSI"
    
    st.markdown(f"""
        <div style="font-size: 0.7rem; line-height: 1.4; color: #38bdf8;">
            <b>📋 ESTADO DIRECTO DE ENERGIZACIÓN (ATA 24/28):</b><br>
            • MAIN BUS POWER  : {status_v}<br>
            • PUMP LH 1A      : <span style="color:{'#10b981' if st.session_state.p_boost_1a == 'ON' else '#ef4444'}">{status_p1}</span><br>
            • PUMP CTR 2A     : <span style="color:{'#10b981' if st.session_state.p_boost_2a == 'ON' else '#ef4444'}">{status_p2a}</span><br>
            • PUMP CTR 2B     : <span style="color:{'#10b981' if st.session_state.p_boost_2b == 'ON' else '#ef4444'}">{status_p2b}</span><br>
            • PUMP RH 3A      : <span style="color:{'#10b981' if st.session_state.p_boost_3a == 'ON' else '#ef4444'}">{status_p3}</span><br>
            • APU BLEED AIR   : <span style="color:{'#fbbf24' if st.session_state.p_bleed == 'OPEN' else '#64748b'}">{st.session_state.p_bleed}</span>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<div style='border-top: 1px dashed #1e293b; margin: 10px 0;'></div>", unsafe_allow_html=True)
    
    # Logs del Crew Alerting System (CAS)
    st.markdown("<div style='font-size: 0.7rem; font-weight: bold; margin-bottom: 6px; color: #94a3b8;'>🔔 CREW ALERTING SYSTEM:</div>", unsafe_allow_html=True)
    log_html = "".join([f"<div style='margin-bottom: 4px; font-size:0.68rem;'>{x}</div>" for x in st.session_state.p_cas])
    st.markdown(f"<div style='background: #050b14; padding: 8px; border-radius: 3px; border: 1.5px solid #1e293b; min-height: 120px;'>{log_html}</div>", unsafe_allow_html=True)
    
    st.markdown("</div>", unsafe_allow_html=True)
