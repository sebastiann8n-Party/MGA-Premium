# Skill: Nube de Palabras (WordCloud)

## Misión
Visualizar la **importancia o frecuencia** de palabras en un corpus de texto. Convierte datos cualitativos (comentarios, tweets, reseñas) en una representación visual cuantitativa donde el tamaño de la palabra es proporcional a su ocurrencia.

## Guía de Ejes

### Conceptos Clave
-   **Corpus**: El texto completo a analizar.
-   **Stopwords**: Palabras comunes ("el", "la", "de", "que") que se eliminan por no aportar significado semántico.
-   **Tokenización**: División del texto en palabras individuales.
-   **Máscara (Mask)**: Imagen en blanco y negro que define la forma de la nube.

### ¿Cuándo usarlo?
-   Resumen rápido de temas en encuestas abiertas.
-   Identificar palabras clave en SEO o descripciones de productos.
-   Análisis de sentimiento visual (nube positiva vs negativa).
-   Presentaciones de impacto visual (portadas, diapositivas).

---

## Implementación

### 1. WordCloud (Librería Estándar)
La librería `wordcloud` es la herramienta de facto en Python. Requiere `pip install wordcloud`.

```python
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt

# Texto de ejemplo
text = """
Python es un lenguaje de programación interpretado cuya filosofía hace hincapié en la legibilidad de su código.
Se trata de un lenguaje de programación multiparadigma, ya que soporta parcialmente la orientación a objetos, programación imperativa y, en menor medida, programación funcional.
Es un lenguaje interpretado, dinámico y multiplataforma.
"""

# Configuración de Stopwords (En español hay que definirlas o importarlas)
stopwords = set(STOPWORDS)
stopwords.update(["de", "la", "que", "el", "en", "un", "los", "del", "se", "las", "por", "un", "para", "con", "no", "una", "su", "al", "lo", "como", "más", "pero", "sus", "le", "ya", "o", "porque", "muy", "sin", "sobre", "también", "me", "hasta", "desde", "nos", "durante", "uno", "ni", "contra", "ese", "eso", "mí", "qué", "otro", "él", "cual", "poco", "ella", "estar", "estos", "algunas", "algo", "nosotros", "mi", "mis", "tú", "te", "ti", "tu", "tus", "ellas", "nosotras", "vosostros", "vosostras", "os", "mío", "mía", "míos", "mías", "tuyo", "tuya", "tuyos", "tuyas", "suyo", "suya", "suyos", "suyas", "nuestro", "nuestra", "nuestros", "nuestras", "vuestro", "vuestra", "vuestros", "vuestras", "esos", "esas", "estoy", "estás", "está", "estamos", "estáis", "están", "esté", "estés", "estemos", "estéis", "estén", "estaré", "estarás", "estará", "estaremos", "estaréis", "estarán", "estaría", "estarías", "estaríamos", "estaríais", "estarían", "estaba", "estabas", "estábamos", "estabais", "estaban", "estuve", "estuviste", "estuvo", "estuvimos", "estuvisteis", "estuvieron", "hubiera", "hubieras", "hubiéramos", "hubierais", "hubieran", "hubiese", "hubieses", "hubiésemos", "hubieseis", "hubiesen", "habiendo", "habido", "habida", "habidos", "habidas", "soy", "eres", "es", "somos", "sois", "son", "sea", "seas", "seamos", "seáis", "sean", "seré", "serás", "será", "seremos", "seréis", "serán", "sería", "serías", "seríamos", "seríais", "serían", "era", "eras", "éramos", "erais", "eran", "fui", "fuiste", "fue", "fuimos", "fuisteis", "fueron", "fuera", "fueras", "fuéramos", "fuerais", "fueran", "fuese", "fueses", "fuésemos", "fueseis", "fuesen", "sintiendo", "sentido", "sentida", "sentidos", "sentidas", "siente", "sentid", "tengo", "tienes", "tiene", "tenemos", "tenéis", "tienen", "tenga", "tengas", "tengamos", "tengáis", "tengan", "tendré", "tendrás", "tendrá", "tendremos", "tendréis", "tendrán", "tendría", "tendrías", "tendríamos", "tendríais", "tendr















""", "y"]) 

# Generar Nube
wordcloud = WordCloud(
    width=800,
    height=400,
    background_color='white',
    stopwords=stopwords,
    min_font_size=10
).generate(text)

# Mostrar con Matplotlib
plt.figure(figsize=(10, 5), facecolor=None)
plt.imshow(wordcloud)
plt.axis("off") # Ocultar ejes
plt.tight_layout(pad=0)
plt.show()
```

### 2. Máscara de Imagen (Forma Personalizada)
Puedes hacer que la nube tome la forma de una imagen (silueta en negro sobre fondo blanco).

```python
from PIL import Image
import numpy as np

# Cargar máscara
mask = np.array(Image.open("twitter_mask.png"))

wc = WordCloud(
    background_color="white",
    max_words=200,
    mask=mask,
    stopwords=stopwords,
    contour_width=3,
    contour_color='steelblue'
)
wc.generate(text)
plt.imshow(wc, interpolation='bilinear')
plt.axis("off")
plt.show()
```

---

## Reglas de Diseño

1.  **Limpieza es Crucial**: Una nube llena de "de", "y", "el" no sirve. Dedica tiempo a definir las `stopwords` específicas de tu dominio (ej: en análisis de tweets, quita "https", "co", "rt").
2.  **Color**: Usa colormaps que no sean aleatorios si quieres transmitir algo (ej: rojos para palabras negativas, verdes para positivas si tienes scores).
3.  **No usar para Comparación Precisa**: El tamaño de la palabra es difícil de comparar visualmente si las frecuencias son cercanas. Para eso usa un gráfico de barras horizontal. La nube es para *impacto* y *descubrimiento*, no precisión.
4.  **Orientación**: Evita muchas palabras verticales o diagonales si dificultan la lectura. `prefer_horizontal=0.9` es una buena configuración.

## Origen
Skill desarrollada siguiendo estándares de Nivel 3 (Experto) para visualización de texto no estructurado.
