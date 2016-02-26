总结

程序说明：
1.首先对commit中message处理为去掉除#以外标点的文本，进行分词，并取得词干后保存到commits_words表中：changeMessToWords.py；
2.对commits_words表中message首先计算tfidf，得到对应的向量；然后对文本构成的向量使用scikit-learn包中的MiniBatchKMeans方法聚类：MiniBatchKMeans.py。

MiniBatchKMeans的选取原因：
实际使用kmeans++聚类，选取尽可能远的中心点，MiniBatchKMeans实现批量聚类，缩短聚类时间，相比kMeans会有较小的误差。

k值的确定：
inertia用来评估簇的个数是否合适，距离越小说明簇分的越好，选取临界点的簇个数；为了尽可能选取合适的k值，需要多次试验，inertia随着k的增大而减小，折线图应为下降先快后慢，取中间拐点处，即为最适合的k值。（目前由于运行时间原因，还未找到比较合适的k值）

数据库表结构：
见vccfinder.sql。

对commit聚类后语义的分析思路：
除了commit中message的相似性，可能有：作者、对应的issue_id、是否为bug、提交人、更改方式（add、delete、change）、时间上是否接近、是否相同repos（受到repos中commit数量的影响）的影响。

对于代码的语义分析思路：
经过查阅资料，初步觉得是否可以借鉴代码搜索引擎、代码克隆检测的方法。
