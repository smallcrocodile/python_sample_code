#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# cate,sy,jine,tmpstr,tmp.tmpun,int等等都是什么?

# 定义一个函数用来，money参数传入钱数
def zhaoqian(money):

    loop = True

    # tmp 是字符串变量，用来显示输出钱的总金额是多少元
    tmp = ['总金额：' + str(money) + '元']

    # cate 元组，存放钱的面值列表 单位：元
    cate = (100,
            50,
            20,
            10,
            5,
            1,
            0.5,
            0.1)
    # sy 是整数型变量 把钱数 X 10后 int（）函数转换成整数
    sy = int(money * 10)
    while loop:
        if sy == 0:
            # 如果钱数为0 就把loop设成False，用来结束while循环
            loop = False
        else:
            # 钱数不为0则：
            for row in cate:
                tmpStr = ''
            jine = int(row * 10)
            if jine >= 10:
                tmpUn = '元'
            else:
            tmpUn = '角'
            if sy >= jine and tmpStr == '':
                m = sy // jine
            sy = sy % jine
            if jine >= 10:
                tmpStr = str(jine // 10) + tmpUn + str(m) + '张'
            else:
            tmpStr = str(jine) + tmpUn + str(m) + '张'
            tmp.append(tmpStr)
            return tmp

a = zhaoqian(59153.8)
for x in a:
    print x