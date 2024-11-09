import g4f
import g4f.Provider
import pathlib
from pydantic.dataclasses import dataclass


@dataclass
class InputData:
	prompt: str
	type: str
	model: str | g4f.Model
	provider: str | g4f.Provider.ProviderType
	image: str | pathlib.Path

@dataclass
class Answer:
	text: str
	executionTime: float | str
	fileID: str
	answered_at: str
	






