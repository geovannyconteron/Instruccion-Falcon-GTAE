import streamlit as st

st.set_page_config(page_title="Simulador Falcon 7X - GTAE", page_icon="✈️", layout="wide")

# Estilos de inmersión para calcar la cabina oscura y botones grises de aviación
st.markdown("""
    <style>
    .main { background-color: #05070c; color: #f1f5f9; }
    
    /* Botones estilo cabina gris oscuro militar */
    .stButton>button { 
        width: 100%; 
        font-weight: bold; 
        height: 50px; 
        border-radius: 4px; 
        font-size: 0.82rem;
        background-color: #2a3547 !important;
        color: #ffffff !important;
        border: 2px solid #475569 !important;
    }
    .stButton>button:disabled {
        background-color: #1e2430 !important;
        color: #4b5563 !important;
        border: 1px solid #111827 !important;
    }
    
    /* Consola física gris de fondo */
    .consola-gris { background-color: #4a5568; border: 4px solid #2d3748; padding: 25px; border-radius: 8px; margin-bottom: 15px; box-shadow: inset 0 2px 5px rgba(0,0,0,0.5); }
    .seccion-dc { border: 3px solid #22c55e; padding: 15px; border-radius: 6px; background-color: #2d3748; }
    .titulo-dc { color: #ffffff; font-weight: bold; font-size: 1rem; text-align: center; font-family: monospace; letter-spacing: 1px; margin-bottom: 15px; }
    
    /* Réplica exacta de la Pantalla CRT Honeywell EASy (Totalmente Hermética) */
    .crt-easy-display { font-family: 'Courier New', Courier, monospace; background-color: #000000; border: 5px solid #4a5568; border-radius: 8px; padding: 25px; min-height: 500px; box-shadow: inset 0px 0px 30px rgba(0,255,102,0.15), 0 10px 15px rgba(0,0,0,0.7); color: #00ff66; }
    .crt-header-line { display: flex; justify-content: space-between; border-bottom: 2px solid #064e3b; padding-bottom: 8px; margin-bottom: 20px; color: #00d2ff; font-size: 0.85rem; font-weight: bold; }
    .crt-section-title { color: #00d2ff; font-weight: bold; margin-bottom: 12px; font-size: 0.95rem; }
    .crt-txt-green { font-size: 0.95rem; margin-bottom: 6px; font-weight: bold; color: #00ff66; }
    .crt-txt-amber { font-size: 0.95rem; margin-bottom: 6px; font-weight: bold; color: #ffb700; }
    .crt-txt-gray { font-size: 0.95rem; margin-bottom: 6px; font-weight: bold; color: #4b5563; }
    
    /* Caja de Alertas CAS interna */
    .crt-cas-container { border-top: 1px dashed #064e3b; padding-top: 15px; margin-top: 20px; }
    .crt-cas-label { color: #ffb700; font-weight: bold; font-size: 0.9rem; margin-bottom: 10px; border-bottom: 1px solid #78350f; padding-bottom: 4px; }
    .crt-cas-msg { font-size: 0.88rem; line-height: 1.5; white-space: pre-line; background-color: #050505; border: 1px solid #1f2937; padding: 15px; border-radius: 4px; }
    
    /* Anunciadores de luces integrados debajo de los botones */
    .luz-f7x-verde { background-color: #064e3b; color: #00ff66; border: 1px solid #22c55e; font-weight: bold; text-align: center; border-radius: 2px; font-size: 0.75rem; padding: 4px; margin-top: 3px; }
    .luz-f7x-amber { background-color: #78350f; color: #ffb700; border: 1px solid #d97706; font-weight: bold; text-align: center; border-radius: 2px; font-size: 0.75rem; padding: 4px; margin-top: 3px; }
    .luz-f7x-off { background-color: #1a202c; color: #4a5568; border: 1px solid #2d3748; text-align: center; border-radius: 2px; font-size: 0.75rem; padding: 4px; margin-top: 3px; }
    </style>
""", unsafe_allow_html=True)

st.title("✈️ Sistema de Simulación Falcon 7X - GTAE")
st.subheader("Entrenamiento Técnico ATA 24: Distribución Real DC SUPPLY")
st.markdown("---")

if "auto_step" not in st.session_state: st.session_state.auto_step = 0

