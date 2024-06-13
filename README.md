## Prerequisites



- kaggle online training enivronment

https://www.kaggle.com/code/zxl2022/paper-source-trace-zxl-1999-rank15-pst



You can try running the test dataset and download it locally at "/kaggle/working/"



## Getting Started



### Installation



Clone this repo.

```
git clone https://github.com/THUDM/paper-source-trace.git
cd paper-source-trace
```



## Run Baselines for [KDD Cup 2024](https://www.biendata.xyz/competition/pst_kdd_2024/)

Preparing DataSet and Trainging Weight



DataSet(paper-xml)

https://drive.google.com/drive/folders/1MqpsQw6Kev70DuRKjYP0C7dvnA72mdfT?usp=sharing



Trainging Weight(bert-base-uncased,Need to be placed in the bertModel folder) 

https://huggingface.co/google-bert/bert-base-uncased/tree/main



Training

```
python trainBert.py  # output at out/kddcup/bertModel/
```



Testing

```
python testBert.py  
```



## Results on Test Set



| Method | MAP    |
| ------ | ------ |
| BERT   | 0.3554 |



Model checkpoints are in the out/kddcup/bertModel folder