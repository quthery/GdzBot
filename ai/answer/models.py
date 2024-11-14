import g4f
import g4f.Provider
from typing import Any
import pathlib
from pydantic.dataclasses import dataclass


@dataclass
class InputData:
	type: str
	image: str
	prompt: str

@dataclass
class OutputData:
	model: Any
	type: str
	prompt: str
	image: str | pathlib.Path


@dataclass
class Answer:
	text: str
	executionTime: float | str
	fileID: str
	answered_at: str
	





