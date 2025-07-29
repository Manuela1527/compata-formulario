import streamlit as st
import requests
import json
import pandas as pd
from datetime import datetime, date
import time

def show_formulario(METABASE_BASE_URL, METABASE_API_KEY):
    # CSS para el formulario
    st.markdown("""
    <style>
        .form-container {
            max-width: 800px;
            margin: 0 auto;
            padding: 2rem;
        }
        
        .form-title {
            font-size: 2.5rem;
            font-weight: bold;
            color: #333;
            text-align: center;
            margin-bottom: 1rem;
        }
        
        .form-subtitle {
            font-size: 1.1rem;
            color: #666;
            text-align: center;
            margin-bottom: 3rem;
        }
        
        .form-section {
            background: white;
            padding: 2rem;
            border-radius: 15px;
            box-shadow: 0 5px 15px rgba(0,0,0,0.1);
            margin-bottom: 2rem;
        }
        
        .section-header {
            font-size: 1.3rem;
            font-weight: bold;
            color: #333;
            margin-bottom: 1.5rem;
            padding-bottom: 0.5rem;
            border-bottom: 2px solid #28a745;
        }
        
        .info-box {
            background: #e8f5e8;
            border-left: 4px solid #28a745;
            padding: 1rem;
            border-radius: 8px;
            margin: 1rem 0;
        }
        
        .required-field {
            color: #dc3545;
        }
        
        .success-message {
            background: #d4edda;
            color: #155724;
            padding: 1rem;
            border-radius: 8px;
            border: 1px solid #c3e6cb;
            margin: 1rem 0;
        }
        
        .error-message {
            background: #f8d7da;
            color: #721c24;
            padding: 1rem;
            border-radius: 8px;
            border: 1px solid #f5c6cb;
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

    # Funciones auxiliares
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
        st.info("🔍 Consultando base de datos Metabase...")
        
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

    # Título del formulario
    st.markdown("""
    <div class="form-container">
        <h1 class="form-title">Información de tu Empresa</h1>
        <p class="form-subtitle">
            Completa estos datos para encontrar las mejores tarifas eléctricas disponibles en tu zona
        </p>
    </div>
    """, unsafe_allow_html=True)

    # Mostrar resultados o formulario
    if st.session_state.form_submitted and st.session_state.providers_data:
        st.session_state.page = "results"
        st.rerun()
    else:
        # Formulario principal
        with st.form("formulario_empresa", clear_on_submit=False):
            # Sección de información de contacto
            st.markdown("""
            <div class="form-section">
                <div class="section-header">📞 Información de Contacto</div>
            </div>
            """, unsafe_allow_html=True)
            
            col1, col2 = st.columns(2)
            with col1:
                correo = st.text_input("Correo electrónico *", placeholder="ejemplo@empresa.com")
            with col2:
                celular = st.text_input("Celular *", placeholder="3001234567")

            # Sección de información empresarial
            st.markdown("""
            <div class="form-section">
                <div class="section-header">🏢 Información Empresarial</div>
            </div>
            """, unsafe_allow_html=True)
            
            col1, col2 = st.columns(2)
            with col1:
                nombre_apellido = st.text_input("Nombre y apellido del contacto *", placeholder="Juan Pérez")
                nombre_empresa = st.text_input("Nombre de la empresa *", placeholder="Mi Empresa S.A.S.")
            with col2:
                nit_empresa = st.text_input("NIT *", placeholder="900123456-1")
                consumo_energia = st.number_input("Consumo mensual promedio (COP) *", min_value=0, value=1500000, step=100000)

            # Sección técnica
            st.markdown("""
            <div class="form-section">
                <div class="section-header">⚡ Información Técnica y de Facturación</div>
            </div>
            """, unsafe_allow_html=True)
            
            col1, col2 = st.columns(2)
            with col1:
                nivel_tension = st.selectbox("Nivel de tensión *", 
                    ["", "level1", "level2", "level3"],
                    help="Nivel 1: Residencial/Pequeño comercio, Nivel 2: Comercial/Industrial medio, Nivel 3: Gran industria")
                fecha_ultima_factura = st.date_input("Fecha de la última factura *", 
                    help="Nos ayuda a entender tu ciclo de facturación")
            with col2:
                comercializador_actual = st.selectbox("Comercializador actual *", [""] + comercializadores)
                operador_red = st.selectbox("Operador de red *", [""] + operadores_red)

            # Sección de ubicación
            st.markdown("""
            <div class="form-section">
                <div class="section-header">📍 Ubicación y Configuración</div>
            </div>
            """, unsafe_allow_html=True)
            
            col1, col2 = st.columns(2)
            with col1:
                ubicacion = st.selectbox("Ubicación (Ciudad/Departamento) *", [""] + ubicaciones)
            with col2:
                propiedad_equipo = st.selectbox("Propiedad del equipo de medida *", 
                    ["", "usuario", "operador"],
                    help="¿De quién es el medidor eléctrico?")

            st.markdown("""
            <div class="info-box">
                💡 <strong>Información importante:</strong> Todos los campos marcados con * son obligatorios. 
                La información proporcionada será utilizada únicamente para encontrar las mejores opciones de tarifas eléctricas.
            </div>
            """, unsafe_allow_html=True)

            # Botón de envío
            col1, col2, col3 = st.columns([1, 2, 1])
            with col2:
                submitted = st.form_submit_button("🔍 Buscar Mejores Tarifas", 
                    use_container_width=True,
                    type="primary")
            
            if submitted:
                # Validar campos obligatorios
                required_fields = [
                    (correo, "Correo electrónico"),
                    (celular, "Celular"),
                    (nombre_apellido, "Nombre y apellido"),
                    (nombre_empresa, "Nombre de la empresa"),
                    (nit_empresa, "NIT"),
                    (nivel_tension, "Nivel de tensión"),
                    (fecha_ultima_factura, "Fecha de la última factura"),
                    (comercializador_actual, "Comercializador actual"),
                    (ubicacion, "Ubicación"),
                    (operador_red, "Operador de red"),
                    (propiedad_equipo, "Propiedad del equipo")
                ]
                
                missing_fields = [field_name for field_value, field_name in required_fields if not field_value]
                
                if missing_fields:
                    st.markdown(f"""
                    <div class="error-message">
                        ❌ <strong>Faltan campos obligatorios:</strong><br>
                        • {', '.join(missing_fields)}
                    </div>
                    """, unsafe_allow_html=True)
                else:
                    # Guardar datos del formulario
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
                    
                    # Buscar proveedores
                    with st.spinner("🔄 Analizando tarifas disponibles..."):
                        providers = get_best_providers_simple(st.session_state.form_data)
                        st.session_state.providers_data = providers
                        st.session_state.form_submitted = True
                    
                    if providers:
                        st.markdown("""
                        <div class="success-message">
                            ✅ <strong>¡Análisis completado!</strong> Encontramos opciones para ti. Redirigiendo a los resultados...
                        </div>
                        """, unsafe_allow_html=True)
                        time.sleep(2)  # Pequeña pausa para mostrar el mensaje
                        st.rerun()
                    else:
                        st.markdown("""
                        <div class="error-message">
                            ⚠️ <strong>No encontramos resultados</strong> para tu configuración específica. 
                            Intenta con diferentes parámetros o contáctanos para asistencia personalizada.
                        </div>
                        """, unsafe_allow_html=True)

        # Botón para volver al inicio
        st.markdown("<br>", unsafe_allow_html=True)
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            if st.button("← Volver al inicio", use_container_width=True):
                st.session_state.page = "landing"
                st.rerun()