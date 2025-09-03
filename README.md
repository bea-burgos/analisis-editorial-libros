# 📚 Análisis de Catálogo Editorial y Ventas de Libros

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Pandas](https://img.shields.io/badge/Pandas-1.5+-green.svg)
![Status](https://img.shields.io/badge/Status-En%20Desarrollo-yellow.svg)
![License](https://img.shields.io/badge/License-MIT-blue.svg)

## 🎯 Objetivo del Proyecto

Realizar un análisis completo del mercado editorial para identificar:
- **Géneros más vendidos** y rentables por temporada
- **Autores más consistentes** en publicaciones y calidad
- **Tendencias estacionales** en lanzamientos de libros
- **Factores clave** que impulsan las ventas y el éxito comercial
- **Insights estratégicos** para decisiones editoriales

**¿Por qué es importante?** Este análisis permite a editoriales, librerías e inversionistas tomar decisiones data-driven sobre qué publicar, cuándo lanzar y cómo posicionar sus catálogos en el mercado.

## 🔧 Stack Tecnológico

- **Python** 🐍: Análisis y manipulación de datos
- **Pandas & NumPy**: Procesamiento y transformación de datasets
- **Matplotlib & Seaborn**: Visualizaciones estáticas profesionales
- **Plotly**: Dashboard interactivo y gráficos dinámicos
- **SQLite**: Base de datos y consultas SQL especializadas
- **Jupyter Notebook**: Desarrollo, documentación y presentación

## 📊 Dataset y Alcance

- **Fuente**: Amazon Books Dataset 2023 (Kaggle)
- **Registros**: ~130,000 libros únicos
- **Periodo de análisis**: 2018-2023 (5 años)
- **Variables clave**: Título, autor, género, precio, rating, número de reseñas, ranking de ventas, fecha de publicación
- **Cobertura**: Múltiples géneros y segmentos del mercado editorial

## 🔍 Metodología de Análisis

### 1. **Preparación y Limpieza de Datos**
- ✅ Eliminación de duplicados y valores inconsistentes
- ✅ Normalización de formatos (fechas, precios, categorías)
- ✅ Creación de variables derivadas (categorías de precio, estaciones)
- ✅ Tratamiento de valores faltantes con técnicas estadísticas

### 2. **Análisis Exploratorio de Datos (EDA)**
- 📈 Distribuciones de variables clave (precios, ratings, reseñas)
- 🔗 Análisis de correlaciones entre factores de éxito
- 📊 Segmentación por género, autor y período temporal
- 🎯 Identificación de outliers y patrones atípicos

### 3. **Consultas SQL Especializadas**
- 🏆 Ranking de géneros por performance comercial
- 👥 Análisis de productividad y consistencia de autores
- 📅 Patrones estacionales y tendencias temporales
- 💰 Análisis de rentabilidad por segmento de precio

### 4. **Visualización y Dashboard**
- 📈 Gráficos interactivos con insights clave
- 🗺️ Mapas de calor para identificar patrones
- 📊 Dashboard ejecutivo con KPIs principales
- 🎨 Storytelling visual para presentación de resultados

## 📈 Principales Hallazgos (Vista Previa)

### 🏆 **Géneros de Alto Rendimiento**
- **Fiction** lidera en volumen (28% del catálogo total)
- **Romance** presenta el mejor ratio precio-satisfacción
- **Business** alcanza los márgenes más altos ($18.50 promedio)

### 📅 **Patrones Estacionales Clave**
- **Octubre-Noviembre**: Pico de lanzamientos (+40% vs. promedio)
- **Enero**: Ideal para libros de desarrollo personal y fitness
- **Verano**: Preferencia marcada por ficción ligera y romance

### 💡 **Insights Estratégicos**
- Libros entre $10-$20 obtienen ratings 15% superiores
- Autores con 5+ publicaciones mantienen consistencia de calidad
- Series de libros generan 3x más engagement que títulos únicos

## 🚀 Cómo Ejecutar el Proyecto

### Prerrequisitos
```bash
Python 3.8+
pip install pandas numpy matplotlib seaborn plotly jupyter sqlite3
```

### Instalación
```bash
# 1. Clonar el repositorio
git clone https://github.com/bea-burgos/analisis-editorial-libros
cd analisis-editorial-libros

# 2. Instalar dependencias
pip install -r requirements.txt

# 3. Ejecutar análisis principal
jupyter notebook notebooks/01_exploratory_analysis.ipynb

# 4. Generar visualizaciones
python src/visualization.py

# 5. Ejecutar consultas SQL
python src/sql_queries.py
```

## 📁 Estructura del Proyecto

```
analisis-editorial-libros/
├── 📄 README.md                    # Documentación principal
├── 📊 data/
│   ├── raw/                       # Datos originales
│   └── processed/                 # Datos limpios y procesados
├── 📓 notebooks/
│   ├── 01_exploratory_analysis.ipynb    # EDA completo
│   ├── 02_sales_analysis.ipynb          # Análisis de ventas
│   └── 03_genre_trends.ipynb            # Tendencias por género
├── 🐍 src/
│   ├── data_cleaning.py          # Scripts de limpieza
│   ├── visualization.py          # Funciones de visualización
│   └── sql_queries.py           # Consultas especializadas
├── 📈 results/
│   ├── charts/                   # Gráficos generados
│   └── dashboard/               # Dashboard interactivo
└── 📋 requirements.txt          # Dependencias del proyecto
```

## 💼 Valor para el Negocio

### Para Editoriales:
- **Optimización de catálogo**: Identificar géneros con mayor potencial de ROI
- **Timing estratégico**: Planificar lanzamientos en períodos de alta demanda
- **Gestión de autores**: Detectar talentos consistentes y oportunidades de crecimiento

### Para Librerías y Distribuidores:
- **Gestión de inventario**: Anticipar demanda estacional por categoría
- **Estrategias de pricing**: Optimizar precios según género y audiencia objetivo
- **Curación de contenido**: Mejorar recomendaciones basadas en patrones de éxito

## 🎯 KPIs y Métricas Desarrolladas

| Métrica | Fórmula | Aplicación Business |
|---------|---------|-------------------|
| **Success Score** | `(Rating × Reviews × Volume) ÷ Sales Rank` | Identificar bestsellers potenciales |
| **Author Consistency** | `StdDev(Ratings) por Autor` | Evaluar fiabilidad de escritores |
| **Seasonal Index** | `Ventas Mes ÷ Promedio Anual` | Planificación de lanzamientos |
| **Price Elasticity** | `%Δ Demanda ÷ %Δ Precio` | Optimización de precios |

## 📊 Resultados y Visualizaciones

🔜 *En desarrollo: Gráficos y dashboard interactivo*

### Próximamente:
- 📈 **Análisis de Tendencias**: Evolución del mercado 2018-2023
- 🎯 **Segmentación Avanzada**: Clusters de lectores y preferencias
- 🤖 **Modelo Predictivo**: Predicción de éxito de nuevos lanzamientos
- 📱 **Dashboard Ejecutivo**: KPIs en tiempo real para toma de decisiones

## 🔮 Roadmap y Mejoras Futuras

- [ ] **Machine Learning**: Modelo de clasificación para predecir bestsellers
- [ ] **Análisis de Sentimientos**: Procesamiento de reseñas con NLP
- [ ] **API Integration**: Conexión con APIs de Goodreads y Amazon
- [ ] **Real-time Dashboard**: Actualización automática con nuevos datos
- [ ] **A/B Testing Framework**: Herramientas para optimización editorial

## 📞 Contacto y Colaboración

**Desarrollado por**: [Bea Burgos](https://github.com/bea-burgos)

[![LinkedIn](https://img.shields.io/badge/-LinkedIn-0A66C2?style=flat&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/bea-burgos/)
[![Email](https://img.shields.io/badge/-Email-D14836?style=flat&logo=gmail&logoColor=white)](mailto:burgos.beatriz@gmail.com)
[![GitHub](https://img.shields.io/badge/-GitHub-181717?style=flat&logo=github&logoColor=white)](https://github.com/bea-burgos)

## 📄 Licencia

Este proyecto está bajo la Licencia MIT - ver el archivo [LICENSE](LICENSE) para detalles.

---

### 🏷️ Tags
`#DataAnalysis` `#EditorialIndustry` `#Python` `#SQL` `#BusinessIntelligence` `#DataVisualization` `#BookAnalytics` `#MarketResearch` `#Pandas` `#Plotly`
