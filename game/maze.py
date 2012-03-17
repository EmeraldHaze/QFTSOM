from api import Place, PlaceNet
from lib.new import player

boneBranch = 'This tunnel, which seems to made of bones, suddenly branches to the side.'
evilCorner = 'This small jagged tunnel, smelling of human rot, has a dim, vile light at the other end.'
slimeTunnel = 'You have to bend to avoid the slime on the walls of this tiny tunnel'
iceHall = "You're in the corner of a massive room with stalactites on the ceiling. The walls are covered with a layer of frost, and you feel your lungs turn turn into blocks of ice from the cold emitting from he center of the room, where stands a magnificent throne, made of bones of all shapes and sizes"
fancyCorner = 'A superbly made, although rather twisty, turn. There are marble columns and all sorts of other precious things, all of which are extremely immovable.'
sharpCorner = 'Going though this very awkward and sharp corner, you earn yourself several scratches from the none-too-smooth walls.'
fancyCorner2 = 'An tastefully designed turn, with a very interesting color scheme.'
meetHall = "You're in the corner of an extremely military-looking hall, with tables and chairs of steel. There's a central table, with a map on it. The map is clearly of some very odd lands which you know nothing of, since you can't make heads or tails out of it."
crumbCorner = "You've almost twisted your ankle several times over on the very crumbly and uneven floor of this bent passage. The ceiling looks as if it's about to collapse."
imageCorner = 'A rather unsettling corner, due to images engraved on the walls. They are mostly abstract, but something about them chills you to the bone. '
wordCorner = "On the forbidding stone walls of this corner, you see lines and lines of words, in a commanding font, as if some underground god-king wrote his sacred book in the wall. It still chills you to the bone. Of course, it might be a teenage caveman's manifesto of anarchy, but it gives you the creeps all the same"
oddWall = 'As you go along this tunnel, it gets progressively darker (You ponder this for a long time, and finally realize that the fungus growing on the walls is inversly phosphorus. Lost in thoughts, you walk straight into a stone wall, although in a very odd manner. You walk about a foot into the wall, and only then you get pushed out, as if the wall rejected you.'
oldCorner = "A very worn old corner. It's covered with dust- you must of been the first to move this air for quite a while."


