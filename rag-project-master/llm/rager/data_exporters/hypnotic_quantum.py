import numpy as np
import spacy
from elasticsearch import Elasticsearch

nlp = spacy.load('en_core_web_sm')


@data_exporter
def search(*args, **kwargs):
    query = 'Can I join the course if the course already started?'
    
    doc = nlp(query)
    tokens = [token.lemma_ for token in doc]
    
    text = ' '.join(tokens)
    doc = nlp(text)
    query_embedding = np.mean([token.vector for token in doc], axis=0).tolist()
    
    knn_query = {
        "knn": {
            "field": "embedding",
            "query_vector": query_embedding,
            "k": 5,
            "num_candidates": 100,
        },
        "_source":['chunk']
    }

    es_host = 'elasticsearch'
    es_port = 9200
    es_client = Elasticsearch([{'host': es_host, 'port': es_port, "scheme": "http"}])
    
    response = es_client.search(
        index='documents',
        body=knn_query
    )

    print([[hit['_source'] for hit in response['hits']['hits']]])
    return [[hit['_source'] for hit in response['hits']['hits']]]