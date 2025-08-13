from miniworld import envs, miniworld
from miniworld.entity import Agent, Entity
from miniworld.envs import *

__version__ = "2.1.0"

# Make the environment classes available at the top level
__all__ = [
    'Agent',
    'Entity',
    'miniworld',
    'envs'
]
