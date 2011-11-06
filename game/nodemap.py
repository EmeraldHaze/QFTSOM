from api import Net, Node
from lib import simple, limb#, fancy

#nodemap = Net('head', {
    #'head': Node(['tail', 'a'], ["Go forth along the dire worme's tail!", "A?"], limb.fight),
    #'tail': Node(['head', 'net'], ["Go backth along the dire worme's tail!", "Go INTO the worme!"], simple.fight),
    #'a'   : Node(['head', 'tail'], ["Go backth along the dire worme's tail!", "Go forth along the wormes!"]),# fancy.fight),
    #'net': Net('one', {
        #'one': Node(['two'], ['Advance via guts!'], {'say':'Eugh the bloods!'}),
        #'two': Node(['three'], ['Advance once more via guts!'], {'say':'Eugh the bloods!'}),
        #'three': Node([], [], {'say':'You ascend out of the worme!'}, exit_='head'),
        #})
    #})
nodemap = Net(0, {\
    0:Node([1], ["Advance!"], [('say',"You must fight some weird stuff! (Hint: choose a limb to attack, then an attack)"), ("battle", [limb.mad]), ('say',"You must go on to fight wirder stuff!")]),
    1:Node([2], ["Procced!"], [('battle', [limb.python])]),
    2:Node([3], ["Procced!"], [('battle', [limb.monty])]),
    3:Node([4], ["Procced!"], [('battle', [limb.flylord])])
    })