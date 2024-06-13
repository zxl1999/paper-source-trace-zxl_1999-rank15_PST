import os
import json
import networkx as nx
import pandas as pd

# 文件路径
matched_titles_train_path = 'processed_matched_titles_train.json'
matched_titles_test_path = 'processed_matched_titles_test.json'
citation_data_train_path = 'paper_source_trace_train_ans.json'
citation_data_test_path = 'paper_source_trace_test_wo_ans.json'
output_csv_path = 'graph_edges.csv'

# 读取处理过的 matched_titles_train JSON 文件
with open(matched_titles_train_path, 'r', encoding='utf-8') as file:
    matched_titles_train = json.load(file)

# 读取处理过的 matched_titles_test JSON 文件
with open(matched_titles_test_path, 'r', encoding='utf-8') as file:
    matched_titles_test = json.load(file)

# 读取 paper_source_trace_train_ans.json 文件
with open(citation_data_train_path, 'r', encoding='utf-8') as file:
    citation_data_train = json.load(file)

# 读取 paper_source_trace_test_wo_ans.json 文件
with open(citation_data_test_path, 'r', encoding='utf-8') as file:
    citation_data_test = json.load(file)

# 创建一个有向图
G = nx.DiGraph()

# 遍历 citation_data_train，添加节点和边
for item in citation_data_train:
    paper_id = item['_id']
    references = item.get('references', [])
    
    G.add_node(paper_id)
    for cited_paper in references:
        G.add_edge(paper_id, cited_paper)

# 遍历 citation_data_test，添加节点和边
for item in citation_data_test:
    paper_id = item['_id']
    references = item.get('references', [])
    
    G.add_node(paper_id)
    for cited_paper in references:
        G.add_edge(paper_id, cited_paper)

# 处理 matched_titles_train 并添加边
for paper_id, matched_papers in matched_titles_train.items():
    for matched_paper in matched_papers:
        G.add_edge(paper_id, matched_paper)

# 处理 matched_titles_test 并添加边
for paper_id, matched_papers in matched_titles_test.items():
    for matched_paper in matched_papers:
        G.add_edge(paper_id, matched_paper)

# 提取点信息
nodes = list(G.nodes)
# 提取边信息
edges = list(G.edges)

# 打印节点和边信息的数量
print(f"Number of nodes: {len(nodes)}")
print(f"Number of edges: {len(edges)}")

# 查看前5个节点和边
print("Sample nodes:", nodes[:5])
print("Sample edges:", edges[:5])

# 保存边信息为CSV文件
edges_df = pd.DataFrame(edges, columns=['Source', 'Target'])
edges_df.to_csv(output_csv_path, index=False)

print(f"Edge list saved to {output_csv_path}")