maze = PlaceNet('Maze',[
    Place("A1", ['A2', 'B1'], named_links=['S', 'E'], info=sharpCorner),
    Place("A2", ['A1', 'A3'], named_links=['N', 'S'], info=slimeTunnel),
    Place("A3", ['A2', 'B3'], named_links=['N', 'E'], info=oldCorner),
    Place("A4", ['B4', 'A5'], named_links=['E', 'S'], info=wordCorner),
    Place("A5", ['A4', 'B5'], named_links=['N', 'E'], info=wordCorner),
    Place("A6", ['B6', 'A7'], named_links=['E', 'S'], info=fancyCorner),
    Place("A7", ['A6', 'A8'], named_links=['N', 'S'], info="On the walls of this rather magnificent and grand wall, you observe a stately mural or a rather large number of heroes spouting blood and guts, and dieing horribly in no uncertain manner. There are also a number of paintings and statues of the same- heroes. You decide that normal eyes don't look like that, and part hurriedly."),
    Place("A8", ['A7', 'B8'], named_links=['N', 'E'], info=fancyCorner),
    Place("B1", ['B2', 'A1'], named_links=['S', 'W'], info=sharpCorner),
    Place("B2", ['B1'], named_links=['N'], info=oddWall),
    Place("B3", ['A3', 'B4'], named_links=['W', 'S'], info=oldCorner),
    Place("B4", ['B3', 'A4'], named_links=['N', 'W'], info=imageCorner),
    Place("B5", ['A5', 'B6'], named_links=['W', 'S'], info=imageCorner),
    Place("B6", ['C6', 'B5'], named_links=['E', 'N'], info="The tunnel-road exits into a medium-sized stone caravan. The two exits are perpendicular to each other. In the center of the caravan, you see an worn, engraved, table. The title seems to be ZGHCVQ PELCGB WHAXVRF, and what's beneath the title is very worn out, but you can make out the general shape of an 8x8 map."),
    Place("B7", ['B8'], beings=[player], named_links=['S'], info='Behind you, you see not only the awesome foe that is the Rough Ground of Unwalkability, but also an Indestructible Fallen Log, which had fallen immediately after your entrance. There is no escape, but forward. Such is life, for those lacking in motivation.'),
    Place("B8", ['B7', 'A8', 'C8'], named_links=['N', 'W', 'E'], info='The tunnel goes into an ornate room, with two doors out. The one two the west posses a magnificent grandeur, whilst the one two the east seems rather flimsy and fake, although both are equally splendid. In the middle is depicted the god Janus, as a statue, with a particularly mocking expression.'),
    Place("C1", ['C2'], named_links=['S'], info="Finally! You've found the way out, although the unholy splendor of the obsidian stairway out is somewhat unsettling."),
    Place("C2", ['C1', 'D2'], named_links=['N', 'E'], info=evilCorner),
    Place("C3", ['C4', 'D3'], named_links=['S', 'E'], info=iceHall),
    Place("C4", ['C3', 'C5', 'D4'], named_links=['N', 'S', 'E'], info=iceHall),
    Place("C5", ['C4', 'D5'], named_links=['N', 'E'], info=imageCorner),
    Place("C6", ['C7', 'D6'], named_links=['S', 'E'], info=fancyCorner2),
    Place("C7", ['C6', 'D7'], named_links=['N', 'E'], info=fancyCorner),
    Place("C8", ['B8', 'D8'], named_links=['W', 'E'], info='A wide and ornate hall, covered in all manner of shiny things, all of which are firmly affixed, ultimately, to the floor.'),
    Place("D1", ['D2', 'E1'], named_links=['S', 'E'], info=evilCorner),
    Place("D2", ['D1', 'C2'], named_links=['N', 'W'], info="You've found the source of the rotting smell: Zombies who weren't deemed fit for the attack. Or so you think- there are old zombies in this bent corridor, anyways."),
    Place("D3", ['D4', 'C3'], named_links=['S', 'W'], info=iceHall),
    Place("D4", ['D3', 'C4'], named_links=['N', 'W'], info=iceHall),
    Place("D5", ['C5', 'E5', 'D6'], named_links=['W', 'E', 'S'], info="The tunnel-path opens into a large room with two exits. In the middle stands a large scale. On the west part of the scale is a viper twisted into a mobius strip, on the east side, a mongoose in a priest's robe. Both of them are alive, and while they try not to move, every so often one of them gets out of position, flickers, and returned to it's original state."),
    Place("D6", ['C6', 'D5'], named_links=['W', 'N'], info='Expecting to see another superbly made turn, you are startled too see a exquisitely and tastefully designed bend in the passage.'),
    Place("D7", ['C7', 'D8'], named_links=['W', 'S'], info=fancyCorner2),
    Place("D8", ['C8', 'D7'], named_links=['W', 'N'], info=fancyCorner),
    Place("E1", ['D1', 'F1'], named_links=['W', 'E'], info='Contrary to the pure light right next to this part of the tunnel, this passage is rather dark and damp, and you can smell rot.'),
    Place("E2", ['E3', 'F2'], named_links=['S', 'E'], info=meetHall),
    Place("E3", ['E2', 'F3'], named_links=['N', 'E'], info=meetHall),
    Place("E4", ['F4', 'E5'], named_links=['E', 'S'], info=fancyCorner2),
    Place("E5", ['D5', 'E4'], named_links=['W', 'N'], info=fancyCorner),
    Place("E6", ['E7', 'F6'], named_links=['S', 'E'], info=oldCorner),
    Place("E7", ['E6', 'E8'], named_links=['N', 'S'], info=slimeTunnel),
    Place("E8", ['E7', 'F8'], named_links=['N', 'E'], info=oldCorner),
    Place("F1", ['G1', 'E1', 'H8'], named_links=['E', 'W', 'T'], info='A large portal, made of pure marble and filled with pure white light, stands in the middle of this shining passage.'),
    Place("F2", ['F3', 'E2'], named_links=['S', 'W'], info=meetHall),
    Place("F3", ['E3', 'F4', 'F2'], named_links=['W', 'S', 'N'], info=meetHall),
    Place("F4", ['E4', 'F3', 'F5'], named_links=['E', 'N', 'S'], info='Entering, you see a fabulous marble-shot room, with two ways out. In the center is a dual statue, made of marble. The northern part of it is a paladin with an upraised hammer, to the south, a fearsome lich with a bundle of something black in his hands.'),
    Place("F5", ['F4', 'G5', 'F6'], named_links=['N', 'E', 'S'], info=boneBranch),
    Place("F6", ['F5', 'E6', 'F7'], named_links=['N', 'W', 'S'], info=boneBranch),
    Place("F7", ['F6', 'G7'], named_links=['N', 'E'], info=evilCorner),
    Place("F8", ['E8', 'G8'], named_links=['W', 'E'], info='You have to bend over as the tunnel gets smaller and narrower, for quite some time.'),
    Place("G1", ['F1', 'H1'], named_links=['W', 'E'], info='The pure white light shining from the walls of this massive hallway lifts your mood.'),
    Place("G2", ['G3', 'H2'], named_links=['S', 'E'], info=crumbCorner),
    Place("G3", ['G2', 'G4'], named_links=['N', 'S'], info='You have to avoid chunks fallen from the ceiling as you navigate this hall.'),
    Place("G4", ['G3', 'H4'], named_links=['N', 'E'], info=crumbCorner),
    Place("G5", ['F5', 'G6'], named_links=['W', 'S'], info=oldCorner),
    Place("G6", ['G5', 'H6'], named_links=['N', 'E'], info=oldCorner),
    Place("G7", ['F7', 'H7'], named_links=['W', 'E'], info='A large hallway, with a vile emerald haze here and there, snaking out in tendrils, as well as some dark, snaky lines tracing here and there.'),
    Place("G8", ['F8'], named_links=['W'], info=oddWall),
    Place("H1", ['G1', 'H2'], named_links=['W', 'S'], info='This turn seems full of good spirits and warmness.'),
    Place("H2", ['H3', 'G2', 'H1'], named_links=['S', 'W', 'N'], info='What used to be a grand intersection is now a slightly less grand intersection due to the fact that one passage is caved in.'),
    Place("H3", ['B7'], named_links=['T'], info='Walking forward, you trip over the none-to-good floor. Your fall dislodges some sharp rocks from the ceiling, which impale you. (T to start over)'),
    Place("H4", ['G4', 'H5'], named_links=['W', 'S'], info=crumbCorner),
    Place("H5", ['H4'], named_links=['N'], info="There's no way south in this crumbling passage anymore, since the roof has done it's thing and crumbled down behind you."),
    Place("H6", ['H5', 'G6'], named_links=['N', 'W'], info=crumbCorner),
    Place("H7", ['G7', 'H8'], named_links=['W', 'S'], info=evilCorner),
    Place("H8", ['H7', 'F1'], named_links=['N', 'T'], info='You observe a large portal, made of bone. The emerald haze, which has been rampant up to this point along the trail, is practically solid within the portal.'),
])
