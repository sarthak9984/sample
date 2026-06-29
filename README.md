from pyspark.sql import SparkSession, DataFrame
from pyspark.sql.functions import col, trim, min, max, avg, count
from pyspark.sql.types import IntegerType

def load_feedback_data(spark: SparkSession, path: str) -> DataFrame:
    return spark.read.option("header", "true").option("inferSchema", "true").csv(path)

def clean_missing_and_invalid_emails(df: DataFrame) -> DataFrame:
    return df.filter(
        (col("email").isNotNull()) & 
        (trim(col("email")) != "") & 
        (col("email").contains("@"))
    )

def compute_rating_stats(df: DataFrame) -> dict:
    processed_df = df.withColumn("rating", col("rating").cast(IntegerType())).filter(col("rating").isNotNull())
    stats = processed_df.agg(
        min("rating").alias("min_rating"),
        max("rating").alias("max_rating"),
        avg("rating").alias("avg_rating")
    ).collect()
    
    if not stats or stats[0]["min_rating"] is None:
        return {"min_rating": 0, "max_rating": 0, "avg_rating": 0.0}
        
    return {
        "min_rating": int(stats[0]["min_rating"]),
        "max_rating": int(stats[0]["max_rating"]),
        "avg_rating": float(stats[0]["avg_rating"])
    }

def count_ratings(df: DataFrame) -> int:
    return int(df.filter(col("rating").isNotNull()).count())

def most_common_rating(df: DataFrame) -> int:
    processed_df = df.withColumn("rating", col("rating").cast(IntegerType())).filter(
        (col("rating").isNotNull()) & (col("rating").between(1, 5))
    )
    grouped_df = processed_df.groupBy("rating").agg(count("rating").alias("count")).sort(
        col("count").desc(), col("rating").asc()
    )
    result = grouped_df.limit(1).collect()
    return int(result[0]["rating"]) if result else 0
