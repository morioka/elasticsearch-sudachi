# Elasticsearch + Sudachi
Docker Composeを使って、Elasticsearch + Sudachiの環境構築を行います。

## 環境

- Elasticsearch: 7.10.1
- analysis-sudachi: v2.1.0
- SudachiDict: sudachi-dictionary-20201223-core

## 実行

```sh
$ docker compose up --build
```

## 起動確認

```sh
$ curl http://127.0.0.1:9200/_cat/health
```

- kibana: http://localhost:5601/