# seanborn库常用接口文档（自用）
**1）、seaborn.set(\*args,\*\*kwargs)函数**
- seaborn.set_theme(context='notebook', style='darkgrid', palette='deep', font='sans-serif', font_scale=1, color_codes=True, rc=None)

|    参数           |                   说明                        |
|-------------------|-----------------------------------------------|
|   context         |改变图的元素大小：paper, notebook, talk, poster     
|   style           |主题风格：darkgrid, whitegrid, dark, white, ticks
|   palette         |返回定义调色板的颜色列表或连续颜色图：deep, muted, bright, pastel, dark, colorblind
|   font            |Font family, see matplotlib font manager.
|   font_scale      |总体字号大小
|   color_codes     |If True and palette is a seaborn palette, remap the shorthand color codes (e.g. “b”, “g”, “r”, etc.) to the colors from this palette.
|   rc              |Dictionary of rc parameter mappings to override the above.

**2）、seaborn.lmplot()绘制回归图函数**
- seaborn.lmplot(x, y, data, hue=None, col=None, row=None, palette=None, col_wrap=None, height=5, aspect=1, markers='o', sharex=True, sharey=True, hue_order=None, col_order=None, row_order=None, legend=True, legend_out=True, x_estimator=None, x_bins=None, x_ci='ci', scatter=True, fit_reg=True, ci=95, n_boot=1000, units=None, order=1, logistic=False, lowess=False, robust=False, logx=False, x_partial=None, y_partial=None, truncate=False, x_jitter=None, y_jitter=None, scatter_kws=None, line_kws=None, size=None)

|    参数           |                   说明                        |
|-------------------|-----------------------------------------------|
|   x, y, data,     |x，y轴数据，和总数据输入
|   aspect          |控制图的长宽比
|   sharex          |共享x轴刻度（默认为True）
|   sharey          |共享y轴刻度（默认为True）
|   col             |根据所指定属性(有输入数据中选择)在列上分类
|   row             |根据所指定属性在行上分类
|   hue             |用于分类，如hue="sex"
|   ci              |控制回归的置信区间.ci=0.95#采用α=0.95的置信区间
|  x_jitter/y_jitter|给x/y轴随机增加噪音点 不影响最后的回归直线
|   order           |控制进行回归的幂次（一次以上即是多项式回归）
|   markers         |散点标志，列表中的标志会与hue中的变量对应hue="smoker"，markers=["o", "x"]   
|   size            |散点大小，已被height代替
|   fit_reg         |是否开启线性回归