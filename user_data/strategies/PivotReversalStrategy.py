from freqtrade.strategy import IStrategy
from pandas import DataFrame

import talib.abstract as ta

class PivotReversalStrategy(IStrategy):
  timeframe = '15m'
  can_short = True
  
  def populate_indicators(self, dataframe: DataFrame, metadata: dict) -> DataFrame:
    dataframe["adx"] = ta.ADX(dataframe)
    return dataframe
