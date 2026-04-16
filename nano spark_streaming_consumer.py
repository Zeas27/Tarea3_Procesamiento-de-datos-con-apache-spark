from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json, col, avg, min, max, to_date
from pyspark.sql.types import StructType, StructField, StringType, DoubleType

# Crear sesión Spark
spark = SparkSession.builder \
    .appName("TRMStreamingFix") \
    .getOrCreate()

spark.sparkContext.setLogLevel("WARN")

# Esquema correcto
schema = StructType([
    StructField("vigencia", StringType(), True),
    StructField("valor", DoubleType(), True)
])

# Leer desde Kafka
df = spark.readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "localhost:9092") \
    .option("subscribe", "trm_data") \
    .option("startingOffsets", "earliest") \
    .load()

# Convertir JSON
parsed_df = df.selectExpr("CAST(value AS STRING)") \
    .select(from_json(col("value"), schema).alias("data")) \
    .select("data.*")

#  USAR to_date (NO to_timestamp)
parsed_df = parsed_df.withColumn(
    "fecha",
    to_date(col("vigencia"), "yyyy-MM-dd")
)

# Filtrar datos válidos
clean_df = parsed_df.filter(
    col("fecha").isNotNull() & col("valor").isNotNull()
)

#  AGREGACIÓN SIMPLE (SIN WINDOW para evitar errores)
agg_df = clean_df.groupBy("fecha").agg(
    avg("valor").alias("trm_promedio"),
    min("valor").alias("trm_min"),
    max("valor").alias("trm_max")
)

# Escribir en consola
query = agg_df.writeStream \
    .outputMode("complete") \
    .format("console") \
    .option("truncate", False) \
    .option("checkpointLocation", "/tmp/trm_checkpoint") \
    .start()

query.awaitTermination()