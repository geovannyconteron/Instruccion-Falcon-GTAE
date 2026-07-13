import streamlit as st
import streamlit.components.v1 as components

# Configuración estructural de la cabina táctica FAE
st.set_page_config(page_title="Falcon 7X Flight Deck - GTAE", page_icon="✈️", layout="wide")

# ==============================================================================
# ESTILOS SKEUOMÓRFICOS TRIDIMENSIONALES DE CABINA (CSS GLOBAL)
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
# MEMORIAS OPERACIONALES GENERALES
# ==============================================================================
if "autenticado" not in st.session_state: st.session_state.autenticado = False
if "audio_alarma" not in st.session_state: st.session_state.audio_alarma = None
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

# ==============================================================================
# SISTEMA DE LOGIN DE SEGURIDAD CON LA FOTO DEL FALCON FAE
# ==============================================================================
if not st.session_state.autenticado:
    st.markdown("<br><br>", unsafe_allow_html=True)
    _, col_login, _ = st.columns([1, 1.6, 1])
    with col_login:
        st.markdown("<div class='portada-container'><h1 style='color: #ffffff; font-size: 1.6rem; font-family: monospace;'>SISTEMA DE INSTRUCCIÓN SIMULADA</h1><h3 style='color: #3b82f6; font-size: 1.1rem; font-family: monospace;'>FALCON 7X - GTAE</h3></div>", unsafe_allow_html=True)
        st.image("https://images.unsplash.com/photo-1540962351504-03099e0a754b?q=80&w=1200&auto=format&fit=crop", caption="Fuerza Aérea Ecuatoriana - Grupo de Transporte Aéreo Especial", use_container_width=True)
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

# Manejador acústico de errores en mantenimiento
if st.session_state.audio_alarma == "alarma_critica":
    components.html("<script>try{const ctx=new(window.AudioContext||window.webkitAudioContext)();const osc=ctx.createOscillator();const gain=ctx.createGain();osc.type='sawtooth';osc.frequency.setValueAtTime(450,ctx.currentTime);gain.gain.setValueAtTime(0.2,ctx.currentTime);osc.connect(gain);gain.connect(ctx.destination);osc.start();setTimeout(()=>{osc.stop();},1200);}catch(e){}</script>", height=0, width=0)
    st.session_state.audio_alarma = None

# Barra lateral
with st.sidebar:
    st.markdown("<h3 style='color: #38bdf8; font-family: monospace;'>🖥 booster MANDO DE INSTRUCCIÓN</h3>", unsafe_allow_html=True)
    entorno_activo = st.radio("SELECCIONE EL TIPO DE PROCEDIMIENTO:", ["✈️ PANTALLAS DE PROCEDIMIENTOS OPERATIVOS", "🔧 PANTALLAS DE MANTENIMIENTO"])
    st.markdown("---")
    if entorno_activo == "✈️ PANTALLAS DE PROCEDIMIENTOS OPERATIVOS":
        modulo_activo = st.radio("MÓDULOS DE VUELO DISPONIBLES:", ["MÓDULO III: ARRANCADO DE MOTORES (PW307A)"])
    else:
        modulo_activo = st.radio("MÓDULOS MECÁNICOS DISPONIBLES:", ["MÓDULO I: DISTRIBUCIÓN ELÉCTRICA (ATA 24)", "MÓDULO II: PRESIÓN DE COMBUSTIBLE (ATA 28)"])

