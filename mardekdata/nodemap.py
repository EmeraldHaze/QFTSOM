from api.net import Net, Node
nodemap = Net('start', {'start':Node([], [], ['say Welcome to text-only Mardek 2 (First saviour battle)', 'battle aalia, bernard, vennie, bartholio|die, win|scheduale = agl']
    'head': Node(['tail', 'a'], ["Go forth along the dire worme's tail!", "A?"], ["say Do kill it!", 'battle dwarf, dwarf2, rouge|die, win|schedule = same']),
    'tail': Node(['head', 'net'], ["Go backth along the dire worme's tail!", "Go INTO the worme!"]),
    'a'   : Node(['head', 'tail'], ["Go backth along the dire worme's tail!", "Go forth along the wormes!"]),
    'net': Net('one', {
        'one': Node(['two'], ['Advance via guts!'], ['say Eugh the bloods!']),
        'two': Node(['three'], ['Advance once more via guts!'], ['say Oh gawds the bloods!']),
        'three': Node([], [], ['say You ascend out of the worme!'], exit_='head'),
        })
    })