# Lista de comprobación secuencial en español incluyendo el paso de la RAT
PDU_GUIDE = {
    0: "RECEPTÁCULO ABIERTO — ESPERANDO PLANTA EXTERNA GPU\n\n[ACCIÓN]: CONECTE EL ENCHUFE FÍSICO DE LA GPU EN TIERRA.",
    1: "CABLE DE GPU DETECTADO — CONFIGURACIÓN DE VOLTAJE EN ESPERA\n\n[ACCIÓN]: AJUSTE EL VOLTAJE NOMINAL A 28.0 VDC EN EL PANEL EXTERNO.",
    2: "ENERGÍA DE GPU DISPONIBLE — INTERRUPTOR DE LÍNEA APAGADO\n\n[ACCIÓN]: COLOQUE EL SWITCH DE CONTROL DE LA GPU EN POSICIÓN 'ON'.",
    3: "LÍNEA DE TIERRA ESTABLE — VERIFICACIÓN MECÁNICA PREVIA\n\n[ACCIÓN]: ENGANCHE EL FRENO DE PARQUEO EN EL PEDESTAL (1ER DIENTE).",
    4: "PARÁMETROS DE SEGURIDAD OK — LÍNEA DE ALIMENTACIÓN ABIERTA\n\n[ACCIÓN]: ACTIVE LOS SELECTORES CENTRALES 'BAT 1' Y 'BAT 2' EN POSICIÓN 'AUTO'.",
    5: "ALIMENTACIÓN BAJA REQUERIDA — PROTECCIÓN DE DESPACHO EN EMERGENCIA\n\n[ACCIÓN]: PRESIONE EL BOTÓN DE CONTROL ELECTRÓNICO 'RAT AUTO'.",
    6: "INHIBICIÓN RAT CONFIRMADA — ACOPLAMIENTO DE RED REQUERIDO\n\n[ACCIÓN]: PRESIONE EL INTERRUPTOR 'BUS TIE' UBICADO EN EL CENTRO.",
    7: "BARRAS EN ESTADO DE ACOPLAMIENTO — INICIALIZACIÓN DE LÍNEAS\n\n[ACCIÓN]: PRESIONE LOS BOTONES DE CONTROL 'LH INIT' Y 'RH INIT'.",
    8: "LÍNEA DE AVIÓNICA EN ESPERA — CONTACTOR DE ENERGÍA TIERRA\n\n[ACCIÓN]: PRESIONE EL BOTÓN REGULADOR LUMINOSO VERDE 'EXT POWER'.",
    9: "ALIMENTACIÓN PRINCIPAL CONECTADA — PROTECCIÓN DE CARGA DE CABINA\n\n[ACCIÓN]: COLOQUE EL BOTÓN 'CABIN MASTER' EN POSICIÓN 'OFF'.",
    10: "TRANSFERENCIA DE ALIMENTACIÓN ACTIVA — CONFIGURACIÓN DE RED\n\n[ACCIÓN]: PRESIONE LOS CONTACTORES DE SEPARACIÓN 'LH / RH ISOL'.",
    11: "RED DE DISTRIBUCIÓN PARCIAL — INTERRUPTORES MAESTROS DE BARRA\n\n[ACCIÓN]: PRESIONE 'LH MASTER' Y 'RH MASTER' PARA COMPLETAR EL FLUJO NOMINAL.",
    12: "⚡ RED ELÉCTRICA AC/DC ENERGIZADA COMPLETAMENTE CON ÉXITO\n\nTODAS LAS BARRAS EN PARÁMETROS NOMINALES — COCKPIT READY FOR COLD OPERATIONS."
}

col_panels, col_display = st.columns([1.2, 1])

