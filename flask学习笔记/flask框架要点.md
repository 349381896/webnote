1、flsk的Context机制
    -Flask框架中有许多魔法将Web应用开发者与一些细节隔离开来，其中Context机制又是有别于其他框架的，这个机制让开发人员在处理web请求时可以非常简单的获取上下文
    -flask提供4个机制
        -Context机制实现了应用上下文（App Context）
        -请求上下文（Request Context）
        -session
        -g