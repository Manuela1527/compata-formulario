import streamlit as st
import requests
import json
import pandas as pd
from datetime import datetime, date
import time
import os
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

# Configuración de la página
st.set_page_config(
    page_title="Compata - Formulario",
    page_icon="⚡",
    layout="centered"
)

# Configuración de Metabase desde .env
METABASE_BASE_URL = os.getenv('METABASE_BASE_URL')
METABASE_API_KEY = os.getenv('METABASE_API_KEY')

# CSS simple sin caracteres especiales
st.markdown("""
<style>
    .main-title {
        font-size: 2rem;
        font-weight: bold;
        color: #333;
        text-align: center;
        margin-bottom: 1rem;
    }
    .subtitle {
        font-size: 1rem;
        color: #666;
        text-align: center;
        margin-bottom: 2rem;
    }
    .info-box {
        background: #f0f8ff;
        padding: 1rem;
        border-radius: 8px;
        margin: 1rem 0;
    }
</style>
""", unsafe_allow_html=True)

# Listas de datos
ubicaciones = [
    'ANTIOQUIA', 'ARAUCA', 'BAJO PUTUMAYO', 'BOGOTA', 'BOYACA', 'CALDAS', 
    'CALI', 'CAQUETA', 'CARIBE MAR', 'CARIBE SOL', 'CARTAGO', 'CASANARE', 
    'CAUCA', 'CHOCO', 'CUCUTA', 'CUNDINAMARCA', 'HUILA', 'MEDELLIN', 'META', 
    'NARINO', 'NARIÑO', 'NORTE SANTANDER', 'PACIFICO', 'PEREIRA', 'PUERTO TEJADA', 
    'PUTUMAYO', 'QUINDIO', 'RISARALDA', 'RUITOQUE', 'SANTANDER', 'TOLIMA', 
    'TULUA', 'VALLE', 'YUMBO'
]

comercializadores = [
    'AFINIA', 'AIRE', 'BIA ENERGY', 'CEDENAR', 'CELSIA', 'CELSIA TOLIMA', 
    'CELSIA VALLE', 'CENS', 'CEO', 'CETSA', 'CHEC', 'DICEL', 'DICELER', 
    'DISPAC', 'EBSA', 'EDEQ', 'EEBP', 'EEBPSA', 'EEP', 'ELECTROCAQUETA', 
    'ELECTROHUILA', 'EMCALI', 'EMSA', 'ENEL', 'ENEL X', 'ENELAR', 'ENERCA', 
    'ENERCO', 'ENERMAS', 'ENERTOTAL', 'EPM', 'ESSA', 'NEU', 'NEU ENERGY', 
    'PEESA', 'QIENERGY', 'RUITOQUE', 'SPECTRUM', 'TENERGETICAS', 'VATIA'
]

operadores_red = [
    'CARIBEMAR', 'CEDENAR', 'CELSIA COLOMBIA', 'CELSIA TOLIMA', 'CENS', 
    'CEO', 'CETSA', 'CHEC', 'DISPAC', 'EBSA', 'EDEQ', 'EEBP', 'EEP', 
    'ELECTROCAQUETA', 'ELECTROHUILA', 'EMCALI', 'EMCARTAGO', 'EMSA', 
    'ENEL', 'ENELAR', 'ENERCA', 'EPM', 'ESSA', 'PEESA', 'RUITOQUE'
]

# Funciones
def query_metabase(database_id, query):
    try:
        headers = {
            'X-API-KEY': METABASE_API_KEY,
            'Content-Type': 'application/json'
        }
        
        payload = {
            'type': 'native',
            'native': {
                'query': query
            },
            'database': database_id
        }
        
        response = requests.post(
            f"{METABASE_BASE_URL}/api/dataset",
            headers=headers,
            json=payload,
            timeout=30
        )
        
        if response.status_code == 200:
            result = response.json()
            if 'data' in result and 'rows' in result['data']:
                return result['data']
        elif response.status_code == 202:
            result = response.json()
            if 'data' in result and 'rows' in result['data']:
                return result['data']
        
        st.error(f"Error en Metabase: {response.status_code}")
        return None
            
    except Exception as e:
        st.error(f"Error conectando con Metabase: {str(e)}")
        return None

def get_tech_rating(provider_name):
    ratings = {
        'bia': '⭐⭐⭐⭐⭐',
        'neu': '⭐⭐⭐⭐',
        'peesa': '⭐⭐⭐⭐',
        'spectrum': '⭐⭐⭐⭐⭐'
    }
    
    for key, rating in ratings.items():
        if key in provider_name.lower():
            return rating
    return '⭐⭐⭐'

def get_service_rating(provider_name):
    ratings = {
        'bia': '⭐⭐⭐⭐⭐',
        'neu': '⭐⭐⭐⭐',
        'peesa': '⭐⭐⭐⭐⭐',
        'spectrum': '⭐⭐⭐⭐'
    }
    
    for key, rating in ratings.items():
        if key in provider_name.lower():
            return rating
    return '⭐⭐⭐'

