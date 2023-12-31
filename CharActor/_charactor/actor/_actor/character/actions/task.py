from abc import ABC, abstractmethod
import random
import json as _json
from typing import Optional, Union

from pyglet.event import EventDispatcher

from CharActor._quiet_dict import QuietDict as _QuietDict
from CharActor._charactor.dicts import load_dict

def _load_json(path):
    with open(path, 'r') as f:
        return _json.load(f)

_TASKS_DICT = load_dict('tasks')

_QUALITIES = ['base', 'fair', 'average', 'good', 'better', 'excellent', 'exceptional', 'outstanding', 'superb', 'perfect']

class TaskMeta(type):
    def __new__(cls, name, bases, attrs):
        attrs['_dispatcher'] = EventDispatcher()
        return super().__new__(cls, name, bases, attrs)

class AbstractTask(metaclass=TaskMeta):
    def __init__(self):
        self._name = None
        self._description = None
        self._required_skill = None
        self._required_skill_level = None
        self._difficulty_class = None
        self._required_tools = None
        self._required_materials = None
        self._required_zone = None
        self._product = None
        self._product_quantity = None
        self._product_quality = None
        self._required_time = None
        self._success = None
        self._failure = None
        self._experience_reward = None
        self._gold_reward = None

    @abstractmethod
    def execute(self, worker):
        pass

class Task(AbstractTask):
    def __init__(
            self,
            name: Optional[str] = None,
            description: Optional[str] = None,
            required_skill: Optional[str] = None,
            required_skill_level: Optional[int] = None,
            difficulty_class: Optional[int] = None,
            required_time: Optional[int] = None,
            required_tools: Optional[list] = None,
            required_materials: Optional[list] = None,
            required_zone: Optional[str] = None,
            product: Optional[str] = None,
            product_quantity: Optional[int] = None,
            product_quality: Optional[int] = None,
            experience_reward: Optional[int] = None,
            gold_reward: Optional[int] = None,
            *args, **kwargs
    )-> None:
        super().__init__()
        self._name = name
        self._description = description
        self._required_skill = required_skill
        self._required_skill_level = required_skill_level
        self._difficulty_class = difficulty_class
        self._required_time = required_time
        self._required_tools = required_tools
        self._required_materials = required_materials
        self._required_zone = required_zone
        self._product = product
        self._product_quantity = product_quantity
        self._product_quality = product_quality
        self._experience_reward = experience_reward
        self._gold_reward = gold_reward
        self._input_materials = None
        self._output_materials = None

    @property
    def name(self) -> str:
        return self._name
    
    @property
    def description(self) -> str:
        return self._description
        
    @property
    def required_skill(self) -> str:
        return self._required_skill
    
    @property
    def required_skill_level(self) -> int:
        return self._required_skill_level
    
    @property
    def difficulty_class(self) -> int:
        return self._difficulty_class
    
    @property
    def required_tools(self) -> Union[list, str]:
        return self._required_tools
    
    @property
    def required_materials(self) -> Union[list, str]:
        return self._required_materials
    
    @property
    def required_zone(self) -> str:
        return self._required_zone
    
    @property
    def product(self) -> str:
        return self._product
    
    @property
    def product_quantity(self) -> int:
        return self._product_quantity
    
    @property
    def product_quality(self) -> int:
        return self._product_quality
    
    @property
    def required_time(self) -> int:
        return self._required_time
    
    @property
    def success(self) -> str:
        return self._success
    
    @property
    def failure(self) -> str:
        return self._failure
    
    @property
    def experience_reward(self) -> int:
        return self._experience_reward
    
    @property
    def gold_reward(self) -> int:
        return self._gold_reward

    @property
    def input_materials(self):
        return self._input_materials

    @property
    def output_materials(self):
        return self._output_materials
    

    def execute(self, worker):
        if not self._check_requirements(worker):
            return
        for item in self._required_materials:
            for _ in range(self._required_materials[item]):
                self._input_materials = worker.inventory._full_contains
                worker.inventory.remove_item(worker.inventory._full_contains)
        if self.required_skill is not None:
            return (
                self._produce(worker)
                if getattr(worker.skillbook, f'{self.required_skill}').check(
                    self.difficulty_class
                )
                else self._fail(worker)
            )
        if worker.Strength.ability_check(self.difficulty_class):
            return self._produce(worker)
        else:
            return self._fail(worker)


    def _check_skill(self, worker):
        if self.required_skill is not None and getattr(worker.skillbook, f'{self.required_skill}').level >= self.required_skill_level:
            return True
        return f'{worker.name} does not have the required skill level.'

    def _check_materials(self, worker):
        return next(
            (
                f'{worker.name} does not have the necessary materials.'
                for item in self._required_materials
                if item not in worker.inventory
            ),
            True,
        )
    
    def _check_tools(self, worker):
        return next(
            (
                f'{worker.name} does not have the necessary tools.'
                for tool in self._required_tools
                if tool not in worker.inventory
            ),
            True,
        )

    def _check_zone(self, worker):
        if self._required_zone is not None and worker.zone != self._required_zone:
            return f'{worker.name} is not in the correct zone.'
        return True

    def _check_requirements(self, worker):
        return all(
            (self._check_skill(worker),
            self._check_materials(worker),
            self._check_tools(worker),
            self._check_zone(worker),)
        )

    # TODO Rename this here and in `execute`
    def _produce(self, worker):
        if self.product['success'] is not None and self.product['success'] == 'Same':
            product = self.input_materials
        else:
            product = self.product['success']
        quality = _QUALITIES[random.randint(0,self._product_quality)] if self._product_quality is not None else ""
        quantity = self._product_quantity if self._product_quantity is not None else 1
        worker.inventory.add_item(product, quantity)
        worker._give_xp(self._experience_reward)
        return f'Success. +{self.product_quantity} {quality} {product}'
    
    def _fail(self, worker):
        product = self._product.get('failure', None)
        if product is not None:
            worker.inventory.add_item(product)
        return f'Failure. +1 {product}'


class TaskFactory:
    @staticmethod
    def create_task(task_id: str) -> Task:
        task = _TASKS_DICT[task_id]
        return Task(
            name=task['name'],
            description=task['description'],
            required_skill=task.get('required_skill', None),
            required_skill_level=task.get('required_skill_level', None),
            difficulty_class=task['difficulty_class'],
            required_time=task['required_time'],
            required_tools=task['required_tools'],
            required_materials=task['required_materials'],
            required_zone=task.get('required_zone', None),
            product=task['product'],
            product_quantity=task['product_quantity'],
            product_quality=task['product_quality'],
            experience_reward=task['experience_reward'],
            gold_reward=task['gold_reward']
        )
    
        
class TaskList(_QuietDict):
    def __init__(self):
        self._tasks = None
        self._add_tasks()

    @property
    def items(self):
        if self._tasks is None:
            self._tasks = {}
        return self._tasks

    @property
    def tasks(self):
        if self._tasks is None:
            self._tasks = {}
        return self._tasks

    def _add_tasks(self):
        for task_id, task in _TASKS_DICT.items():
            task_inst = TaskFactory.create_task(task_id)
            setattr(self, f'{task["name"].replace(" ", "_")}', task_inst)
            self.update({f'{task["name"]}': task_inst})


task_list = TaskList()
