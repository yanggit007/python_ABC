import time
import datetime
import calendar

# 时间戳timestamp: 格林尼治1970年1月1日0时0分0秒的时间偏移量，总秒数
# 结构化时间struct_time: 含9个时间属性的struct_time类 | 9个字段的元组
# 格式化时间str_time: 可读字符串（24个字符固定格式的字符串 | 自定义字符串）
# 三者可相互转化，结构化时间是桥梁。

# 实时时间戳
print(time.time())                                         # 无参数，返回一个浮点数
print('%f' % time.time())                                  # 这种表达式默认保留6个小数点的字符串

# 时间戳 --> 结构化时间 （得到的是time_struct实例对象）
print(time.gmtime())        # 执行结果：time.struct_time(tm_year=2021, tm_mon=12, tm_mday=1,
print(time.gmtime(0))       # tm_hour=13, tm_min=48, tm_sec=10, tm_wday=2, tm_yday=335, tm_isdst=0)
print(time.gmtime(3600))

print(time.localtime())
print(time.localtime(0))
print(time.localtime(3600))

# 结构化时间 --> 字符串时间 （两种结构化形式 --> 两种字符串格式）
print(time.asctime((2021, 12, 1, 9, 21, 50, 2, 335, 0)))   # 执行结果：Wed Dec  1 09:21:50 2021
print(time.asctime(time.gmtime()))                         # 执行结果：Wed Dec  1 13:20:51 2021
print(time.asctime(time.localtime()))                      # 执行结果：Wed Dec  1 21:20:51 2021

print(time.strftime('%Y-%m-%d %H:%M:%S', (2021, 12, 1, 9, 21, 50, 2, 335, 0)))
print(time.strftime('%c', time.gmtime()))                  # 执行结果：Wed Dec  1 13:20:51 2021
print(time.strftime('%X %x %Z %W %w %p %j %A %B', time.localtime()))

# 字符串时间 --> 结构化时间 （两个参数必须对应才能解析parsing，解析结果是完整的time_struct类）
print(time.strptime('Wed Dec  1 09:55:30 2021', '%c'))
print(time.strptime('2021-12-01 09:21:50', '%Y-%m-%d %H:%M:%S'))
print(time.strptime('12/01/21 中国标准时间 48 3 PM 335', '%x %Z %W %w %p %j'))

# 结构化时间 --> 时间戳
print(time.mktime((2021, 12, 1, 9, 21, 50, 2, 335, 0)))    # 执行结果：1638321710.0
print(time.mktime(time.gmtime()))                          # 执行结果：1638336051.0
print(time.mktime(time.localtime(3600)))                   # 执行结果：3600.0

# 时间戳 --> 字符串时间 （返回本地时间字符串，没有相反过程的函数）
print(time.ctime())                                        # 执行结果：Wed Dec  1 21:20:51 2021
print(time.ctime(0))                                       # 执行结果：Thu Jan  1 08:00:00 1970
print(time.ctime(3600))                                    # 执行结果：Thu Jan  1 09:00:00 1970

# sleep函数可推迟调用程序
print('Start :\t %s' % time.ctime())
time.sleep(2)
print('End :\t %s' % time.ctime())


# datetime的date对象 （初始化需要三个参数：year, month, day）
print(datetime.date(2018, 7, 1))                           # 执行结果：2018-07-01
print(datetime.date.today())                               # 执行结果：2021-12-01
print(datetime.date.today().weekday())                     # 执行结果：2  今天星期几，0是星期一
print(datetime.date.today().isoweekday())                  # 执行结果：3  今天星期几，1是星期一

print(datetime.date(2018, 7, 1).isoformat())               # 执行结果：2018-07-01 固定像str'%04d-%02d-%02d'格式
print(datetime.date(2018, 7, 1).strftime('%Y-%m-%d'))      # 执行结果：2018-07-01 自定义
print(datetime.date(2018, 7, 1).strftime('%y-%m-%d'))      # 执行结果：18-07-01

# datetime的time对象 （初始化参数：hour, minutes, 秒，微秒，时区等……都有默认值。）
print(datetime.time())                                     # 执行结果：00:00:00
print(datetime.time(8, 23, 46))                            # 执行结果：08:23:46
print(datetime.time(hour=8, second=46))                    # 执行结果：08:00:46

print(datetime.time.min)                                   # 执行结果：00:00:00
print(datetime.time.max)                                   # 执行结果：23:59:59.999999
print(datetime.time.resolution)                            # 执行结果：0:00:00.000001

print(datetime.time(hour=8, second=7).isoformat())         # 执行结果：08:00:07 打印time调用的就是这个方法
print(datetime.time(hour=16, second=7, microsecond=123).strftime('%H:%M:%S'))        # 执行结果：16:00:07
print(datetime.time(hour=16, second=7, microsecond=123).strftime('%p %I:%M:%S:%f'))  # 执行结果：PM 04:00:07:000123

