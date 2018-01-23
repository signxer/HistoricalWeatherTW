# HistoricalWeatherTW 台灣歷史天氣爬蟲
資料來自 [觀測資料查詢系統](http://e-service.cwb.gov.tw/HistoryDataQuery/) 
## Usage 使用
修改以下兩個參數，可以更換觀測站，名稱以及ID可以在 [觀測資料查詢系統](http://e-service.cwb.gov.tw/HistoryDataQuery/) 查詢

  station_id = "467490"
  station_name = "臺中"

修改所需資料的起始時間及結束時間

  begin_date = datetime.date(2016,1,1)
  end_date = datetime.date(2016,12,31)
  
## Updates 更新
V1.0
第一版