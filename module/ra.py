import slot
from adv import adv_test

t = 0

def test(adv, conf, duration=180):
    print('dps,cname,star,ele,wt,att,wpset,cond,-,amulet1,amulet2,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-')

    ams = []
    amulets_withalias = slot.a.amulets
    for i in amulets_withalias:
        if i not in ams:
            ams.append(i)
    amlen = len(ams)
    for m in range(amlen):
        for n in range(m+1,amlen):
            i = ams[m]
            j = ams[n]
            conf['slots.a'] = i() + j()
            conf['slot.a'] = conf['slots.a']
            adv.comment = '(',type(i()).__name__, type(j()).__name__,')'
            adv_test.test(adv, conf, verbose=255, mass=0, duration=duration)
