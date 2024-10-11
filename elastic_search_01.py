# Streamline Log Analysis using ElasticSearch

from elasticsearch import Elasticsearch

def analyze_logs(es_host, index_name):
    es = Elasticsearch([es_host])
    query = {
        "query": {
            "match": {"log_level": "ERROR"}
        }
    }
    results = es.search(index=index_name, body=query)
    for hit in results['hits']['hits']:
        print(f"Log: {hit['_source']}")

# Example usage
analyze_logs("http://localhost:9200", "security-logs")
