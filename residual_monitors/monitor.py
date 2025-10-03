"""
Generic monitoring utilities for training stability.

This module provides simple functions to compute running statistics
and detect anomalies in metrics such as residuals or gradient norms.
These are generic utilities; no proprietary algorithms are included.
"""
import collections

class RunningStats:
    """Keeps a running window of the last N values and computes statistics."""
    def __init__(self, window_size=100):
        self.window_size = window_size
        self.data = collections.deque(maxlen=window_size)

    def add(self, value):
        self.data.append(value)

    def mean(self):
        return sum(self.data) / len(self.data) if self.data else 0.0

    def std(self):
        if not self.data:
            return 0.0
        mean = self.mean()
        return (sum((x - mean) ** 2 for x in self.data) / len(self.data)) ** 0.5

    def is_anomaly(self, value, threshold=3.0):
        """Detect if a value is an anomaly based on mean +/- threshold*std."""
        if not self.data:
            return False
        mean = self.mean()
        std = self.std()
        return abs(value - mean) > threshold * std
