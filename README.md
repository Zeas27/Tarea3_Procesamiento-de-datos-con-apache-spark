# Tarea3_Procesamiento-de-datos-con-apache-spark
Este proyecto implementa un proceso de análisis de datos en tiempo real enfocado en la Tasa Representativa del Mercado (TRM) en Colombia, con el objetivo de monitorear su comportamiento y generar información útil para la toma de decisiones.

La solución se basa en una arquitectura de streaming utilizando Apache Kafka como sistema de mensajería y Apache Spark Structured Streaming como motor de procesamiento distribuido. Los datos son obtenidos desde una API pública de la TRM y enviados continuamente a un tópico de Kafka mediante un productor desarrollado en Python.

Posteriormente, un consumidor implementado con Spark Streaming procesa los datos en tiempo real, aplicando transformaciones como parsing de datos JSON, validación de tipos y agregaciones. Este enfoque permite analizar la información de manera continua, identificando patrones y tendencias a medida que los datos son generados.

A diferencia del procesamiento batch, esta solución permite una respuesta inmediata a los cambios en la TRM, lo que resulta especialmente útil en escenarios donde la información actualizada es crítica.

Finalmente, los resultados del procesamiento pueden ser visualizados en consola o integrados con otros sistemas para análisis posteriores, facilitando la toma de decisiones basada en datos en tiempo real.
