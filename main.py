#! /bin/usr/env python3

import re

'''
data_f    由chinese open wordnet提供的同义词集数据
code_senses 一个集合，用来存放data文件中名词性词语的编码和词义，编码为key，词义列表为value
lmf_f     xml格式的文档，存放了每个synset的信息，包括词语间的关系
word_hype 由编码组成的集合，从xml中匹配得到的synset及其上位词的编码信息，synset的编码为key，上位词的编码列表为value
word_hypo 记录下位词
res_f     结果输出文件，每一行由下位词和上位词组成，中间用Tab键隔开
'''

data_f='./wn-data-cmn.tab'
code_senses={}
lmf_f='./wn-cmn-lmf.xml'
word_hype={}
word_hypo={}
res_lst=[]
res_f='./result2.txt'

#过滤data文件中的词语，保留名词性词语，保存到code_senses中
with open(data_f,'r') as f:
	for line in f.readlines():
		res=line.split()
		if len(res)>=3 and res[0][-1]=='n':
			code=res[0]
			senses=res[2:]
			if code in code_senses.keys():
				for sense in senses:
					code_senses[code].append(sense)
			else:
				code_senses[code]=senses


#正则匹配lmf文档，获得文档中描述的信息，获得synset的编码及其上位词的编码，存放的word_hype中
with open(lmf_f,'r') as f:
	#读lmf文档
	lmf=f.read()
	#定义正则表达式进行文档匹配;pattern1匹配每个同义词，pattern2匹配同义词中的上位词,pattern3匹配下位词
	pattern1=re.compile(r'''<Synset id='cmn-10-(?P<synset_code>.*-n)' baseConcept='3'>\n.*<SynsetRelations>\n.*(\n|.)*?</SynsetRelations>(\n|.)*?</Synset>''')
	pattern2=re.compile(r'''<SynsetRelation targets='cmn-10-(?P<hype_code>.*-n)' relType='hype'/>''')
	pattern3=re.compile(r'''<SynsetRelation targets='cmn-10-(?P<hypo_code>.*-n)' relType='hypo'/>''')
	lst=pattern1.finditer(lmf)
	for res in lst:
		synset_code=res.group('synset_code')
		hype_code_lst=[]
		hypo_code_lst=[]

		#保存上位词编码列表
		for hype in pattern2.finditer(res.group()):
			hype_code=hype.group('hype_code')
			if hype_code not in hype_code_lst:
				hype_code_lst.append(hype_code)
		if len(hype_code_lst)>0:
			word_hype[synset_code]=hype_code_lst
		
		#保存下位词编码列表
		for hypo in pattern3.finditer(res.group()):
			hypo_code=hypo.group('hypo_code')
			if hypo_code not in hypo_code_lst:
				hypo_code_lst.append(hypo_code)
		if len(hypo_code_lst)>0:
			word_hypo[synset_code]=hypo_code_lst


#遍历word_hype，将synset_code与hype_code的编码与code_word中的信息对应，获得synset和hype,写入文件
for synset_code in word_hype.keys():
	if synset_code in code_senses.keys():
		synset=code_senses[synset_code][0]	
		for hype_code in word_hype[synset_code]:
			if hype_code in code_senses.keys():
				hype=code_senses[hype_code][0]
				if synset==hype:
					continue
				pair=[synset,hype]
				if pair not in res_lst:
					res_lst.append(pair)	

for synset_code in word_hypo.keys():
	if synset_code in code_senses.keys():
		synset=code_senses[synset_code][0]
		for hypo_code in word_hypo[synset_code]:
			if hypo_code in code_senses.keys():
				hypo=code_senses[hypo_code][0]
				if synset==hypo:
					continue
				pair=[hypo,synset]
				if pair not in res_lst:
					res_lst.append(pair)

with open(res_f,'a') as o:
	for pair in res_lst:
		o.write(pair[0])
		o.write('\t')
		o.write(pair[1])
		o.write('\n')
