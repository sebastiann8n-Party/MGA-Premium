from apa.apa_citas import ApaCitas, Cita, Autor
from mga_identificacion import MgaIdentificacion, Problema, Poblacion, Objetivo, Alternativa, Participante
from mga_preparacion import MgaPreparacion, DatosMercado, ProductoMercado, EspecificacionTecnica, Ubicacion, CadenaValor, CadenaValorItem, Riesgo, Beneficio
from mga_evaluacion import MgaEvaluacion, FlujoCajaDetail, IndicadorManual
from mga_programacion import MgaProgramacion, Indicador, FuenteFinanciacionDetail, CronogramaActividad
from document_factory import ProjectAssembler

def generar_proyecto_cites():
    print("Iniciando Generación de Proyecto CITES (MGA Web)...")

    # --- MÓDULO 1: IDENTIFICACIÓN ---
    
    # 1.1 Problema
    problema = Problema(
        descripcion="Limitada capacidad de anticipacion, supervision y respuesta ante riesgos de desastres en territorios vulnerables de Colombia...",
        causas_directas=[
            "Debilidad en la supervision tecnica de obras de mitigacion",
            "Carencia de enfoque diferencial en sistemas de alerta temprana",
            "Obsolescencia tecnologica en prediccion hidrometeorologica"
        ],
        causas_indirectas=[
            "Falta de veeduria contractual especializada",
            "Ausencia de integracion de saberes ancestrales",
            "Dependencia de tecnologias extranjeras"
        ],
        efectos_directos=[
            "Perdida de vidas humanas por eventos previsibles",
            "Detrimento patrimonial por inversiones ineficientes",
            "Dependencia tecnologica extranjera"
        ],
        efectos_indirectos=[
            "Aumento de victimas mortales",
            "Perdidas economicas en sector agropecuario",
            "Desconfianza ciudadana"
        ],
        magnitud_actual="Costo anual atencion desastres: $850,000 millones. Municipios con alertas: 13%."
    )

    # 1.2 Población
    poblacion = Poblacion(
        ubicacion="Nacional (Prioridad: Putumayo, Chocó, Caribe)",
        cantidad=5000000,
        caracteristicas=[
            "Indígenas: 850,000",
            "Afrodescendientes: 1,200,000",
            "Pobreza > 40% en zonas prioritarias"
        ],
        fuente_info="DANE 2024, registros UNGRD"
    )

    # 1.3 Objetivos (Árbol Completo)
    objetivos = Objetivo(
        general="Fortalecer la capacidad nacional de anticipacion, supervision y respuesta ante riesgos de desastres en territorios vulnerables de Colombia mediante la implementacion de un Centro de Inteligencia Territorial con tecnologias LIDAR, IA y enfoque diferencial.",
        especificos=[
            "1. Implementar sistema de supervision contractual de obras de mitigacion.",
            "2. Desarrollar sistema de alertas tempranas con enfoque diferencial.",
            "3. Implementar plataforma predictiva con tecnologias LIDAR e IA.",
            "- Establecer veeduria contractual especializada.",
            "- Integrar saberes ancestrales en sistemas de alerta.",
            "- Desplegar red de 150 sensores telemetricos.",
            "- Formar 1,123 jovenes en gestion del riesgo.",
            "- Desarrollar modelos de IA para prediccion."
        ],
        fines_directos=[
            "Reducir victimas mortales por eventos previsibles",
            "Minimizar detrimento patrimonial por inversiones eficientes",
            "Alcanzar soberania tecnologica en gestion del riesgo"
        ],
        fines_indirectos=[
            "Disminucion de victimas mortales por desastres naturales",
            "Proteccion del sector agropecuario",
            "Fortalecimiento de confianza ciudadana",
            "Equidad en proteccion de comunidades etnicas"
        ],
        indicador="Porcentaje de precision en prediccion de eventos con 48h de anticipacion. Meta: 80%. Fuente: Registros CITES validados por IDEAM."
    )

    mod_id = MgaIdentificacion(
        nombre_proyecto="Centro de Inteligencia Territorial y Supervision de Riesgos - CITES",
        bpin="Por asignar",
        localizacion="Colón, Putumayo - Cobertura Nacional",
        problema=problema,
        poblacion=poblacion,
        objetivos=objetivos
    )

    # Políticas
    mod_id.set_contribucion_politica([
        "PND 2022-2026: Colombia Potencia Mundial de la Vida - Estrategia IA y Soberanía.",
        "PNGRD 2024-2028: Prevención y reducción del riesgo.",
        "Planes Territoriales: Putumayo, Chocó, Córdoba (Gestión del Riesgo)."
    ])

    # Participantes
    mod_id.agregar_participante(Participante("Comunidades Indígenas", "Beneficiario", "Alertas en lenguas nativas", "Consulta previa"))
    mod_id.agregar_participante(Participante("UNGRD", "Cooperante", "Fortalecimiento SNGRD", "Cofinanciación"))
    mod_id.agregar_participante(Participante("Actores políticos locales", "Oponente (Posible)", "Status quo contractual", "Socialización"))

    # Alternativas
    alt1 = Alternativa("CITES - Centro Completo", "Implementación completa Putumayo, LIDAR/IA.", True, "Combina tecnología de punta, soberanía y alto impacto social.")
    alt2 = Alternativa("Ampliación UNGRD", "Más personal y equipos básicos.", False)
    alt3 = Alternativa("Centros Regionales", "5 centros pequeños sin tecnología avanzada.", False)
    
    mod_id.agregar_alternativa(alt1)
    mod_id.agregar_alternativa(alt2)
    mod_id.agregar_alternativa(alt3)

    # --- MÓDULO 2: PREPARACIÓN ---
    mod_prep = MgaPreparacion()
    
    # 2.1 Mercado
    # Producto 1
    p1_mercado = ProductoMercado("Monitoreo hidrometeorológico", [
        DatosMercado("2020-2024", 150, 1123, 973, "Histórico", "Municipios sin cobertura"),
        DatosMercado("2026", 150, 1123, 973, "Sin Proyecto", "Sin CITES"),
        DatosMercado("2026", 1123, 1123, 0, "Con CITES", "Cobertura Total"),
        DatosMercado("2030", 1123, 1123, 0, "Con CITES", "Sostenibilidad")
    ])
    mod_prep.agregar_producto_mercado(p1_mercado)
    mod_prep.analisis_deficit = "El déficit total es del 100% para servicios especializados. CITES atenderá el 100% de demanda de monitoreo."

    # 2.2 Técnico
    mod_prep.agregar_especificacion(EspecificacionTecnica("Observatorio ONGRD", "Estructura tripartita con cobertura nacional", [
        "Plataforma cloud híbrida", "APIs abiertas SNGRD", "Procesamiento real-time", "Interfaz multilingüe"
    ]))
    mod_prep.agregar_especificacion(EspecificacionTecnica("Sistema LIDAR", "Escaneo topográfico de alta precisión", [
        "2 sistemas (terrestre/aéreo)", "Alcance 1km", "Precisión 5cm", "Vida útil 10 años"
    ]))
    mod_prep.agregar_especificacion(EspecificacionTecnica("Red Sensores", "Monitoreo real-time", [
        "150 sensores IoT", "Transmisión Satelital/4G", "Precisión ±0.1mm", "Vida útil 8 años"
    ]))

    # 2.3 Localización
    mod_prep.set_ubicacion(Ubicacion(
        "Putumayo", "Colón", "Distrito de Drenaje del Alto Putumayo",
        ["Laboratorio Hídrico Natural", "Alta pluviosidad (8,000mm)", "Vulnerabilidad demostrada", "Cumplimiento descentralización"],
        {"Putumayo": 50, "Chocó": 30, "Costa Pacífica": 25, "Costa Caribe": 25, "Amazonía": 10}
    ))

    # 2.4 Cadena de Valor (Ejemplo resumido de la 1 y 3)
    cv1 = CadenaValor("Observatorio ONGRD", [
        CadenaValorItem("Adecuación Infraestructura", "Materiales", "Materiales", "Inversión", 5000),
        CadenaValorItem("Desarrollo Software", "Servicios tec", "Servicios", "Inversión", 2000),
        CadenaValorItem("Operación", "Servicios", "Servicios", "Operación", 800, "/año")
    ])
    mod_prep.agregar_cadena_valor(cv1)
    
    cv3 = CadenaValor("Red de Sensores", [
        CadenaValorItem("Adquisición Sensores", "Equipos IoT", "Maquinaria", "Inversión", 4500),
        CadenaValorItem("Instalación", "Mano de obra", "MO", "Inversión", 1500),
        CadenaValorItem("Conectividad", "Satelital", "Servicios", "Operación", 300, "/año")
    ])
    mod_prep.agregar_cadena_valor(cv3)

    # 2.5 Riesgos
    mod_prep.agregar_riesgo(Riesgo("Alto", "Técnico", "Falla sensores clima", "Media", "Alto", "Redundancia 20%, Mto preventivo"))
    mod_prep.agregar_riesgo(Riesgo("Alto", "Institucional", "Resistencia política", "Media", "Alto", "Socialización temprana"))
    mod_prep.agregar_riesgo(Riesgo("Medio", "Financiero", "Incumplimiento cofinanciación", "Baja", "Alto", "Diversificación fuentes"))

    # 2.6 Beneficios
    mod_prep.agregar_beneficio(Beneficio("Reducción víctimas mortales", "Social", "Vidas salvadas", 
        "Reducción por alertas 48h anticipación", 
        [{"Año": "2026", "Vidas": "50", "Valor": "$100,000 M"}, {"Año": "2027", "Vidas": "100", "Valor": "$200,000 M"}]
    ))
    mod_prep.agregar_beneficio(Beneficio("Ahorro supervisión obras", "Económico", "Contratos auditados", 
        "Reducción 20% detrimento patrimonial", 
        [{"Año": "2026", "Cant": "20", "Valor": "$10,000 M"}, {"Año": "2027", "Cant": "50", "Valor": "$25,000 M"}]
    ))

    # --- MÓDULO 3: EVALUACIÓN ---
    mod_eval = MgaEvaluacion(tasa_social_descuento=0.12)
    
    # Flujos Detallados (Millones)
    mod_eval.agregar_flujo_detalle(0, -44000, 0, 0, -44000)
    mod_eval.agregar_flujo_detalle(1, -7000, -2980, 860000, 850020)
    mod_eval.agregar_flujo_detalle(2, -7000, -2980, 1475000, 1465020)
    mod_eval.agregar_flujo_detalle(3, -7000, -2980, 2100000, 2090020)
    mod_eval.agregar_flujo_detalle(4, -7000, -2980, 2975000, 2965020)
    
    # Indicadores
    mod_eval.agregar_indicador("VPN (Financiero)", "$52,450 Millones", "Positivo - Genera valor")
    mod_eval.agregar_indicador("TIR (Financiera)", "28.5%", "Superior a TSD (12%) - Rentable")
    mod_eval.agregar_indicador("Relación B/C", "2.19:1", "Mayor a 1 - Beneficios > Costos")
    mod_eval.agregar_indicador("VPN Económico", "$142,850 Millones", "Positivo - Alto valor social")
    mod_eval.agregar_indicador("TIR Económica", "42.3%", "Muy rentable socialmente")
    mod_eval.agregar_indicador("Relación B/C Económica", "4.24:1", "Beneficios sociales superan costos ampliamente")
    
    mod_eval.set_analisis("El proyecto CITES presenta indicadores financieros y económicos favorables que demuestran su viabilidad. El VPN positivo de $52,450 millones indica valor sobre el costo de oportunidad. La TIR del 28.5% supera la TSD del 12%. Los indicadores económicos (VPN Eco $142,850M) reflejan el alto impacto social.")
    
    mod_eval.set_decision("VIABLE - El proyecto CITES es viable técnicamente, económicamente, financieramente y socialmente. Se recomienda su aprobación para ingreso al BPIN.")
    
    # --- MÓDULO 4: PROGRAMACIÓN ---
    mod_prog = MgaProgramacion()
    
    # Cap 1: Indicadores Producto
    mod_prog.agregar_indicador_producto(Indicador("Observatorio ONGRD implementado", "Unidad", "1", "Informe técnico", "Acta recibo"))
    mod_prog.agregar_indicador_producto(Indicador("Sensores telemétricos instalados", "Unidad", "150", "Informe técnico", "Registros instalación"))
    mod_prog.agregar_indicador_producto(Indicador("Municipios con cobertura", "Municipio", "1,123", "Informe técnico", "Reportes cobertura"))
    mod_prog.agregar_indicador_producto(Indicador("Jóvenes formados Red Nacional", "Persona", "1,123", "Certificado", "Certificados UNIPUTUMAYO"))
    mod_prog.agregar_indicador_producto(Indicador("Contratos auditados", "Porcentaje", "100%", "Informe técnico", "Informes veeduría"))
    mod_prog.agregar_indicador_producto(Indicador("Comunidades con alertas diferenciales", "Comunidad", "500", "Informe técnico", "Registros activación"))
    mod_prog.agregar_indicador_producto(Indicador("Eventos predichos 48h anticipación", "Porcentaje", "80%", "Informe técnico", "Validación IDEAM"))
    mod_prog.agregar_indicador_producto(Indicador("Sistema LIDAR operativo", "Unidad", "2", "Informe técnico", "Certificados calibración"))

    # Cap 2: Indicadores Gestión
    mod_prog.agregar_indicador_gestion(Indicador("Personal técnico contratado", "Persona", "36", "Doc oficial", "Contratos laborales"))
    mod_prog.agregar_indicador_gestion(Indicador("Convenios interinst. firmados", "Convenio", "5", "Doc oficial", "Convenios firmados"))
    mod_prog.agregar_indicador_gestion(Indicador("Consultas previas adelantadas", "Proceso", "3", "Informe técnico", "Actas consulta"))
    mod_prog.agregar_indicador_gestion(Indicador("Capacitaciones personal", "Capacitación", "24", "Certificado", "Certif. formación"))
    mod_prog.agregar_indicador_gestion(Indicador("Informes gestión presentados", "Informe", "16", "Informe técnico", "Informes trimestrales"))
    mod_prog.agregar_indicador_gestion(Indicador("Auditorías internas realizadas", "Auditoría", "4", "Informe técnico", "Informes auditoría"))
    
    # Cap 3: Financiación
    mod_prog.agregar_fuente(FuenteFinanciacionDetail("Inversion", "Nacion", "Min. Igualdad y Equidad", "Aporte fiscal", 15000, "2026-2027"))
    mod_prog.agregar_fuente(FuenteFinanciacionDetail("Inversion", "Nacion", "MinCiencias - Fondo CTI", "Aporte fiscal", 12000, "2026-2028"))
    mod_prog.agregar_fuente(FuenteFinanciacionDetail("Inversion", "Nacion", "Regalías OCAD Paz", "Regalías", 10000, "2026-2029"))
    mod_prog.agregar_fuente(FuenteFinanciacionDetail("Inversion", "Nacion", "UNGRD", "Cofinanciación", 5000, "2026-2027"))
    mod_prog.agregar_fuente(FuenteFinanciacionDetail("Inversion", "Internacional", "Cooperación Internacional", "Donación", 2000, "2026-2030"))
    mod_prog.agregar_fuente(FuenteFinanciacionDetail("Operacion", "Nacion", "Diversas fuentes", "Aporte fiscal", 2980, "2027-2030 (Anual)"))
    
    mod_prog.set_cierre_financiero("44,000 millones COP", "2,980 millones COP", "10 años (2026-2036)")
    
    # Cap 4: Resumen
    mod_prog.agregar_supuesto("Continuidad política en gestión del riesgo")
    mod_prog.agregar_supuesto("Disponibilidad fuentes financiación")
    mod_prog.agregar_supuesto("Cooperación entidades territoriales")
    mod_prog.agregar_supuesto("Disponibilidad tecnológica LIDAR/Sensores")
    mod_prog.agregar_supuesto("Cobertura celular/satelital en zonas")
    mod_prog.agregar_supuesto("Interés jóvenes Red Nacional")
    mod_prog.agregar_supuesto("Autorización comunidades indígenas")
    mod_prog.agregar_supuesto("Continuidad académica UNIPUTUMAYO")
    
    # Cronograma
    mod_prog.agregar_actividad_cronograma(CronogramaActividad("PROCESO PRECONTRACTUAL", "X", "", "", "", ""))
    mod_prog.agregar_actividad_cronograma(CronogramaActividad("PROCESO CONTRACTUAL", "", "X", "", "", ""))
    mod_prog.agregar_actividad_cronograma(CronogramaActividad("FASE 1: INFRAESTRUCTURA (Sede, Equipos, Personal)", "", "X", "X", "", ""))
    mod_prog.agregar_actividad_cronograma(CronogramaActividad("FASE 2: TECNOLOGÍA (LIDAR, Sensores, IA)", "", "", "X", "X", ""))
    mod_prog.agregar_actividad_cronograma(CronogramaActividad("FASE 3: RED JÓVENES (Convocatoria, Formación)", "", "", "", "X", "X"))
    
    mod_prog.agregar_item_resumen("Nombre Proyecto", "Centro de Inteligencia Territorial y Supervisión de Riesgos - CITES")
    mod_prog.agregar_item_resumen("Código BPIN", "Por asignar")
    mod_prog.agregar_item_resumen("Entidad Ejecutora", "Por definir (MinIgualdad / UNGRD)")
    mod_prog.agregar_item_resumen("Sector", "Gestión del Riesgo de Desastres")
    mod_prog.agregar_item_resumen("Localización", "Colón, Putumayo - Cobertura Nacional")
    mod_prog.agregar_item_resumen("Población Objetivo", "5,000,000 habitantes")
    mod_prog.agregar_item_resumen("Inversión Total", "$44,000 millones COP")
    mod_prog.agregar_item_resumen("Horizonte Ev.", "10 años")
    mod_prog.agregar_item_resumen("VPN", "$52,450 millones")
    mod_prog.agregar_item_resumen("TIR", "28.5%")

    mod_prog.set_firma("_________________________", "______________________", "Director Ejecutivo CITES", "Por definir", "Febrero 2026")

    # --- ENSAMBLE ---
    assembler = ProjectAssembler("Documento_Tecnico_CITES_Completo.docx")
    assembler.registrar_modulo(mod_id)
    assembler.registrar_modulo(mod_prep)
    assembler.registrar_modulo(mod_eval)
    assembler.registrar_modulo(mod_prog)
    
    assembler.construir()

if __name__ == "__main__":
    generar_proyecto_cites()
