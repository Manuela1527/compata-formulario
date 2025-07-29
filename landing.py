import streamlit as st

def show_landing():
    # CSS personalizado para la landing
    st.markdown("""
    <style>
        .main-container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 0 20px;
        }
        
        .hero-section {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            padding: 80px 0;
            margin: -1rem -1rem 3rem -1rem;
            color: white;
            text-align: center;
            border-radius: 0 0 20px 20px;
        }
        
        .hero-title {
            font-size: 3.5rem;
            font-weight: bold;
            margin-bottom: 1rem;
            line-height: 1.2;
        }
        
        .hero-subtitle {
            font-size: 1.2rem;
            margin-bottom: 2rem;
            opacity: 0.9;
            max-width: 600px;
            margin-left: auto;
            margin-right: auto;
        }
        
        .cta-button {
            background: #28a745;
            color: white;
            padding: 15px 30px;
            border: none;
            border-radius: 50px;
            font-size: 1.1rem;
            font-weight: bold;
            cursor: pointer;
            text-decoration: none;
            display: inline-block;
            margin: 20px 0;
            transition: all 0.3s ease;
        }
        
        .cta-button:hover {
            background: #218838;
            transform: translateY(-2px);
            box-shadow: 0 5px 15px rgba(40, 167, 69, 0.3);
        }
        
        .stats-section {
            background: #f8f9fa;
            padding: 40px 20px;
            margin: 3rem -1rem;
            text-align: center;
            border-radius: 15px;
        }
        
        .stat-number {
            font-size: 2.5rem;
            font-weight: bold;
            color: #28a745;
            margin-bottom: 0.5rem;
        }
        
        .stat-text {
            font-size: 1rem;
            color: #666;
            margin-bottom: 1rem;
        }
        
        .features-section {
            padding: 60px 0;
        }
        
        .section-title {
            font-size: 2.5rem;
            font-weight: bold;
            text-align: center;
            margin-bottom: 1rem;
            color: #333;
        }
        
        .section-subtitle {
            text-align: center;
            color: #666;
            margin-bottom: 3rem;
            font-size: 1.1rem;
        }
        
        .feature-card {
            background: white;
            padding: 30px;
            border-radius: 15px;
            text-align: center;
            box-shadow: 0 5px 15px rgba(0,0,0,0.1);
            margin-bottom: 30px;
            transition: transform 0.3s ease;
        }
        
        .feature-card:hover {
            transform: translateY(-5px);
        }
        
        .feature-icon {
            font-size: 3rem;
            margin-bottom: 1rem;
        }
        
        .feature-title {
            font-size: 1.3rem;
            font-weight: bold;
            margin-bottom: 1rem;
            color: #333;
        }
        
        .feature-description {
            color: #666;
            line-height: 1.6;
        }
        
        .testimonials-section {
            background: #f8f9fa;
            padding: 60px 20px;
            margin: 3rem -1rem;
            border-radius: 15px;
        }
        
        .testimonial-card {
            background: white;
            padding: 30px;
            border-radius: 15px;
            margin-bottom: 20px;
            box-shadow: 0 3px 10px rgba(0,0,0,0.1);
        }
        
        .testimonial-text {
            font-style: italic;
            font-size: 1.1rem;
            margin-bottom: 1rem;
            color: #333;
        }
        
        .testimonial-author {
            font-weight: bold;
            color: #28a745;
        }
        
        .testimonial-company {
            color: #666;
            font-size: 0.9rem;
        }
        
        .final-cta {
            background: linear-gradient(135deg, #28a745 0%, #20c997 100%);
            color: white;
            padding: 60px 20px;
            margin: 3rem -1rem -1rem -1rem;
            text-align: center;
            border-radius: 20px 20px 0 0;
        }
        
        .final-cta-title {
            font-size: 2.5rem;
            font-weight: bold;
            margin-bottom: 1rem;
        }
        
        .final-cta-subtitle {
            font-size: 1.2rem;
            margin-bottom: 2rem;
            opacity: 0.9;
        }
        
        .services-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 30px;
            margin: 40px 0;
        }
        
        .highlight-green {
            color: #28a745;
            font-weight: bold;
        }
        
        .highlight-blue {
            color: #007bff;
            font-weight: bold;
        }
    </style>
    """, unsafe_allow_html=True)

    # Hero Section
    st.markdown("""
    <div class="hero-section">
        <div class="main-container">
            <h1 class="hero-title">
                Encuentra la <span class="highlight-green">mejor tarifa</span> de energía en Colombia
            </h1>
            <p class="hero-subtitle">
                Compara comercializadores de energía y encuentra opciones que se adapten a tu consumo. Ahorra dinero y mejora tu servicio energético.
            </p>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Botón CTA principal - MUY GRANDE Y CENTRADO
    st.markdown("""
    <style>
        .mega-cta-container {
            display: flex;
            justify-content: center;
            margin: 3rem 0;
            padding: 2rem;
        }
        
        .mega-cta-button {
            background: linear-gradient(135deg, #28a745 0%, #20c997 100%);
            color: white;
            padding: 25px 60px;
            border: none;
            border-radius: 60px;
            font-size: 1.8rem;
            font-weight: bold;
            cursor: pointer;
            text-decoration: none;
            display: inline-block;
            box-shadow: 0 10px 30px rgba(40, 167, 69, 0.4);
            transition: all 0.3s ease;
            text-align: center;
            min-width: 400px;
            animation: pulse-glow 2s infinite;
        }
        
        .mega-cta-button:hover {
            background: linear-gradient(135deg, #218838 0%, #1e7e34 100%);
            transform: translateY(-3px);
            box-shadow: 0 15px 40px rgba(40, 167, 69, 0.6);
        }
        
        @keyframes pulse-glow {
            0% { box-shadow: 0 10px 30px rgba(40, 167, 69, 0.4); }
            50% { box-shadow: 0 15px 40px rgba(40, 167, 69, 0.7); }
            100% { box-shadow: 0 10px 30px rgba(40, 167, 69, 0.4); }
        }
        
        /* Responsivo */
        @media (max-width: 768px) {
            .mega-cta-button {
                font-size: 1.4rem;
                padding: 20px 40px;
                min-width: 300px;
            }
        }
    </style>
    """, unsafe_allow_html=True)
    
    # Crear el botón mega centrado
    col1, col2, col3 = st.columns([0.5, 3, 0.5])
    with col2:
        st.markdown('<div class="mega-cta-container">', unsafe_allow_html=True)
        if st.button("🚀 Quiero un nuevo comercializador de energía", 
                    key="main_cta", 
                    help="Comenzar comparación ahora",
                    use_container_width=True):
            st.session_state.page = "formulario"
            st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)

    # Stats Section
    st.markdown("""
    <div class="stats-section">
        <div class="stat-number">+1.000.000</div>
        <div class="stat-text">de usuarios han optimizado su servicio de energía al cambiar de comercializador</div>
    </div>
    """, unsafe_allow_html=True)

    # Services Icons
    st.markdown('<div style="margin: 50px 0;">', unsafe_allow_html=True)
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown("""
        <div style="text-align: center;">
            <div style="font-size: 3rem; margin-bottom: 10px;">🏠</div>
            <div style="font-weight: bold;">Hotelería</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div style="text-align: center;">
            <div style="font-size: 3rem; margin-bottom: 10px;">🏪</div>
            <div style="font-weight: bold;">Retail</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div style="text-align: center;">
            <div style="font-size: 3rem; margin-bottom: 10px;">🏭</div>
            <div style="font-weight: bold;">Manufactura</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        st.markdown("""
        <div style="text-align: center;">
            <div style="font-size: 3rem; margin-bottom: 10px;">🌾</div>
            <div style="font-weight: bold;">Agro</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

    # Why Change Section
    st.markdown("""
    <div class="features-section">
        <h2 class="section-title">¿Por qué cambiar de comercializador?</h2>
        <p class="section-subtitle">
            Descubre las ventajas de elegir el comercializador de energía que mejor se adapte a tus necesidades
        </p>
    </div>
    """, unsafe_allow_html=True)

    # Features Grid
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown("""
        <div class="feature-card">
            <div class="feature-icon">💰</div>
            <div class="feature-title">Mejores tarifas</div>
            <div class="feature-description">
                Encuentra opciones más económicas que se adapten a tu consumo energético
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="feature-card">
            <div class="feature-icon">🎧</div>
            <div class="feature-title">Atención al cliente</div>
            <div class="feature-description">
                Comercializadores con servicio al cliente especializado y disponible
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="feature-card">
            <div class="feature-icon">⚙️</div>
            <div class="feature-title">Tecnología en gestión</div>
            <div class="feature-description">
                Plataformas modernas para gestionar tu servicio de manera eficiente
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        st.markdown("""
        <div class="feature-card">
            <div class="feature-icon">📱</div>
            <div class="feature-title">Servicios complementarios</div>
            <div class="feature-description">
                Apps móviles, alertas automáticas, autogestión y herramientas digitales
            </div>
        </div>
        """, unsafe_allow_html=True)

    # Testimonials Section
    st.markdown("""
    <div class="testimonials-section">
        <h2 class="section-title">Lo que dicen nuestros usuarios</h2>
        <p class="section-subtitle">
            Miles de personas y empresas ya han mejorado su servicio energético
        </p>
    </div>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="testimonial-card">
            <div style="font-size: 2rem; color: #28a745; margin-bottom: 10px;">⭐⭐⭐⭐⭐</div>
            <div class="testimonial-text">
                "No sabía que me podía cambiar de comercializador, fue mi mejor decisión."
            </div>
            <div class="testimonial-author">Laura</div>
            <div class="testimonial-company">Medellín</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="testimonial-card">
            <div style="font-size: 2rem; color: #28a745; margin-bottom: 10px;">⭐⭐⭐⭐⭐</div>
            <div class="testimonial-text">
                "En menos de una semana ya tenía una tarifa mejor para mi empresa."
            </div>
            <div class="testimonial-author">Andrés</div>
            <div class="testimonial-company">Empresa Textil</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="testimonial-card">
            <div style="font-size: 2rem; color: #28a745; margin-bottom: 10px;">⭐⭐⭐⭐⭐</div>
            <div class="testimonial-text">
                "Comparar fue fácil y los resultados me sorprendieron."
            </div>
            <div class="testimonial-author">Carolina</div>
            <div class="testimonial-company">Bogotá</div>
        </div>
        """, unsafe_allow_html=True)

    # Final CTA
    st.markdown("""
    <div class="final-cta">
        <h2 class="final-cta-title">¿Listo para encontrar tu mejor opción?</h2>
        <p class="final-cta-subtitle">
            Únete a más de 1 millón de usuarios que ya han optimizado su servicio energético
        </p>
    </div>
    """, unsafe_allow_html=True)

    # Botón CTA final
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("🚀 Cámbiate de comercializador", key="final_cta", help="Comenzar comparación"):
            st.session_state.page = "formulario"
            st.rerun()

    # Footer
    st.markdown("""
    <div style="margin-top: 60px; padding: 40px 0; border-top: 1px solid #eee;">
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 30px;">
            <div>
                <h4 style="color: #333; margin-bottom: 15px;">🔥 Compata</h4>
                <p style="color: #666; font-size: 0.9rem;">
                    El comparador líder de tarifas de energía en Colombia. Encuentra la mejor opción para tu hogar o empresa.
                </p>
            </div>
            <div>
                <h4 style="color: #333; margin-bottom: 15px;">Servicios</h4>
                <ul style="list-style: none; padding: 0; color: #666; font-size: 0.9rem;">
                    <li style="margin-bottom: 8px;">Comparación de tarifas</li>
                    <li style="margin-bottom: 8px;">Asesoría energética</li>
                    <li style="margin-bottom: 8px;">Gestión de cambio</li>
                </ul>
            </div>
            <div>
                <h4 style="color: #333; margin-bottom: 15px;">Ayuda</h4>
                <ul style="list-style: none; padding: 0; color: #666; font-size: 0.9rem;">
                    <li style="margin-bottom: 8px;">¿Cómo funciona?</li>
                    <li style="margin-bottom: 8px;">Preguntas frecuentes</li>
                    <li style="margin-bottom: 8px;">Contacto</li>
                </ul>
            </div>
            <div>
                <h4 style="color: #333; margin-bottom: 15px;">Legal</h4>
                <ul style="list-style: none; padding: 0; color: #666; font-size: 0.9rem;">
                    <li style="margin-bottom: 8px;">Términos y condiciones</li>
                    <li style="margin-bottom: 8px;">Política de privacidad</li>
                    <li style="margin-bottom: 8px;">Tratamiento de datos</li>
                </ul>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)