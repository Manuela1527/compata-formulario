import streamlit as st
import os
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

# Configuración de la página
st.set_page_config(
    page_title="Compata - Comparador de Energía",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Importar las páginas
from landing import show_landing
from app import show_formulario
from results import show_results

# Configuración de Metabase (compartida)
METABASE_BASE_URL = os.getenv('METABASE_BASE_URL') or st.secrets.get("METABASE_BASE_URL", "https://bia.metabaseapp.com")
METABASE_API_KEY = os.getenv('METABASE_API_KEY') or st.secrets.get("METABASE_API_KEY", "mb_gpEWL1xnHvLH3Tl+6ltslSBVE5mC9fGwaRdOv1aSG5s=")

# CSS global
st.markdown("""
<style>
    /* Ocultar el menú de Streamlit */
    #MainMenu {visibility: hidden;}
    
    /* Ocultar el footer */
    footer {visibility: hidden;}
    
    /* Ocultar el header */
    header {visibility: hidden;}
    
    /* Ajustar el padding del contenedor principal */
    .main .block-container {
        padding-top: 1rem;
        padding-bottom: 0rem;
        padding-left: 1rem;
        padding-right: 1rem;
        max-width: none;
    }
    
    /* Navbar fijo */
    .navbar {
        position: fixed;
        top: 0;
        left: 0;
        right: 0;
        background: white;
        border-bottom: 1px solid #eee;
        padding: 1rem 2rem;
        z-index: 999;
        display: flex;
        justify-content: space-between;
        align-items: center;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    
    .navbar-brand {
        font-size: 1.5rem;
        font-weight: bold;
        color: #333;
        text-decoration: none;
    }
    
    .navbar-nav {
        display: flex;
        gap: 2rem;
        align-items: center;
    }
    
    .navbar-link {
        color: #666;
        text-decoration: none;
        font-weight: 500;
        transition: color 0.3s ease;
    }
    
    .navbar-link:hover {
        color: #28a745;
    }
    
    .navbar-link.active {
        color: #28a745;
        font-weight: bold;
    }
    
    /* Ajustar el contenido para el navbar fijo */
    .main-content {
        margin-top: 80px;
    }
    
    /* Responsivo */
    @media (max-width: 768px) {
        .navbar {
            padding: 1rem;
        }
        
        .navbar-nav {
            gap: 1rem;
        }
        
        .main .block-container {
            padding-left: 0.5rem;
            padding-right: 0.5rem;
        }
    }
</style>
""", unsafe_allow_html=True)

# Inicializar session state
if 'page' not in st.session_state:
    st.session_state.page = 'landing'

if 'form_submitted' not in st.session_state:
    st.session_state.form_submitted = False

if 'providers_data' not in st.session_state:
    st.session_state.providers_data = []

if 'form_data' not in st.session_state:
    st.session_state.form_data = {}

# Navbar
def show_navbar():
    current_page = st.session_state.page
    
    navbar_html = f"""
    <div class="navbar">
        <div class="navbar-brand">⚡ Compata</div>
        <div class="navbar-nav">
            <a href="#" class="navbar-link {'active' if current_page == 'landing' else ''}" 
               onclick="window.parent.postMessage({{type: 'streamlit:setComponentValue', value: 'landing'}}, '*')">
               Inicio
            </a>
            <a href="#" class="navbar-link {'active' if current_page == 'formulario' else ''}"
               onclick="window.parent.postMessage({{type: 'streamlit:setComponentValue', value: 'formulario'}}, '*')">
               Comparar
            </a>
            <a href="#" class="navbar-link" style="color: #007bff;">¿Cómo funciona?</a>
            <a href="#" class="navbar-link" style="color: #007bff;">Ayuda</a>
        </div>
    </div>
    """
    
    st.markdown(navbar_html, unsafe_allow_html=True)

# Función de navegación simplificada
def navigate_to(page_name):
    st.session_state.page = page_name
    if page_name == 'landing':
        st.session_state.form_submitted = False
        st.session_state.providers_data = []
    st.rerun()

# Botones de navegación en sidebar (oculto pero funcional)
with st.sidebar:
    st.write("Navegación")
    if st.button("🏠 Inicio", key="nav_home"):
        navigate_to('landing')
    if st.button("📝 Formulario", key="nav_form"):
        navigate_to('formulario')

# Mostrar navbar
show_navbar()

# Contenido principal
st.markdown('<div class="main-content">', unsafe_allow_html=True)

# Router principal
if st.session_state.page == 'landing':
    show_landing()

elif st.session_state.page == 'formulario':
    show_formulario(METABASE_BASE_URL, METABASE_API_KEY)

elif st.session_state.page == 'results':
    show_results()

else:
    # Página por defecto
    show_landing()

st.markdown('</div>', unsafe_allow_html=True)

# JavaScript para manejar la navegación del navbar
st.markdown("""
<script>
window.addEventListener('message', function(event) {
    if (event.data.type === 'streamlit:setComponentValue') {
        // Aquí manejaríamos la navegación si fuera necesario
        console.log('Navigate to:', event.data.value);
    }
});
</script>
""", unsafe_allow_html=True)