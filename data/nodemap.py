from api.net import net, node
nodemap = net('head',{
    'head':node(['tail', 'a'],["Go forth along the dire worme's tail!", "A?"], ["say Do kill it!", 'battle player, man|win, die|dummy']),
    'tail':node(['head', 'net'],["Go backth along the dire worme's tail!", "Go INTO the worme!"]),
    'a'   :node(['head', 'tail'],["Go backth along the dire worme's tail!", "Go forth along the wormes!"]),
    'net':net('one',{
        'one':node(['two'], ['Advance via guts!'], ['say Eugh the bloods!']),
        'two':node(['three'], ['Advance once more via guts!'], ['say Oh gawds the bloods!']),
        'three':node([], [], ['say You ascend out of the worme!'], exit_ = 'head'),
        })
    })
