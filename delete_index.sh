
# close index
curl -X POST http://localhost:9200/test_index-1/_close?pretty

# delete index
curl -X DELETE http://localhost:9200/test_index-1?pretty
