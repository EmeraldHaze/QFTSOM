from api import Net, Node
nodemap = Net('head', {
    'head': Node(['tail', 'a'], ["Go forth along the dire worme's tail!", "A?"], ["say Do kill it!", 'battle lib.limb.python, lib.limb.man|die:lib.limb.limbdie|schedule:lib.base.rules.speed']),
    'tail': Node(['head', 'net'], ["Go backth along the dire worme's tail!", "Go INTO the worme!"], ['battle lib.simple.man, lib.simple.player, lib.simple.man2, lib.simple.staffo, lib.simple.oddman||']),
    'a'   : Node(['head', 'tail'], ["Go backth along the dire worme's tail!", "Go forth along the wormes!"], ['battle lib.fancy.mage, lib.fancy.rouge, lib.fancy.dwarf, lib.fancy.dwarf2||']),
    'net': Net('one', {
        'one': Node(['two'], ['Advance via guts!'], ['say Eugh the bloods!']),
        'two': Node(['three'], ['Advance once more via guts!'], ['say Oh gawds the bloods!']),
        'three': Node([], [], ['say You ascend out of the worme!'], exit_='head'),
        })
    })
