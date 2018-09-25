
1.Web浏览器发送HTTP请求到服务端，被Controller(Servlet)获取并进行处理（例如参数解析、请求转发）

2.Controller(Servlet)调用核心业务逻辑——Model部分

3.Model进行数据库存取操作，并将操作结果返回给Model

4.Controller(Servlet)将业务逻辑处理结果交给View（JSP），动态输出HTML内容

5.动态生成的HTML内容返回到浏览器显示

Spring MVC提供了一个DispacherServlet（可以Spring MVC是以Servlet技术为基础的），
这个Servlet把Web应用中Servlet中经常要实现的功能封装起来并提供一层公共抽象，
想象对应于一个Web请求后端要做的事情，比如：

URL映射（对应HTTP URL和方法，应该调用什么代码）
权限验证（当前的URL是否允许当前用户访问）
参数解析（如何从Servlet中获得参数）
数据绑定（如何将Servlet中的参数，绑定到业务逻辑对象中）
数据验证（判断数据是否符合业务规则，比如邮件格式是否正确）
视图解析（使用哪个视图模板进行渲染）
模型传递与视图渲染（将数据传递给模板，并且在模板中引用）
...


Hibernate是一个Java ORM开发框架
ORM是Object Relation Mapping的缩写，顾名思义，即对象关系映射。
ORM是一种以面向对象的方式来进行数据库操作的技术。
Web开发中常用的语言，都会有对应的ORM框架。
而Hibernate就是Java开发中一种常用ORM框架，另一个现在流行的ORM框架是Mybatis。


而ORM的作用就非常直观了，无须赘述，它提供了与数据库操作的一层中间抽象，这样Model的代码自然会更加简单。
Spring MVC基本可以帮你屏蔽Servlet的API，ORM则可以帮你屏蔽JDBC的API了，
也就是说你在更高的抽象层次上写程序了，更高的抽象层次一般意味着以更符合我们思维的方式来思考，
自然效率更高。这事实上是软件技术发展的一个重要驱动力之一。
你想想，从汇编语言发展出高级语言，从文件系统发展出数据库，其实本质规律是类似的。
