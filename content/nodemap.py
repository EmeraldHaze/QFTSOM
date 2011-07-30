from api.net import net, node
nodemap = net('head',{
    'head':node(['tail'],["Go forth along the dire worme's tail!"]),
    'tail':node(['head'],["Go backth along the dire worme's tail!"])
    })
