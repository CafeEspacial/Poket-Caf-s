from typing import Typing
import creature

class Trainer:
  def __init__(self, name, money, creature):
    self.name = name
    self.money = money
    self.creature = creature

  def list_creatures(self):
    print("\n {}'s creatures: \n ".format(self.name))
    for c in self.creature:
      print("{}: [{}, {}]".format(c.name, c.type1.name, c.type2.name))