with col_panels:
    st.markdown("<div class='consola-gris'><div class='seccion-dc'><div class='titulo-dc'>⚡ DC SUPPLY PANEL ⚡</div>", unsafe_allow_html=True)
    
    # --- FILA SUPERIOR DEL OVERHEAD Panel ---
    fs = st.columns(8)
    
    with fs[0]:
        st.button("GALLEY MASTER", disabled=True, key="galley")
        st.markdown("<div class='luz-f7x-off'>OFF</div>", unsafe_allow_html=True)
        
    with fs[1]:
        if st.button("LH MASTER", disabled=(st.session_state.auto_step != 11), key="lhmstr"):
            st.session_state.auto_step = 12
            st.rerun()
        st.markdown("<div class='luz-f7x-verde'>ON</div>" if st.session_state.auto_step >= 12 else "<div class='luz-f7x-amber'>OFF</div>", unsafe_allow_html=True)
        
    with fs[2]:
        if st.button("LH INIT", disabled=(st.session_state.auto_step != 7), key="lhinit"):
            pass
        st.markdown("<div class='luz-f7x-off'>RUN</div>" if st.session_state.auto_step >= 8 else "<div class='luz-f7x-amber'>OFF</div>", unsafe_allow_html=True)
        
    with fs[3]:
        if st.button("BUS TIE", disabled=(st.session_state.auto_step != 6), key="bustie"):
            st.session_state.auto_step = 7
            st.rerun()
        st.markdown("<div class='luz-f7x-amber'>TIED</div>" if st.session_state.auto_step >= 7 else "<div class='luz-f7x-off'>AUTO</div>", unsafe_allow_html=True)
        
    with fs[4]:
        if st.button("RH INIT", disabled=(st.session_state.auto_step != 7), key="rhinit"):
            st.session_state.auto_step = 8
            st.rerun()
        st.markdown("<div class='luz-f7x-off'>RUN</div>" if st.session_state.auto_step >= 8 else "<div class='luz-f7x-amber'>OFF</div>", unsafe_allow_html=True)
        
    with fs[5]:
        if st.button("RH MASTER", disabled=(st.session_state.auto_step != 11), key="rhmstr"):
            st.session_state.auto_step = 12
            st.rerun()
        st.markdown("<div class='luz-f7x-verde'>ON</div>" if st.session_state.auto_step >= 12 else "<div class='luz-f7x-amber'>OFF</div>", unsafe_allow_html=True)
        
    with fs[6]:
        if st.button("CABIN MASTER", disabled=(st.session_state.auto_step != 9), key="cabin"):
            st.session_state.auto_step = 10
            st.rerun()
        st.markdown("<div class='luz-f7x-amber'>OFF</div>" if st.session_state.auto_step >= 10 else "<div class='luz-f7x-verde'>ON</div>", unsafe_allow_html=True)
        
    with fs[7]:
        if st.button("EXT POWER", disabled=(st.session_state.auto_step != 8), key="extpwr"):
            st.session_state.auto_step = 9
            st.rerun()
        st.markdown("<div class='luz-f7x-verde'>ONLINE</div>" if st.session_state.auto_step >= 9 else "<div class='luz-f7x-off'>OFF</div>", unsafe_allow_html=True)

    st.markdown("<div style='border-top: 4px solid #ffffff; margin-top: 25px; margin-bottom: 25px;'></div>", unsafe_allow_html=True)

    # --- FILA INFERIOR DEL OVERHEAD Panel ---
    fi = st.columns(8)
    
    with fi[0]:
        st.button("GEN 1", disabled=True, key="gen1")
        st.markdown("<div class='luz-f7x-off'>OFF</div>", unsafe_allow_html=True)
        
    with fi[1]:
        if st.button("LH ISOL", disabled=(st.session_state.auto_step != 10), key="lhisol"):
            st.session_state.auto_step = 11
            st.rerun()
        st.markdown("<div class='luz-f7x-off'>TIED</div>" if st.session_state.auto_step >= 11 else "<div class='luz-f7x-amber'>ISOL</div>", unsafe_allow_html=True)
        
    with fi[2]:
        if st.button("BAT 1", disabled=(st.session_state.auto_step != 4), key="bat1"):
            pass
        st.markdown("<div class='luz-f7x-verde'>AUTO</div>" if st.session_state.auto_step >= 5 else "<div class='luz-f7x-off'>OFF</div>", unsafe_allow_html=True)
        
    with fi[3]:
        if st.button("BAT 2", disabled=(st.session_state.auto_step != 4), key="bat2"):
            st.session_state.auto_step = 5
            st.rerun()
        st.markdown("<div class='luz-f7x-verde'>AUTO</div>" if st.session_state.auto_step >= 5 else "<div class='luz-f7x-off'>OFF</div>", unsafe_allow_html=True)
        
    with fi[4]:
        if st.button("RAT AUTO", disabled=(st.session_state.auto_step != 5), key="ratauto"):
            st.session_state.auto_step = 6
            st.rerun()
        st.markdown("<div class='luz-f7x-amber'>INHIBIT</div>" if st.session_state.auto_step >= 6 else "<div class='luz-f7x-off'>OFF</div>", unsafe_allow_html=True)
        
    with fi[5]:
        if st.button("RH ISOL", disabled=(st.session_state.auto_step != 10), key="rhisol"):
            st.session_state.auto_step = 11
            st.rerun()
        st.markdown("<div class='luz-f7x-off'>TIED</div>" if st.session_state.auto_step >= 11 else "<div class='luz-f7x-amber'>ISOL</div>", unsafe_allow_html=True)
        
    with fi[6]:
        st.button("GEN 2", disabled=True, key="gen2")
        st.markdown("<div class='luz-f7x-off'>OFF</div>", unsafe_allow_html=True)
        
    with fi[7]:
        st.button("GEN 3", disabled=True, key="gen3")
        st.markdown("<div class='luz-f7x-off'>OFF</div>", unsafe_allow_html=True)

    st.markdown("</div></div>", unsafe_allow_html=True)

    # --- CONTROLES AUXILIARES DE ENERGÍA Y SEGURIDAD EXTERNA ---
    st.markdown("<div class='consola-gris' style='background-color: #2d3748;'><div class='titulo-overhead'>🔧 CONTROLES INICIALES DE TRANSICIÓN EN HANGAR</div>", unsafe_allow_html=True)
    cx1, cx2, cx3, cx4 = st.columns(4)
    with cx1:
        if st.button("🔌 CONECTAR ACOPLE GPU", disabled=(st.session_state.auto_step != 0), key="con_gpu"):
            st.session_state.auto_step = 1
            st.rerun()
        st.markdown("<div class='luz-f7x-verde'>CONECTADO</div>" if st.session_state.auto_step >= 1 else "<div class='luz-f7x-off'>DESCONECTADO</div>", unsafe_allow_html=True)
    with cx2:
        if st.button("⚡ SETEAR A 28.0 VDC", disabled=(st.session_state.auto_step != 1), key="set_volt"):
            st.session_state.auto_step = 2
            st.rerun()
        st.markdown("<div class='luz-f7x-verde'>28.0 VDC OK</div>" if st.session_state.auto_step >= 2 else "<div class='luz-f7x-off'>0.0 VDC</div>", unsafe_allow_html=True)
    with cx3:
        if st.button("🎛️ SWITCH GPU A ON", disabled=(st.session_state.auto_step != 2), key="sw_gpu"):
            st.session_state.auto_step = 3
            st.rerun()
        st.markdown("<div class='luz-f7x-verde'>LÍNEA ONLINE</div>" if st.session_state.auto_step >= 3 else "<div class='luz-f7x-off'>LÍNEA OFF</div>", unsafe_allow_html=True)
    with cx4:
        if st.button("⚙️ FRENO PARQUEO", disabled=(st.session_state.auto_step != 3), key="park_brake"):
            st.session_state.auto_step = 4
            st.rerun()
        st.markdown("<div class='luz-f7x-verde'>ENGANCHADO</div>" if st.session_state.auto_step >= 4 else "<div class='luz-f7x-off'>LIBERADO</div>", unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("🚨 REINICIAR PROCEDIMIENTO DE INSTRUCCIÓN", key="reset_sim"):
        st.session_state.auto_step = 0
        st.rerun()
    st.markdown("</div>", unsafe_allow_html=True)

with col_display:
    st.markdown("### 📺 Honeywell EASy Display (PDU 1)")
    
    # Bloque de renderizado hermético para simular el display integrado
    if st.session_state.auto_step == 0:
        st.markdown("""
            <div class='crt-display-box' style='font-family: monospace; background-color: #000000; border: 5px solid #4a5568; border-radius: 8px; padding: 25px; min-height: 500px; color: #4b5563; text-align: center; padding-top: 180px;'>
                <div style='font-size: 1.1rem; font-weight: bold;'>[ DISPLAY CRT INERTE — RED SIN ENERGÍA ]</div>
                <div style='font-size: 0.85rem; margin-top: 15px; color: #2d3748;'>A la espera de transferencia eléctrica por GPU externa en hangar.</div>
            </div>
        """, unsafe_allow_html=True)
    else:
        volt_gpu = "28.0 VDC" if st.session_state.auto_step >= 2 else "0.0 VDC"
        volt_ess = "28.1 V" if st.session_state.auto_step >= 9 else "0.0 V"
        status_isol = "CONECTADO [── GREEN ──]" if st.session_state.auto_step >= 11 else "AISLADO [| AMBER |]"
        
        class_ess = "crt-txt-green" if st.session_state.auto_step >= 9 else "crt-txt-gray"
        class_isol = "crt-txt-green" if st.session_state.auto_step >= 11 else "crt-txt-amber"
        color_cas_text = "#ffb700" if st.session_state.auto_step < 12 else "#00ff66"

        # Todo el contenido se escribe de manera directa dentro de la pantalla simulada
        pantalla_html = (
            "<div class='crt-easy-display'>"
                "<div class='crt-header-line'>"
                    "<span>SISTEMA: HONEYWELL EASY MDU 1</span>"
                    "<span>MODO: SINÓPTICO ELÉCTRICO ATA 24</span>"
                "</div>"
                "<div class='crt-section-title'>⚙️ TELEMETRÍA DE RED DE BARRAS EN TIERRA:</div>"
                "<div class='crt-txt-green'>• ALIMENTACIÓN DE GPU EXT : " + volt_gpu + "</div>"
                "<div class='" + class_ess + "'>• BARRA ESENCIAL LH     : " + volt_ess + "</div>"
                "<div class='" + class_ess + "'>• BARRA ESENCIAL RH     : " + volt_ess + "</div>"
                "<div class='" + class_isol + "'>• ESTADO CONTACTOR ISOL : " + status_isol + "</div>"
                "<div class='crt-cas-container'>"
                    "<div class='crt-cas-label'>🔔 Crew Alerting System (CAS) & Procedimiento Automático:</div>"
                    "<div class='crt-cas-msg' style='color: " + color_cas_text + ";'>"
                        + PDU_GUIDE[st.session_state.auto_step] +
                    "</div>"
                "</div>"
            "</div>"
        )
        
        st.markdown(pantalla_html, unsafe_allow_html=True)