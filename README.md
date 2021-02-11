# bert_mulit_label_chinese
```
1. Follow bert_wwm/readme.md steps to download pre-model files 
2. pip install -r requirements.txt
```

------------


# 快速啟動
``` python3 mulit_label.py ```

# 訓練部分
### 訓練參數

```
train_batch_size = 16
eval_batch_size = 16
predict_batch_size = 16
learning_rate = 5e-5
num_train_epochs = 35
```


### 輸入資料

範例檔案
```
  data/
      - train.tsv
      - test.tsv
```

輸出:
```
0:事物說明
1:他人描述
2:自我探討
```

f1:
```
class00_f1 = 0.5
class00_precision = 0.5
class00_recall = 0.5


class01_f1 = 0.8
class01_precision = 0.6666666666666666
class01_recall = 1.0


class02_f1 = 0.888888888888889
class02_precision = 0.8
class02_recall = 1.0


class_intent_f1 = 0.7407407407407408
class_intent_precision = 0.6666666666666666
class_intent_recall = 0.8333333333333334
```
