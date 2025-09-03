# generate_sample_data.py
# Primer script del proyecto de análisis editorial
# Genera datos de ejemplo y crea visualizaciones básicas

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime, timedelta
import random

# Configurar estilo visual
plt.style.use('seaborn-v0_8')
sns.set_palette("husl")

print("📚 GENERADOR DE DATOS EDITORIALES")
print("=" * 50)

def generar_datos_libros():
    """
    Genera dataset de ejemplo con información de libros
    """
    print("🔄 Generando datos de ejemplo...")
    
    # Configurar semilla para reproducibilidad
    random.seed(42)
    np.random.seed(42)
    
    # Definir listas base
    generos = ['Fiction', 'Romance', 'Mystery', 'Sci-Fi', 'Business', 
               'Self-Help', 'Biography', 'Fantasy', 'History', 'Health']
    
    autores = ['Stephen King', 'J.K. Rowling', 'Dan Brown', 'John Grisham',
               'Paulo Coelho', 'Malcolm Gladwell', 'Dale Carnegie', 'Agatha Christie',
               'George R.R. Martin', 'Gillian Flynn', 'James Patterson', 'Nicholas Sparks']
    
    # Número de libros a generar
    num_libros = 1000
    
    # Generar datos realistas
    data = {
        'titulo': [f'Libro Ejemplo {i+1}' for i in range(num_libros)],
        'autor': np.random.choice(autores, num_libros),
        'genero': np.random.choice(generos, num_libros),
        'precio': np.round(np.random.exponential(12, num_libros), 2),
        'rating': np.round(np.random.normal(4.0, 0.8, num_libros), 1),
        'num_reviews': np.random.exponential(300, num_libros).astype(int),
        'paginas': np.random.normal(280, 80, num_libros).astype(int),
        'fecha_publicacion': pd.date_range('2020-01-01', '2024-12-31', periods=num_libros)
    }
    
    # Crear DataFrame
    df = pd.DataFrame(data)
    
    # Limpiar datos (valores realistas)
    df['precio'] = df['precio'].clip(0, 50)  # Precios entre $0-50
    df['rating'] = df['rating'].clip(1, 5)   # Ratings entre 1-5
    df['paginas'] = df['paginas'].clip(50, 800)  # Páginas entre 50-800
    
    print(f"✅ Dataset creado: {len(df)} libros")
    print(f"📅 Período: {df['fecha_publicacion'].min().strftime('%Y-%m-%d')} a {df['fecha_publicacion'].max().strftime('%Y-%m-%d')}")
    print(f"📚 Géneros incluidos: {len(df['genero'].unique())}")
    
    return df

def crear_visualizacion_basica(df):
    """
    Crea gráficos básicos del análisis
    """
    print("\n📊 Generando visualizaciones...")
    
    # Configurar figura con múltiples gráficos
    fig, axes = plt.subplots(2, 2, figsize=(15, 12))
    fig.suptitle('📚 Análisis Básico del Catálogo Editorial', fontsize=16, fontweight='bold')
    
    # Gráfico 1: Distribución por género
    genero_counts = df['genero'].value_counts()
    axes[0, 0].bar(genero_counts.index, genero_counts.values, color='skyblue')
    axes[0, 0].set_title('📖 Libros por Género')
    axes[0, 0].set_xlabel('Género')
    axes[0, 0].set_ylabel('Cantidad de Libros')
    axes[0, 0].tick_params(axis='x', rotation=45)
    
    # Gráfico 2: Distribución de precios
    axes[0, 1].hist(df['precio'], bins=20, color='lightgreen', alpha=0.7)
    axes[0, 1].set_title('💰 Distribución de Precios')
    axes[0, 1].set_xlabel('Precio ($)')
    axes[0, 1].set_ylabel('Frecuencia')
    axes[0, 1].axvline(df['precio'].mean(), color='red', linestyle='--', 
                       label=f'Promedio: ${df["precio"].mean():.2f}')
    axes[0, 1].legend()
    
    # Gráfico 3: Relación Precio vs Rating
    axes[1, 0].scatter(df['precio'], df['rating'], alpha=0.6, color='purple')
    axes[1, 0].set_title('⭐ Precio vs Rating')
    axes[1, 0].set_xlabel('Precio ($)')
    axes[1, 0].set_ylabel('Rating')
    
    # Línea de tendencia
    z = np.polyfit(df['precio'], df['rating'], 1)
    p = np.poly1d(z)
    axes[1, 0].plot(df['precio'], p(df['precio']), "r--", alpha=0.8)
    
    # Gráfico 4: Top 5 autores
    top_autores = df['autor'].value_counts().head(5)
    axes[1, 1].barh(top_autores.index, top_autores.values, color='coral')
    axes[1, 1].set_title('✍️ Top 5 Autores Más Prolíficos')
    axes[1, 1].set_xlabel('Número de Libros')
    
    plt.tight_layout()
    
    # Guardar gráfico (para cuando ejecutes local)
    # plt.savefig('analisis_basico.png', dpi=300, bbox_inches='tight')
    
    print("✅ Visualizaciones creadas exitosamente")
    return fig

def mostrar_estadisticas_basicas(df):
    """
    Muestra estadísticas descriptivas del dataset
    """
    print("\n📈 ESTADÍSTICAS BÁSICAS DEL DATASET")
    print("-" * 40)
    
    print(f"📊 Total de libros: {len(df):,}")
    print(f"📚 Géneros únicos: {df['genero'].nunique()}")
    print(f"✍️ Autores únicos: {df['autor'].nunique()}")
    
    print(f"\n💰 PRECIOS:")
    print(f"   Promedio: ${df['precio'].mean():.2f}")
    print(f"   Mediana: ${df['precio'].median():.2f}")
    print(f"   Rango: ${df['precio'].min():.2f} - ${df['precio'].max():.2f}")
    
    print(f"\n⭐ RATINGS:")
    print(f"   Promedio: {df['rating'].mean():.2f}/5.0")
    print(f"   Mediana: {df['rating'].median():.1f}/5.0")
    
    print(f"\n📝 RESEÑAS:")
    print(f"   Promedio: {df['num_reviews'].mean():.0f} reseñas")
    print(f"   Mediana: {df['num_reviews'].median():.0f} reseñas")
    
    print(f"\n🏆 TOP 3 GÉNEROS MÁS POPULARES:")
    top_generos = df['genero'].value_counts().head(3)
    for i, (genero, cantidad) in enumerate(top_generos.items(), 1):
        print(f"   {i}. {genero}: {cantidad} libros ({cantidad/len(df)*100:.1f}%)")

def main():
    """
    Función principal que ejecuta todo el análisis
    """
    print("🚀 INICIANDO ANÁLISIS DE DATOS EDITORIALES")
    print("=" * 50)
    
    # Paso 1: Generar datos
    df = generar_datos_libros()
    
    # Paso 2: Mostrar estadísticas
    mostrar_estadisticas_basicas(df)
    
    # Paso 3: Crear visualizaciones
    fig = crear_visualizacion_basica(df)
    
    # Paso 4: Mostrar gráficos (si estás ejecutando local)
    # plt.show()
    
    print("\n🎉 ANÁLISIS COMPLETADO EXITOSAMENTE")
    print("📁 Para ver los gráficos, ejecuta este script en tu computadora local")
    print("💡 Próximo paso: Crear notebooks de Jupyter para análisis más detallado")
    
    return df

# Ejecutar si el script se corre directamente
if __name__ == "__main__":
    datos = main()
