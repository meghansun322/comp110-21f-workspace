"""Utility class for numerical operations."""

from __future__ import annotations

from typing import Union

__author__ = "YOUR PID HERE"


class Simpy:
    values: list[float]

    def __init__(self, values: list[float]):
        """Constructor."""
        self.values = values

    def __str__(self) -> str:
        """Prints Values."""
        return "Simpy(" + f"{self.values}" + ")"

    def __add__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Adds Value Items."""
        result: Simpy = Simpy([])
        if isinstance(rhs, float):
            for value in self.values:
                result.values.append(value + rhs)
        else:
            assert len(self.values) == len(rhs.values)
            i: int = 0
            while i < len(self.values):
                result.values.append(self.values[i] + rhs.values[i])
                i = i + 1
        return result

    def __pow__(self, power: Union[float, Simpy]) -> Simpy:
        """Powers each value items."""
        result: Simpy = Simpy([])
        if isinstance(power, float):
            for value in self.values:
                result.values.append(value ** power)
        else:
            assert len(self.values) == len(power.values)
            i: int = 0
            while i < len(self.values):
                result.values.append(self.values[i] ** power.values[i])
                i = i + 1 
        return result

    def __eq__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Returns list of boolean if equal."""
        result: list[bool] = []
        if isinstance(rhs, float):
            for value in self.values:
                if(value == rhs):
                    result.append(True)
                else:
                    result.append(False)
        else:
            assert len(self.values) == len(rhs.values)
            i: int = 0
            while i < len(self.values):
                if (self.values[i] == rhs.values[i]):
                    result.append(True)
                else:
                    result.append(False)
                i = i + 1
        return result

    def __gt__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Returns boolean list of if values greater than."""
        result: list[bool] = []

        if isinstance(rhs, float):
            for value in self.values:
                if(value > rhs):
                    result.append(True)
                else:
                    result.append(False)
        else:
            assert len(self.values) == len(rhs.values)
            i: int = 0
            while i < len(self.values):
                if (self.values[i] > rhs.values[i]):
                    result.append(True)
                else:
                    result.append(False)
                i = i + 1
        return result

    def __getitem__(self, rhs: Union[int, list[bool]]) -> Union[float, Simpy]:
        """Gets item that fits condition."""
        result: Union[float, Simpy] = Simpy([])

        if isinstance(rhs, int):
            result = self.values[rhs]
        else: 
            i: int = 0
            while i < len(self.values):
                if rhs[i]:
                    result.values.append(self.values[i])
                i = i + 1
        return result

    def fill(self, value: float, count: int) -> None:
        """Fills values in values field."""
        new_values: list[float] = []
        i: int = 0
        while i < count:
            new_values.append(value)
            i = i + 1
        self.values = new_values

    def arange(self, start: float, stop: float, step: float = 1.0) -> None:
        """Sets values in range."""
        new_values: list[float] = []

        assert step != 0.0

        current: float = start
        i: int = 0
        if (start < stop):
            while (current) < stop:
                new_values.append(current)
                i = i + 1
                current = current + step
        else:
            while (current) > stop:
                new_values.append(current)
                i = i + 1
                current = current + step 
        self.values = new_values

    def sum(self) -> float:
        """Sums values."""
        return sum(self.values)
