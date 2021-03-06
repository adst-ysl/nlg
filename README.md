# nlg
## slack
```
https://slack.com/intl/ja-jp/
iriteamhq
yu_shenglong@ines.co.jp
1ysl123
```

## teams
```
https://teams.microsoft.com/
yu_shenglong@ines.co.jp
1Ysl12345
```

## 2020-07-10 meeting
```
本日の議事メモを展開します。
word2vecの懸念点の解決方法
・USEのベクトルを出す→USEで類似度を出す→単語ベースでの類似度も出す→USEと単語の類似度を足して評価する
・類似度にバイアスをかけて意味ベースで出せる。USE×２、単語×0.1みたいな。機械学習で最適な値が出る。アンサンブル的な
・重要な単語に重みづけをする。TF-IDFで出来る。

開発方針レビューの話
北海道支社がガイダンスコンテンツを作成しているので、そこと認識合わせが必要。
★このチームとしてはAI技術の汎用性を高めることを目標とすべきで、この先は増田さんと調整。
　レビュー時点ではガイダンスの出すタイミング、表示の仕方を気にしていたので、今はそこには注力しない。

ガイダンスを出すタイミング
内容の質よりもタイミングが重要。
分からない、知らない時に適切にレコメンドできるように。
ベテランの方に出すタイミングを調整してもらうことも視野に。
ガイダンスが適切なタイミングに表示されたらいいね！して精度を調整する。
欲しいときにクリックして出すかどんどん出して溜めていくか
→溜めた方が聞き漏らしの解決できる

ガイダンスコンテンツをAIで読み取りやすい形で記載する
→AIチャットボットではネット上等で抜き出しやすい日本語を考える研究が進んでいる
吉岡さんに交渉して、コンテンツにカラムを追加して上手くできないか

やらなければいけないタスク
・キーワードマッチを上回る精度を出せるように
　USE+word2vecで汎化性と精度を上げる
　　→まずはword2vec（単語類語の類似度、類義語のデータ追加）の精度を出して、そこから汎化性を考える
　　　曖昧語の対応
・どういうガイダンスの書き方が良いか
・モデルの組み合わせの最適を探す

スケジュール
技術評価のリスケを考える（細谷さんと増田さんと打ち合わせが必要）
→技術評価の中で業務評価の指標を考えておけば両方同時にできるので並列にする
業務評価
ガイダンスチームに発言に対してどういうコンテンツが出るのが正しいか正解を用意してもらって、
AIチームで出した模擬シナリオ中に出してきたものと比較して評価する。
吉岡さんのチームで出来るか調整してから（正しいガイダンスが何か判断出来るか）
```
