
# delete index template
curl -X DELETE localhost:9200/_index_template/template_1

# create index template
curl -X PUT localhost:9200/_index_template/template_1?pretty -H 'Content-Type: application/json' -d @index_template.json
