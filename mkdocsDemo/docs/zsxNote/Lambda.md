### 一、Lambda例：

````java
//使用Lambda前
Comparator<Apple> byweight = new Comparator<Apple>(){
    public int compare(Apple a1,Apple a2){
        return a1.getWeight().compareTo(a2.getWeight());
    }
};
//使用后
Comparator<Apple> byWeight = (Apple a1, Apple a2) -> a1.getWeight.compareTo(a2.getWeight())
````

### 二、Lambda的三个部分

- #### 参数列表（可以为空）

- #### 箭头（必须存在）

- #### Lambda主题（*要么是隐式的返回值 要么是 花括号框住的表达式）

![image-20220327220527815](C:\Users\zsx\AppData\Roaming\Typora\typora-user-images\image-20220327220527815.png)

## 函数式接口

**函数式接口就是只定义一个抽象方法的接口，接口现在还可以有默认方法（即在类没有对方进行实现时，其主体为方法提供默认实现的方法），哪怕有很多的默认方法，只要接口定义了一个抽象方法，它就是一个函数式接口**

### Lambda允许以内联的形式为函数式接口的抽象方法进行实现，并把整个表达式作为函数式作为函数式接口的实例(具体来说式函数式接口一个具体实现的实例)。

````java
public static void process(Runnable r){
    r.run();
} 
//使用Lambda
Runnable r1 = () -> System.out.println("Hello world 1");

//使用匿名类
Runnable r2 = new Runnable(){
    public void run(){
        system.out.println("Hello world 2");
    }
};

process(r1);
process(r2);
process(() -> System.out.println("Hello world 3"));
````

