"""Utility class for numerical operations."""

from __future__ import annotations

from typing import Union

__author__ = "730577405"


class Simpy:
    """Simpy class created."""
    values: list[float]

    def __init__(self, ones: list[float]) -> None:
        """Simpy class constructor."""
        self.values = ones

    def __repr__(self) -> str:
        """String representation."""
        return f"Simpy({self.values})"

    def fill(self, x: float, y: int) -> None:
        """Fills amounts of same number with Simpy."""
        i: int = 0
        self.values = []
        while i < y:
            self.values.append(x)
            i += 1
        return None

    def arange(self, start: float, stop: float, step: float = 1.0) -> None:
        """Makes list of numbers incrementing by step value."""
        if start >= 0:
            while start < stop:
                self.values.append(start)
                start += step
        elif start < 0:
            while start > stop:
                self.values.append(start)
                start += step
        return None

    def sum(self) -> float:
        """Sum of Simpy values."""
        number: float = 0.0
        number = sum(self.values)
        return number

    def __add__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Simpy values added up."""
        result: Simpy = Simpy([])
        if isinstance(rhs, float):
            for item in self.values:
                result.values.append(item + rhs)
        else:
            assert len(self.values) == len(rhs.values)
            for i in range(len(self.values)):
                result.values.append(self.values[i] + rhs.values[i])
        return result

    def __pow__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Simpy values to the exponent of one another list."""
        result: Simpy = Simpy([])
        if isinstance(rhs, float):
            for item in self.values:
                result.values.append(item ** rhs)
        else:
            assert len(self.values) == len(rhs.values)
            for i in range(len(self.values)):
                result.values.append(self.values[i] ** rhs.values[i])
        return result

    def __eq__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Checks for equality of each value."""
        end: list[bool] = []
        if isinstance(rhs, float):
            for _ in self.values:
                if _ == rhs:
                    end.append(True)
                else:
                    end.append(False)
        else:
            assert len(self.values) == len(rhs.values)
            for _ in range(len(self.values)):
                if self.values[_] == rhs.values[_]:
                    end.append(True)
                else:
                    end.append(False)
        return end

    def __gt__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Checks for greater than in values."""
        end: list[bool] = []
        if isinstance(rhs, float):
            for _ in self.values:
                if _ > rhs:
                    end.append(True)
                else:
                    end.append(False)
        else:
            assert len(self.values) == len(rhs.values)
            for _ in range(len(self.values)):
                if self.values[_] > rhs.values[_]:
                    end.append(True)
                else:
                    end.append(False)
        return end

    def __getitem__(self, rhs: Union[int, list[bool]]) -> Union[float, Simpy]:
        """Allows one to use subscription operator."""
        if isinstance(rhs, int):
            return self.values[rhs]
        else:
            another: Simpy = Simpy([])
            assert len(self.values) == len(rhs)
            for _ in range(len(self.values)):
                if rhs[_] is True:
                    another.values.append(self.values[_])
        return another
