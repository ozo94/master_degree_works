# 数据接口的完成
>为企业提供数据，存在两种模式（本次使用的是后一种方法）
- 企业数据接口完成，向对应url提交json数据流(post)
- 构建自己的接口程序（服务器上线），提供账号密码来返回数据给申请者

>本文使用了flask框架，数据接口是需要可视化网页的  

- [详细的讲解参考地址](http://blog.csdn.net/u010098331/article/details/52781081)

>通过命令模拟向指定的url传入json数据，api接收指定数据后，会将其按照格式存入数据库中去的
```
curl -i -H "Content-Type: application/json" -X POST -d "{""account"":""lm"",""password"":""lm12345""}"\
http://localhost:5000/todo/api/v1.0/tasks
```
