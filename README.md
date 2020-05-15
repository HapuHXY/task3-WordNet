# 基于中文WordNet实现上下位关系自动抽取

## Chinese Open Wordnet 
http://compling.hss.ntu.edu.sg/omw/cgi-bin/wn-gridx.cgi?gridmode=cow
  * 英文WordNet是由Princeton 大学的心理学家，语言学家和计算机工程师联合设计的一种基于认知语言学的英语词典。
它不是光把单词以字母顺序排列，而且按照单词的意义组成一个“单词的网络”。
  * 名词，动词，形容词和副词各自被组织成一个同义词的网络，每个同义词集合都代表一个基本的语义概念，并且这些集合之间也由各种关系连接。
一个多义词将出现在它的每个意思的同义词集合中。
  * 名词网络的主干是蕴涵关系的层次(上位/下位关系)，它占据了关系中的将近80%。
层次中的最顶层是11个抽象概念，称为基本类别始点（unique beginners），例如实体（entity，“有生命的或无生命的具体存在”），心理特征（psychological feature，“生命有机体的精神上的特征）。
  * 42,315 synsets
  * 79,812 senses
  * 61,536 unique words
  
## Source 
  2014-01-23 (initial public beta release)
  * list of synset-lemma pairs (tab separated, zipped) http://compling.hss.ntu.edu.sg/omw/wns/cmn.zip
  * Wordnet LMF (zipped xml http://compling.hss.ntu.edu.sg/omw/wns/cmn+xml.zip

## 算法思想
  * 预处理wn-data-cmn.tab文件:保留文件中所有名词性词语的编号和词义    
  * 解析xml文档:利用正则匹配，对xml文档进行预处理，获得每个编号词语的上下位关系词 
  * 抽取上下位关系词对,存放到上下位关系数据集中

## References
Shan Wang and Francis Bond (2013)
      Building the Chinese Wordnet (COW): Starting from Core Synsets. In Proceedings of the 11th Workshop on Asian Language Resources: ALR-2013 a Workshop of The 6th International Joint Conference on Natural Language Processing (IJCNLP-6). Nagoya. pp.10-18.
      http://compling.hss.ntu.edu.sg/pdf/2013-alr-cow.pdf
      
      
