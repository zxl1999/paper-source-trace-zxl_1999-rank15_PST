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