# ------------------------------------------------------------------------------
# PANTALLA 1: PROCEDIMIENTOS OPERATIVOS (3 MOTORES INTEGRALES EN CLIENTE)
# ------------------------------------------------------------------------------
if entorno_activo == "✈️ PANTALLAS DE PROCEDIMIENTOS OPERATIVOS":
    st.title("✈️ Pantalla de Procedimientos Operativos (Pilotos)")
    st.subheader("Entrenamiento de Arranque de Plantas Motrices - Relojes Triples")
    st.markdown("---")

    html_triple_clocks = """
    <div style="background-color: #04070e; border: 5px solid #334155; padding: 22px; border-radius: 8px; color: #38bdf8; font-family: 'Courier New', monospace;">
        <div style="display: flex; justify-content: space-between; border-bottom: 2px solid #334155; padding-bottom: 5px; margin-bottom: 20px; font-weight: bold;">
            <span>HONEYWELL EASy: TRIPLE ENGINE DISPLAY</span><span>ATA: 70/72</span>
        </div>
        
        <div style="display: flex; gap: 10px; background: #1a202c; padding: 15px; border-radius: 6px; border: 2px solid #2d3748; margin-bottom: 20px; justify-content: space-around; flex-wrap: wrap;">
            <div style="text-align:center;">
                <button onclick="controlAPU()" style="padding: 10px 14px; font-weight: bold; background: #334155; color: white; border: 1px solid #475569; border-radius: 4px; cursor: pointer;">APU MASTER</button>
                <div id="apu_lbl" style="margin-top: 5px; font-size:0.75rem; color:#4b5563; font-weight:bold;">OFF</div>
            </div>
            <div style="text-align:center;">
                <button onclick="controlBleed()" style="padding: 10px 14px; font-weight: bold; background: #334155; color: white; border: 1px solid #475569; border-radius: 4px; cursor: pointer;">APU BLEED VALVE</button>
                <div id="bleed_lbl" style="margin-top: 5px; font-size:0.75rem; color:#4b5563; font-weight:bold;">CLOSED</div>
            </div>
            <div style="text-align:center; border-left: 2px dashed #475569; padding-left: 15px;">
                <button onclick="startEng(0)" style="padding: 8px 12px; font-weight: bold; background: #1e293b; color: white; border: 1px solid #ef4444; border-radius: 4px; cursor: pointer;">ENG 1 START</button>
                <button onclick="toggleLever(0)" id="lv0" style="padding: 4px 8px; font-size:0.7rem; background: #7f1d1d; color: white; border: none; border-radius: 2px; cursor: pointer; margin-top:3px; display:block; width:100%;">SHUTOFF</button>
            </div>
            <div style="text-align:center;">
                <button onclick="startEng(1)" style="padding: 8px 12px; font-weight: bold; background: #1e293b; color: white; border: 1px solid #ef4444; border-radius: 4px; cursor: pointer;">ENG 2 START</button>
                <button onclick="toggleLever(1)" id="lv1" style="padding: 4px 8px; font-size:0.7rem; background: #7f1d1d; color: white; border: none; border-radius: 2px; cursor: pointer; margin-top:3px; display:block; width:100%;">SHUTOFF</button>
            </div>
            <div style="text-align:center;">
                <button onclick="startEng(2)" style="padding: 8px 12px; font-weight: bold; background: #1e293b; color: white; border: 1px solid #ef4444; border-radius: 4px; cursor: pointer;">ENG 3 START</button>
                <button onclick="toggleLever(2)" id="lv2" style="padding: 4px 8px; font-size:0.7rem; background: #7f1d1d; color: white; border: none; border-radius: 2px; cursor: pointer; margin-top:3px; display:block; width:100%;">SHUTOFF</button>
            </div>
        </div>

        <div style="display: flex; justify-content: space-between; align-items: center; gap: 20px;">
            <div style="flex: 1; text-align: center; background: #0b0f19; padding: 15px; border-radius: 6px; border: 1px solid #1e293b;">
                <div style="font-weight: bold; color: #38bdf8; margin-bottom: 10px;">ENGINE 1 (LH)</div>
                <canvas id="c_n1_0" width="110" height="110"></canvas><div id="t_n1_0" style="font-size:0.9rem; font-weight:bold; color:#22c55e;">0.0%</div>
                <canvas id="c_n2_0" width="110" height="110"></canvas><div id="t_n2_0" style="font-size:0.9rem; font-weight:bold; color:#22c55e;">0.0%</div>
                <canvas id="c_itt_0" width="110" height="110"></canvas><div id="t_itt_0" style="font-size:0.9rem; font-weight:bold; color:#f59e0b;">15°C</div>
            </div>
            <div style="flex: 1; text-align: center; background: #0b0f19; padding: 15px; border-radius: 6px; border: 1px solid #1e293b;">
                <div style="font-weight: bold; color: #38bdf8; margin-bottom: 10px;">ENGINE 2 (CTR)</div>
                <canvas id="c_n1_1" width="110" height="110"></canvas><div id="t_n1_1" style="font-size:0.9rem; font-weight:bold; color:#22c55e;">0.0%</div>
                <canvas id="c_n2_1" width="110" height="110"></canvas><div id="t_n2_1" style="font-size:0.9rem; font-weight:bold; color:#22c55e;">0.0%</div>
                <canvas id="c_itt_1" width="110" height="110"></canvas><div id="t_itt_1" style="font-size:0.9rem; font-weight:bold; color:#f59e0b;">15°C</div>
            </div>
            <div style="flex: 1; text-align: center; background: #0b0f19; padding: 15px; border-radius: 6px; border: 1px solid #1e293b;">
                <div style="font-weight: bold; color: #38bdf8; margin-bottom: 10px;">ENGINE 3 (RH)</div>
                <canvas id="c_n1_2" width="110" height="110"></canvas><div id="t_n1_2" style="font-size:0.9rem; font-weight:bold; color:#22c55e;">0.0%</div>
                <canvas id="c_n2_2" width="110" height="110"></canvas><div id="t_n2_2" style="font-size:0.9rem; font-weight:bold; color:#22c55e;">0.0%</div>
                <canvas id="c_itt_2" width="110" height="110"></canvas><div id="t_itt_2" style="font-size:0.9rem; font-weight:bold; color:#f59e0b;">15°C</div>
            </div>
        </div>

        <div style="border-top: 1px dashed #334155; margin-top: 20px; padding-top: 15px;">
            <div style="font-weight: bold; color: #fbbf24;">🔔 CREW ALERTING SYSTEM (CAS) DISPLAY FEED:</div>
            <div id="cas_box" style="color:#38bdf8; font-size:0.85rem; margin-top:5px;">🟢 SYSTEMS GENERAL RUN NOMINAL</div>
        </div>
    </div>

    <script>
        let apu = "OFF", bleed = false;
        let engines = [
            { phase: "STBY", lever: false, n1: 0, n2: 0, itt: 15 },
            { phase: "STBY", lever: false, n1: 0, n2: 0, itt: 15 },
            { phase: "STBY", lever: false, n1: 0, n2: 0, itt: 15 }
        ];

        function controlAPU() {
            apu = (apu === "OFF") ? "RUN" : "OFF";
            if(apu === "OFF") bleed = false;
            document.getElementById("apu_lbl").innerText = apu === "RUN" ? "🟢 RUN (100%)" : "OFF";
            document.getElementById("apu_lbl").style.color = apu === "RUN" ? "#4ade80" : "#4b5563";
            document.getElementById("bleed_lbl").innerText = bleed ? "🔶 OPEN" : "CLOSED";
        }

        function controlBleed() {
            if(apu !== "RUN") return;
            bleed = !bleed;
            document.getElementById("bleed_lbl").innerText = bleed ? "🔶 OPEN (PRES)" : "CLOSED";
            document.getElementById("bleed_lbl").style.color = bleed ? "#fbbf24" : "#4b5563";
        }

        function toggleLever(idx) {
            engines[idx].lever = !engines[idx].lever;
            let el = document.getElementById("lv" + idx);
            el.innerText = engines[idx].lever ? "RUN" : "SHUTOFF";
            el.style.background = engines[idx].lever ? "#22c55e" : "#7f1d1d";
            
            if(engines[idx].lever && engines[idx].phase === "CRANK" && engines[idx].n2 < 15.0) {
                engines[idx].phase = "FAIL";
                document.getElementById("cas_box").innerText = "🚨 ALERT CAS: HOT START IN ENGINE " + (idx+1) + "!\\n Inyección prematura de combustible con rotación N2 crítica.";
                document.getElementById("cas_box").style.color = "#ef4444";
                playAlarmSound();
            }
        }

        function startEng(idx) {
            if(!bleed) {
                document.getElementById("cas_box").innerText = "🚨 FALLO DE ARRANQUE: No hay presión neumática (APU BLEED CLOSED).";
                document.getElementById("cas_box").style.color = "#ef4444";
                return;
            }
            if(engines[idx].phase === "STBY") {
                engines[idx].phase = "CRANK";
            }
        }

        function playAlarmSound() {
            try {
                const ctx = new (window.AudioContext || window.webkitAudioContext)();
                const osc = ctx.createOscillator(); const gain = ctx.createGain();
                osc.type = 'sawtooth'; osc.frequency.value = 450; gain.gain.value = 0.2;
                osc.connect(gain); gain.connect(ctx.destination); osc.start();
                setTimeout(() => osc.stop(), 1000);
            } catch(e){}
        }

        function drawGauge(id, val, maxVal, isItt) {
            let canvas = document.getElementById(id); if(!canvas) return;
            let ctx = canvas.getContext("2d"); ctx.clearRect(0,0,110,110);
            let cx = 55, cy = 55, r = 45;
            ctx.beginPath(); ctx.arc(cx,cy,r,0,2*Math.PI); ctx.strokeStyle="#2d3748"; ctx.lineWidth=3; ctx.stroke();
            let pct = val / maxVal; if(pct>1) pct=1;
            let angle = 0.75*Math.PI + pct*(1.5*Math.PI);
            ctx.beginPath(); ctx.moveTo(cx,cy); ctx.lineTo(cx+ (r-10)*Math.cos(angle), cy+ (r-10)*Math.sin(angle));
            ctx.strokeStyle = isItt ? "#f59e0b" : "#4ade80"; ctx.lineWidth=3; ctx.stroke();
        }

        setInterval(() => {
            for(let i=0; i<3; i++) {
                let e = engines[i];
                if(e.phase === "CRANK") {
                    e.n2 += 0.5; if(e.n2 >= 18.0 && e.lever) e.phase = "IGN";
                    if(e.n2 >= 25.0 && !e.lever) e.n2 = 25.0;
                } else if(e.phase === "IGN") {
                    e.n2 += 0.6; e.itt += 9; if(e.itt >= 520) e.phase = "RUN";
                } else if(e.phase === "RUN") {
                    if(e.n2 < 57.4) e.n2 += 0.4; else e.n2 = 57.4;
                    if(e.n1 < 24.2) e.n1 += 0.3; else e.n1 = 24.2;
                    if(e.itt > 490) e.itt -= 2; else e.itt = 490;
                }
                document.getElementById("t_n1_" + i).innerText = e.n1.toFixed(1) + "%";
                document.getElementById("t_n2_" + i).innerText = e.n2.toFixed(1) + "%";
                document.getElementById("t_itt_" + i).innerText = Math.round(e.itt) + "°C";
                drawGauge("c_n1_" + i, e.n1, 100, false);
                drawGauge("c_n2_" + i, e.n2, 100, false);
                drawGauge("c_itt_" + i, e.itt, 800, true);
            }
        }, 40);
    </script>
    """
    components.html(html_triple_clocks, height=650)

