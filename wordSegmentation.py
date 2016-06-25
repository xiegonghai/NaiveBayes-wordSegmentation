#朴素贝爷斯分词(含义是分词后，得分的假设是基于两词之间是独立的，后词的出现与前词无关)
# p[i][n]表示从i到n的句子的最佳划分的得分,我们用dp表达式p[i][n]=max(freq(s[i:k])+p[k][n])
# 依次求出长度为1,2,3,n的句子划分，那么p[0][n]便是最佳划分结果,用t[i]表示产生的最佳划分每次向前走几个字符
import math
d = {}
log = lambda x: float('-inf') if not x else math.log(x) #匿名函数
prob = lambda x: d[x] if x in d else 0 if len(x)>1 else 1

def init(filename='SogouLabDic.dic'):
    d['_N_'] = 0.0
    with open(filename, 'r',encoding='gb18030') as handle:
        for line in handle:
            #print(line)
            word, freq = line.split('\t')[0:2]  #取list的前2个元素,词和相应的词数
            d['_N_'] += int(freq)+1             # 此表的词频总和,每个词数都加1    
            try:
                #print('utf')
                d[word.decode('utf-8')] = int(freq)+1 #词数加1
            except:
                #print('gbk')
                try:
                    d[word] = int(freq)+1            #词数加1
                except:
                    print(word)
                    break
def solve(s):
    l = len(s)
    p = [0 for i in range(l+1)] #1,2,...,l位置为0
    t = [0 for i in range(l)]
    # 如'大床房多少钱'，当前位置到末尾分别为1,2,...l长度的词，t[i]保留从当前位置向前划分的最佳长度，比如从'大'开始，
    #大床最佳，或大床房最佳，取决词库
    for i in range(l-1, -1, -1): #start,stop，step
        # prob(s[i:i+k])/d['_t_']为词表词频度
        p[i], t[i] = max((prob(s[i:i+k])/d['_N_']+p[i+k], k)#在一个二元组列表里返回第一个元素最大的二元组,
                         for k in range(1, l-i+1))
    dis = 0
    while dis<l:  #dis=0,不断向前遍历分割词汇
        yield s[dis:dis+t[dis]]
        dis += t[dis]
    
if __name__ == '__main__':
    init()
    st='中国人都爱中华人民共和国'
    #st2='大床房多少钱'
    print(len(st))
    lpp=list(solve(st))
    for o in range(len(lpp)):
        print(lpp[o])
    print (' '.join(list(solve(st))))
