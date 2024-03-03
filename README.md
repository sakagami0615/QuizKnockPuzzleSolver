# QuizKnockPuzzleSolver

以下の動画に出てくるクイズを解くプログラムとなります。

[【大決戦】コンピュータを使ってでもパズル王に勝ちたい！！](https://www.youtube.com/watch?v=4mh9qsH0Zhs)

詳細は、下記のQiita記事を確認ください。

[「QuizKnockパズル王vs.コンピュータ」のパズルを解くプログラムを作ってみた](https://qiita.com/sakagami_notebook/items/5fc8116d385a2ce598ba)

## ファイル

+ 以下のファイルは、逆ポーランド記法の演算および全探索のコードとなります。
  + RPN/calc_rpn.py
  + RPN/calc_rpn_simple.py
  + RPN/search_rpn_all.py
+ 以下のファイルは、動画内で出てきた問題を今回作成したプログラムに入力できる形で保存したスクリプトとなります。
  + ./sample_input.py
+ 以下のファイルは、クイズを解くソルバーと動作確認用コードとなります。
  + ./quizknock_solver.py
  + ./check.py
+ 以下のファイルは、ソルバーの検証用のスクリプトとなります。
  + ./test_quizknock_solver.py
+ 以下のファイルは、上記のコードをGoogleColaboratoryで動かせるようにしたノートブックとなります。
  + colab_notebook/QuizKnock_PuzzleKing-vs-Program.ipynb
