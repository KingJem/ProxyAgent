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



# 遇到的问题
   1. apscheduler 虽然有可以支持异步的调度器,但是本身sqlalchemy 不支持异步,有支持异步
   orm框架可以使用,但是在视图函数中的使用orm查询数据的时候,会出现同步的视图函数步骤和异步的
   orm 操作,这样Python解释器就会把异步的代码全部变成同步的代码,最后异步函数就相当于没有写一样
   2. 使用requests+gevent 或者多进程多线程的方式加速爬取,加速验证
   3. flask 的orm框架依赖flask的上下文来运行db运行会丢失上下文环境,sqlalchemy 的实例化在不同的地方被导入
   导致程序运行的时候循环导入
 