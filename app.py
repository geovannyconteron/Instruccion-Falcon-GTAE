import streamlit as st
import streamlit.components.v1 as components

# Configuración de la cabina táctica
st.set_page_config(page_title="Falcon 7X Flight Deck - GTAE", page_icon="✈️", layout="wide")

# ==============================================================================
# SCRIPT DE AUDIO INSTANTÁNEO Y ENTORNO GLOBAL
# ==============================================================================
# Este componente inyecta un sintetizador de audio directamente en la ventana principal
# para que cada botón reaccione acústicamente en tiempo real al tacto del operador.
components.html("""
    <script>
    const parentDoc = window.parent.document;
    
    // Configuración del sintetizador para clics de interruptores reales
    function playCockpitClick() {
        try {
            const AudioContext = window.AudioContext || window.webkitAudioContext;
            const ctx = new AudioContext();
            
            // Oscilador principal para el impacto mecánico
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
        } catch(e) { console.log("Audio demorado o bloqueado por el navegador"); }
    }

    // Escucha global de interacciones en los botones de Streamlit
    parentDoc.addEventListener('click', function(e) {
        const target = e.target;
        if (target && (target.tagName === 'BUTTON' || target.closest('button'))) {
            playCockpitClick();
        }
    }, true);
    </script>
""", height=0, width=0)

# ==============================================================================
# DISEÑO TRIDIMENSIONAL SKEUOMÓRFICO (CABINA REALISTA)
# ==============================================================================
st.markdown("""
    <style>
    /* Fondo general que simula la oscuridad de la cabina por la noche */
    .main { 
        background-color: #0b0f19; 
        color: #e2e8f0;
        font-family: 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
    }
    
    /* Contenedor principal que emula la estructura física del Overhead Panel */
    .overhead-frame {
        background: linear-gradient(145deg, #1e2530, #131822);
        border: 6px solid #2d3748;
        border-radius: 12px;
        padding: 25px;
        box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.8), inset 0 2px 4px rgba(255,255,255,0.1);
        margin-bottom: 25px;
        position: relative;
    }
    
    /* Bloques metálicos individuales para cada subpanel (Efecto 3D empotrado) */
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
    
    /* Líneas de demarcación táctica que separan los sistemas en el panel real */
    .linea-tactica {
        border-top: 2px solid #4a5568;
        border-bottom: 1px solid #1a202c;
        margin: 15px 0;
    }
    
    /* Títulos de sección estilo serigrafía militar */
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
    
    /* Botones transformados en interruptores de empuje mecánicos pesados */
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
    
    /* Efecto físico de pulsación profunda en el botón */
    .stButton>button:active {
        transform: translateY(3px);
        box-shadow: 0 2px 4px rgba(0,0,0,0.6);
        border-top: 2px solid #0f172a !important;
        border-bottom: 1px solid #475569 !important;
    }
    
    .stButton>button:hover {
        background: linear-gradient(180deg, #3d4e66, #243246) !important;
        color: #ffffff !important;
    }
    
    /* Luces de los anunciadores con tecnología de brillo dicroico (Glow) */
    .anunciador-verde { 
        background-color: #042f1a; 
        color: #4ade80; 
        border: 2px solid #22c55e; 
        font-weight: bold; 
        text-align: center; 
        border-radius: 4px; 
        font-size: 0.75rem; 
        padding: 5px; 
        font-family: monospace;
        box-shadow: 0 0 12px rgba(34, 197, 94, 0.6);
        text-shadow: 0 0 4px rgba(34, 197, 94, 0.8);
    }
    
    .anunciador-ambar { 
        background-color: #451a03; 
        color: #fbbf24; 
        border: 2px solid #f59e0b; 
        font-weight: bold; 
        text-align: center; 
        border-radius: 4px; 
        font-size: 0.75rem; 
        padding: 5px; 
        font-family: monospace;
        box-shadow: 0 0 12px rgba(245, 158, 11, 0.6);
        text-shadow: 0 0 4px rgba(245, 158, 11, 0.8);
    }
    
    .anunciador-apagado { 
        background-color: #181f2a; 
        color: #4b5563; 
        border: 2px solid #374151; 
        text-align: center; 
        border-radius: 4px; 
        font-size: 0.75rem; 
        padding: 5px; 
        font-family: monospace;
        box-shadow: inset 0 2px 4px rgba(0,0,0,0.5);
    }
    
    /* Pantallas de lectura digital de tubos de cátodo / LED */
    .display-digital-principal {
        background-color: #020203;
        border: 3px solid #475569;
        border-radius: 6px;
        color: #f87171;
        font-family: 'Courier New', Courier, monospace;
        font-size: 2.4rem;
        font-weight: bold;
        text-align: center;
        letter-spacing: 5px;
        padding: 12px;
        box-shadow: inset 0 0 20px rgba(239, 68, 68, 0.4), 0 4px 6px rgba(0,0,0,0.5);
    }
    
    .display-digital-secundario {
        background-color: #020203;
        border: 2px solid #475569;
        border-radius: 6px;
        color: #fbbf24;
        font-family: 'Courier New', Courier, monospace;
        font-size: 1.6rem;
        font-weight: bold;
        text-align: center;
        letter-spacing: 3px;
        padding: 8px;
        box-shadow: inset 0 0 12px rgba(245, 158, 11, 0.3);
    }
    
    .pantalla-mfd {
        font-family: 'Courier New', Courier, monospace; 
        border: 5px solid #334155; 
        background-color: #04070e; 
        color: #38bdf8; 
        padding: 22px; 
        border-radius: 8px; 
        min-height: 520px; 
        box-shadow: inset 0 0 30px rgba(0,0,0,0.9), 0 10px 30px rgba(0,0,0,0.7); 
        white-space: pre-wrap;
    }
    </style>
""", unsafe_allow_html=True)

