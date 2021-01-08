from pyspark.sql import SparkSession
from pyspark.sql.functions import *

spark = SparkSession.Builder().appName('ventas').getOrCreate()

#sales.csv
sales_df = spark.read.option('inferschema', 'true')\
                     .option('header', 'true')\
                     .csv('data/sales.csv')

resultado = sales_df.groupBy('COUNTRY_CODE')\
        .sum('AMOUNT')\
        .orderBy(desc('sum(AMOUNT)'))

resultado.show
