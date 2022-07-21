## 1.创建一个React应用

##### 命令行输入 npx create-react-app my-app

## 2.vsCode常用插件

- **Simple React Snippets**  **React 常用命令**
- **Path Intellisense** **路径自动补全**
- **AUTO Close Tag** **自动补全标签**

## 3.箭头函数

```*
onClick={function() { alert('click'); }}
{/* 替换为 */}
onClick={() => alert('click')}
```

## 4.使用父组件去控制多个子组件

**当你遇到需要同时获取多个子组件数据，或者两个组件之间需要相互通讯的情况时，需要把子组件的 state 数据提升至其共同的父组件当中保存。之后父组件可以通过 props 将状态数据传递到子组件当中。这样应用当中所有组件的状态数据就能够更方便地同步共享了。**