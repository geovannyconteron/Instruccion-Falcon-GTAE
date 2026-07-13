import streamlit as st
import streamlit.components.v1 as components

# Configuración estructural de la cabina táctica FAE
st.set_page_config(page_title="Falcon 7X Flight Deck - GTAE", page_icon="✈️", layout="wide")

# ==============================================================================
# DISEÑO SKEUOMÓRFICO TRIDIMENSIONAL DE CABINA (CSS GLOBAL)
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
# SISTEMA DE LOGIN DE SEGURIDAD CON FOTO MAESTRA FAE
# ==============================================================================
if "autenticado" not in st.session_state: st.session_state.autenticado = False

if not st.session_state.autenticado:
    st.markdown("<br><br>", unsafe_allow_html=True)
    _, col_login, _ = st.columns([1, 1.6, 1])
    with col_login:
        st.markdown("""
            <div class='portada-container'>
                <h1 style='color: #ffffff; font-size: 1.6rem; font-family: monospace; margin-bottom: 5px;'>SISTEMA DE INSTRUCCIÓN SIMULADA</h1>
                <h3 style='color: #3b82f6; font-size: 1.1rem; font-family: monospace; margin-bottom: 10px;'>FALCON 7X - GTAE</h3>
            </div>
        """, unsafe_allow_html=True)
        
        st.image("https://images.unsplash.com/photo-1540962351504-03099e0a754b?q=80&w=1200&auto=format&fit=crop", 
                 caption="Fuerza Aérea Ecuatoriana - Grupo de Transporte Aéreo Especial", use_container_width=True)
        
        with st.form("credenciales_cabina"):
            st.markdown("<h5 style='text-align: center; color: #94a3b8;'>🔒 CONTROL RESTRINGIDO - TRIPULACIÓN DE VUELO</h5>", unsafe_allow_html=True)
            txt_user = st.text_input("Técnico / Piloto ID:", placeholder="gtae_operator")
            txt_pass = st.text_input("Palabra de Paso:", type="password", placeholder="••••••••")
            if st.form_submit_button("CONECTAR INTERFACES DE FLOTA"):
                if txt_user == "gtae" and txt_pass == "7X2026":
                    st.session_state.autenticado = True
                    st.rerun()
                else: st.error("❌ Credenciales incorrectas.")
    st.stop()

# ==============================================================================
# MEMORIAS OPERACIONALES GENERALES
# ==============================================================================
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

# Variables de persistencia para el motor (evitan la pérdida de estados en la barra lateral)
if "engine_running_js" not in st.session_state: st.session_state.engine_running_js = False
if "apu_ready_js" not in st.session_state: st.session_state.apu_ready_js = False
if "bleed_open_js" not in st.session_state: st.session_state.bleed_open_js = False

