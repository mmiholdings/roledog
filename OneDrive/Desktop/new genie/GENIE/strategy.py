def OnData(data):
    if self.IsWarmingUp:
        return
    if data["SPY"].Price > self.rolling_mean.Current.Value:
        self.SetHoldings("SPY", 1)