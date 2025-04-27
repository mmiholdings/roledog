
from AlgorithmImports import *
import json

class GenieSmartFlowSentimentStrategy(QCAlgorithm):
    def Initialize(self):
        self.SetStartDate(2024, 1, 1)
        self.SetCash(100000)
        self.symbol = self.AddEquity("SPY", Resolution.Hour).Symbol
        self.Schedule.On(self.DateRules.EveryDay(), self.TimeRules.Every(30), self.RefreshSmartFlow)

    def RefreshSmartFlow(self):
        try:
            raw = self.Download("https://your-smartflow-api.com/latest_bias")
            data = json.loads(raw)
            self.smartflow_bias = float(data.get("bias", 0))
            self.Debug(f"SmartFlow Bias: {self.smartflow_bias}")
        except Exception as e:
            self.smartflow_bias = 0
            self.Debug(f"Error fetching SmartFlow: {e}")

    def OnData(self, data):
        if not data.ContainsKey(self.symbol): return
        if self.smartflow_bias > 1.5:
            self.SetHoldings(self.symbol, 1.0)
        elif self.smartflow_bias < -1.5:
            self.SetHoldings(self.symbol, -1.0)
