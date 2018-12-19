import adv_test
import adv
import wep.wand


def module():
    return Maribelle

class Maribelle(adv.Adv):
    conf = {}
    conf.update( {
        "s1_dmg"  : 1.61*6 ,
        "s1_sp"   : 2648   ,
        "s1_time" : 2.7    ,

        "s2_dmg"  : 2.44*4 ,
        "s2_sp"   : 5838   ,
        "s2_time" : 1.8    ,

        "s3_dmg"  : 4*2.71   ,
        "s3_sp"   : 8597     ,
        "s3_time" : 1.9        ,
        } )
    conf.update(wep.wand.conf)

    def sp_mod(this, name):
        return 1

    def dmg_mod_s(this, name):
        return 1.65*1.15

    def init(this):
        this.s1.charge(20000)
        this.s2.charge(20000)
        this.s3.charge(20000)


    def s1_proc(this, e):
        pass
    def s2_proc(this, e):
        pass
    def s3_proc(this, e):
        pass


if __name__ == '__main__':
    conf = {}
    conf['al'] = {
        #'sp': ["s1","s2"],
        'x5': ["s1","s2","s3"],
        'x4': [],
        'x3': ["s1","s2","s3"],
        'x2': ["s1","s2","s3"],
        'x1': ["s1","s2","s3"],
        's':  ["s1","s2","s3"],
        } 

    adv_test.test(module(), conf, verbose=0)
