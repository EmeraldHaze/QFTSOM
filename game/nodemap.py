from api import Net, Node
nodemap = Net('head', {
    'head': Node(['tail', 'a'], ["Go forth along the dire worme's tail!", "A?"], ["say Do kill it!"]),
    'tail': Node(['head', 'net'], ["Go backth along the dire worme's tail!", "Go INTO the worme!"], ['battle simple.man, simple.player, simple.man2, simple.staffo, simple.oddman||']),
    'a'   : Node(['head', 'tail'], ["Go backth along the dire worme's tail!", "Go forth along the wormes!"], ["battle fancy.rouge, fancy.dwarf, fancy.dwarf2, fancy.mage||"]),
    'net': Net('one', {
        'one': Node(['two'], ['Advance via guts!'], ['say Eugh the bloods!']),
        'two': Node(['three'], ['Advance once more via guts!'], ['say Oh gawds the bloods!']),
        'three': Node([], [], ['say You ascend out of the worme!'], exit_='head'),
        })
    })
