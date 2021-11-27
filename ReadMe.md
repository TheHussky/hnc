<br>|
|_app - directory for executables, python files in our case. In docker it's /opt/spark-apps/
|_storage - directory for data, .csv, .json, etc. In docker it's /opt/spark-data
|_Dockerfile - used to create image. Add all possible dependencies to lines 5-6 of this file
|_docker-compose.yml - sets servers configs
|_spark.sh - service env script, used in Dockerrfile only.
|_master.sh, worker_a.sh, worker_b.sh - launch task on instance. execute on master if you don't care<br/>
