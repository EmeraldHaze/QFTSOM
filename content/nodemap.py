from api.net import net, node
nodemap = net('head',{
    'head':node(['tail', 'a'],["Go forth along the dire worme's tail!", "A?"], "Do kill),
    'tail':node(['head'],["Go backth along the dire worme's tail!"]),
    'a'   :node(['head', 'tail'],["Go backth along the dire worme's tail!", "Go forth along the wormes!"])
    },
    []
    )
