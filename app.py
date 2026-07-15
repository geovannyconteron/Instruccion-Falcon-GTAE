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
# DISEÑO CSS AVANZADO: REPLICACIÓN EXACTA DEL CHASIS METÁLICO DASSAULT
# ==============================================================================
st.markdown("""
    <style>
    .main { background-color: #0d1117; color: #e2e8f0; font-family: sans-serif; }
    
    /* Chasis Gris del Overhead del Falcon 7X */
    .overhead-grey-chassis {
        background-color: #5a6370;
        border: 4px solid #3a414c;
        border-radius: 8px;
        padding: 20px;
        box-shadow: inset 0 2px 4px rgba(255,255,255,0.2), 0 15px 35px rgba(0,0,0,0.8);
    }
    
    /* Cajas Negras de Sub-módulos del Manual */
    .panel-modulo-negro {
        background: #11141a;
        border: 2px solid #282f3a;
        border-bottom: 3px solid #0a0d12;
        border-radius: 6px;
        padding: 15px;
        margin-bottom: 15px;
        box-shadow: inset 0 2px 5px rgba(0,0,0,0.8);
    }
    
    .label-serigrafia {
        color: #a0aec0;
        font-family: 'Courier New', monospace;
        font-weight: bold;
        font-size: 0.75rem;
        text-align: center;
        letter-spacing: 2px;
        margin-bottom: 12px;
        text-transform: uppercase;
        border-bottom: 1px solid #232a35;
        padding-bottom: 4px;
    }

    /* Korry Switches Reales del Falcon 7X */
    .korry-switch-container {
        background: linear-gradient(180deg, #2d3545, #191f29);
        border: 2px solid #3d495c;
        border-bottom: 4px solid #0b0e14;
        border-radius: 4px;
        padding: 6px;
        text-align: center;
        min-height: 85px;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        box-shadow: 0 4px 6px rgba(0,0,0,0.5);
    }
    
    .korry-text {
        font-family: 'Courier New', monospace;
        font-size: 0.65rem;
        font-weight: bold;
        color: #94a3b8;
    }

    .luz-dividida-top {
        height: 16px; border-radius: 2px; font-size: 0.6rem; font-weight: 900; line-height: 16px; margin-bottom: 2px;
    }
    .luz-dividida-btm {
        height: 16px; border-radius: 2px; font-size: 0.6rem; font-weight: 900; line-height: 16px;
    }

    /* Brillos Dicroicos del CAS y Anunciadores */
    .glow-green { background-color: #042f1a; color: #4ade80; border: 1px solid #22c55e; box-shadow: 0 0 8px #22c55e; }
    .glow-amber { background-color: #451a03; color: #fbbf24; border: 1px solid #f59e0b; box-shadow: 0 0 8px #f59e0b; }
    .glow-red { background-color: #3b0712; color: #f87171; border: 1px solid #ef4444; box-shadow: 0 0 10px #ef4444; }
    .glow-off { background-color: #0b0e14; color: #2d3748; border: 1px solid #1a202c; }

    .pantalla-mfd {
        font-family: 'Courier New', monospace; border: 5px solid #334155; background-color: #01040a; 
        color: #38bdf8; padding: 22px; border-radius: 8px; min-height: 560px; box-shadow: inset 0 0 30px rgba(0,0,0,0.9);
    }
    </style>
""", unsafe_allow_html=True)

# ==============================================================================
# ENTORNO PROTEGIDO - NAVEGACIÓN LATERAL GENERAL RESTRUCTURADA
# ==============================================================================
with st.sidebar:
    st.markdown("<h4 style='color:#38bdf8; font-family:monospace;'>✈️ FAE SIM CONTROL</h4>", unsafe_allow_html=True)
    if st.button("🔒 DESCONECTAR CABINA"):
        st.session_state.autenticado = False
        st.rerun()
    st.markdown("---")
    tipo_procedimiento = st.radio("ENTORNO DE SIMULACIÓN:", ["✈️ PROCEDIMIENTOS OPERATIVOS (PILOTOS)", "🔧 PROCEDIMIENTOS DE MANTENIMIENTO (TÉCNICOS)"])
    
    if tipo_procedimiento == "🔧 PROCEDIMIENTOS DE MANTENIMIENTO (TÉCNICOS)":
        opcion_sistema = st.radio("CONSOLA INTERACTIVA TÉCNICA:", ["MÓDULO I: ENERGIZACIÓN (ATA 24)", "MÓDULO II: COMBUSTIBLE (ATA 28)"])
    else:
        opcion_sistema = "MÓDULO III: ENCENDIDO DE MOTORES"

