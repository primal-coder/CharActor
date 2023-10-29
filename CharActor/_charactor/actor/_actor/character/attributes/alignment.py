from abc import ABC as _ABC
from typing import Optional as _Optional
import json as _json

def _load_json(path):
    with open(path, 'r') as f:
        return _json.load(f)


ALIGNMENTS = _load_json('CharActor/_charactor/dicts/alignments.json')

ALIGNMENT_INSTANCES = {}

class AbstractAlignment(_ABC):
    def __init__(self):
        self._title = None
        self._ethics = None
        self._morals = None

    @property
    def title(self) -> str:
        return self._title
    
    @title.setter
    def title(self, title):
        self._title = title

    @property
    def ethics(self) -> str:
        return self._ethics
    
    @ethics.setter
    def ethics(self, ethics):
        self._ethics = ethics

    @property
    def morals(self) -> str:
        return self._morals
    
    @morals.setter
    def morals(self, morals):
        self._morals = morals

    def __repr__(self):
        return f'{self.title.replace("_", " ").title()}'

class BaseAlignment(AbstractAlignment):
    def __init__(self, title):
        attrs = ALIGNMENTS[title]
        self.title = title.replace('_', ' ').title()
        self.ethics = attrs['ethics']
        self.morals = attrs['morals']

class AlignmentFactory:
    @staticmethod
    def create_alignment(title):
        attrs = ALIGNMENTS[title]
        if attrs is not None:
            return type(title, (BaseAlignment, ), {})