# ==============================================================================
# ADVERTENCIAS PROCEDIMENTALES (ALARMAS TRAS RECARGA)
# ==============================================================================
if "audio_alarma" not in st.session_state:
    st.session_state.audio_alarma = None

if st.session_state.audio_alarma == "alarma_critica":
    components.html("""
        <script>
        try {
            const ctx = new (window.AudioContext || window.webkitAudioContext)();
            const osc = ctx.createOscillator();
            const gain = ctx.createGain();
            osc.type = 'sawtooth';
            osc.frequency.setValueAtTime(380, ctx.currentTime);
            gain.gain.setValueAtTime(0.3, ctx.currentTime);
            osc.connect(gain);
            gain.connect(ctx.destination);
            osc.start();
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
            const osc = ctx.createOscillator();
            osc.type = 'sine';
            osc.frequency.setValueAtTime(520, ctx.currentTime);
            osc.connect(ctx.destination);
            osc.start();
            setTimeout(() => { osc.stop(); }, 400);
        } catch(e){}
        </script>
    """, height=0, width=0)
    st.session_state.audio_alarma = None


# ==============================================================================
# INTERFAZ DE INGRESO DE SEGURIDAD
# ==============================================================================
if "autenticado" not in st.session_state:
    st.session_state.autenticado = False

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
        
        st.image("https://images.unsplash.com/photo-1540962351504-03099e0a754b?q=80&w=1200&auto=format&fit=crop", 
                 caption="Grupo de Transporte Aéreo Especial - FAE", use_container_width=True)
        
        with st.form("credenciales_cabina"):
            st.markdown("<h5 style='text-align: center; color: #94a3b8;'>🔒 CONTROL DE SOBERANÍA Y ACCESO</h5>", unsafe_allow_html=True)
            txt_user = st.text_input("Identificador Técnico:", placeholder="gtae_operator")
            txt_pass = st.text_input("Clave de Bloqueo:", type="password", placeholder="••••••••")
            btn_acceso = st.form_submit_button("CONECTAR SISTEMAS EMBARCADOS")
            
            if btn_acceso:
                if txt_user == "gtae" and txt_pass == "7X2026":
                    st.session_state.autenticado = True
                    st.rerun()
                else:
                    st.error("Credenciales incorrectas. Origen de datos no autorizado.")
    st.stop()


# ==============================================================================
# PANEL DE CONTROL OPERATIVO (SIDEBAR DE CONTROL)
# ==============================================================================
with st.sidebar:
    st.markdown("<h4 style='color: #38bdf8; font-family: monospace;'>✈️ AVIONICS SIDEBAR</h4>", unsafe_allow_html=True)
    st.markdown("**Destacamento:** Grupo de Transporte Aéreo Especial")
    if st.button("🔒 DESCONECTAR CABINA"):
        st.session_state.autenticado = False
        st.rerun()
    st.markdown("---")
    
    opcion_sistema = st.radio(
        "CONSOLA INTERACTIVA:",
        ["MÓDULO I: ENERGIZACIÓN (ATA 24)", "MÓDULO II: COMBUSTIBLE (ATA 28)"]
    )

# Inicialización de memorias operacionales de rampa
if "combustible_actual" not in st.session_state: st.session_state.combustible_actual = 1150
if "combustible_objetivo" not in st.session_state: st.session_state.combustible_objetivo = 10500
if "valvula_izq" not in st.session_state: st.session_state.valvula_izq = "OFF"
if "valvula_ctr" not in st.session_state: st.session_state.valvula_ctr = "OFF"
if "valvula_der" not in st.session_state: st.session_state.valvula_der = "OFF"
if "bombeo_activo" not in st.session_state: st.session_state.bombeo_activo = False

# Simulación cíclica del paso de combustible bajo presión
if st.session_state.bombeo_activo and st.session_state.combustible_actual < st.session_state.combustible_objetivo:
    st.session_state.combustible_actual += 400
    if st.session_state.combustible_actual >= st.session_state.combustible_objetivo:
        st.session_state.combustible_actual = st.session_state.combustible_objetivo
        st.session_state.bombeo_activo = False
        st.session_state.audio_alarma = "carga_completa"
    st.rerun()


