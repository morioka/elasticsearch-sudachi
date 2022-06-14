# AQLクイズ問題を題材に
AQLクイズ問題を題材に elasticsearch + kibana 環境構築を行います。

## 素材

- [AQL2020全国大会一般の部問題集（2021年1月10-11日/2月28日開催）](https://aql.booth.pm/items/3357932)
  - Google Spredsheet で TSV形式に変換しておく
  - ファイル名は `quiz-AQL-japan-2020-general.tsv` を想定

## 環境

- elasticsearch==7.10.0
- asyncio
- pandas
- unicodedata

## 実行

```sh
# jupyter notebookを実行し、データを成型
# before: quiz-AQL-japan-2020-general.tsv
# after:  quiz-AQL-japan-2020-general_clean.tsv

# index_template "template_1" の再作成
bash ./create_index_template.sh

# 既存indexの削除
bash ./delete_index.sh

# index "test-index-1" の作成とドキュメント追加
bash ./bulk_insert.sh
```

