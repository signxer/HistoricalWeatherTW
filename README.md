# HistoricalWeatherTW 台灣歷史天氣爬蟲
資料來自 [觀測資料查詢系統](http://e-service.cwb.gov.tw/HistoryDataQuery/) 
## Usage 使用
原資料會存在一些非數字形式(例如風向不定V，有雨跡T等)，以下開啟參數會將其簡單替換成數字：

`conv2num = True`

修改所需資料的起始時間及結束時間：

`begin_date = datetime.date(2016,1,1)`

`end_date = datetime.date(2016,12,31)`
  
## Updates 更新
V2.0
加入全台觀測站

V1.0
第一版
