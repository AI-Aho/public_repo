from pyspark.sql import DataFrame
from pyspark.sql import SparkSession

# Create the Spark session
# Naming the session
# # Make it multiple lines wiht \
spark : SparkSession = SparkSession.builder \
    .appName("example") \
    .config("spark.driver.host", "localhost") \
    .master("local") \
    .getOrCreate()
spark.sparkContext.setLogLevel("ERROR")
spark.conf.set("spark.sql.shuffle.partitions", "5")

df : DataFrame = spark.read \
    .option("header", True) \
    .csv("testusers.csv")

df_users = df.createOrReplaceTempView("users")

def GetAllUsers() -> DataFrame:
    sql = "SELECT * FROM users"
    return spark.sql(sql)

print("All users:")
print(GetAllUsers().show())

def GetAllTitles() -> DataFrame:
    sql = """
    SELECT
      Title,
      COUNT(Title) AS titleCount
    FROM users
    GROUP BY Title
    """
    return spark.sql(sql)

print("All titles:")
print(GetAllTitles().show())
