import json
import numpy as np

# 读取 JSON 文件
def read_json(filename):
    with open(filename, 'r') as f:
        return json.load(f)

# 计算三个列表的平均值
def average_lists(list1, list2):
    array1 = np.array(list1)
    array2 = np.array(list2)
    
    return ((array1 + array2) / 2).tolist()

# 主函数
def main():
    # 读取文件内容
    #albert_data = read_json('test_submission_albert.json')
    bert_data = read_json('test_submission_bert.json')
    scibert_data = read_json('node_importance_adjusted_deepwalking.json')

    # 初始化结果字典
    result_data = {}

    # 遍历所有键，计算平均值
    for key in bert_data.keys():
        result_data[key] = average_lists(bert_data[key], scibert_data[key])

    # 将结果写入新的 JSON 文件
    with open('test_submission_average_bert_deepwalking.json', 'w') as f:
        json.dump(result_data, f, indent=4)

if __name__ == "__main__":
    main()
