## Mybatis

#### 依赖：

```
<!-- Mysql -->
<dependency>
    <groupId>mysql</groupId>
    <artifactId>mysql-connector-java</artifactId>
    <version>8.0.16</version>
</dependency>

<!-- Mybatis -->
<dependency>
    <groupId>org.mybatis.spring.boot</groupId>
    <artifactId>mybatis-spring-boot-starter</artifactId>
    <version>2.2.0</version>
</dependency>

<dependency>
    <groupId>org.apache.tomcat</groupId>
    <artifactId>tomcat-jdbc</artifactId>
    <version>8.0.23</version>
</dependency>
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-jdbc</artifactId>
</dependency>
```

#### 配置文件：

```
spring:
  datasource:
    driver-class-name: com.mysql.cj.jdbc.Driver
    url: jdbc:mysql://127.0.0.1:3306/test?useUnicode=true & characterEncoding=utf-8 &
      useSSL=true & serverTimezone=Asia/Shanghai
    username: root
    password: 330825
    type: com.alibaba.druid.pool.DruidDataSource

mybatis:
  mapper-locations: classpath:/mapper/*.xml
  type-aliases-package: com.spring.zsx.entity
```

在使用com.mysql.cj.jdbc.Driver后，我们需要在url添加时区为Asia/Shanghai

mapper-locations：mapper存放地址

type-aliases-package：实体类地址

#### 整体框架：

![image-20220104225426020](C:\Users\zsx\AppData\Roaming\Typora\typora-user-images\image-20220104225426020.png)

controller层负责具体的业务模块流程的控制
entity层用于存放我们的实体类，与数据库中的属性值基本保持一致，实现set和get的方法
dao层主要是做数据持久层的工作，负责与数据库联络，封装了增删改查基本操作
service层主要负责业务模块的逻辑应用设计，具体要调用到已定义的DAO层的接口
<img src="https://img-blog.csdnimg.cn/20200721224827284.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQyNTgyNDg5,size_16,color_FFFFFF,t_70#pic_center" alt="s6" style="zoom:50%;" />

用户从页面前端，也就是我们所说的 view 层进行查询访问，进入到 controller 层找到对应的接口，接 着 controller 进行对 service 层进行业务功能的调用，service 要进入 dao 层查询数据，dao 层调用 mapper.xml 文件生成 sql 语句到数据库中进行查询。

在数据库中查询到数据，dao 层拿到实体对象的数据，接着交付给 service 层，接着 service 进行业务 逻辑的处理，返回结果给 controller，controller 根据结果进行最后一步的处理，返回结果给前端页 面。

创建一个访问用户信息的流程为：entity->dao->mapper->service->controller，这里 mapper 指的是存放 SQL 语句的 xml 文件。

**所有Dao层中的方法，都需要在mapper的xml文件中进行手动写入，并且xml中的namespace需要改成自己的dao层文件*

**相关链接：https://blog.csdn.net/qq_42582489/article/details/107500836?spm=1001.2014.3001.5501**

## Mybatis-Plus

#### 依赖：

```
<!-- Mysql -->
<dependency>
    <groupId>mysql</groupId>
    <artifactId>mysql-connector-java</artifactId>
    <version>8.0.16</version>
</dependency>


<!-- Mybatis-plus -->
<dependency>
    <groupId>com.baomidou</groupId>
    <artifactId>mybatis-plus-boot-starter</artifactId>
    <version>3.4.3</version>
</dependency>
<dependency>
    <groupId>com.alibaba</groupId>
    <artifactId>druid</artifactId>
    <version>1.2.8</version>
</dependency>
<dependency>
    <groupId>org.apache.tomcat</groupId>
    <artifactId>tomcat-jdbc</artifactId>
    <version>8.0.23</version>
</dependency>
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-jdbc</artifactId>
</dependency>
```

#### 配置文件：

```
spring:
  datasource:
    driver-class-name: com.mysql.cj.jdbc.Driver
    url: jdbc:mysql://127.0.0.1:3306/test?useUnicode=true & characterEncoding=utf-8 &
      useSSL=true & serverTimezone=Asia/Shanghai
    username: root
    password: 330825
    type: com.alibaba.druid.pool.DruidDataSource
```

与Mybatis相比只是多了一个Type

#### 整体框架：

![image-20220104230152818](C:\Users\zsx\AppData\Roaming\Typora\typora-user-images\image-20220104230152818.png)

我们只需要在entity中添加我们的实体类

![image-20220104230226066](C:\Users\zsx\AppData\Roaming\Typora\typora-user-images\image-20220104230226066.png)

@TableName 实体类相对应的表名

@TableId 主键

@TableFiedl 其他列名



并且UserDao继承`public interface UserDao extends BaseMapper<User>` ，这样就可以调用Mybatis-Plus它支持的较为简单的增删改查，以及分页操作。

但是分页操作我们需要自己注入分页的Bean才能得到得到的total总数

```java
@Bean
public MybatisPlusInterceptor mybatisPlusInterceptor() {
    MybatisPlusInterceptor interceptor = new MybatisPlusInterceptor();
    interceptor.addInnerInterceptor(new PaginationInnerInterceptor(DbType.MYSQL));
    return interceptor;
}
```