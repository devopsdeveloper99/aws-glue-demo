from awsglue.context import GlueContext
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext

# Initialize Spark and Glue context
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session

print("✅ Hello from AWS Glue 4.0 container!")
print("Spark Version:", spark.version)
print("Successfully executed Glue ETL script!")
