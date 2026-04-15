# Tarea3_Procesamiento-de-datos-con-apache-spark
Este proyecto implementa un proceso de análisis de datos en batch enfocado en la Tasa Representativa del Mercado (TRM) en Colombia, con el objetivo de comprender su comportamiento a lo largo del tiempo y generar información útil para la toma de decisiones.

La solución se basa en el uso de Apache Spark (PySpark) como motor de procesamiento distribuido, lo que permite manejar grandes volúmenes de datos de manera eficiente. El proceso inicia con la carga de un conjunto de datos históricos de la TRM, el cual contiene registros diarios del valor del dólar en Colombia.

Posteriormente, se realiza una etapa de transformación de datos que incluye limpieza, validación de tipos de datos y estructuración de la información para su análisis. Durante esta fase, se aplican operaciones como filtrado, agregaciones y cálculos estadísticos, permitiendo identificar tendencias y patrones relevantes en la evolución de la TRM.

El procesamiento se ejecuta en modo batch, lo que significa que los datos son procesados en bloques o conjuntos completos en lugar de flujos en tiempo real. Este enfoque es adecuado para el análisis histórico, ya que permite trabajar con grandes volúmenes de información de manera estructurada y reproducible.

Finalmente, los resultados del procesamiento pueden ser visualizados en consola o almacenados para análisis posteriores, facilitando la interpretación de los datos y el soporte en la toma de decisiones económica
