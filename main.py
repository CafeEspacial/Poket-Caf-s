from Wilson import Trainer
import creature

Wilson = Trainer("Wilson", 4, [
 creature.Robsu(),
 creature.Josefu(),
 creature.Sonic(),
 creature.Cetrion()
])
Wilson.list_creatures()