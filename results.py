import streamlit as st

def show_results():
    # CSS para la página de resultados
    st.markdown("""
    <style>
        .results-container {
            max-width: 1000px;
            margin: 0 auto;
            padding: 2rem;
        }
        
        .results-title {
            font-size: 2.5rem;
            font-weight: bold;
            color: #28a745;
            text-align: center;
            margin-bottom: 1rem;
        }
        
        .results-subtitle {
            font-size: 1.2rem;
            color: #666;
            text-align: center;
            margin-bottom: 3rem;
        }
        
        .provider-card {
            background: white;
            border-radius: 15px;
            padding: 2rem;
            margin-bottom: 2rem;
            box-shadow: 0 5px 15px rgba(0,0,0,0.1);
            border: 2px solid transparent;
            transition: all 0.3s ease;
        }
        
        .provider-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 10px 25px rgba(0,0,0,0.15);
        }
        
        .provider-card.recommended {
            border-color: #28a745;
            background: linear-gradient(135deg, #f8fff8 0%, #e8f5e8 100%);
        }
        
        .provider-name {
            font-size: 1.8rem;
            font-weight: bold;
            color: #333;
            margin-bottom: 1rem;
        }
        
        .provider-name.bia {
            color: #28a745;
        }
        
        .recommended-badge {
            background: #28a745;
            color: white;
            padding: 0.3rem 1rem;
            border-radius: 20px;
            font-size: 0.8rem;
            font-weight: bold;
            display: inline-block;
            margin-bottom: 1rem;
        }
        
        .provider-details {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 1.5rem;
            margin-bottom: 2rem;
        }
        
        .detail-item {
            text-align: center;
        }
        
        .detail-label {
            font-size: 0.9rem;
            color: #666;
            margin-bottom: 0.5rem;
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }
        
        .detail-value {
            font-size: 1.3rem;
            font-weight: bold;
            color: #333;
        }
        
        .price-value {
            font-size: 2rem;
            color: #28a745;
        }
        
        .contact-section {
            display: flex;
            justify-content: space-between;
            align-items: center;
            flex-wrap: wrap;
            gap: 1rem;
            border-top: 1px solid #eee;
            padding-top: 1.5rem;
        }
        
        .provider-info {
            flex: 1;
            min-width: 200px;
        }
        
        .contact-button {
            background: #007bff;
            color: white;
            padding: 12px 24px;
            border: none;
            border-radius: 25px;
            font-weight: bold;
            cursor: pointer;
            transition: all 0.3s ease;
            text-decoration: none;
            display: inline-block;
        }
        
        .contact-button:hover {
            background: #0056b3;
            transform: translateY(-2px);
        }
        
        .contact-button.primary {
            background: #28a745;
        }
        
        .contact-button.primary:hover {
            background: #218838;
        }
        
        .summary-card {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 2rem;
            border-radius: 15px;
            margin-bottom: 3rem;
            text-align: center;
        }
        
        .summary-title {
            font-size: 1.5rem;
            font-weight: bold;
            margin-bottom: 1rem;
        }
        
        .summary-details {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
            gap: 1rem;
            margin-top: 1.5rem;
        }
        
        .summary-item {
            background: rgba(255,255,255,0.1);
            padding: 1rem;
            border-radius: 10px;
        }
        
        .actions-section {
            background: #f8f9fa;
            padding: 2rem;
            border-radius: 15px;
            text-align: center;
            margin-top: 3rem;
        }
        
        .no-results {
            text-align: center;
            padding: 3rem;
            color: #666;
        }
        
        .no-results-icon {
            font-size: 4rem;
            margin-bottom: 1rem;
        }
    </style>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="results-container">
        <h1 class="results-title">¡Encontramos las mejores opciones para ti! 🎉</h1>
        <p class="results-subtitle">
            Estas son las tarifas más competitivas disponibles para tu empresa
        </p>
    </div>
    """, unsafe_allow_html=True)

    # Mostrar resumen de búsqueda
    if 'form_data' in st.session_state and st.session_state.form_data:
        form_data = st.session_state.form_data
        st.markdown(f"""
        <div class="summary-card">
            <div class="summary-title">Resumen de tu búsqueda</div>
            <div class="summary-details">
                <div class="summary-item">
                    <strong>Empresa:</strong><br>{form_data.get('nombre_empresa', 'N/A')}
                </div>
                <div class="summary-item">
                    <strong>Ubicación:</strong><br>{form_data.get('ubicacion', 'N/A')}
                </div>
                <div class="summary-item">
                    <strong>Consumo mensual:</strong><br>${form_data.get('consumo_energia', 0):,} COP
                </div>
                <div class="summary-item">
                    <strong>Nivel de tensión:</strong><br>{form_data.get('nivel_tension', 'N/A')}
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

    # Mostrar resultados
    if st.session_state.providers_data:
        for i, provider in enumerate(st.session_state.providers_data):
            is_bia = provider.get('is_bia', False)
            is_recommended = i == 0 or is_bia
            
            # Crear tarjeta de proveedor usando componentes de Streamlit
            if is_recommended:
                st.success("✨ **Recomendado**")
            
            with st.container():
                # Título del proveedor
                if is_bia:
                    st.markdown(f"### 🏆 **{provider['nombre']}**")
                else:
                    st.markdown(f"### **{provider['nombre']}**")
                
                # Crear columnas para la información
                col1, col2, col3, col4 = st.columns(4)
                
                with col1:
                    st.metric(
                        label="💰 Tarifa por kWh", 
                        value=f"${provider['tarifa']}"
                    )
                
                with col2:
                    st.write("**⚙️ Tecnología**")
                    st.write(provider['tecnologia'])
                
                with col3:
                    st.write("**🎧 Servicio al cliente**")
                    st.write(provider['servicio'])
                
                with col4:
                    st.write("**📍 Ciudad**")
                    st.write(provider.get('ciudad', 'N/A'))
                
                # Información adicional
                st.write("**🔄 Servicios adicionales:**")
                if is_bia:
                    st.write("• Plataforma digital avanzada")
                    st.write("• Asesoría especializada en eficiencia energética")
                    st.write("• Monitoreo en tiempo real")
                    st.write("• Soporte técnico 24/7")
                else:
                    st.write("• Atención al cliente especializada")
                    st.write("• Facturación digital")
                    st.write("• Reportes de consumo")
                
                # Botón de contacto
                col_btn1, col_btn2, col_btn3 = st.columns([1, 2, 1])
                with col_btn2:
                    if st.button(
                        f"📞 Contactar {provider['nombre']}", 
                        key=f"btn_{i}", 
                        use_container_width=True,
                        type="primary" if is_recommended else "secondary"
                    ):
                        st.success(f"¡Excelente elección! Te conectaremos con {provider['nombre']} pronto.")
                        # Aquí podrías agregar lógica para enviar el lead
                
                st.divider()  # Separador entre proveedores
                    # Aquí podrías agregar lógica para enviar el lead a un CRM o sistema de seguimiento

    else:
        # No hay resultados
        st.markdown("""
        <div class="no-results">
            <div class="no-results-icon">🔍</div>
            <h3>No se encontraron resultados</h3>
            <p>No encontramos tarifas disponibles para tu configuración específica.<br>
            Intenta ajustar los parámetros de búsqueda o contáctanos para asistencia personalizada.</p>
        </div>
        """, unsafe_allow_html=True)

    # Sección de acciones
    st.markdown("""
    <div class="actions-section">
        <h3>¿Qué sigue?</h3>
        <p>Nuestro equipo te acompañará en todo el proceso de cambio sin costo adicional</p>
    </div>
    """, unsafe_allow_html=True)

    # Botones de acción
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if st.button("🔄 Hacer nueva búsqueda", use_container_width=True):
            # Limpiar datos y volver al formulario
            st.session_state.form_submitted = False
            st.session_state.providers_data = []
            st.session_state.form_data = {}
            st.session_state.page = "formulario"
            st.rerun()
    
    with col2:
        if st.button("📊 Ver más detalles", use_container_width=True):
            st.info("📋 Pronto podrás ver análisis detallados de consumo y proyecciones de ahorro.")
    
    with col3:
        if st.button("🏠 Volver al inicio", use_container_width=True):
            st.session_state.page = "landing"
            st.rerun()

    # Información adicional
    st.markdown("""
    <div style="margin-top: 3rem; padding: 2rem; background: #f8f9fa; border-radius: 15px;">
        <h4 style="color: #333; margin-bottom: 1rem;">💡 Información importante sobre el cambio</h4>
        <ul style="color: #666; line-height: 1.8;">
            <li><strong>Proceso sin costo:</strong> El cambio de comercializador no tiene ningún costo para ti</li>
            <li><strong>Sin interrupción:</strong> Tu suministro eléctrico continúa normalmente durante el proceso</li>
            <li><strong>Tiempo estimado:</strong> El proceso completo toma entre 15 a 30 días hábiles</li>
            <li><strong>Documentos necesarios:</strong> Solo necesitas tu última factura y documentos de identidad de la empresa</li>
            <li><strong>Soporte continuo:</strong> Te acompañamos durante todo el proceso de cambio</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)