# ------------------------------------------------------------------------------
# DESARROLLO VISUAL MÓDULO I: OVERHEAD ELECTRICAL PANEL (ATA 24)
# ------------------------------------------------------------------------------
if opcion_sistema == "MÓDULO I: ENERGIZACIÓN (ATA 24)":
    st.markdown("<h2 style='text-align: center; color: #f1f5f9; font-family: monospace;'>OVERHEAD COCKPIT PANEL</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #94a3b8;'>Simulación Estructural Tridimensional de la Planta de Distribución Eléctrica</p>", unsafe_allow_html=True)
    
    procedimiento = st.radio(
        "⚙️ SELECCIONE PROCEDIMIENTO DE EVALUACIÓN:",
        ["ENERGIZACIÓN COMPLETA (COLD OPERATIONS)", "DESENERGIZACIÓN COMPLETA (SHUTDOWN)"],
        horizontal=True
    )

    if "fase_e" not in st.session_state: st.session_state.fase_e = 0
    if "fase_d" not in st.session_state: st.session_state.fase_d = 0
    if "falla_procedimiento" not in st.session_state: st.session_state.falla_procedimiento = False
    if "descripcion_falla" not in st.session_state: st.session_state.descripcion_falla = ""

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
        st.session_state.descripcion_falla = texto
        st.session_state.audio_alarma = "alarma_critica"

    col_fisica_panel, col_telemetria_pdu = st.columns([1.3, 1])

    with col_fisica_panel:
        # Envoltura del bastidor del Overhead Panel
        st.markdown("<div class='overhead-frame'>", unsafe_allow_html=True)
        
        # SUBPANEL SUP: DC SUPPLY CONTROL
        st.markdown("<div class='subpanel-3d'><div class='titulo-serigrafia'>⚡ DC SUPPLY PANEL ⚡</div>", unsafe_allow_html=True)
        grid_sup = st.columns(8)
        
        with grid_sup[0]:
            st.button("GALLEY MSTR", disabled=True, key="btn_galley")
            st.markdown("<div class='anunciador-apagado'>OFF</div>", unsafe_allow_html=True)
            
        with grid_sup[1]:
            if st.button("LH MSTR", key="btn_lhmstr"):
                if procedimiento == "ENERGIZACIÓN COMPLETA (COLD OPERATIONS)":
                    if st.session_state.fase_e == 11: st.session_state.fase_e = 12
                    else: forzar_alarma("LH MASTER activado de forma prematura fuera de la secuencia técnica.")
                else: forzar_alarma("LH MASTER se mantiene enclavado de manera automática en esta fase.")
                st.rerun()
            luz = "<div class='anunciador-verde'>ON</div>" if (procedimiento == "ENERGIZACIÓN COMPLETA (COLD OPERATIONS)" and st.session_state.fase_e >= 12) or procedimiento == "DESENERGIZACIÓN COMPLETA (SHUTDOWN)" else "<div class='anunciador-ambar'>OFF</div>"
            st.markdown(luz, unsafe_allow_html=True)
            
        with grid_sup[2]:
            if st.button("LH INIT", key="btn_lhinit"):
                if procedimiento == "ENERGIZACIÓN COMPLETA (COLD OPERATIONS)":
                    if st.session_state.fase_e == 7: st.session_state.fase_e = 8
                    else: forzar_alarma("LH INIT accionado sin acoplamiento estructural del BUS TIE.")
                else: forzar_alarma("LH INIT protegido por solenoide de retención durante el corte.")
                st.rerun()
            luz = "<div class='anunciador-apagado'>RUN</div>" if (procedimiento == "ENERGIZACIÓN COMPLETA (COLD OPERATIONS)" and st.session_state.fase_e >= 8) or procedimiento == "DESENERGIZACIÓN COMPLETA (SHUTDOWN)" else "<div class='anunciador-ambar'>OFF</div>"
            st.markdown(luz, unsafe_allow_html=True)
            
        with grid_sup[3]:
            if st.button("BUS TIE", key="btn_bustie"):
                if procedimiento == "ENERGIZACIÓN COMPLETA (COLD OPERATIONS)":
                    if st.session_state.fase_e == 6: st.session_state.fase_e = 7
                    else: forzar_alarma("BUS TIE accionado previo al armado de seguridad de la RAT.")
                else: forzar_alarma("Corte directo inhabilitado; el contactor se rige por la lógica del switch maestro.")
                st.rerun()
            luz = "<div class='anunciador-ambar'>TIED</div>" if (procedimiento == "ENERGIZACIÓN COMPLETA (COLD OPERATIONS)" and st.session_state.fase_e >= 7) or procedimiento == "DESENERGIZACIÓN COMPLETA (SHUTDOWN)" else "<div class='anunciador-apagado'>AUTO</div>"
            st.markdown(luz, unsafe_allow_html=True)
            
        with grid_sup[4]:
            if st.button("RH INIT", key="btn_rhinit"):
                if procedimiento == "ENERGIZACIÓN COMPLETA (COLD OPERATIONS)":
                    if st.session_state.fase_e == 7: st.session_state.fase_e = 8
                    else: forzar_alarma("RH INIT accionado sin acoplamiento estructural del BUS TIE.")
                else: forzar_alarma("RH INIT protegido por solenoide de retención durante el corte.")
                st.rerun()
            luz = "<div class='anunciador-apagado'>RUN</div>" if (procedimiento == "ENERGIZACIÓN COMPLETA (COLD OPERATIONS)" and st.session_state.fase_e >= 8) or procedimiento == "DESENERGIZACIÓN COMPLETA (SHUTDOWN)" else "<div class='anunciador-ambar'>OFF</div>"
            st.markdown(luz, unsafe_allow_html=True)
            
        with grid_sup[5]:
            if st.button("RH MSTR", key="btn_rhmstr"):
                if procedimiento == "ENERGIZACIÓN COMPLETA (COLD OPERATIONS)":
                    if st.session_state.fase_e == 11: st.session_state.fase_e = 12
                    else: forzar_alarma("RH MASTER activado de forma prematura fuera de la secuencia técnica.")
                else: forzar_alarma("RH MASTER se mantiene enclavado de manera automática en esta fase.")
                st.rerun()
            luz = "<div class='anunciador-verde'>ON</div>" if (procedimiento == "ENERGIZACIÓN COMPLETA (COLD OPERATIONS)" and st.session_state.fase_e >= 12) or procedimiento == "DESENERGIZACIÓN COMPLETA (SHUTDOWN)" else "<div class='anunciador-ambar'>OFF</div>"
            st.markdown(luz, unsafe_allow_html=True)
            
        with grid_sup[6]:
            if st.button("CABIN MSTR", key="btn_cabin"):
                if procedimiento == "ENERGIZACIÓN COMPLETA (COLD OPERATIONS)":
                    if st.session_state.fase_e == 9: st.session_state.fase_e = 10
                    else: forzar_alarma("CABIN MASTER accionado sin alimentación estable en barras de distribución.")
                else: forzar_alarma("El disyuntor comercial se drena al deponer la línea de alimentación principal.")
                st.rerun()
            luz = "<div class='anunciador-ambar'>OFF</div>" if (procedimiento == "ENERGIZACIÓN COMPLETA (COLD OPERATIONS)" and st.session_state.fase_e >= 10) or procedimiento == "DESENERGIZACIÓN COMPLETA (SHUTDOWN)" else "<div class='anunciador-verde'>ON</div>"
            st.markdown(luz, unsafe_allow_html=True)
            
        with grid_sup[7]:
            if st.button("EXT PWR", key="btn_extpwr"):
                if procedimiento == "ENERGIZACIÓN COMPLETA (COLD OPERATIONS)":
                    if st.session_state.fase_e == 8: st.session_state.fase_e = 9
                    else: forzar_alarma("EXT POWER conectado sin configurar los parámetros nominales de la planta externa.")
                else:
                    if st.session_state.fase_d == 0: st.session_state.fase_d = 1
                    else: forzar_alarma("EXT POWER debe ser deprimido en primera instancia para iniciar la desenergización.")
                st.rerun()
            luz = "<div class='anunciador-verde'>ONLINE</div>" if (procedimiento == "ENERGIZACIÓN COMPLETA (COLD OPERATIONS)" and st.session_state.fase_e >= 9) or (procedimiento == "DESENERGIZACIÓN COMPLETA (SHUTDOWN)" and st.session_state.fase_d < 1) else "<div class='anunciador-apagado'>OFF</div>"
            st.markdown(luz, unsafe_allow_html=True)

        st.markdown("</div>", unsafe_allow_html=True)
        st.markdown("<div class='linea-tactica'></div>", unsafe_allow_html=True)

        # SUBPANEL INF: BATERÍAS Y RED DE GENERACIÓN
        st.markdown("<div class='subpanel-3d'>", unsafe_allow_html=True)
        grid_inf = st.columns(8)
        
        with grid_inf[0]: st.button("GEN 1", disabled=True, key="b_g1"); st.markdown("<div class='anunciador-apagado'>OFF</div>", unsafe_allow_html=True)
        
        with grid_inf[1]:
            if st.button("LH ISOL", key="btn_lhisol"):
                if procedimiento == "ENERGIZACIÓN COMPLETA (COLD OPERATIONS)":
                    if st.session_state.fase_e == 10: st.session_state.fase_e = 11
                    else: forzar_alarma("Válvula de aislamiento de barras accionada antes del acoplamiento comercial de cabina.")
                else: forzar_alarma("El aislamiento ISOL se autoprotege por caída de tensión de excitación.")
                st.rerun()
            luz = "<div class='anunciador-apagado'>TIED</div>" if (procedimiento == "ENERGIZACIÓN COMPLETA (COLD OPERATIONS)" and st.session_state.fase_e >= 11) or procedimiento == "DESENERGIZACIÓN COMPLETA (SHUTDOWN)" else "<div class='anunciador-ambar'>ISOL</div>"
            st.markdown(luz, unsafe_allow_html=True)
            
        with grid_inf[2]:
            if st.button("BAT 1", key="btn_bat1"):
                if procedimiento == "ENERGIZACIÓN COMPLETA (COLD OPERATIONS)":
                    if st.session_state.fase_e == 4: st.session_state.fase_e = 5
                    else: forzar_alarma("BAT 1 activada sin comprobar el freno de estacionamiento hidráulico de rampa.")
                else:
                    if st.session_state.fase_d == 1: st.session_state.fase_d = 2
                    else: forzar_alarma("BAT 1 debe conmutarse a la posición OFF en estricta sincronía tras deponer el EXT POWER.")
                st.rerun()
            luz = "<div class='anunciador-verde'>AUTO</div>" if (procedimiento == "ENERGIZACIÓN COMPLETA (COLD OPERATIONS)" and st.session_state.fase_e >= 5) or (procedimiento == "DESENERGIZACIÓN COMPLETA (SHUTDOWN)" and st.session_state.fase_d < 2) else "<div class='anunciador-apagado'>OFF</div>"
            st.markdown(luz, unsafe_allow_html=True)
            
        with grid_inf[3]:
            if st.button("BAT 2", key="btn_bat2"):
                if procedimiento == "ENERGIZACIÓN COMPLETA (COLD OPERATIONS)":
                    if st.session_state.fase_e == 4: st.session_state.fase_e = 5
                    else: forzar_alarma("BAT 2 activada sin comprobar el freno de estacionamiento hidráulico de rampa.")
                else:
                    if st.session_state.fase_d == 1: st.session_state.fase_d = 2
                    else: forzar_alarma("BAT 2 debe conmutarse a la posición OFF en estricta sincronía tras deponer el EXT POWER.")
                st.rerun()
            luz = "<div class='anunciador-verde'>AUTO</div>" if (procedimiento == "ENERGIZACIÓN COMPLETA (COLD OPERATIONS)" and st.session_state.fase_e >= 5) or (procedimiento == "DESENERGIZACIÓN COMPLETA (SHUTDOWN)" and st.session_state.fase_d < 2) else "<div class='anunciador-apagado'>OFF</div>"
            st.markdown(luz, unsafe_allow_html=True)
            
        with grid_inf[4]: st.button("RAT RSET", disabled=True, key="b_rat"); st.markdown("<div class='anunciador-apagado'>OFF</div>", unsafe_allow_html=True)
        
        with grid_inf[5]:
            if st.button("RH ISOL", key="btn_rhisol"):
                if procedimiento == "ENERGIZACIÓN COMPLETA (COLD OPERATIONS)":
                    if st.session_state.fase_e == 10: st.session_state.fase_e = 11
                    else: forzar_alarma("Válvula de aislamiento de barras accionada antes del acoplamiento comercial de cabina.")
                else: forzar_alarma("El aislamiento ISOL se autoprotege por caída de tensión de excitación.")
                st.rerun()
            luz = "<div class='anunciador-apagado'>TIED</div>" if (procedimiento == "ENERGIZACIÓN COMPLETA (COLD OPERATIONS)" and st.session_state.fase_e >= 11) or procedimiento == "DESENERGIZACIÓN COMPLETA (SHUTDOWN)" else "<div class='anunciador-ambar'>ISOL</div>"
            st.markdown(luz, unsafe_allow_html=True)
            
        with grid_inf[6]: st.button("GEN 2", disabled=True, key="b_g2"); st.markdown("<div class='anunciador-apagado'>OFF</div>", unsafe_allow_html=True)
        with grid_inf[7]: st.button("GEN 3", disabled=True, key="b_g3"); st.markdown("<div class='anunciador-apagado'>OFF</div>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)
        
        st.markdown("<div class='linea-tactica'></div>", unsafe_allow_html=True)

        # SUBPANEL DE RAMPA EXTERNA (ACOPLE DE GPU)
        st.markdown("<div class='subpanel-3d'><div class='titulo-serigrafia'>🔌 EXTERNAL GROUND POWER UNIT CONFIGURATION</div>", unsafe_allow_html=True)
        grid_rampa = st.columns(5)
        
        with grid_rampa[0]:
            if st.button("🔌 RECEPTÁCULO GPU", key="acople_gpu"):
                if procedimiento == "ENERGIZACIÓN COMPLETA (COLD OPERATIONS)":
                    if st.session_state.fase_e == 0: st.session_state.fase_e = 1
                    else: forzar_alarma("Línea física acoplada fuera del orden de prevuelo.")
                else:
                    if st.session_state.fase_d == 5: st.session_state.fase_d = 6
                    else: forzar_alarma("Desconexión física del mazo de cables sin deponer la planta eléctrica de rampa.")
                st.rerun()
            luz = "<div class='anunciador-verde'>CONECTADO</div>" if (procedimiento == "ENERGIZACIÓN COMPLETA (COLD OPERATIONS)" and st.session_state.fase_e >= 1) or (procedimiento == "DESENERGIZACIÓN COMPLETA (SHUTDOWN)" and st.session_state.fase_d < 6) else "<div class='anunciador-apagado'>DESCONECTADO</div>"
            st.markdown(luz, unsafe_allow_html=True)
            
        with grid_rampa[1]:
            if st.button("⚡ POTENCIÓMETRO", key="pot_volt"):
                if procedimiento == "ENERGIZACIÓN COMPLETA (COLD OPERATIONS)":
                    if st.session_state.fase_e == 1: st.session_state.fase_e = 2
                    else: forzar_alarma("Regulación de voltaje modificada sin alimentación base de rampa.")
                else: forzar_alarma("El reóstato de control de tensión externa permanece bloqueado durante el apagado.")
                st.rerun()
            luz = "<div class='anunciador-verde'>28.0 VDC OK</div>" if (procedimiento == "ENERGIZACIÓN COMPLETA (COLD OPERATIONS)" and st.session_state.fase_e >= 2) or (procedimiento == "DESENERGIZACIÓN COMPLETA (SHUTDOWN)" and st.session_state.fase_d < 6) else "<div class='anunciador-apagado'>0.0 VDC</div>"
            st.markdown(luz, unsafe_allow_html=True)
            
        with grid_rampa[2]:
            if st.button("🎛️ BREAK SW GPU", key="breaker_gpu"):
                if procedimiento == "ENERGIZACIÓN COMPLETA (COLD OPERATIONS)":
                    if st.session_state.fase_e == 2: st.session_state.fase_e = 3
                    else: forzar_alarma("Breaker de protección cerrado sin estabilización de voltaje nominal.")
                else:
                    if st.session_state.fase_d == 3: st.session_state.fase_d = 4
                    else: forzar_alarma("El interruptor de protección de línea debe desactivarse tras inhibir la protección de la RAT.")
                st.rerun()
            luz = "<div class='anunciador-verde'>LÍNEA ONLINE</div>" if (procedimiento == "ENERGIZACIÓN COMPLETA (COLD OPERATIONS)" and st.session_state.fase_e >= 3) or (procedimiento == "DESENERGIZACIÓN COMPLETA (SHUTDOWN)" and st.session_state.fase_d < 4) else "<div class='anunciador-apagado'>LÍNEA OFF</div>"
            st.markdown(luz, unsafe_allow_html=True)
            
        with grid_rampa[3]:
            if st.button("⚙️ FRENO PARQUEO", key="freno_p"):
                if procedimiento == "ENERGIZACIÓN COMPLETA (COLD OPERATIONS)":
                    if st.session_state.fase_e == 3: st.session_state.fase_e = 4
                    else: forzar_alarma("Freno de estacionamiento ignorado; riesgo de desplazamiento estructural en rampa.")
                else: forzar_alarma("El freno de estacionamiento permanece bloqueado por seguridad operativa.")
                st.rerun()
            luz = "<div class='anunciador-verde'>ENGANCHADO</div>" if (procedimiento == "ENERGIZACIÓN COMPLETA (COLD OPERATIONS)" and st.session_state.fase_e >= 4) or procedimiento == "DESENERGIZACIÓN COMPLETA (SHUTDOWN)" else "<div class='anunciador-apagado'>LIBERADO</div>"
            st.markdown(luz, unsafe_allow_html=True)
            
        with grid_rampa[4]:
            if st.button("🚪 COMPUERTA RECEPT", key="compuerta_ext"):
                if procedimiento == "DESENERGIZACIÓN COMPLETA (SHUTDOWN)":
                    if st.session_state.fase_d == 6: st.session_state.fase_d = 7
                    else: forzar_alarma("Intento de cierre de compuerta estructural con el cable de rampa acoplado.")
                else: forzar_alarma("La compuerta exterior debe mantenerse abierta durante el suministro continuo.")
                st.rerun()
            luz_c = "<div class='anunciador-apagado'>CERRADA</div>" if procedimiento == "DESENERGIZACIÓN COMPLETA (SHUTDOWN)" and st.session_state.fase_d >= 7 else "<div class='anunciador-verde'>ABIERTA</div>"
            st.markdown(luz_c, unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("🚨 RESTABLECER PARÁMETROS DEL OVERHEAD", key="btn_master_reset"):
            st.session_state.fase_e = 0
            st.session_state.fase_d = 0
            st.session_state.falla_procedimiento = False
            st.session_state.descripcion_falla = ""
            st.rerun()
        st.markdown("</div>", unsafe_allow_html=True)
        
        st.markdown("</div>", unsafe_allow_html=True) # Cierre overhead-frame

    with col_telemetria_pdu:
        st.markdown("### 📺 Honeywell EASy Avionics Display")
        st.markdown("<div class='subpanel-3d'>", unsafe_allow_html=True)
        st.markdown("<div style='color: #f87171; font-weight: bold; font-size: 0.8rem; margin-bottom: 10px; text-align: center; font-family: monospace;'>INDEPENDENT MECHANICAL BOX (RAT CONTROL)</div>", unsafe_allow_html=True)
        
        if st.button("🔘 RAT AUTO SELECTOR", key="btn_rat_auto"):
            if procedimiento == "ENERGIZACIÓN COMPLETA (COLD OPERATIONS)":
                if st.session_state.fase_e == 5: st.session_state.fase_e = 6
                else: forzar_alarma("RAT AUTO accionada fuera de la secuencia estipulada en la Orden Técnica.")
            else:
                if st.session_state.fase_d == 2: st.session_state.fase_d = 3
                else: forzar_alarma("La salvaguarda RAT AUTO debe ser normalizada inmediatamente tras cortar las baterías.")
            st.rerun()
        luz_rat_box = "<div class='anunciador-amber'>INHIBIT</div>" if (procedimiento == "ENERGIZACIÓN COMPLETA (COLD OPERATIONS)" and st.session_state.fase_e >= 6) or (procedimiento == "DESENERGIZACIÓN COMPLETA (SHUTDOWN)" and st.session_state.fase_d < 3) else "<div class='anunciador-apagado'>OFF (NORMAL POSITION)</div>"
        st.markdown(luz_rat_box, unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

        st.markdown("<div class='subpanel-3d' style='background-color: #111827;'>", unsafe_allow_html=True)
        st.markdown("<div style='color: #38bdf8; font-weight: bold; font-size: 0.8rem; margin-bottom: 10px; text-align: center; font-family: monospace;'>⚙️ EXTERNAL RAMPMAN CONTROL INTERFACE</div>", unsafe_allow_html=True)
        
        if st.button("🛑 CORTE DE MOTOR GPU DE RAMPA", key="btn_stop_gpu"):
            if procedimiento == "DESENERGIZACIÓN COMPLETA (SHUTDOWN)":
                if st.session_state.fase_d == 4: st.session_state.fase_d = 5
                else: forzar_alarma("Corte de combustión del motor ejecutado sin desconectar el switch de protección de línea.")
            else: forzar_alarma("Comando inválido. El motor de rampa debe suministrar energía continua durante el prevuelo.")
            st.rerun()
        luz_motor = "<div class='anunciador-apagado'>MOTOR APAGADO</div>" if (procedimiento == "DESENERGIZACIÓN COMPLETA (SHUTDOWN)" and st.session_state.fase_d >= 5) or (procedimiento == "ENERGIZACIÓN COMPLETA (COLD OPERATIONS)" and st.session_state.fase_e == 0) else "<div class='anunciador-verde'>MOTOR RUNNING (GENERANDO)</div>"
        st.markdown(luz_motor, unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

        # Procesamiento de estados para la pantalla MFD
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
            borde_crt = "#ef4444"
            fondo_crt = "#200d0d"
            texto_crt = "#fca5a5"
            status_easydisplay = f"🚨 CAS ALERT: ERROR PROCEDIMENTAL DETECTADO\n\n  REPORTE CRÍTICO: {st.session_state.descripcion_falla}\n\n  [SECUENCIA QUEBRADA]: Violación de la directiva Dassault.\n  Utilice el control de restablecimiento para purgar las líneas."
        elif finalizado:
            borde_crt = "#22c55e"
            fondo_crt = "#06130b"
            texto_crt = "#4ade80"
            status_easydisplay = "⚡ SYSTEMS STATUS: ENTORNO INTEGRADO CORRECTAMENTE\n\n  Fase concluida satisfactoriamente.\n  Los parámetros de distribución cumplen con las especificaciones técnicas\n  del Grupo de Transporte Aéreo Especial."
        else:
            borde_crt = "#475569"
            fondo_crt = "#030712"
            texto_crt = "#38bdf8"
            status_easydisplay = "📲 MONITOR DE EVALUACIÓN TÁCTICA ACTIVO\n\n  Sistemas de telemetría a la espera de conmutación física en el overhead.\n  Proceda guiándose firmemente por la secuencia establecida."

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


# ------------------------------------------------------------------------------
# DESARROLLO VISUAL MÓDULO II: PRESSURE FUELING PANEL (ATA 28)
# ------------------------------------------------------------------------------
elif opcion_sistema == "MÓDULO II: COMBUSTIBLE (ATA 28)":
    st.markdown("<h2 style='text-align: center; color: #f1f5f9; font-family: monospace;'>PRESSURE FUELING PANEL</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #94a3b8;'>Réplica Skeuomórfica del Dispositivo Físico de Rampa (Lbs)</p>", unsafe_allow_html=True)
    
    col_panel_comb, col_monitor_comb = st.columns([1.3, 1])
    
    with col_panel_comb:
        st.markdown("<div class='overhead-frame'>", unsafe_allow_html=True)
        st.markdown("<div class='subpanel-3d' style='background: linear-gradient(180deg, #242b35, #161b22); border: 3px solid #0f172a;'>", unsafe_allow_html=True)
        st.markdown("<div style='text-align: center; font-weight: bold; font-family: monospace; font-size: 1rem; color: #ffffff; margin-bottom: 15px;'>REFUELING PANEL EN RAMPA DE VUELO</div>", unsafe_allow_html=True)
        
        # Display de segmentos estilo cabina real
        st.markdown(f"<div class='display-digital-principal'>{st.session_state.combustible_actual:05d}</div>", unsafe_allow_html=True)
        st.markdown("<div style='text-align: center; font-weight: bold; font-size: 0.75rem; color: #94a3b8; margin-bottom: 25px; font-family: monospace;'>TOTAL QUANTITY (Lbs)</div>", unsafe_allow_html=True)
        
        grid_valvulas = st.columns(3)
        with grid_valvulas[0]:
            st.markdown("<div style='text-align: center; font-weight: bold; font-size: 0.8rem; color: #f1f5f9; font-family: monospace;'>LEFT VALVE</div>", unsafe_allow_html=True)
            est_l = "<div class='anunciador-verde'>FULL</div>" if st.session_state.combustible_actual >= (st.session_state.combustible_objetivo * 0.3) else "<div class='anunciador-apagado'>OFF</div>"
            st.markdown(est_l, unsafe_allow_html=True)
            st.session_state.valvula_izq = st.radio("V_Izq:", ["ON", "OFF"], index=1 if st.session_state.valvula_izq == "OFF" else 0, key="sel_v_izq", label_visibility="collapsed")
            
        with grid_valvulas[1]:
            st.markdown("<div style='text-align: center; font-weight: bold; font-size: 0.8rem; color: #f1f5f9; font-family: monospace;'>CENTER VALVE</div>", unsafe_allow_html=True)
            est_c = "<div class='anunciador-verde'>FULL</div>" if st.session_state.combustible_actual >= (st.session_state.combustible_objetivo * 0.8) else "<div class='anunciador-apagado'>OFF</div>"
            st.markdown(est_c, unsafe_allow_html=True)
            st.session_state.valvula_ctr = st.radio("V_Ctr:", ["ON", "OFF"], index=1 if st.session_state.valvula_ctr == "OFF" else 0, key="sel_v_ctr", label_visibility="collapsed")
            
        with grid_valvulas[2]:
            st.markdown("<div style='text-align: center; font-weight: bold; font-size: 0.8rem; color: #f1f5f9; font-family: monospace;'>RIGHT VALVE</div>", unsafe_allow_html=True)
            est_r = "<div class='anunciador-verde'>FULL</div>" if st.session_state.combustible_actual >= st.session_state.combustible_objetivo else "<div class='anunciador-apagado'>OFF</div>"
            st.markdown(est_r, unsafe_allow_html=True)
            st.session_state.valvula_der = st.radio("V_Der:", ["ON", "OFF"], index=1 if st.session_state.valvula_der == "OFF" else 0, key="sel_v_der", label_visibility="collapsed")

        st.markdown("<div class='linea-tactica'></div>", unsafe_allow_html=True)

        grid_controles_inf = st.columns(4)
        with grid_controles_inf[0]:
            if st.button("🧪 HIGH LEVEL"): st.toast("Líneas hidráulicas sometidas a prueba de estanqueidad...")
            if st.button("💡 ANNUN TEST"): st.toast("Filtros dicroicos y filamentos verificados.")
        with grid_controles_inf[1]:
            st.markdown(f"<div class='display-digital-secundario'>{st.session_state.combustible_objetivo:05d}</div>", unsafe_allow_html=True)
            st.markdown("<div style='text-align: center; font-weight: bold; font-size: 0.65rem; color: #94a3b8; font-family: monospace;'>QTY SELECT</div>", unsafe_allow_html=True)
        with grid_controles_inf[2]:
            if st.button("🔼 INC QUANTITY"):
                if st.session_state.combustible_objetivo < 24000: st.session_state.combustible_objetivo += 100; st.rerun()
            if st.button("🔽 DEC QUANTITY"):
                if st.session_state.combustible_objetivo > 1000: st.session_state.combustible_objetivo -= 100; st.rerun()
        with grid_controles_inf[3]:
            sel_modo = st.radio("Modo Suministro:", ["MÁXIMO", "PRESELECCIÓN"], index=1, key="sel_modo_c")
            if sel_modo == "MÁXIMO": st.session_state.combustible_objetivo = 24000

        st.markdown("</div>", unsafe_allow_html=True)
        
        # MANDOS MECÁNICOS CISTERNA ADYACENTE
        st.markdown("<div class='subpanel-3d' style='background-color: #1a202c;'>", unsafe_allow_html=True)
        st.markdown("<div style='color: #fbbf24; font-weight: bold; font-size: 0.8rem; margin-bottom: 10px; text-align: center; font-family: monospace;'>🚧 PANEL DE ACOPLE DEL CAMIÓN CISTERNA DE RAMPA</div>", unsafe_allow_html=True)
        grid_botones_camion = st.columns(3)
        with grid_botones_camion[0]:
            if st.button("🚀 INICIAR BOMBEO ACTIVO"):
                if "ON" in [st.session_state.valvula_izq, st.session_state.valvula_ctr, st.session_state.valvula_der]:
                    st.session_state.bombeo_activo = True
                    st.rerun()
                else: st.error("Abra al menos un selector de válvula (ON) para permitir el flujo por presión.")
        with grid_botones_camion[1]:
            if st.button("⏹️ PAUSAR PRESIÓN"):
                st.session_state.bombeo_activo = False
                st.rerun()
        with grid_botones_camion[2]:
            if st.button("🚨 PURGAR LÍNEAS / RESET"):
                st.session_state.combustible_actual = 1150
                st.session_state.bombeo_activo = False
                st.rerun()
        st.markdown("</div>", unsafe_allow_html=True)
        
        st.markdown("</div>", unsafe_allow_html=True) # Cierre overhead-frame

    with col_monitor_comb:
        st.markdown("### 📋 Flight Deck Verification Unit")
        
        if st.session_state.bombeo_activo:
            inf_combustible = "⚡ SUCCIÓN DE ALTA PRESIÓN EN CURSO ⚡\n\n Transfiriendo masa de carburante hacia los depósitos estructurales alares y central de la aeronave."
        elif st.session_state.combustible_actual == st.session_state.combustible_objetivo:
            inf_combustible = "🟢 CARGA DE COMBUSTIBLE NOMINAL CONCLUIDA\n\n Valores de peso y balance balanceados.\n Boquilla de rampa autorizada para desconexión de forma segura."
        else:
            inf_combustible = "📲 CIRCUITO DE ALIMENTACIÓN ENGANCHADO\n\n Unidad a la espera de comandos de presión.\n Configure el dial 'QTY SELECT' y sitúe las compuertas deseadas en ON."

        st.markdown(f"""
            <div class="pantalla-mfd" style="border: 5px solid #d97706; background-color: #0c0702; color: #fbbf24;">
<div style="display: flex; justify-content: space-between; border-bottom: 2px solid #78350f; padding-bottom: 8px; margin-bottom: 25px; font-size: 0.8rem; font-weight: bold;"><span>MONITOR: FUEL SYSTEM DATA</span><span>RAMPA: FAE-QUITO</span></div>
📊 PARÁMETROS HIDRÁULICOS Y MECÁNICOS DEL SISTEMA ATA 28:

 • VÁLVULA DE ENTRADA ALA IZQUIERDA : {st.session_state.valvula_izq}
 • VÁLVULA DE ENTRADA TANQUE CENTRAL: {st.session_state.valvula_ctr}
 • VÁLVULA DE ENTRADA ALA DERECHA   : {st.session_state.valvula_der}
 
 • COMBUSTIBLE PROGRAMADO EN DIAL   : {st.session_state.combustible_objetivo} Lbs
 • COMBUSTIBLE REAL EN INTERIOR     : {st.session_state.combustible_actual} Lbs

 ──────────────── SISTEMA DE INTEGRACIÓN Y CONFIGURACIÓN ────────────────
 
 [ ACOPLE PRINCIPAL ] ──> VALVULA DE ENTRADA BOQUILLA : ESTABLE
 [ MASA A TIERRA ]    ──> CONEXIÓN DE SEGURIDAD (BONDING): ACTIVE

----------------------------------------------------------------------
🔔 CONTROL ALERTING SYSTEM (RAMPA) - REPORT:

{inf_combustible}
            </div>
        """, unsafe_allow_html=True)
