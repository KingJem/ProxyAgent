#  需求说明

1. 根据API和浏览器返回不同的数据 浏览器端返回管理界面
2. 支持返回http https 高匿 透明 和匿名代理
3. 全局设置
4. 支持http 和https的代理验证
5. 根据不同的标签返回数据
6. 根据配置信息可以爬取做到定时爬取和爬取间隔配置



# 初始化db

```python 
python manage.py shell
>> from app import db
>> db.create_all()
```

# 启动服务

``` python
python manage.py runserver -h 0.0.0.0 -p 8888
#其他参数
python manage.py runserver -?
```

# 配置数据库
``` python
`SQLALCHEMY_DATABASE_URI = 'mysql://user:password@host:port/dbname'`
```

