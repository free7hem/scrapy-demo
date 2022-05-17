## Scrapy demo

## run scrapy
```shell
scrapy crawl my_spider -O whisky.json
```

## insert result to meilisearch
```shell
curl -X POST 'http://meilisearch:7700/indexes/whisky/documents' -H 'Content-Type: application/json' -d @whisky.json
```
