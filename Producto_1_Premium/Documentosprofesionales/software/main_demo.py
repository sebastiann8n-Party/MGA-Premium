from apa.apa_citas import ApaCitas, Cita, Autor
from mga_identificacion import MgaIdentificacion, Problema, Poblacion
from mga_preparacion import MgaPreparacion, Insumo
from mga_evaluacion import MgaEvaluacion, FlujoCaja
from mga_programacion import MgaProgramacion, FuenteFinanciacion
from document_factory import ProjectAssembler

def generar_documento_mga_premium():
    """Simula la entrada de datos del Chat y genera el documento."""
    
    print("Iniciando Fábrica de Documentos MGA Premium...")

    # 1. Configuración de Datos (Lo que vendría del Chat)
    problema = Problema(
        descripcion="Baja productividad en el sector agroindustrial debido a falta de tecnificación",
        causas=["Maquinaria obsoleta", "Falta de capacitación"],
        efectos=["Bajos ingresos", "Desempleo rural"]
    )
    poblacion = Poblacion(ubicacion="Córdoba", cantidad=50000, caracteristicas=["Rural", "Agricultores"])
    
    # 2. Módulos
    mod_id = MgaIdentificacion("Tecnificación Agroindustrial Córdoba 2026", problema, poblacion)
    
    mod_prep = MgaPreparacion()
    mod_prep.set_analisis_mercado("Existe una demanda insatisfecha de productos procesados en la región Caribe de 500 toneladas anuales.")
    mod_prep.agregar_insumo(Insumo("Maquinaria Industrial", "Unidad", 2, 500000000))
    mod_prep.agregar_insumo(Insumo("Capacitación", "Sesiones", 10, 5000000))

    mod_eval = MgaEvaluacion(tasa_descuento=0.12)
    # Flujos simulados: Inversión año 0, Beneficios años 1-5
    mod_eval.agregar_flujo(FlujoCaja(0, inversion=1050000000, costos_operacion=0, beneficios=0))
    for i in range(1, 6):
        mod_eval.agregar_flujo(FlujoCaja(i, inversion=0, costos_operacion=100000000, beneficios=450000000))

    mod_prog = MgaProgramacion()
    mod_prog.agregar_fuente(FuenteFinanciacion("SGR - Regalías", 800000000, "Inversión"))
    mod_prog.agregar_fuente(FuenteFinanciacion("Alcaldía", 250000000, "Cofinanciación"))
    mod_prog.agregar_hito("Mes 1: Licitación")
    mod_prog.agregar_hito("Mes 3: Instalación de Maquinaria")

    # 3. Ensamble
    assembler = ProjectAssembler("Proyecto_MGA_Premium_Generado.docx")
    assembler.registrar_modulo(mod_id)
    assembler.registrar_modulo(mod_prep)
    assembler.registrar_modulo(mod_eval)
    assembler.registrar_modulo(mod_prog)
    
    assembler.construir()
    
    # 4. Cita APA de ejemplo print
    autor = Autor("Porter", "M.")
    cita = Cita([autor], "2024", pagina="45")
    print(f"\nEjemplo Cita APA Generada internamente: {ApaCitas.generar_parentetica(cita)}")

if __name__ == "__main__":
    generar_documento_mga_premium()
