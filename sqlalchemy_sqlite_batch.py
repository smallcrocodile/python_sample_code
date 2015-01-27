#!/usr/bin/env python 
# -*- coding: utf-8 -*- 

 # -*- coding: utf-8 -*-

import sqlalchemy as sa

# 用Sqlite做例子,别的数据库连接字符串不同
engine = sa.create_engine('sqlite://', echo=True)
metadata = sa.MetaData()

# 假定这个是表结构
widgets_table = sa.Table('widgets', metadata,
    sa.Column('id', sa.Integer, primary_key=True),
    sa.Column('foo', sa.String(50)),
    sa.Column('bar', sa.String(50)),
    sa.Column('biz', sa.Boolean),
    sa.Column('baz', sa.Integer),
    )
metadata.create_all(engine)

# 假定这是你的数据结构,在一个list中每个元组是一条记录
values = [
    (None, "Test", True, 3),
    (None, "Test", True, 3),
    ]
# 主要是参考这部分如何批量插入
with engine.connect() as connection:
    with connection.begin() as transaction:
        try:
            markers = ','.join('?' * len(values[0]))
            # 按段数拼成makers = '(?,?,?,?)'
            ins = 'INSERT INTO {tablename} VALUES ({markers})'
            ins = ins.format(tablename=widgets_table.name, markers=markers)
            # 如果你的表已经存在了,widgets_table.name改成表名就行了.
            connection.execute(ins, values)
        except:
            transaction.rollback()
            raise
        else:
            transaction.commit()