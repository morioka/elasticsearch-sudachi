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

## 今後

- sudachiのフィルタ見直し
- ベクトルの類似度に基づく検索
  - Bing: elasticsearch ベクトル
  - [Elasticsearchのベクトルフィールドをテキスト類似性検索に活用する | Elastic Blog](https://www.elastic.co/jp/blog/text-similarity-search-with-vectors-in-elasticsearch)
  - [Elasticsearchを用いて類似度ベクトル検索をやってみてわかったこと - ログミーTech](https://logmi.jp/tech/articles/322022)
  - [ElasticsearchでSudachiとベクトル検索を組み合わせて使う方法 ①Sudachi導入編 | 株式会社AI Shift](https://www.ai-shift.co.jp/techblog/168)
  - [ElasticsearchでSudachiとベクトル検索を組み合わせて使う方法 ②ベクトル検索編 | 株式会社AI Shift](https://www.ai-shift.co.jp/techblog/460)
  - [Elasticsearchを使用したスケーラブルなセマンティックベクトル検索](https://ichi.pro/elasticsearch-o-shiyoshita-suke-raburu-na-semanthikku-bekutoru-kensaku-254672523082382)
  - [Elasticsearchで類似ベクトル探索 / 類似画像検索 - Qiita](https://qiita.com/kumonkumon/items/a18b157f1888f1edd8f2)
  - [続) Elasticsearchで類似ベクトル探索 / 類似画像検索 - Qiita](https://qiita.com/kumonkumon/items/322b75296ec356a347f3)
