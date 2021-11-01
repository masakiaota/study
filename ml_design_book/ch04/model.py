from dataclasses import dataclass
from typing import Tuple

from torch import nn, FloatTensor


# unsafe_hashはまだ完全に理解できないけどdataclassは便利そうなので使っていこう
@dataclass(unsafe_hash=True)
class MLPScoreFunc(nn.Module):
    """多層パーセプトロンによるスコアリング関数.u

    パラメータ
    ----------
    input_size: int
        特徴量ベクトルの次元数.

    hidden_layer_sizes: Tuple[int, ...]
        隠れ層におけるニューロンの数を定義するタプル.
        (10, 10)が与えられたら、ニューロン数が10個の隠れ層を持つ多層パーセプトロンが定義される.

    activation_func: torch.nn.functional, default=torch.nn.functional.elu
        活性化関数.

    """

    input_size: int
    hidden_layer_sizes: Tuple[int, ...]
    activation_func: nn.functional = nn.functional.elu

    def __post_init__(self) -> None:
        super().__init__()
        self.hidden_layers = nn.ModuleList()
        self.hidden_layers.append(
            nn.Linear(self.input_size, self.hidden_layer_sizes[0])
        )
        for hin, hout in zip(self.hidden_layer_sizes, self.hidden_layer_sizes[1:]):
            self.hidden_layers.append(nn.Linear(hin, hout))
        self.output = nn.Linear(self.hidden_layer_sizes[-1], 1)

    def forward(self, x: FloatTensor) -> FloatTensor:
        '''f_{\phi}に相当する関数を返す。スコアは確率的にはまだなっていない'''
        h = x
        for layer in self.hidden_layers:
            h = self.activation_func(layer(h))
        return self.output(h).flatten(1)  # f_{\phi}, (batch_size, number_of_documents)