# ==============================================================================
# SEPARACIÓN ESTRUCTURAL DE PANTALLAS (Barra Lateral Restringida)
# ==============================================================================
with st.sidebar:
    st.markdown("<h3 style='color: #38bdf8; font-family: monospace;'>🖥️ MANDO DE INSTRUCCIÓN</h3>", unsafe_allow_html=True)
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
# PANTALLA 1: PROCEDIMIENTOS OPERATIVOS (PILOTOS - ENGINE CLOCKS INTEGRADO)
# ------------------------------------------------------------------------------
if entorno_activo == "✈️ PANTALLAS DE PROCEDIMIENTOS OPERATIVOS":
    st.title("✈️ Pantalla de Procedimientos Operativos (Pilotos)")
    st.subheader("Entrenamiento de Arranque de Plantas Motrices - Indicadores Tipo Reloj")
    st.markdown("---")

    # Inyección del sistema autónomo Honeywell en JavaScript para evitar el parpadeo
    # Dibuja tres relojes de aguja reales (N1, N2, ITT) con animación vectorial por hardware.
    html_engine_clocks = f"""
    <div style="background-color: #04070e; border: 5px solid #334155; padding: 20px; border-radius: 8px; color: #38bdf8; font-family: 'Courier New', monospace; min-height: 580px;">
        <div style="display: flex; justify-content: space-between; border-bottom: 2px solid #334155; padding-bottom: 5px; margin-bottom: 15px; font-weight: bold;">
            <span>HONEYWELL EASy: AVIATION GAUGES DISP</span><span>ATA: 70/72</span>
        </div>
        
        <div style="display: flex; gap: 15px; background: #1a202c; padding: 15px; border-radius: 6px; border: 2px solid #2d3748; margin-bottom: 20px; justify-content: space-around;">
            <div style="text-align:center;">
                <button onclick="controlAPU()" style="padding: 10px 15px; font-weight: bold; background: #334155; color: white; border: 1px solid #475569; border-radius: 4px; cursor: pointer;">APU MASTER</button>
                <div id="apu_lbl" style="margin-top: 5px; font-size:0.75rem; color:#4b5563; font-weight:bold;">OFF</div>
            </div>
            <div style="text-align:center;">
                <button onclick="controlBleed()" style="padding: 10px 15px; font-weight: bold; background: #334155; color: white; border: 1px solid #475569; border-radius: 4px; cursor: pointer;">APU BLEED VALVE</button>
                <div id="bleed_lbl" style="margin-top: 5px; font-size:0.75rem; color:#4b5563; font-weight:bold;">CLOSED</div>
            </div>
            <div style="text-align:center;">
                <button onclick="startEngine1()" style="padding: 10px 15px; font-weight: bold; background: #b91c1c; color: white; border: 1px solid #ef4444; border-radius: 4px; cursor: pointer;">ENG 1 START</button>
                <div id="eng1_lbl" style="margin-top: 5px; font-size:0.75rem; color:#4b5563; font-weight:bold;">STBY</div>
            </div>
            <div style="text-align:center;">
                <button onclick="toggleLever()" style="padding: 10px 15px; font-weight: bold; background: #475569; color: white; border: 1px solid #64748b; border-radius: 4px; cursor: pointer;">RUN / SHUTOFF LEVER</button>
                <div id="lever_lbl" style="margin-top: 5px; font-size:0.75rem; color:#ef4444; font-weight:bold;">❄️ SHUT OFF</div>
            </div>
        </div>

        <div style="display: flex; justify-content: space-around; align-items: center; margin-top: 30px; flex-wrap: wrap;">
            <div style="text-align: center;">
                <canvas id="clockN1" width="160" height="160"></canvas>
                <div style="font-weight: bold; margin-top: 8px; color: #e2e8f0;">N1 (FAN %)</div>
                <div id="val_n1" style="font-size: 1.3rem; font-weight: bold; color: #22c55e;">0.0%</div>
            </div>
            <div style="text-align: center;">
                <canvas id="clockN2" width="160" height="160"></canvas>
                <div style="font-weight: bold; margin-top: 8px; color: #e2e8f0;">N2 (CORE %)</div>
                <div id="val_n2" style="font-size: 1.3rem; font-weight: bold; color: #22c55e;">0.0%</div>
            </div>
            <div style="text-align: center;">
                <canvas id="clockITT" width="160" height="160"></canvas>
                <div style="font-weight: bold; margin-top: 8px; color: #e2e8f0;">ITT (°C)</div>
                <div id="val_itt" style="font-size: 1.3rem; font-weight: bold; color: #f59e0b;">15 °C</div>
            </div>
        </div>

        <div style="border-top: 1px dashed #334155; margin-top: 25px; padding-top: 15px;">
            <div style="font-weight: bold; color: #fbbf24;">🔔 CREW ALERTING SYSTEM (CAS) LIVE DATA FEED:</div>
            <div id="cas_msg" style="margin-top: 8px; color: #38bdf8; font-size:0.85rem; white-space: pre-wrap;">🟢 SYSTEMS GENERAL RUN NOMINAL\n Parámetros operacionales dentro de los límites estipulados por Dassault.</div>
        </div>
    </div>

    <script>
        // Variables internas de simulación local
        let apuStatus = "OFF", apuRpm = 0, bleedOpen = false, engPhase = "STBY", leverRun = false;
        let n1 = 0, n2 = 0, itt = 15;
        
        function controlAPU() {{
            const ac = new (window.AudioContext || window.webkitAudioContext)();
            let osc = ac.createOscillator(); osc.connect(ac.destination); osc.start(); osc.stop(ac.currentTime + 0.05);
            if (apuStatus === "OFF") {{ apuStatus = "RUN"; apuRpm = 100; }} else {{ apuStatus = "OFF"; apuRpm = 0; bleedOpen = false; }}
            document.getElementById("apu_lbl").innerText = apuStatus === "RUN" ? "🟢 RUN (100%)" : "OFF";
            document.getElementById("apu_lbl").style.color = apuStatus === "RUN" ? "#4ade80" : "#4b5563";
            updateLabels();
        }}
        
        function controlBleed() {{
            if (apuStatus !== "RUN") {{ alert("No hay presión neumática. Inicialice la APU."); return; }}
            bleedOpen = !bleedOpen;
            document.getElementById("bleed_lbl").innerText = bleedOpen ? "🔶 OPEN (PRES)" : "CLOSED";
            document.getElementById("bleed_lbl").style.color = bleedOpen ? "#fbbf24" : "#4b5563";
        }}
        
        function toggleLever() {{
            leverRun = !leverRun;
            document.getElementById("lever_lbl").innerText = leverRun ? "🔥 RUN (FUEL ON)" : "❄️ SHUT OFF";
            document.getElementById("lever_lbl").style.color = leverRun ? "#4ade80" : "#ef4444";
            if (leverRun && engPhase === "CRANK" && n2 < 15.0) {{
                engPhase = "FALLO";
                document.getElementById("cas_msg").innerText = "🚨 ALERT CAS: HOT START IN ENGINE 1!\\n Combustible inyectado prematuramente con rotación N2 inferior al 15%. Terminar proceso.";
                document.getElementById("cas_msg").style.color = "#ef4444";
            }}
        }}

        function startEngine1() {{
            if (!bleedOpen) {{
                document.getElementById("cas_msg").innerText = "🚨 FALLO DE ARRANQUE: No hay presión neumática disponible en las líneas (APU BLEED está CLOSED).";
                document.getElementById("cas_msg").style.color = "#ef4444";
                return;
            }}
            if (engPhase === "STBY") {{
                engPhase = "CRANK";
                document.getElementById("eng1_lbl").innerText = "🔶 CRANK";
                document.getElementById("eng1_lbl").style.color = "#fbbf24";
            }}
        }}

        function updateLabels() {{
            if (apuStatus === "OFF") {{
                document.getElementById("bleed_lbl").innerText = "CLOSED"; document.getElementById("bleed_lbl").style.color = "#4b5563";
            }}
        }}

        // Motor de renderizado analógico (HTML5 Canvas Clocks)
        function drawGauge(canvasId, value, minVal, maxVal, label) {{
            const canvas = document.getElementById(canvasId); if(!canvas) return;
            const ctx = canvas.getContext("2d");
            const cx = canvas.width / 2, cy = canvas.height / 2, r = canvas.width / 2 - 10;
            ctx.clearRect(0, 0, canvas.width, canvas.height);
            
            // Corona exterior del instrumento
            ctx.beginPath(); ctx.arc(cx, cy, r, 0, 2*Math.PI); ctx.strokeStyle = "#475569"; ctx.lineWidth = 4; ctx.stroke();
            
            // Escala arco interno
            ctx.beginPath(); ctx.arc(cx, cy, r - 6, 0.75 * Math.PI, 2.25 * Math.PI); ctx.strokeStyle = "#1e293b"; ctx.lineWidth = 6; ctx.stroke();
            
            // Cálculo del ángulo de la aguja analógica
            let pct = (value - minVal) / (maxVal - minVal); if(pct < 0) pct = 0; if(pct > 1) pct = 1;
            let angle = 0.75 * Math.PI + pct * (1.5 * Math.PI);
            
            // Dibujar aguja de aviación
            ctx.beginPath(); ctx.moveTo(cx, cy);
            ctx.lineTo(cx + (r - 15) * Math.cos(angle), cy + (r - 15) * Math.sin(angle));
            ctx.strokeStyle = canvasId === "clockITT" ? "#ef4444" : "#4ade80"; ctx.lineWidth = 3; ctx.stroke();
            
            // Centro físico
            ctx.beginPath(); ctx.arc(cx, cy, 5, 0, 2*Math.PI); ctx.fillStyle = "#ffffff"; ctx.fill();
        }}

        // Bucle dinámico local (Corre a 30 FPS en el cliente, Cero recargas de Streamlit)
        setInterval(() => {{
            if (engPhase === "CRANK") {{
                n2 += 0.4; if (n2 >= 18.0 && leverRun) {{ engPhase = "IGN"; document.getElementById("eng1_lbl").innerText = "🔶 IGNITION"; }}
                if (n2 >= 25.0 && !leverRun) n2 = 25.0;
            }} else if (engPhase === "IGN") {{
                n2 += 0.5; itt += 8; if (itt >= 520) {{ engPhase = "RUN"; document.getElementById("eng1_lbl").innerText = "🟩 RUN IDLE"; document.getElementById("eng1_lbl").style.color = "#4ade80"; }}
            }} else if (engPhase === "RUN") {{
                if (n2 < 57.4) n2 += 0.3; else n2 = 57.4;
                if (n1 < 24.2) n1 += 0.2; else n1 = 24.2;
                if (itt > 490) itt -= 1.5; else itt = 490;
            }}
            
            document.getElementById("val_n1").innerText = n1.toFixed(1) + "%";
            document.getElementById("val_n2").innerText = n2.toFixed(1) + "%";
            document.getElementById("val_itt").innerText = Math.round(itt) + " °C";
            
            drawGauge("clockN1", n1, 0, 100, "N1");
            drawGauge("clockN2", n2, 0, 100, "N2");
            drawGauge("clockITT", itt, 0, 800, "ITT");
        }}, 33);
    </script>
    """
    components.html(html_engine_clocks, height=620)

