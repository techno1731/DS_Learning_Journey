#!/usr/bin/env spark-shell

import org.apache.spark.sql.{ SparkSession }

case class Stock(symbol: String, data: String, price: Double)


Object RDDApp {
  val spark = SparkSession.builder()
    .appName("RDD App")
    .master("local[2]")
    .getOrCreate()
    def main(args: Array[String]): Unit = {
      val sc = spark.sparkContext
      sc.setLogLevel("ERROR")

      //case class Stock(symbol: String, data: String, price: Double)
      val stocksRDD = sc.textFile("data/stocks.csv")
        .map(linea => linea.split(","))
        .filter(registro => registro(0).toUpperCase() == registro(0))
        .map(registro => Stock(registro(0),registro(1),registro(2).toDouble))

        //control resultado
      stocksRDD.take(10).foreach(println)
      
      import spark.implicits._
      
      val stockDF = stocksRDD.toDF()
      
      stockDF.show(10)
      
      stockDF.select("symbol")
        .where($"price" > 50.0)
        .show(10,false)

      stockDF.createOrReplaceTempView("stocks")
      spark.sql("SELECT * FROM stocks").show(40, false)
      
      stockDF.rdd.take(10).foreach(println)
      
      //version
      val stockDFv2 = spark.read
        .option("header","true")
        .option("inferSchema","true")
        .csv("data/stocks.csv")

        //conversion a DS
      val stocksDS = stockDFv2.as[Stock]
      stocksDS.filter(stock => stock.price > 45.5)

} 
}