def get_best_providers_simple(form_data):
    st.info("Consultando base de datos Metabase...")
    
    # Mapear nivel de tensión del formulario al query
    nivel_mapping = {
        'level1': 'nivel_1_operator',
        'level2': 'nivel_2_operator', 
        'level3': 'nivel_3_operator'
    }
    
    nivel_query = nivel_mapping.get(form_data["nivel_tension"], 'nivel_2_operator')
    
    # Nuevo query actualizado
    main_query = f"""
    SELECT 
        "source"."mes" AS "mes",
        "source"."provider" AS "provider",
        "source"."city" AS "city",
        "source"."nivel_de_tension" AS "nivel_de_tension",
        "source"."tarifa" AS "tarifa"
    FROM (
        SELECT
            to_char(r.start_date, 'YYYY-MM') AS mes,
            r.provider AS provider,
            r.city AS city,
            v.nivel_de_tension AS nivel_de_tension,
            v.tarifa AS tarifa
        FROM
            public.rates AS r
            CROSS JOIN LATERAL (
                VALUES
                    ('nivel_1_operator', r.total_level_1_operator),
                    ('nivel_1_user', r.total_level_1_user),
                    ('nivel_2_operator', r.total_level_2_operator),
                    ('nivel_3_operator', r.total_level_3_operator),
                    ('nivel_1_shared', r.total_level_1_shared)
            ) AS v(nivel_de_tension, tarifa)
        WHERE
            to_char(r.start_date, 'YYYY-MM') = '2025-07'
            AND r.city ILIKE '%{form_data["ubicacion"]}%'
            AND v.nivel_de_tension = '{nivel_query}'
            AND v.tarifa IS NOT NULL
            AND v.tarifa > 0
            AND r.deleted_at IS NULL
        ORDER BY
            v.tarifa ASC
    ) AS "source"
    LIMIT 10
    """
    
    providers = []
    
    # Ejecutar query
    result = query_metabase(15, main_query)
    st.write("DEBUG QUERY RESULT:")
    st.json(result)
    
    if result and 'rows' in result and len(result['rows']) > 0:
        # Priorizar BIA si existe
        bia_providers = []
        other_providers = []
        
        for row in result['rows']:
            if len(row) >= 5:
                provider_data = {
                    'mes': row[0],
                    'nombre': row[1],
                    'ciudad': row[2],
                    'nivel_tension': row[3],
                    'tarifa': round(float(row[4]), 2),
                    'tecnologia': get_tech_rating(row[1]),
                    'servicio': get_service_rating(row[1]),
                    'is_bia': 'bia' in row[1].lower()
                }
                
                if 'bia' in row[1].lower():
                    bia_providers.append(provider_data)
                else:
                    other_providers.append(provider_data)
        
        # Agregar BIA primero, luego otros
        providers.extend(bia_providers[:1])  # Solo 1 BIA
        providers.extend(other_providers[:3])  # Máximo 3 otros
    
    return providers

# Session state
if 'form_submitted' not in st.session_state:
    st.session_state.form_submitted = False

if 'providers_data' not in st.session_state:
    st.session_state.providers_data = []

# Título
st.markdown('<h1 class="main-title">Información de tu Empresa</h1>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Completa estos datos para encontrar las mejores tarifas eléctricas</p>', unsafe_allow_html=True)

# Mostrar resultados o formulario
if st.session_state.form_submitted:
    st.markdown("# ¡Encontramos las mejores opciones para ti!")
    
    if st.button("Hacer una nueva consulta"):
        st.session_state.form_submitted = False
        st.session_state.providers_data = []
        st.rerun()
    
    if st.session_state.providers_data:
        for i, provider in enumerate(st.session_state.providers_data):
            st.markdown(f"### **{provider['nombre']}**")
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("Tarifa", f"${provider['tarifa']}")
            with col2:
                st.write(f"Tecnología: {provider['tecnologia']}")
            with col3:
                st.button(f"Contactar {provider['nombre']}", key=f"btn_{i}")

else:
    # Formulario
    with st.form("formulario_empresa"):
        correo = st.text_input("Correo electrónico *")
        celular = st.text_input("Celular *")
        consumo_energia = st.number_input("Consumo mensual (COP) *", min_value=0, value=1500000)
        nombre_apellido = st.text_input("Nombre y apellido *")
        nombre_empresa = st.text_input("Nombre empresa *")
        nit_empresa = st.text_input("NIT *")
        nivel_tension = st.selectbox("Nivel tensión *", ["", "level1", "level2", "level3"])
        fecha_ultima_factura = st.date_input("Fecha última factura *")
        comercializador_actual = st.selectbox("Comercializador actual *", [""] + comercializadores)
        ubicacion = st.selectbox("Ubicación *", [""] + ubicaciones)
        operador_red = st.selectbox("Operador red *", [""] + operadores_red)
        propiedad_equipo = st.selectbox("Propiedad equipo *", ["", "usuario", "operador"])
        
        submitted = st.form_submit_button("Buscar Mejores Tarifas")
        
        if submitted:
            if all([correo, celular, nombre_apellido, nombre_empresa, nit_empresa, 
                   nivel_tension, fecha_ultima_factura, comercializador_actual, 
                   ubicacion, operador_red, propiedad_equipo]):
                
                st.session_state.form_data = {
                    'correo': correo,
                    'celular': celular,
                    'consumo_energia': consumo_energia,
                    'nombre_apellido': nombre_apellido,
                    'nombre_empresa': nombre_empresa,
                    'nit_empresa': nit_empresa,
                    'nivel_tension': nivel_tension,
                    'fecha_ultima_factura': str(fecha_ultima_factura),
                    'comercializador_actual': comercializador_actual,
                    'ubicacion': ubicacion,
                    'operador_red': operador_red,
                    'propiedad_equipo': propiedad_equipo
                }
                
                with st.spinner("Analizando tarifas..."):
                    providers = get_best_providers_simple(st.session_state.form_data)
                    st.session_state.providers_data = providers
                    st.session_state.form_submitted = True
                
                st.rerun()
            else:
                st.error("Complete todos los campos obligatorios")