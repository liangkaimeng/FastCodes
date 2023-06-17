# -*- coding: utf-8 -*-
# Author: lkm
# date: 2023/6/18 1:20

from pyecharts import options as opts
from pyecharts.charts import WordCloud

# 创建词云图的数据
data = [
    ("词语1", 100),
    ("词语2", 80),
    ("词语3", 60),
    ("词语4", 50),
    ("词语5", 40),
]

# 创建词云图
wordcloud = (
    WordCloud()
    .add("", data, word_size_range=[20, 100])
    .set_global_opts(title_opts=opts.TitleOpts(title="词云图示例"))
)

# 渲染生成HTML文件（可选）
wordcloud.render("wordcloud.html")
wordcloud.render_notebook()
