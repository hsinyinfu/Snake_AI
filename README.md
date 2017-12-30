# Snake_AI

## 繪圖

### 系統架構
將`snake.py`, `rock.png`, `candy.png`, `snake_head.png`, `snake_body.png`一起放在
跟主程式同一個資料夾內。

### 使用套件
`pip install pygame`

### import
`import snake`

### 使用
一開始要先call `snake.init()`來初始化pygame視窗。

之後深度學習每算出一個output，就call一次`snake.draw( map_array, head_index_tuple )`。

可以參考`test.py`如何使用`snake.py`.