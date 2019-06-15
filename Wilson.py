from typing import Typing
import creatures

class Trainer:
  def __init__(self, name, money, creatures):
    self.name = name
    self.money = money
    self.creatures = creatures

  def list_creatures(self):
    print("\n {}'s creatures: \n ".format(self.name))
    for c in self.creatures:
      print("{}: [{}, {}]".format(c.name, c.type1.name, c.type2.name))

  def defeated(self):
    result = True

    for creature in self. creatures:
      result = result and creature. fainted()
      return result