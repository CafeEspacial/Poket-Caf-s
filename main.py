from Wilson import Trainer
import creatures

wilson = Trainer(
	"Wilson",
	4,
	[
		creatures.Robsu(),
		creatures.Josefu()
	]
)
wilson.list_creatures()

Goku = Trainer(
	"Goku",
	4,
	[
		creatures.Sonic(),
		creatures.Cetrion()
	]
)
Goku.list_creatures()

def tackle (a, b):
	b.curr_health -= round(40 * (a.attack / 255))

Robsu = wilson.creatures[0]
Josefu = wilson.creatures[1]
Robsu.do_move(Josefu, tackle)

Robsu.status()
Josefu.status()