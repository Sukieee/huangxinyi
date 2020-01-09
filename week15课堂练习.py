#!/usr/bin/env python
# coding: utf-8

# In[4]:


text = "在尼比鲁星球探查期间，企业号舰长柯克为营救史波克采取了胆大妄为的举动，几乎危及全舰队员的生命，他也为此付出代价。"

# snownlp
from snownlp import SnowNLP
doc = SnowNLP(text)
doc.words


# In[ ]:


# 准确率(precision) 准确率（P）＝切分结果中正确分词数/切分结果中所有分词数*100%
# p = 20/32*100%
#   = 62.5%

#召回率(recall) 召回率（R）＝切分结果中正确分词数/标准答案中所有分词数*100%
# R = 20/26*100%
#   = 76.92%

#F-评价(F-measure 综合准确率和召回率的评价指标 ) F-指标＝2PR/(P+R)
# F = 2*62.5%*76.92/(62.5%+76.92%)
#   = 0.6896


# In[5]:


# jieba
import jieba
words = jieba.cut(text)
[w for w in words]


# In[ ]:


# 准确率(precision) 准确率（P）＝切分结果中正确分词数/切分结果中所有分词数*100%
# p = 20/27*100%
#   = 74.07%

#召回率(recall) 召回率（R）＝切分结果中正确分词数/标准答案中所有分词数*100%
# R = 20/26*100%
#   = 76.92%

#F-评价(F-measure 综合准确率和召回率的评价指标 ) F-指标＝2PR/(P+R)
# F = 0.7547


# In[ ]:


# stanfordcorenlp
from stanfordcorenlp import StanfordCoreNLP
nlp = StanfordCoreNLP('http://localhost',port=2002)
nlp.word_tokenize(text)


# In[ ]:


# 准确率(precision) 准确率（P）＝切分结果中正确分词数/切分结果中所有分词数*100%
# p = 100%

#召回率(recall) 召回率（R）＝切分结果中正确分词数/标准答案中所有分词数*100%
# R = 100%

#F-评价(F-measure 综合准确率和召回率的评价指标 ) F-指标＝2PR/(P+R)
# F = 1

