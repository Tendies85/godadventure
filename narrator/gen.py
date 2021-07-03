from dataclasses import dataclass

import typing as t


@dataclass
class God:
    name: str
    power: int


@dataclass
class Choice:
    text: str
    value: int


@dataclass
class Question:
    text: str
    choices: t.List[Choice]
    result: Choice = None
