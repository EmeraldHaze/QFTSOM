from api import Net, Node
from lib import limb, simple, fancy

nodemap = Net('head', {
    'head': Node(['tail', 'a'], ["Go forth along the dire worme's tail!", "A?"], limb.fight),
    'tail': Node(['head', 'net'], ["Go backth along the dire worme's tail!", "Go INTO the worme!"], simple.fight),
    'a'   : Node(['head', 'tail'], ["Go backth along the dire worme's tail!", "Go forth along the wormes!"], fancy.fight),
    'net': Net('one', {
        'one': Node(['two'], ['Advance via guts!'], ['say Eugh the bloods!']),
        'two': Node(['three'], ['Advance once more via guts!'], ['say Oh gawds the bloods!']),
        'three': Node([], [], ['say You ascend out of the worme!'], exit_='head'),
        })
    })