# ------------------------------------------------------------------------------
# PANTALLA 2: PROCEDIMIENTOS DE MANTENIMIENTO (TÉCNICOS - RESTAURADO INTEGRAL)
# ------------------------------------------------------------------------------
else:
    st.title("🔧 Pantalla de Procedimientos de Mantenimiento (Técnicos)")
    st.markdown("---")
    
    # --- MÓDULO I: DISTRIBUCIÓN ELÉCTRICA (ATA 24) ---
    if modulo_activo == "MÓDULO I: DISTRIBUCIÓN ELÉCTRICA (ATA 24)":
        st.subheader("Módulo I: Distribución Eléctrica y Secuenciación Avanzada de Barras")
        procedimiento = st.radio("⚙️ SELECCIONE PROCEDIMIENTO DE EVALUACIÓN:", ["ENERGIZACIÓN COMPLETA (COLD OPERATIONS)", "DESENERGIZACIÓN COMPLETA (SHUTDOWN)"], horizontal=True)
        
        def forzar_alarma(texto):
            st.session_state.falla_procedimiento = True
            st.session_state.descripcion_falla = texto

        col_fisica_panel, col_telemetria_pdu = st.columns([1.3, 1])
        with col_fisica_panel:
            st.markdown("<div class='overhead-frame'>", unsafe_allow_html=True)
            st.markdown("<div class='subpanel-3d'><div class='titulo-serigrafia'>⚡ DC SUPPLY PANEL (OVERHEAD UPPER ROW) ⚡</div>", unsafe_allow_html=True)
            grid_sup = st.columns(8)
            with grid_sup[0]:
                st.button("GALLEY MSTR", disabled=True, key="g_m_row")
                st.markdown("<div class='anunciador-apagado'>OFF</div>", unsafe_allow_html=True)
            with grid_sup[1]:
                if st.button("LH MSTR", key="l_mstr_full"):
                    if procedimiento == "ENERGIZACIÓN COMPLETA (COLD OPERATIONS)":
                        if st.session_state.fase_e == 11: st.session_state.fase_e = 12
                        else: forzar_alarma("LH MASTER activado de forma prematura fuera de la secuencia técnica.")
                    st.rerun()
                luz = "<div class='anunciador-verde'>ON</div>" if (procedimiento == "ENERGIZACIÓN COMPLETA (COLD OPERATIONS)" and st.session_state.fase_e >= 12) or procedimiento == "DESENERGIZACIÓN COMPLETA (SHUTDOWN)" else "<div class='anunciador-amber'>OFF</div>"
                st.markdown(luz, unsafe_allow_html=True)
            with grid_sup[2]:
                if st.button("LH INIT", key="lh_init_full"):
                    if procedimiento == "ENERGIZACIÓN COMPLETA (COLD OPERATIONS)":
                        if st.session_state.fase_e == 7: st.session_state.fase_e = 8
                        else: forzar_alarma("LH INIT accionado sin acoplamiento estructural del BUS TIE.")
                    st.rerun()
                luz = "<div class='anunciador-apagado'>RUN</div>" if (procedimiento == "ENERGIZACIÓN COMPLETA (COLD OPERATIONS)" and st.session_state.fase_e >= 8) or procedimiento == "DESENERGIZACIÓN COMPLETA (SHUTDOWN)" else "<div class='anunciador-amber'>OFF</div>"
                st.markdown(luz, unsafe_allow_html=True)
            with grid_sup[3]:
                if st.button("BUS TIE", key="bt_full"):
                    if procedimiento == "ENERGIZACIÓN COMPLETA (COLD OPERATIONS)":
                        if st.session_state.fase_e == 6: st.session_state.fase_e = 7
                        else: forzar_alarma("BUS TIE accionado previo al armado de seguridad de la RAT.")
                    st.rerun()
                luz = "<div class='anunciador-amber'>TIED</div>" if (procedimiento == "ENERGIZACIÓN COMPLETA (COLD OPERATIONS)" and st.session_state.fase_e >= 7) or procedimiento == "DESENERGIZACIÓN COMPLETA (SHUTDOWN)" else "<div class='anunciador-apagado'>AUTO</div>"
                st.markdown(luz, unsafe_allow_html=True)
            with grid_sup[4]:
                if st.button("RH INIT", key="rh_init_full"):
                    if procedimiento == "ENERGIZACIÓN COMPLETA (COLD OPERATIONS)":
                        if st.session_state.fase_e == 7: st.session_state.fase_e = 8
                        else: forzar_alarma("RH INIT accionado sin acoplamiento estructural del BUS TIE.")
                    st.rerun()
                luz = "<div class='anunciador-apagado'>RUN</div>" if (procedimiento == "ENERGIZACIÓN COMPLETA (COLD OPERATIONS)" and st.session_state.fase_e >= 8) or procedimiento == "DESENERGIZACIÓN COMPLETA (SHUTDOWN)" else "<div class='anunciador-amber'>OFF</div>"
                st.markdown(luz, unsafe_allow_html=True)
            with grid_sup[5]:
                if st.button("RH MSTR", key="rh_mstr_full"):
                    if procedimiento == "ENERGIZACIÓN COMPLETA (COLD OPERATIONS)":
                        if st.session_state.fase_e == 11: st.session_state.fase_e = 12
                        else: forzar_alarma("RH MASTER activado fuera de secuencia reglamentaria.")
                    st.rerun()
                luz = "<div class='anunciador-verde'>ON</div>" if (procedimiento == "ENERGIZACIÓN COMPLETA (COLD OPERATIONS)" and st.session_state.fase_e >= 12) or procedimiento == "DESENERGIZACIÓN COMPLETA (SHUTDOWN)" else "<div class='anunciador-amber'>OFF</div>"
                st.markdown(luz, unsafe_allow_html=True)
            with grid_sup[6]:
                if st.button("CABIN MSTR", key="cabin_full"):
                    if procedimiento == "ENERGIZACIÓN COMPLETA (COLD OPERATIONS)":
                        if st.session_state.fase_e == 9: st.session_state.fase_e = 10
                        else: forzar_alarma("CABIN MASTER accionado sin alimentación principal estable.")
                    st.rerun()
                luz = "<div class='anunciador-amber'>OFF</div>" if (procedimiento == "ENERGIZACIÓN COMPLETA (COLD OPERATIONS)" and st.session_state.fase_e >= 10) or procedimiento == "DESENERGIZACIÓN COMPLETA (SHUTDOWN)" else "<div class='anunciador-verde'>ON</div>"
                st.markdown(luz, unsafe_allow_html=True)
            with grid_sup[7]:
                if st.button("EXT PWR", key="ext_pwr_full"):
                    if procedimiento == "ENERGIZACIÓN COMPLETA (COLD OPERATIONS)":
                        if st.session_state.fase_e == 8: st.session_state.fase_e = 9
                        else: forzar_alarma("EXT POWER conectado sin configurar los parámetros de rampa.")
                    else:
                        if st.session_state.fase_d == 0: st.session_state.fase_d = 1
                    st.rerun()
                luz = "<div class='anunciador-verde'>ONLINE</div>" if (procedimiento == "ENERGIZACIÓN COMPLETA (COLD OPERATIONS)" and st.session_state.fase_e >= 9) or (procedimiento == "DESENERGIZACIÓN COMPLETA (SHUTDOWN)" and st.session_state.fase_d < 1) else "<div class='anunciador-apagado'>OFF</div>"
                st.markdown(luz, unsafe_allow_html=True)
            st.markdown("</div>", unsafe_allow_html=True)
            
            st.markdown("<div class='linea-tactica'></div>", unsafe_allow_html=True)
            
            # FILA INFERIOR COMPLETA
            st.markdown("<div class='subpanel-3d'><div class='titulo-serigrafia'>🔋 GENERATION & BATTERIES</div>", unsafe_allow_html=True)
            grid_inf = st.columns(8)
            with grid_inf[0]: st.button("GEN 1", disabled=True, key="g1_f"); st.markdown("<div class='anunciador-apagado'>OFF</div>", unsafe_allow_html=True)
            with grid_inf[1]:
                if st.button("LH ISOL", key="l_isol_f"):
                    if procedimiento == "ENERGIZACIÓN COMPLETA (COLD OPERATIONS)":
                        if st.session_state.fase_e == 10: st.session_state.fase_e = 11
                        else: forzar_alarma("Válvula de aislamiento de barras armada antes de establecer carga comercial.")
                    st.rerun()
                luz = "<div class='anunciador-apagado'>TIED</div>" if (procedimiento == "ENERGIZACIÓN COMPLETA (COLD OPERATIONS)" and st.session_state.fase_e >= 11) or procedimiento == "DESENERGIZACIÓN COMPLETA (SHUTDOWN)" else "<div class='anunciador-amber'>ISOL</div>"
                st.markdown(luz, unsafe_allow_html=True)
            with grid_inf[2]:
                if st.button("BAT 1", key="b1_f"):
                    if procedimiento == "ENERGIZACIÓN COMPLETA (COLD OPERATIONS)":
                        if st.session_state.fase_e == 4: st.session_state.fase_e = 5
                        else: forzar_alarma("BAT 1 activada sin comprobar el freno hidráulico de estacionamiento.")
                    else:
                        if st.session_state.fase_d == 1: st.session_state.fase_d = 2
                    st.rerun()
                luz = "<div class='anunciador-verde'>AUTO</div>" if (procedimiento == "ENERGIZACIÓN COMPLETA (COLD OPERATIONS)" and st.session_state.fase_e >= 5) or (procedimiento == "DESENERGIZACIÓN COMPLETA (SHUTDOWN)" and st.session_state.fase_d < 2) else "<div class='anunciador-apagado'>OFF</div>"
                st.markdown(luz, unsafe_allow_html=True)
            with grid_inf[3]:
                if st.button("BAT 2", key="b2_f"):
                    if procedimiento == "ENERGIZACIÓN COMPLETA (COLD OPERATIONS)":
                        if st.session_state.fase_e == 4: st.session_state.fase_e = 5
                        else: forzar_alarma("BAT 2 activada sin comprobar el freno hidráulico de estacionamiento.")
                    else:
                        if st.session_state.fase_d == 1: st.session_state.fase_d = 2
                    st.rerun()
                luz = "<div class='anunciador-verde'>AUTO</div>" if (procedimiento == "ENERGIZACIÓN COMPLETA (COLD OPERATIONS)" and st.session_state.fase_e >= 5) or (procedimiento == "DESENERGIZACIÓN COMPLETA (SHUTDOWN)" and st.session_state.fase_d < 2) else "<div class='anunciador-apagado'>OFF</div>"
                st.markdown(luz, unsafe_allow_html=True)
            with grid_inf[4]: st.button("RAT RSET", disabled=True, key="rat_f"); st.markdown("<div class='anunciador-apagado'>OFF</div>", unsafe_allow_html=True)
            with grid_inf[5]:
                if st.button("RH ISOL", key="r_isol_f"):
                    if procedimiento == "ENERGIZACIÓN COMPLETA (COLD OPERATIONS)":
                        if st.session_state.fase_e == 10: st.session_state.fase_e = 11
                        else: forzar_alarma("Válvula de aislamiento de barras armada antes de establecer carga comercial.")
                    st.rerun()
                luz = "<div class='anunciador-apagado'>TIED</div>" if (procedimiento == "ENERGIZACIÓN COMPLETA (COLD OPERATIONS)" and st.session_state.fase_e >= 11) or procedimiento == "DESENERGIZACIÓN COMPLETA (SHUTDOWN)" else "<div class='anunciador-amber'>ISOL</div>"
                st.markdown(luz, unsafe_allow_html=True)
            with grid_inf[6]: st.button("GEN 2", disabled=True, key="g2_f"); st.markdown("<div class='anunciador-apagado'>OFF</div>", unsafe_allow_html=True)
            with grid_inf[7]: st.button("GEN 3", disabled=True, key="g3_f"); st.markdown("<div class='anunciador-apagado'>OFF</div>", unsafe_allow_html=True)
            st.markdown("</div>", unsafe_allow_html=True)
            
            st.markdown("<div class='linea-tactica'></div>", unsafe_allow_html=True)
            
            # MANDOS EXTERNOS DE TIERRA INTEGRALES
            st.markdown("<div class='subpanel-3d'><div class='titulo-serigrafia'>🔧 CONFIGURACIÓN Y ACOPLE DE PLANTA EXTERNA</div>", unsafe_allow_html=True)
            grid_rampa = st.columns(5)
            with grid_rampa[0]:
                if st.button("🔌 RECEPTÁCULO GPU", key="rec_f"):
                    if procedimiento == "ENERGIZACIÓN COMPLETA (COLD OPERATIONS)":
                        if st.session_state.fase_e == 0: st.session_state.fase_e = 1
                        else: forzar_alarma("Planta acoplada fuera del orden de prevuelo.")
                    else:
                        if st.session_state.fase_d == 5: st.session_state.fase_d = 6
                    st.rerun()
                luz = "<div class='anunciador-verde'>CONECTADO</div>" if (procedimiento == "ENERGIZACIÓN COMPLETA (COLD OPERATIONS)" and st.session_state.fase_e >= 1) or (procedimiento == "DESENERGIZACIÓN COMPLETA (SHUTDOWN)" and st.session_state.fase_d < 6) else "<div class='anunciador-apagado'>DESCONECTADO</div>"
                st.markdown(luz, unsafe_allow_html=True)
            with grid_rampa[1]:
                if st.button("⚡ REGULADOR TENSIÓN TIERRA", key="pot_f"):
                    if procedimiento == "ENERGIZACIÓN COMPLETA (COLD OPERATIONS)":
                        if st.session_state.fase_e == 1: st.session_state.fase_e = 2
                        else: forzar_alarma("Ajuste de tensión modificado sin cableado de entrada.")
                    st.rerun()
                luz = "<div class='anunciador-verde'>28.0 VDC OK</div>" if (procedimiento == "ENERGIZACIÓN COMPLETA (COLD OPERATIONS)" and st.session_state.fase_e >= 2) or (procedimiento == "DESENERGIZACIÓN COMPLETA (SHUTDOWN)" and st.session_state.fase_d < 6) else "<div class='anunciador-apagado'>0.0 VDC</div>"
                st.markdown(luz, unsafe_allow_html=True)
            with grid_rampa[2]:
                if st.button("🎛️ SWITCH EXTERNO GPU", key="brk_f"):
                    if procedimiento == "ENERGIZACIÓN COMPLETA (COLD OPERATIONS)":
                        if st.session_state.fase_e == 2: st.session_state.fase_e = 3
                        else: forzar_alarma("Switch GPU colocado en ON sin regulación de voltaje nominal.")
                    else:
                        if st.session_state.fase_d == 3: st.session_state.fase_d = 4
                    st.rerun()
                luz = "<div class='anunciador-verde'>LÍNEA ONLINE</div>" if (procedimiento == "ENERGIZACIÓN COMPLETA (COLD OPERATIONS)" and st.session_state.fase_e >= 3) or (procedimiento == "DESENERGIZACIÓN COMPLETA (SHUTDOWN)" and st.session_state.fase_d < 4) else "<div class='anunciador-apagado'>LÍNEA OFF</div>"
                st.markdown(luz, unsafe_allow_html=True)
            with grid_rampa[3]:
                if st.button("⚙️ CONTROL FRENO PARQUEO", key="frn_f"):
                    if procedimiento == "ENERGIZACIÓN COMPLETA (COLD OPERATIONS)":
                        if st.session_state.fase_e == 3: st.session_state.fase_e = 4
                        else: forzar_alarma("Freno de parqueo omitido antes de la entrada de barras.")
                    st.rerun()
                luz = "<div class='anunciador-verde'>ENGANCHADO</div>" if (procedimiento == "ENERGIZACIÓN COMPLETA (COLD OPERATIONS)" and st.session_state.fase_e >= 4) or procedimiento == "DESENERGIZACIÓN COMPLETA (SHUTDOWN)" else "<div class='anunciador-apagado'>LIBERADO</div>"
                st.markdown(luz, unsafe_allow_html=True)
            with grid_rampa[4]:
                if st.button("🚪 COMPUERTA EXTERIOR F7X", key="door_f"):
                    if procedimiento == "DESENERGIZACIÓN COMPLETA (SHUTDOWN)":
                        if st.session_state.fase_d == 6: st.session_state.fase_d = 7
                    st.rerun()
                luz_c = "<div class='anunciador-apagado'>COMPUERTA CERRADA</div>" if procedimiento == "DESENERGIZACIÓN COMPLETA (SHUTDOWN)" and st.session_state.fase_d >= 7 else "<div class='anunciador-verde'>COMPUERTA ABIERTA</div>"
                st.markdown(luz_c, unsafe_allow_html=True)
            st.markdown("</div>", unsafe_allow_html=True)
            st.markdown("</div>", unsafe_allow_html=True)

        with col_telemetria_pdu:
            st.markdown("### 📺 Honeywell EASy Avionics Display")
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

            borde_crt = "#ef4444" if st.session_state.falla_procedimiento else "#475569"
            fondo_crt = "#200d0d" if st.session_state.falla_procedimiento else "#000000"
            texto_crt = "#fca5a5" if st.session_state.falla_procedimiento else "#38bdf8"
            status_easydisplay = f"🚨 CAS ALERT: ERROR PROCEDIMENTAL DETECTADO\n\n  REPORTE CRÍTICO: {st.session_state.descripcion_falla}" if st.session_state.falla_procedimiento else "📲 MODO EVALUACIÓN ACTIVO"

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

    # --- MÓDULO II: PRESIÓN DE COMBUSTIBLE (ATA 28) ---
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
                st.session_state.valvula_izq = st.radio("V_Izq:", ["ON", "OFF"], index=1 if st.session_state.valvula_izq == "OFF" else 0, key="v1", label_visibility="collapsed")
            with grid_valvulas[1]:
                st.markdown("<div style='font-family: monospace; font-weight:bold;'>CENTER VALVE</div>", unsafe_allow_html=True)
                st.session_state.valvula_ctr = st.radio("V_Ctr:", ["ON", "OFF"], index=1 if st.session_state.valvula_ctr == "OFF" else 0, key="v2", label_visibility="collapsed")
            with grid_valvulas[2]:
                st.markdown("<div style='font-family: monospace; font-weight:bold;'>RIGHT VALVE</div>", unsafe_allow_html=True)
                st.session_state.valvula_der = st.radio("V_Der:", ["ON", "OFF"], index=1 if st.session_state.valvula_der == "OFF" else 0, key="v3", label_visibility="collapsed")
            
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
            st.markdown(f"<div class='pantalla-mfd' style='border-color: #d97706; background-color: #0c0702; color: #fbbf24;'>REAL TIME REAL TOTAL COMBUSTIBLE: {st.session_state.combustible_actual} Lbs</div>", unsafe_allow_html=True)
