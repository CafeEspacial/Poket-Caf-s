from ._base import Base
from typing import Typing

class Sonic(Base):
 def __init__(self):
   super().__init__(
     index=3,
     name="Sonic",
      type1=Typing.GotaGoFast,
     type2=Typing.Null,
     health=45,
     speed=130,
     attack=50,
     sp_attack=35,
     defense=30,
     sp_defense=35
   )