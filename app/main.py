import http.server
import socketserver
from pyspark.sql import SparkSession
#TODO: Delete this comment. lines 8&18 are used for monitoring on spark stand.
PORT=8000

if __name__ == "__main__":
    spark=SparkSession\
        .builder\
        .appName("Server")\
        .getOrCreate()

    Handler = http.server.SimpleHTTPRequestHandler

    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print("serving at port", PORT)
        httpd.serve_forever()
    spark.stop()