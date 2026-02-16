import sys
import os

# Ajuste de path para importar módulos hermanos
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from backend.schemas import FullDocumentSchema, DocumentMetadata, ParagraphBlock
from software.renderer import run_pipeline

def generar_demostracion_offline():
    """
    Genera un documento APA 7 perfecto utilizando datos estáticos.
    Demuestra la capacidad del motor 'renderer.py' sin dependencias de IA.
    """
    print("🚀 Iniciando generación de documento en modo LOCAL-ONLY...")

    # 1. Construcción de Datos (Simulando lo que haría la IA, pero manual)
    datos_simulados = FullDocumentSchema(
        metadata=DocumentMetadata(
            title="Implementación de Arquitecturas Local-First en Entornos Corporativos",
            author="Ingeniera Ana Lovelace",
            institution="Instituto Tecnológico de Antigravity",
            date="Febrero 15, 2026"
        ),
        content=[
            ParagraphBlock(role="titulo1", content="Introducción"),
            ParagraphBlock(role="cuerpo", content="La adopción de arquitecturas 'Local-First' marca un cambio de paradigma significativo en el desarrollo de software moderno. A diferencia de los modelos centrados en la nube, donde la lógica reside en servidores remotos, este enfoque prioriza la ejecución en el dispositivo del usuario."),
            ParagraphBlock(role="cuerpo", content="Este documento explora cómo la soberanía de los datos puede coexistir con la automatización inteligente, reduciendo costos operativos y latencia."),
            
            ParagraphBlock(role="titulo1", content="Metodología"),
            ParagraphBlock(role="cuerpo", content="Se realizó un análisis comparativo entre servicios SaaS tradicionales y soluciones híbridas con procesamiento local. Se utilizaron métricas de tiempo de respuesta, consumo de ancho de banda y costos por transacción."),
            
            ParagraphBlock(role="titulo2", content="Configuración del Experimento"),
            ParagraphBlock(role="cuerpo", content="El entorno de prueba consistió en un clúster de nodos Raspberry Pi 5 ejecutando modelos de lenguaje cuantizados, contrastado contra llamadas a API REST estándar. Como señala Knuth (1974), la optimización prematura es la raíz de todos los males, por lo que nos enfocamos primero en la arquitectura."),
            
            ParagraphBlock(role="cita_larga", content="La computación local no es un retroceso, sino una evolución necesaria hacia la resiliencia digital. Cuando eliminamos la dependencia estricta de la conectividad, empoderamos al usuario final para ser dueño de sus herramientas, no solo un arrendatario de servicios. (Torvalds, 2024, p. 45)"),
            
            ParagraphBlock(role="titulo1", content="Resultados y Discusión"),
            ParagraphBlock(role="cuerpo", content="Los resultados indican una reducción del 95% en costos operativos (OPEX) al trasladar la lógica de negocio al borde (Edge). Sin embargo, se observan desafíos en la consistencia de datos distribuidos, un problema clásico en sistemas descentralizados."),
            
            ParagraphBlock(role="titulo1", content="Conclusión"),
            ParagraphBlock(role="cuerpo", content="La arquitectura Local-First es viable y económicamente superior para cargas de trabajo que requieren alta privacidad y baja latencia. Se recomienda su implementación gradual en módulos críticos de negocio.")
        ],
        references=[
            "Knuth, D. E. (1974). Structured Programming with go to Statements. Computing Surveys, 6(4), 261-301.",
            "Torvalds, L. (2024). The Future of Kernel Development. Linux Journal, 15(2), 40-50.",
            "Kleppmann, M. (2017). Designing Data-Intensive Applications. O'Reilly Media."
        ]
    )

    # 2. Ejecución del Pipeline de Renderizado
    # Ruta de salida relativa a este script
    output_path = os.path.join(os.path.dirname(__file__), "..", "salida", "Reporte_Tecnico_APA_Local.docx")
    
    try:
        run_pipeline(datos_simulados, output_path)
        print(f"✅ ÉXITO: Documento generado en:\n   {os.path.abspath(output_path)}")
    except Exception as e:
        print(f"❌ ERROR: Falló la generación del documento.\n   {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    generar_demostracion_offline()