# Inicializaciones base de memoria
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

# Estados de Cabina de los Pilotos según las capturas del CODDE 2
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
if "p_cas" not in st.session_state: st.session_state.p_cas = ["🟢 COLD DARK CONFIGURATION", "Avión desenergizado en rampa."]

# ------------------------------------------------------------------------------
# MÓDULO III: ARQUITECTURA EXACTA DEL OVERHEAD PANEL REPLICADA
# ------------------------------------------------------------------------------
if opcion_sistema == "MÓDULO III: ENCENDIDO DE MOTORES":
    col_panel_over, col_avionics_display = st.columns([1.3, 1])
    
    with col_panel_over:
        st.markdown("<div class='overhead-grey-chassis'>", unsafe_allow_html=True)
        
        # 1. BLOQUE DE INCENDIOS (FIRE PROTECTION PANEL - PARTE SUPERIOR DEL OVERHEAD)
        st.markdown("<div class='panel-modulo-negro'><div class='label-serigrafia'>🔥 FIRE PROTECTION PANEL</div>", unsafe_allow_html=True)
        c_fire = st.columns([1, 1, 1, 1, 1])
        with c_fire[0]:
            st.markdown("<div class='korry-switch-container'><span class='korry-text'>ENG 1</span>", unsafe_allow_html=True)
            st.markdown("<div class='luz-dividida-top glow-red'>FIRE</div>" if st.session_state.p_fire_test else "<div class='luz-dividida-top glow-off'>FIRE</div>", unsafe_allow_html=True)
            st.markdown("<div class='luz-dividida-btm glow-off'>DISCH</div></div>", unsafe_allow_html=True)
        with c_fire[1]:
            st.markdown("<div class='korry-switch-container'><span class='korry-text'>APU</span>", unsafe_allow_html=True)
            st.markdown("<div class='luz-dividida-top glow-red'>FIRE</div>" if st.session_state.p_fire_test else "<div class='luz-dividida-top glow-off'>FIRE</div>", unsafe_allow_html=True)
            st.markdown("<div class='luz-dividida-btm glow-off'>DISCH</div></div>", unsafe_allow_html=True)
        with c_fire[2]:
            st.markdown("<div class='korry-switch-container'><span class='korry-text'>TEST</span>", unsafe_allow_html=True)
            if st.button("FIRE\nTEST", key="btn_fire_test"):
                if st.session_state.p_bat == "ON":
                    st.session_state.p_fire_test = not st.session_state.p_fire_test
                    if st.session_state.p_fire_test:
                        st.session_state.p_cas = ["🟩 FIRE TEST IN PROGRESS", "All fire warning loops operational."]
                    else:
                        st.session_state.p_cas = ["🔸 28 FUEL: BOOST PUMPS OFF", "🔸 36 BLEED: APU VALVE CLOSED"]
                st.rerun()
            st.markdown("<div class='luz-dividida-btm glow-green'>TEST</div>" if st.session_state.p_fire_test else "<div class='luz-dividida-btm glow-off'>TEST</div>", unsafe_allow_html=True)
            st.markdown("</div>", unsafe_allow_html=True)
        with c_fire[3]:
            st.markdown("<div class='korry-switch-container'><span class='korry-text'>ENG 2</span>", unsafe_allow_html=True)
            st.markdown("<div class='luz-dividida-top glow-red'>FIRE</div>" if st.session_state.p_fire_test else "<div class='luz-dividida-top glow-off'>FIRE</div>", unsafe_allow_html=True)
            st.markdown("<div class='luz-dividida-btm glow-off'>DISCH</div></div>", unsafe_allow_html=True)
        with c_fire[4]:
            st.markdown("<div class='korry-switch-container'><span class='korry-text'>ENG 3</span>", unsafe_allow_html=True)
            st.markdown("<div class='luz-dividida-top glow-red'>FIRE</div>" if st.session_state.p_fire_test else "<div class='luz-dividida-top glow-off'>FIRE</div>", unsafe_allow_html=True)
            st.markdown("<div class='luz-dividida-btm glow-off'>DISCH</div></div>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

        # 2. SECCIÓN DE ENERGIZACIÓN ESENCIAL (DC SUPPLY PANEL)
        st.markdown("<div class='panel-modulo-negro'><div class='label-serigrafia'>⚡ DC SUPPLY & BATTERIES</div>", unsafe_allow_html=True)
        c_elec = st.columns(2)
        with c_elec[0]:
            st.markdown("<div class='korry-switch-container'><span class='korry-text'>BAT 1</span>", unsafe_allow_html=True)
            if st.button("BAT 1", key="b_b1"):
                st.session_state.p_bat = "ON" if st.session_state.p_bat == "OFF" else "OFF"
                st.session_state.p_cas = ["🔸 28 FUEL: BOOST PUMPS OFF", "🔸 36 BLEED: APU VALVE CLOSED"] if st.session_state.p_bat == "ON" else ["🟢 COLD DARK CONFIGURATION"]
                st.rerun()
            st.markdown("<div class='luz-dividida-btm glow-green'>AUTO</div>" if st.session_state.p_bat == "ON" else "<div class='luz-dividida-btm glow-off'>OFF</div>", unsafe_allow_html=True)
            st.markdown("</div>", unsafe_allow_html=True)
        with c_elec[1]:
            st.markdown("<div class='korry-switch-container'><span class='korry-text'>BAT 2</span>", unsafe_allow_html=True)
            if st.button("BAT 2", key="b_b2"):
                st.session_state.p_bat = "ON" if st.session_state.p_bat == "OFF" else "OFF"
                st.rerun()
            st.markdown("<div class='luz-dividida-btm glow-green'>AUTO</div>" if st.session_state.p_bat == "ON" else "<div class='luz-dividida-btm glow-off'>OFF</div>", unsafe_allow_html=True)
            st.markdown("</div>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

        # 3. REPLICACIÓN GEOMÉTRICA EXACTA DEL MÓDULO FUEL (BOMBAS BOOSTER 1A - 2A - 2B - 3A)
        st.markdown("<div class='panel-modulo-negro'><div class='label-serigrafia'>⛽ ATA 28 OVERHEAD FUEL BOOST PUMPS MATRIX</div>", unsafe_allow_html=True)
        
        # Simulación de las celdas de tanques alares del diagrama real
        c_fuel_top = st.columns(2)
        with c_fuel_top[0]:
            st.markdown("<div class='korry-switch-container'><span class='korry-text'>TANK 1 - PUMP 1A</span>", unsafe_allow_html=True)
            if st.button("PUMP 1A", key="b_1a"):
                if st.session_state.p_bat == "ON": st.session_state.p_boost_1a = "ON" if st.session_state.p_boost_1a == "OFF" else "OFF"
                st.rerun()
            st.markdown("<div class='luz-dividida-btm glow-green'>ON</div>" if st.session_state.p_boost_1a == "ON" else "<div class='luz-dividida-btm glow-amber'>OFF</div>", unsafe_allow_html=True)
            st.markdown("</div>", unsafe_allow_html=True)
        with c_fuel_top[1]:
            st.markdown("<div class='korry-switch-container'><span class='korry-text'>TANK 3 - PUMP 3A</span>", unsafe_allow_html=True)
            if st.button("PUMP 3A", key="b_3a"):
                if st.session_state.p_bat == "ON": st.session_state.p_boost_3a = "ON" if st.session_state.p_boost_3a == "OFF" else "OFF"
                st.rerun()
            st.markdown("<div class='luz-dividida-btm glow-green'>ON</div>" if st.session_state.p_boost_3a == "ON" else "<div class='luz-dividida-btm glow-amber'>OFF</div>", unsafe_allow_html=True)
            st.markdown("</div>", unsafe_allow_html=True)
            
        st.markdown("<div style='margin: 10px 0;'></div>", unsafe_allow_html=True)
        
        c_fuel_btm = st.columns(2)
        with c_fuel_btm[0]:
            st.markdown("<div class='korry-switch-container'><span class='korry-text'>TANK 2 - PUMP 2A</span>", unsafe_allow_html=True)
            if st.button("PUMP 2A", key="b_2a"):
                if st.session_state.p_bat == "ON": st.session_state.p_boost_2a = "ON" if st.session_state.p_boost_2a == "OFF" else "OFF"
                st.rerun()
            st.markdown("<div class='luz-dividida-btm glow-green'>ON</div>" if st.session_state.p_boost_2a == "ON" else "<div class='luz-dividida-btm glow-amber'>OFF</div>", unsafe_allow_html=True)
            st.markdown("</div>", unsafe_allow_html=True)
        with c_fuel_btm[1]:
            st.markdown("<div class='korry-switch-container'><span class='korry-text'>TANK 2 - PUMP 2B</span>", unsafe_allow_html=True)
            if st.button("PUMP 2B", key="b_2b"):
                if st.session_state.p_bat == "ON": st.session_state.p_boost_2b = "ON" if st.session_state.p_boost_2b == "OFF" else "OFF"
                st.rerun()
            st.markdown("<div class='luz-dividida-btm glow-green'>ON</div>" if st.session_state.p_boost_2b == "ON" else "<div class='luz-dividida-btm glow-amber'>OFF</div>", unsafe_allow_html=True)
            st.markdown("</div>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

        # 4. SANGRE NEUMÁTICA (APU NEUMÁTICA)
        st.markdown("<div class='panel-modulo-negro'><div class='label-serigrafia'>🌬️ ATA 36 / 49 APU BLEED AIR COOPERATIVE</div>", unsafe_allow_html=True)
        c_pneu = st.columns(2)
        with c_pneu[0]:
            st.markdown("<div class='korry-switch-container'><span class='korry-text'>APU MASTER</span>", unsafe_allow_html=True)
            if st.button("MASTER", key="b_ap_m"):
                if st.session_state.p_bat == "ON":
                    st.session_state.p_apu = "RUN" if st.session_state.p_apu == "OFF" else "OFF"
                    if st.session_state.p_apu == "OFF": st.session_state.p_bleed = "CLOSED"
                st.rerun()
            st.markdown("<div class='luz-dividida-btm glow-green'>START</div>" if st.session_state.p_apu == "RUN" else "<div class='luz-dividida-btm glow-off'>OFF</div>", unsafe_allow_html=True)
            st.markdown("</div>", unsafe_allow_html=True)
        with c_pneu[1]:
            st.markdown("<div class='korry-switch-container'><span class='korry-text'>APU BLEED</span>", unsafe_allow_html=True)
            if st.button("BLEED", key="b_ap_b"):
                if st.session_state.p_bat == "ON" and st.session_state.p_apu == "RUN":
                    st.session_state.p_bleed = "OPEN" if st.session_state.p_bleed == "CLOSED" else "CLOSED"
                    if st.session_state.p_bleed == "OPEN":
                        st.session_state.p_cas = [x for x in st.session_state.p_cas if "36 BLEED" not in x]
                st.rerun()
            st.markdown("<div class='luz-dividida-btm glow-amber'>OPEN</div>" if st.session_state.p_bleed == "OPEN" else "<div class='luz-dividida-btm glow-off'>CLOSED</div>", unsafe_allow_html=True)
            st.markdown("</div>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

        # 5. PANEL DE ARRANCADORES DE LOS MOTORES
        st.markdown("<div class='panel-modulo-negro'><div class='label-serigrafia'>⚙️ MAN START / MOTORING ROW</div>", unsafe_allow_html=True)
        c_st = st.columns(3)
        for i in range(3):
            with c_st[i]:
                st.markdown(f"<div class='korry-switch-container'><span class='korry-text'>ENG {i+1} START</span>", unsafe_allow_html=True)
                if st.button("ENGAGE", key=f"b_st_{i}"):
                    if st.session_state.p_bat == "ON":
                        if st.session_state.p_bleed == "OPEN":
                            st.session_state.p_eng[i] = "CRANK"
                        else:
                            st.session_state.p_cas = [f"🚨 36 BLEED: AIR FAULT ENG {i+1}", "Pneumatic colector has no APU Bleed pressure."]
                            st.session_state.audio_alarma = "alarma_critica"
                    st.rerun()
                st.markdown("<div class='luz-dividida-btm glow-amber'>CRANK</div>" if st.session_state.p_eng[i] == "CRANK" else "<div class='luz-dividida-btm glow-off'>STBY</div>", unsafe_allow_html=True)
                st.markdown("</div>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

        # 6. PEDESTAL CENTRAL: PALANCAS DE COMBUSTIBLE EN EL SUELO
        st.markdown("<div class='pedestal-chasis'><div class='label-serigrafia'>🎮 CENTRAL PEDESTAL (HP FUEL LEVERS)</div>", unsafe_allow_html=True)
        c_lv = st.columns(3)
        for i in range(3):
            with c_lv[i]:
                st.markdown(f"<div class='slot-palanca'>", unsafe_allow_html=True)
                if st.button("CUT/FLUX", key=f"b_lv_{i}"):
                    if st.session_state.p_bat == "ON":
                        st.session_state.p_lever[i] = "RUN" if st.session_state.p_lever[i] == "SHUTOFF" else "SHUTOFF"
                        if st.session_state.p_lever[i] == "RUN":
                            # El manual exige verificar de forma estricta las 4 bombas antes de la mezcla
                            if "OFF" in [st.session_state.p_boost_1a, st.session_state.p_boost_2a, st.session_state.p_boost_2b, st.session_state.p_boost_3a]:
                                st.session_state.p_cas = [f"🚨 28 FUEL: BOOST PUMP FAULT ENG {i+1}", "Checked failed: Booster pumps 1A-2A-2B-3A must be ON."]
                                st.session_state.audio_alarma = "alarma_critica"
                            elif st.session_state.p_eng[i] == "CRANK":
                                st.session_state.p_eng[i] = "RUN IDLE"
                                st.session_state.p_cas = ["🟢 SYSTEMS RUNNING NOMINAL", "Engines profiles stable."]
                            else:
                                st.session_state.p_cas = [f"🚨 72 ENGINE: HOT START DETECTED ENG {i+1}", "HP fuel cock open with no air rotation."]
                                st.session_state.audio_alarma = "alarma_critica"
                    st.rerun()
                st.markdown("<div class='luz-dividida-btm glow-green'>RUN</div>" if st.session_state.p_lever[i] == "RUN" else "<div class='luz-dividida-btm glow-red'>CUT-OFF</div>", unsafe_allow_html=True)
                st.markdown("</div>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

        st.markdown("</div>", unsafe_allow_html=True) # Cierre chasis gris

    with col_avionics_display:
        st.markdown("### 📺 Honeywell EASy Avionics Display")
        
        # Telemetría de relojes síncronos
        html_clocks = ""
        for i in range(3):
            n1 = 24.5 if st.session_state.p_eng[i] == "RUN IDLE" else 0.0
            n2 = 58.2 if st.session_state.p_eng[i] == "RUN IDLE" else (22.0 if st.session_state.p_eng[i] == "CRANK" else 0.0)
            itt = 510 if st.session_state.p_eng[i] == "RUN IDLE" else 15
            html_clocks += f"""
            <div style="display:inline-block; width:30%; background:#020b1e; border:1px solid #1e293b; padding:5px; border-radius:4px; text-align:center; margin:1%;">
                <div style="font-size:0.75rem; color:#38bdf8; font-weight:bold; font-family: monospace;">ENG {i+1}</div>
                <canvas id="n1_{i}" width="70" height="70"></canvas><div style="font-size:0.65rem; color:#4ade80;">N1:{n1}%</div>
                <canvas id="n2_{i}" width="70" height="70"></canvas><div style="font-size:0.65rem; color:#38bdf8;">N2:{n2}%</div>
                <canvas id="itt_{i}" width="70" height="70"></canvas><div style="font-size:0.65rem; color:#fbbf24;">IT:{itt}°C</div>
            </div>
            <script>
                function draw(id, val, max, col) {{
                    let c = document.getElementById(id); if(!c) return;
                    let ctx = c.getContext("2d"); ctx.clearRect(0,0,70,70);
                    ctx.beginPath(); ctx.arc(35,35,28,0.75*Math.PI, 2.25*Math.PI); ctx.strokeStyle="#1a202c"; ctx.lineWidth=2; ctx.stroke();
                    let a = 0.75*Math.PI + (val/max)*(1.5*Math.PI);
                    ctx.beginPath(); ctx.arc(35,35,28,0.75*Math.PI, a); ctx.strokeStyle=col; ctx.lineWidth=2; ctx.stroke();
                }}
                setTimeout(() => {{ draw("n1_{i}", {n1}, 100, "#4ade80"); draw("n2_{i}", {n2}, 100, "#38bdf8"); draw("itt_{i}", {itt}, 800, "#fbbf24"); }}, 50);
            </script>
            """
        components.html(f"<div style='display:flex; justify-content: space-around; background: #020b1e; padding: 5px; border-radius:8px;'>{html_clocks}</div>", height=320)

        contiene_alertas = any("🚨" in x or "FAULT" in x for x in st.session_state.p_cas)
        borde_mfd = "#f87171" if contiene_alertas else "#334155"
        color_pantalla = "#190509" if contiene_alertas else "#020612"

        st.markdown(f"""
            <div class="pantalla-mfd" style="border: 5px solid {borde_mfd}; background-color: {color_pantalla};">
                <div style="border-bottom: 2px solid #1e293b; padding-bottom: 8px; margin-bottom: 25px; display: flex; justify-content: space-between; font-size: 0.8rem; font-weight: bold; color: #94a3b8;">
                    <span>MFD MONITOR: PRIMUS EASy II SYSTEM</span>
                    <span>SYNOPTIC STATUS</span>
                </div>
                <div style="font-size: 0.8rem; line-height: 1.6; font-family: monospace;">
                    <div>📊 REAL TIME SYNOPTIC FEED (ATA 28 / 36):</div>
                    <div>• APU DC ELECT VALVES : {st.session_state.p_bat}</div>
                    <div>• APU AIR BLEED COCK  : {st.session_state.p_bleed}</div>
                    <div>• FUEL PUMP PRESSURE 1A : {"PRESS HIGH" if st.session_state.p_boost_1a == "ON" else "LOW"}</div>
                    <div>• FUEL PUMP PRESSURE 2A : {"PRESS HIGH" if st.session_state.p_boost_2a == "ON" else "LOW"}</div>
                    <div>• FUEL PUMP PRESSURE 2B : {"PRESS HIGH" if st.session_state.p_boost_2b == "ON" else "LOW"}</div>
                    <div>• FUEL PUMP PRESSURE 3A : {"PRESS HIGH" if st.session_state.p_boost_3a == "ON" else "LOW"}</div>
                </div>
                <div style="border-top: 1px dashed #1e293b; margin: 15px 0;"></div>
                <div style="font-size: 0.82rem; font-weight: bold; margin-bottom: 8px;">🔔 CREW ALERTING SYSTEM (CAS) LOGS:</div>
                <div style="background-color: rgba(0,0,0,0.4); padding: 10px; border-radius: 6px; border: 1px solid #1e293b;">
                    {"<br>".join([f"<div style='margin-bottom: 6px;'>{x}</div>" for x in st.session_state.p_cas])}
                </div>
            </div>
        """, unsafe_allow_html=True)

# ==============================================================================
# MÓDULOS DE MANTENIMIENTO TÉCNICO COMPLETO RESTAURADOS AL 100%
# ==============================================================================
else:
    st.title("🔧 Pantalla de Procedimientos de Mantenimiento (Técnicos)")
    st.markdown("---")
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
            status_easydisplay = f"🚨 CAS ALERT: ERROR PROCEDIMENTAL DETECTADO\n\n  REPORTE CRÍTICO: {st.session_state.descripcion_falla}" if st.session_state.falla_procedimiento else f"📲 MODO EVALUACIÓN ACTIVO\n\nFase Eléctrica Actual: Paso {st.session_state.fase_e}/12"

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
