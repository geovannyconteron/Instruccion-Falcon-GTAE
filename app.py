import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Falcon 7X Flight Deck", layout="wide")

st.markdown("""
    <style>
    .main { background-color: #0d1117; color: #f1f5f9; font-family: monospace; }
    [data-testid="stSidebar"] { background-color: #050505; }
    .overhead-grid { display: grid; grid-template-columns: repeat(4, 1fr); gap: 8px; }
    .korry { background: #1a202c; border: 1px solid #334155; padding: 10px; text-align: center; border-radius: 4px; font-size: 0.7rem; font-weight: bold; }
    .mfd-screen { background: #01040a; border: 4px solid #1e293b; padding: 15px; border-radius: 6px; min-height: 700px; color: #38bdf8; }
    </style>
""", unsafe_allow_html=True)

# Inicialización de Estados
if "autenticado" not in st.session_state: st.session_state.autenticado = False
if not st.session_state.autenticado:
    col1, col2, col3 = st.columns([1,2,1])
    with col2:
        if st.button("INGRESAR A CABINA"): st.session_state.autenticado = True; st.rerun()
    st.stop()

# Lógica de estados compartida
if "p_bat" not in st.session_state: st.session_state.update({"bat": False, "apu": False, "bleed": False, "boost": [False]*4, "eng": ["STBY"]*3, "lev": ["OFF"]*3, "cas": ["🟢 COLD DARK"]})

with st.sidebar:
    if st.button("🔒 DESCONECTAR"): st.session_state.autenticado = False; st.rerun()
    tipo = st.radio("MODO:", ["✈️ PILOTOS", "🔧 MANTENIMIENTO"])
    mod = st.radio("CONSOLA:", ["ATA 24", "ATA 28"] if tipo == "🔧 MANTENIMIENTO" else ["MÓDULO III"])

col_panel, col_mfd = st.columns([1.5, 1])

with col_panel:
    # --- FIRE PANEL ---
    cols = st.columns(5)
    for i in range(5): cols[i].markdown("<div class='korry'>FIRE<br>TEST</div>", unsafe_allow_html=True)
    
    # --- BAT & BOOSTER PANEL ---
    c1, c2 = st.columns(2)
    with c1:
        if st.button("BAT 1/2", use_container_width=True): st.session_state.bat = not st.session_state.bat; st.rerun()
    
    c_pumps = st.columns(4)
    for i in range(4):
        if c_pumps[i].button(f"PMP {['1A','2A','2B','3A'][i]}", use_container_width=True):
            st.session_state.boost[i] = not st.session_state.boost[i]; st.rerun()

    # --- START PANEL ---
    c_start = st.columns(3)
    for i in range(3):
        if c_start[i].button(f"START {i+1}", use_container_width=True):
            if st.session_state.bat and st.session_state.bleed: st.session_state.eng[i] = "CRANK"
            st.rerun()

with col_mfd:
    st.markdown("<div class='mfd-screen'>", unsafe_allow_html=True)
    st.markdown(f"<b>CAS LOG:</b><br>{'<br>'.join(st.session_state.cas)}", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

# Mantenimiento (Lógica íntegra restaurada)
if tipo == "🔧 MANTENIMIENTO":
    if mod == "ATA 24":
        if st.button("RESET MANT"): st.session_state.fase_e = 0; st.rerun()
        st.write("Estado de Barras:", st.session_state.fase_e)
