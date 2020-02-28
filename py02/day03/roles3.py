#!/usr/local/bin/python3

class Wuqi:
    def __init__(self, wname, wtype, liliang, zhili):
        self.wname = wname
        self.wtype = wtype
        self.liliang = liliang
        self.zhili = zhili


class Role:
    def __init__(self, name, wuqi):  # 只是习惯于叫self
        '称作构造器方法,创建实例时,自动调用,通常用于将属性绑定到实例'
        self.name = name
        self.wuqi = wuqi

    def show_me(self):
        # 绑定在实例身上的属性,可以在类中的任意位置使用
        print('%s' % self.name)


class ZhanShi(Role):
    pass


class FaShi(Role):
    pass


if __name__ == '__main__':
    ji = Wuqi(wname='方天画戟', wtype='物理伤害', liliang=100, zhili=0)
    lb = ZhanShi('吕布', ji)
    lb.show_me()
    # print(ji.wname, ji.wtype, ji.liliang)
    print('武器:', lb.wuqi.wname, lb.wuqi.wtype, lb.wuqi.liliang)

    mao = Wuqi(wname='丈八蛇矛', wtype='物理伤害', liliang=90, zhili=0)
    zf = ZhanShi('张飞', mao)
    zf.show_me()
    # print(mao.wname, mao.wtype, mao.liliang)
    print('武器:', zf.wuqi.wname, zf.wuqi.wtype, zf.wuqi.liliang)

    shan = Wuqi(wname='羽扇', wtype='魔法伤害', liliang=0, zhili=100)
    km = FaShi('孔明', shan)
    km.show_me()
    print('武器:', km.wuqi.wname, km.wuqi.wtype, km.wuqi.zhili)
