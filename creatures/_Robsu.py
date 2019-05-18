from ._base import Base
from typing import Typing

class Robsu(Base):
 def __init__(self):
	 super().__init__(
		 index=1,
		 name="Robsu",
		 type1=Typing.mamão,
     type2=Typing.Aranha,
		 health=50,
		 speed=90,
		 attack=55,
		 sp_attack=50,
		 defense=40,
		 sp_defense=50
		)