# ------------------------------------------------------------------------------
# PANTALLA 2: PROCEDIMIENTOS DE MANTENIMIENTO (RESTAURADO CON BOTÓN RESET)
# ------------------------------------------------------------------------------
else:
    st.title("🔧 Pantalla de Procedimientos de Mantenimiento (Técnicos)")
    st.markdown("---")
    
    if modulo_activo == "MÓDULO I: DISTRIBUCIÓN ELÉCTRICA (ATA 24)":
        st.subheader("Módulo I: Distribución Eléctrica y Secuenciación Avanzada de Barras")
        procedimiento = st.radio("⚙️ SELECCIONE PROCEDIMIENTO DE EVALUACIÓN:", ["ENERGIZACIÓN COMPLETA (COLD OPERATIONS)", "DESENERGIZACIÓN COMPLETA (SHUTDOWN)"], horizontal=True)
        
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
                        else: st.session_state.falla_procedimiento = True; st.session_state.descripcion_falla = "LH MSTR fuera de secuencia."; st.session_state.audio_alarma = "alarma_critica"
                    st.rerun()
                st.markdown("<div class='anunciador-verde'>ON</div>" if st.session_state.fase_e >= 12 else "<div class='anunciador-amber'>OFF</div>", unsafe_allow_html=True)
            with grid_sup[2]:
                if st.button("LH INIT", key="lh_m"):
                    if procedimiento == "ENERGIZACIÓN COMPLETA (COLD OPERATIONS)" and st.session_state.fase_e == 7: st.session_state.fase_e = 8
                    st.rerun()
                st.markdown("<div class='anunciador-apagado'>RUN</div>" if st.session_state.fase_e >= 8 else "<div class='anunciador-amber'>OFF</div>", unsafe_allow_html=True)
            with grid_sup[3]:
                if st.button("BUS TIE", key="bt_m"):
                    if procedimiento == "ENERGIZACIÓN COMPLETA (COLD OPERATIONS)" and st.session_state.fase_e == 6: st.session_state.fase_e = 7
                    st.rerun()
                st.markdown("<div class='anunciador-amber'>TIED</div>" if st.session_state.fase_e >= 7 else "<div class='anunciador-apagado'>AUTO</div>", unsafe_allow_html=True)
            with grid_sup[4]:
                if st.button("RH INIT", key="rh_m"):
                    if procedimiento == "ENERGIZACIÓN COMPLETA (COLD OPERATIONS)" and st.session_state.fase_e == 7: st.session_state.fase_e = 8
                    st.rerun()
                st.markdown("<div class='anunciador-apagado'>RUN</div>" if st.session_state.fase_e >= 8 else "<div class='anunciador-amber'>OFF</div>", unsafe_allow_html=True)
            with grid_sup[5]:
                if st.button("RH MSTR", key="rhm_m"):
                    if procedimiento == "ENERGIZACIÓN COMPLETA (COLD OPERATIONS)" and st.session_state.fase_e == 11: st.session_state.fase_e = 12
                    st.rerun()
                st.markdown("<div class='anunciador-verde'>ON</div>" if st.session_state.fase_e >= 12 else "<div class='anunciador-amber'>OFF</div>", unsafe_allow_html=True)
            with grid_sup[6]:
                if st.button("CABIN MSTR", key="cb_m"):
                    if procedimiento == "ENERGIZACIÓN COMPLETA (COLD OPERATIONS)" and st.session_state.fase_e == 9: st.session_state.fase_e = 10
                    st.rerun()
                st.markdown("<div class='anunciador-amber'>OFF</div>" if st.session_state.fase_e >= 10 else "<div class='anunciador-verde'>ON</div>", unsafe_allow_html=True)
            with grid_sup[7]:
                if st.button("EXT PWR", key="ep_m"):
                    if procedimiento == "ENERGIZACIÓN COMPLETA (COLD OPERATIONS)" and st.session_state.fase_e == 8: st.session_state.fase_e = 9
                    st.rerun()
                st.markdown("<div class='anunciador-verde'>ONLINE</div>" if st.session_state.fase_e >= 9 else "<div class='anunciador-apagado'>OFF</div>", unsafe_allow_html=True)
            st.markdown("</div>", unsafe_allow_html=True)

            st.markdown("<div class='linea-tactica'></div>", unsafe_allow_html=True)
            
            # FILA INFERIOR COMPLETA RESTAURADA
            st.markdown("<div class='subpanel-3d'><div class='titulo-serigrafia'>🔋 GENERATION & BATTERIES</div>", unsafe_allow_html=True)
            grid_inf = st.columns(8)
            with grid_inf[0]: st.button("GEN 1", disabled=True, key="g1"); st.markdown("<div class='anunciador-apagado'>OFF</div>", unsafe_allow_html=True)
            with grid_inf[1]:
                if st.button("LH ISOL", key="lhi"):
                    if procedimiento == "ENERGIZACIÓN COMPLETA (COLD OPERATIONS)" and st.session_state.fase_e == 10: st.session_state.fase_e = 11
                    st.rerun()
                st.markdown("<div class='anunciador-apagado'>TIED</div>" if st.session_state.fase_e >= 11 else "<div class='anunciador-amber'>ISOL</div>", unsafe_allow_html=True)
            with grid_inf[2]:
                if st.button("BAT 1", key="b1"):
                    if procedimiento == "ENERGIZACIÓN COMPLETA (COLD OPERATIONS)" and st.session_state.fase_e == 4: st.session_state.fase_e = 5
                    st.rerun()
                st.markdown("<div class='anunciador-verde'>AUTO</div>" if st.session_state.fase_e >= 5 else "<div class='anunciador-apagado'>OFF</div>", unsafe_allow_html=True)
            with grid_inf[3]:
                if st.button("BAT 2", key="b2"):
                    if procedimiento == "ENERGIZACIÓN COMPLETA (COLD OPERATIONS)" and st.session_state.fase_e == 4: st.session_state.fase_e = 5
                    st.rerun()
                st.markdown("<div class='anunciador-verde'>AUTO</div>" if st.session_state.fase_e >= 5 else "<div class='anunciador-apagado'>OFF</div>", unsafe_allow_html=True)
            with grid_inf[4]: st.button("RAT RSET", disabled=True, key="rat"); st.markdown("<div class='anunciador-apagado'>OFF</div>", unsafe_allow_html=True)
            with grid_inf[5]:
                if st.button("RH ISOL", key="rhi"):
                    if procedimiento == "ENERGIZACIÓN COMPLETA (COLD OPERATIONS)" and st.session_state.fase_e == 10: st.session_state.fase_e = 11
                    st.rerun()
                st.markdown("<div class='anunciador-apagado'>TIED</div>" if st.session_state.fase_e >= 11 else "<div class='anunciador-amber'>ISOL</div>", unsafe_allow_html=True)
            with grid_inf[6]: st.button("GEN 2", disabled=True); st.markdown("<div class='anunciador-apagado'>OFF</div>", unsafe_allow_html=True)
            with grid_inf[7]: st.button("GEN 3", disabled=True); st.markdown("<div class='anunciador-apagado'>OFF</div>", unsafe_allow_html=True)
            st.markdown("</div>", unsafe_allow_html=True)
            
            st.markdown("<div class='linea-tactica'></div>", unsafe_allow_html=True)
            
            # RECEPTÁCULOS DE TIERRA
            st.markdown("<div class='subpanel-3d'><div class='titulo-serigrafia'>🔧 CONFIGURACIÓN Y ACOPLE DE PLANTA EXTERNA</div>", unsafe_allow_html=True)
            grid_rampa = st.columns(5)
            with grid_rampa[0]:
                if st.button("🔌 RECEPTÁCULO GPU", key="rec"):
                    if procedimiento == "ENERGIZACIÓN COMPLETA (COLD OPERATIONS)" and st.session_state.fase_e == 0: st.session_state.fase_e = 1
                    st.rerun()
                st.markdown("<div class='anunciador-verde'>CONECTADO</div>" if st.session_state.fase_e >= 1 else "<div class='anunciador-apagado'>DESCONECTADO</div>", unsafe_allow_html=True)
            with grid_rampa[1]:
                if st.button("⚡ REGULADOR TENSIÓN TIERRA", key="pot"):
                    if procedimiento == "ENERGIZACIÓN COMPLETA (COLD OPERATIONS)" and st.session_state.fase_e == 1: st.session_state.fase_e = 2
                    st.rerun()
                st.markdown("<div class='anunciador-verde'>28.0 VDC OK</div>" if st.session_state.fase_e >= 2 else "<div class='anunciador-apagado'>0.0 VDC</div>", unsafe_allow_html=True)
            with grid_rampa[2]:
                if st.button("🎛️ SWITCH EXTERNO GPU", key="sw"):
                    if procedimiento == "ENERGIZACIÓN COMPLETA (COLD OPERATIONS)" and st.session_state.fase_e == 2: st.session_state.fase_e = 3
                    st.rerun()
                st.markdown("<div class='anunciador-verde'>LÍNEA ONLINE</div>" if st.session_state.fase_e >= 3 else "<div class='anunciador-apagado'>LÍNEA OFF</div>", unsafe_allow_html=True)
            with grid_rampa[3]:
                if st.button("⚙️ CONTROL FRENO PARQUEO", key="fr"):
                    if procedimiento == "ENERGIZACIÓN COMPLETA (COLD OPERATIONS)" and st.session_state.fase_e == 3: st.session_state.fase_e = 4
                    st.rerun()
                st.markdown("<div class='anunciador-verde'>ENGANCHADO</div>" if st.session_state.fase_e >= 4 else "<div class='anunciador-apagado'>LIBERADO</div>", unsafe_allow_html=True)
            with grid_rampa[4]:
                st.button("🚪 COMPUERTA EXTERIOR", disabled=True)
                st.markdown("<div class='anunciador-verde'>COMPUERTA ABIERTA</div>", unsafe_allow_html=True)
            st.markdown("</div>", unsafe_allow_html=True)
            
            st.markdown("<br>", unsafe_allow_html=True)
            # BOTÓN DE REINICIO MAESTRO RESTAURADO
            if st.button("🚨 CORREGIR / REINICIAR EVALUACIÓN", key="btn_reset_maint"):
                st.session_state.fase_e = 0
                st.session_state.fase_d = 0
                st.session_state.falla_procedimiento = False
                st.session_state.descripcion_falla = ""
                st.rerun()
            st.markdown("</div>", unsafe_allow_html=True)

        with col_telemetria_pdu:
            st.markdown("### 📺 Honeywell EASy Avionics Display")
            st.markdown(f"<div class='pantalla-mfd'>📲 MODO EVALUACIÓN ACTIVO<br><br>Fase Eléctrica Actual: Paso {st.session_state.fase_e}/12</div>", unsafe_allow_html=True)

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
