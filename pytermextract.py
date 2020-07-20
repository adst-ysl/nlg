''
!wget "http://gensen.dl.itc.u-tokyo.ac.jp/soft/pytermextract-0_01.zip"
!unzip pytermextract-0_01.zip
%cd pytermextract-0_01/
!python setup.py install
%cd ..
!pip install janome
'''
import collections
import termextract.japanese_plaintext
import termextract.core
#　抽出されたキーワードにて、一つセンテンスにて、3位までの平均値を取得して、
# ファイルを読み込む
text = '重要度'

# 複合語を抽出し、重要度を算出
frequency = termextract.japanese_plaintext.cmp_noun_dict(text)
LR = termextract.core.score_lr(frequency,
         ignore_words=termextract.japanese_plaintext.IGNORE_WORDS,
         lr_mode=1, average_rate=1
     )
term_imp = termextract.core.term_importance(frequency, LR)

# 重要度が高い順に並べ替えて出力
data_collection = collections.Counter(term_imp)
for cmp_noun, value in data_collection.most_common():
    print(termextract.core.modify_agglutinative_lang(cmp_noun), value, sep="\t")
