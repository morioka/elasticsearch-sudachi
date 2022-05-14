import pandas as pd
import unicodedata

import asyncio
from elasticsearch import AsyncElasticsearch
from elasticsearch.helpers import async_bulk


index_name = "test_index-1"

df = pd.read_csv('quiz-AQL-japan-2020-general_clean.tsv', sep="\t")

#Index(['ID', '出題順', '時事', '難易度', 'ジャンル', '問題', '正解', '別解・判定基準・ 解説など', '裏取り',
#       '作成者', '文字数', '大会名', '出題日', 'ジャンル1', 'ジャンル2', '大会'],

def gendocs():
    docs = []
    for i, row in df.iterrows():
        docs.append(
            {
                'competition': unicodedata.normalize('NFKC', row['大会名']),
                'genre1': unicodedata.normalize('NFKC', row['ジャンル1']),
                'genre2': unicodedata.normalize('NFKC', row['ジャンル2']),
                'question': unicodedata.normalize('NFKC', row['問題']),
                'answer': unicodedata.normalize('NFKC', row['正解']),
                'hint': unicodedata.normalize('NFKC', str(row['別解・判定基準・ 解説など'])),
                'explanation': unicodedata.normalize('NFKC', str(row['裏取り'])),
                'difficulty': row['難易度'],
                'question_id': row['ID'],
                'question_number': row['出題順'],
                'question_type': unicodedata.normalize('NFKC', row['時事']),
                'question_length': row['文字数'],
                'author': unicodedata.normalize('NFKC', row['作成者']),
                'date': unicodedata.normalize('NFKC', row['出題日'])
            }
        )
    return docs

# 非同期対応したElasticsearchインスタンスを作成
es = AsyncElasticsearch("http://localhost:9200")

async def gendata():
    # 登録したいドキュメント
    docs = gendocs()
    
    # bulkで扱えるデータ構造に変換します
    for doc in docs:
        yield {
            "_op_type": "create",
            "_index": index_name,
            "_source": doc
        }


async def main():
    # 非同期でバルクインサートを実行
    await async_bulk(es, gendata())
    # セッションをクローズ
    await es.close()

# イベントループを取得
loop = asyncio.get_event_loop()
# 並列に実行して終るまで待つ
loop.run_until_complete(main())
