from elasticsearch import Elasticsearch
from datetime import datetime

host = 'http://127.0.0.1:9200'
es = Elasticsearch(
    ['localhost'],
    http_auth=('elastic', 'changeme'),
    scheme='http',
    port=9200
)

_index = "my-index-000001"
_id = 42
_doc = {
    'any': 'data',
    'timestamp': datetime.now()
}


resp = es.indices.create(index=_index)