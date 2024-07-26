#### Poetry Package Manager
pip install poetry 
poetry init 
poetry install
poetry env info 
poetry shell
poetry env list
poetry add request 
poetry remove request 

deactivate

#### Running ElasticSearch
docker run -it \
    --rm \
    --name elasticsearch \
    -p 9200:9200 \
    -p 9300:9300 \
    -m 2GB\
    -e "discovery.type=single-node" \
    -e "xpack.security.enabled=false" \
    docker.elastic.co/elasticsearch/elasticsearch:8.4.3

curl localhost:9200