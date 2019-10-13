## 参考文献
- サーベイ論文(長くて読んでない) https://ieeexplore.ieee.org/stamp/stamp.jsp?arnumber=8466590
- 参考になりそうなサイト(導入としてこちらから) https://towardsdatascience.com/human-interpretable-machine-learning-part-1-the-need-and-importance-of-model-interpretation-2ed758f5f476

- めっちゃまとまってそうな本 https://christophm.github.io/interpretable-ml-book/

- まとめっていそうな日本語の資料 https://www.slideshare.net/SatoshiHara3/ss-126157179

## 実装
- Skater https://github.com/oracle/Skater
- ELI5 https://github.com/TeamHG-Memex/eli5
- SHAP https://github.com/slundberg/shap

## モチベーション
「どうすればあなたのモデルを信用できますか?」や「あなたのモデルは実際にどのように意思決定を行うのだろうか。｣という質問に答えたい。

また、モデルが公平(？)かどうか判断することもできる。


## XIAにおける重要な3点
- モデルの全体的な意思決定において、どのような特徴量が重要視されているのか。
- あるサンプルに対して意思決定をしたときになぜそう判断したのか。
- モデルの決定を信じられるか？ モデルの判断を人間に説明したときに人間が理解しやすいか(モデル透明性)

## XIAにおけるスコープ
- global interpretation
    - データセット全体に対して、どういう特徴量が重要でどういうinteractionがあるのか
- local interpretation
    - あるサンプルに対する予測にたいして、どうしてそのように判断したのか


## モデル解釈のための伝統的な方法とその弱点
- データのEDAと可視化も一つのモデル解釈の方法
    - 深層学習で獲得した表現をTSNEで圧縮するとか
    - 決定木の可視化もこれに当たる
- 実際にパフォーマンスを示してモデルを解釈する
    - パフォーマンスでモデルの中身までわかるかというと... (これは発表のときは省略)

## 精度vs解釈性
- 線形モデルや一本の決定木では説明はしやすいが精度はでない。

## モデル解釈のための方法
- Feature Importance
    - 木を使う手法あるある
    - permutation importanceも計算できる
- Partial Dependance Plots
    - 全サンプルのある特徴量をすべてxで上書き。そのxを変化させたときに予測がどのように変化するか見たplots. 
    - どういうふうに読み取れば良いだろう...(その特徴量が増えれば予測がどうなるかがわかる？)
    - 参考 https://linus-mk.hatenablog.com/entry/2018/10/07/222909
- Global Surrogate Models
    - 複雑なモデルを解釈可能ぐらい簡単なモデルに近似させる
    - 例えば訓練済みXGboostを用いて、同じ入出力をするようにDTを学習する。(born again treesというらしい)
- Local Interpretable Model-agnostic Explanations (LIME)
    - サンプルに対してローカルの解釈を与える手法
    - ブラックボックスに対して適応可能(SVM,NN,RF等)
    - 論文 https://arxiv.org/abs/1602.04938
    - 実装 https://github.com/marcotcr/lime 
    - 説明したサンプルに対して摂動を加えたデータセットを用意してblackboxに推論させる。そしてその入出力を真似するように、線形のローカルモデルを訓練して係数を出力するという仕組み。

- Shapley Values and SHapley Additive exPlanations (SHAP)
    - これも任意のモデルに適応できるみたい。
    - ローカルの説明にゲーム理論と関連しているらしい？Shaply valueってやつ
    - 論文 http://papers.nips.cc/paper/7062-a-unified-approach-to-interpreting-model-predictions
    - モデル推論において特徴量をゲームのplayerと見立てている
    - そのサンプルの特徴量がyの平均に対してどのように作用してその値になったのか説明しようという試み。
    - **んーゲーム理論の下りがよくわからない**
    - これの28pから説明がある https://www.slideshare.net/SatoshiHara3/ss-126157179
    - こっちのほうがわかりやすいかも https://speakerdeck.com/hightensan/lime-and-shap-ji-jie-xue-xi-moderuniyoruyu-ce-jie-guo-falseshuo-ming-xing?slide=22
    - http://www.ie110704.net/2019/04/26/機械学習モデルを解釈する指標shapについて/
    - http://tmitani-tky.hatenablog.com/entry/2019/02/17/235409

- ANCHORS
    - 実装 https://github.com/marcotcr/anchor
    - 論文 https://www.aaai.org/ocs/index.php/AAAI/AAAI18/paper/view/16982

- influence
    - 予測の根拠となった訓練データを提示する方法
    - 論文 http://proceedings.mlr.press/v70/koh17a.html
    - 実装 https://github.com/kohpangwei/influence-release










