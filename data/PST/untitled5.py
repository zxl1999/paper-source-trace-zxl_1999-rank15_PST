import os
import json
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# 加载待处理的 JSON 数据
with open('paper_source_trace_train_ans.json', 'rb') as f:
    paper_data = json.load(f)

# 加载参考文献列表长度的 JSON 数据
with open('submission_example_valid_cp.json', 'rb') as f:
    reference_lengths = json.load(f)

# 初始化重要性分数字典
importance_scores = {}

for paper_info in paper_data:
    # 获取当前论文的 ID 和引用文献列表
    paper_id = paper_info['_id']
    references = paper_info['references']
    
    # 获取当前论文应有的参考文献列表长度
    expected_length = reference_lengths[paper_id]
    
    # 初始化当前论文的重要性分数列表
    paper_importance_scores = []
    
    # 遍历当前论文的引用文献列表
    for ref_id in references:
        # 检查参考文献是否存在于 paper-xml 文件夹中
        xml_filename = f'paper-xml/{ref_id}.xml'
        
        if os.path.exists(xml_filename):
            # 读取引用文献的内容
            with open(xml_filename, 'r', encoding='utf-8') as f:
                ref_content = f.read()
            
            # 计算当前论文与引用文献的相似度
            vectorizer = TfidfVectorizer()
            tfidf_matrix = vectorizer.fit_transform([paper_info['title'], ref_content])
            similarity_score = cosine_similarity(tfidf_matrix)[0][1]
            
            # 将相似度作为重要性分数
            paper_importance_scores.append(similarity_score)
        else:
            # 如果引用文献不存在，则将分数置为0
            paper_importance_scores.append(0)
    
    # 补齐重要性分数列表的长度
    if len(paper_importance_scores) < len(expected_length):
        paper_importance_scores += [0] * (len(expected_length) - len(paper_importance_scores))
    
    # 截断重要性分数列表的长度
    if len(paper_importance_scores) > len(expected_length):
        paper_importance_scores = paper_importance_scores[:len(expected_length)]
    
    # 将当前论文的重要性分数保存到重要性分数字典中
    importance_scores[paper_id] = paper_importance_scores

# 打印重要性分数字典
print(importance_scores)

with open('result.json', 'w') as f:
    json.dump(importance_scores, f, indent=4)
