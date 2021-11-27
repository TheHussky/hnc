#!/bin/bash
 docker-compose exec spark-worker-a ./bin/spark-submit \
                                --master spark://spark-master:7077 \
                                /opt/spark-apps/main.py \
                                1000 \
                                #--pyfiles __ :add Python .zip, .egg or .py files to the search path with --py-files. \
                                #--driver-memory 1G \
                                #--executor-memory 1G \