trap "docker-compose down" SIGINT

pip install -e .

docker-compose up -d

AIRFLOW_HOME="$(pwd)/medicalpublications/pipelines/" airflow standalone
