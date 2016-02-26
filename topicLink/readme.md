说明：

1.getWordLink.py：对每个cluster内的topic，遍历每两个topic的每对word、word2，getEdge方法获取word与word2之间的边，分为三种情况：word是word2的上位词、word2是word的上位词、word和word2有共同的上位词（计算topic之间关系时，过滤掉这种情况）。由于word和word2可能对应多个synset，因而同义词深度量化得到的最低公共节点可能为多个，取min_depth最大的synset。结果中word和word2之间仅有一种关系。

结果存储到vccfinder数据库的表wordLink中：

-- 
-- Table structure for table `wordLink` 
-- 

DROP TABLE IF EXISTS `wordLink`; 
/*!40101 SET @saved_cs_client     = @@character_set_client */; 
/*!40101 SET character_set_client = utf8 */; 
CREATE TABLE `wordLink` ( 
  `id` int(11) NOT NULL AUTO_INCREMENT, 
  `cluster` varchar(45) DEFAULT NULL, 
  `start` varchar(45) , 
  `end` varchar(45) , 
  `edge` varchar(255), 
  `depth` int(11) DEFAULT NULL, 
  PRIMARY KEY (`id`), 
  KEY `cluster_index` (`cluster`) 
) ENGINE=InnoDB AUTO_INCREMENT=11062247 DEFAULT CHARSET=utf8mb4;

可通过
SELECT cluster,start,end,count(*) FROM vccfinder.wordLink where start like '#%' group by cluster,start,end;
查看两个topic之间的weight（count值）。

2.makeGraphSingle.py：对每个cluster，count作为weight，绘制有向图。（不够精确，无法显示weight）
