from pyspark.context import SparkContext
from awsglue.context import GlueContext
from pyspark.sql import Row

# Initialize Spark and Glue context
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session

print("✅ Hello from AWS Glue 4.0 local container!")
print("Spark Version:", spark.version)

# --- Sample data ---
data = [
    Row(id=1, name="Alice", age=30),
    Row(id=2, name="Bob", age=25),
    Row(id=3, name="Charlie", age=35)
]

# Create Spark DataFrame
df = spark.createDataFrame(data)
print("\n📄 Sample DataFrame:")
df.show()

# Transform: filter age > 30
df_filtered = df.filter(df.age > 30)
print("\n🔹 Filtered DataFrame (age > 30):")
df_filtered.show()

# Save locally as CSV (optional)
output_path = "/home/glue_user/workspace/output"
df_filtered.coalesce(1).write.mode("overwrite").csv(output_path)
print(f"\n✅ Filtered data saved locally at {output_path}")