# datetime的datetime对象 （date和time的结合，参数也是二者的结合，年月日必需，其余可选。）
print(datetime.datetime(year=2018, month=7, day=1, hour=16, second=10))    # 执行结果：2018-07-01 16:00:10
print(datetime.datetime.today())                                           # 执行结果：2021-12-01 21:20:53.603140
print(datetime.datetime.now())                                             # 执行结果：2021-12-01 21:20:53.603159
print(datetime.datetime.now(datetime.timezone.utc))                        # 执行结果：2021-12-01 13:20:53.603174+00:00
print(datetime.datetime.utcnow())                                          # 执行结果：2021-12-01 13:20:53.603203
print(datetime.datetime.fromtimestamp(time.time()-36000))                  # 执行结果：2021-12-01 11:20:53.603216

print(datetime.datetime.now().date())                                      # 执行结果：2021-12-01
print(datetime.datetime.now().time())                                      # 执行结果：21:20:53.603244

d1 = datetime.date(2018, 7, 1)
t1 = datetime.time(8, 15, 10)
dt = datetime.datetime.combine(d1, t1)
print(d1)                                                                  # 执行结果：2018-07-01
print(t1)                                                                  # 执行结果：08:15:10
print(dt.strftime('%Y-%m-%d %H:%M:%S'))                                    # 执行结果：2018-07-01 08:15:10
print(dt.strftime('%y-%m-%d %a %I:%M:%S'))                                 # 执行结果：18-07-01 Sun 08:15:10

# datetime的timedelta对象 （求日期时间差，参数：日期，秒，微秒，毫秒，分钟，小时和星期。默认值0）
dtx = datetime.timedelta(hours=1.5, weeks=-2)
dt1 = datetime.datetime(2018, 7, 1, 16, 15, 10)
dt2 = dt1 + dtx
print(dtx, type(dtx))                  # 执行结果：-14 days, 1:30:00 <class 'datetime.timedelta'>
print(dt1, type(dt1))                  # 执行结果：2018-07-01 16:15:10 <class 'datetime.datetime'>
print(dt2, type(dt2))                  # 执行结果：2018-06-17 17:45:10 <class 'datetime.datetime'>
print(dt2 - dt2)                       # 执行结果：0:00:00 <class 'datetime.timedelta'>
print(dt2 - dt1)                       # 执行结果：-14 days, 1:30:00 <class 'datetime.timedelta'>
print(dt1 - dt2)                       # 执行结果：13 days, 22:30:00 <class 'datetime.timedelta'>

# datetime的tzinfo对象 （tzinfo类不能直接使用，由datetime.timezone生成）
dti = datetime.timezone.utc            # 实现了UTC时区的tzinfo实例，本质上是datetime.timezone(datetime.timedelta(0))
print(dti, type(dti))                  # 执行结果：UTC <class 'datetime.timezone'>

china_timezone = datetime.timezone(datetime.timedelta(hours=8))
utc_timezone = datetime.timezone(datetime.timedelta(hours=0))

china_time = datetime.datetime.now(china_timezone)
utc_time = datetime.datetime.now(utc_timezone)

print(china_time, type(china_time))        # 执行结果：2021-12-01 21:20:53.603504+08:00 <class 'datetime.datetime'>
print(utc_time, type(utc_time))            # 执行结果：2021-12-01 13:20:53.603508+00:00 <class 'datetime.datetime'>


# calendar的isleap方法：是否是闰年
print(calendar.isleap(2021))               # 执行结果：False
print(calendar.isleap(2020))               # 执行结果：True

# calendar的leapdays方法：两个年份之间闰年的总数
print(calendar.leapdays(1900, 2000))       # 执行结果：24
print(calendar.leapdays(2021, 2000))       # 执行结果：-6

# calendar的month方法：标准单月历 （w:width宽度, l:length高度）
print(calendar.month(theyear=2021, themonth=12))
print(calendar.month(theyear=2021, themonth=12, w=3, l=0))
print(calendar.month(theyear=2021, themonth=12, w=3, l=3))

# calendar的monthcalendar方法：单月历（列表形式）
# 接收两上参数，返回一个列表，列表每项也是一个列表，一周一个列表，月外日期为0
print(calendar.monthcalendar(year=2021, month=12))

# calendar的monthrange方法：返回一个两字段元组，2表示本月第一天是周三，31表示本月有31天
print(calendar.monthrange(year=2021, month=12))               # 执行结果：(2, 31)

# calendar的monthrange方法：返回某天是星期几，0表示星期一
print(calendar.weekday(year=2021, month=12, day=1))           # 执行结果：2

# calendar的calendar方法：标准年历 （c:横向两月之间的距离；m:打算把几个月放一排，默认是3）
print(calendar.calendar(2020))
print(calendar.calendar(theyear=2021, w=2, l=1, c=6, m=3))    # 后四个参数是默认值


# 附录：
# 第三方库：dateutil日期工具，为datetime提供了强大的扩展。内有两个比较常用的模块：parser和rrule
# 安装：pip install python-dateutil
