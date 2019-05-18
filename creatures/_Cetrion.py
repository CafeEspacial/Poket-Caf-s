from ._base import Base
from typing import Typing

class Cetrion(Base):
 def __init__(self):
	 super().__init__(
		 index=4,
		 name="Cetrion",
		 type1=Typing.mamão,
     type2=Typing.Null,
		 health=125,
		 speed=30,
		 attack=40,
		 sp_attack=50,
		 defense=35,
		 sp_defense=40
		)