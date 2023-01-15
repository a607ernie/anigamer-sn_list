# anigamer sn_list

# 問題描述

本專案為解決[aniGamerPlus](https://github.com/miyouzi/aniGamerPlus)需要手動產生`sn_list.txt`中內容的問題。

# Usage

1. 設置環境
2. 執行`create_sn_list.py`，得到`sn_list.txt`
3. 依照個人需求修改`sn_list.txt`並儲存
4. 執行[aniGamerPlus](https://github.com/miyouzi/aniGamerPlus)


# How to run

- clone this repo
- install `requirements.txt`

```python
pip install -r requirements.txt
```

- run `main.py`

```python
python main.py
```

# Modify sn_list.txt

- 程式執行完後會產生`sn_list.txt`
```txt
21132 all #Dr.STONE 新石紀 第二季
20620 all #無職轉生，到了異世界就拿出真本事
20612 all #堀與宮村
    ...
    ...
```

- 若不要某些項目，則刪除`sn`和`all`，不可整行刪除，以免下次執行程式時又換被偵測到並加入到`sn_list.txt`

剔除某些項目，如以下範例。

```
#SK8 the Infinity
#轉生成蜘蛛又怎樣！
#BACK ARROW
```

# 若不要某些項目，則刪除`sn`和`all`，不可整行刪除，以免下次執行程式時又會被偵測到並重新加入到`sn_list.txt`


# 免責聲明
本專案所提供相關連結網站之網頁或資料，均為被連結網站所提供，相關權利為該等網站或合法權利人所有，純屬教育研究目的。