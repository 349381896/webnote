1-详情介绍例程：
    -Flask-APScheduler定时任务查询操作数据库（多文件/模块）           https://blog.csdn.net/arnolan/article/details/84936075
    -python3+flask 开发web(九)——flask_apscheduler定时任务框架        https://blog.csdn.net/weixin_39430584/article/details/83509237
    -基于Flask-APScheduler实现添加动态定时任务                       https://www.cnblogs.com/zhangliang91/p/11603916.html

# 2-触发方式（trigger）：
## cron定时调度
        -month      (int|str)                   – 月（1-12）
        -day        (int|str)                   – 日（1-31）
        -year       (int|str)                   – 4位数年份
        -week       (int|str)                   – ISO week (1-53)
        -day_of_week (int|str)                  – 工作日的编号或名称（0-6或周一、周二、周三、周四、周五、周六、周日）
        -hour       (int|str)                   – hour (0-23)
        -minute     (int|str)                   – minute (0-59)
        -second     (int|str)                   – second (0-59)
        -start_date (datetime|str)              – 最早可能触发的日期/时间（包括）
        -end_date   (datetime|str)              – 最晚可能触发的日期/时间（包括）
        -timezone   (datetime.tzinfo|str)       – 用于日期/时间计算的时区（默认为计划程序时区）

## interval间隔调度（循环）：
        -weeks      (int)           – number of weeks to wait
        -days       (int)           – number of days to wait
        -hours      (int)           – number of hours to wait
        -minutes    (int)           – number of minutes to wait
        -seconds    (int)           – number of seconds to wait
        -start_date (datetime|str)  – 间隔计算的起点
        -end_date   (datetime|str)  – 最晚可能触发的日期/时间
        -timezone   (datetime.tzinfo|str) – 用于日期/时间计算的时区

        
    -date定时调度：最基本的一种调度，作业只会执行一次。
        -run_date (datetime|str)        – the date/time to run the job at
        -timezone (datetime.tzinfo|str) – time zone for run_date if it doesn’t have one already  
## 部署注意：不可以将下列初始化放__main__下
        -scheduler.init_app(app)  #初始化定时任务调度   
            scheduler.start()
            