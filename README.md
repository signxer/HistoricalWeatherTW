# HistoricalWeatherTW 台灣歷史天氣爬蟲
資料來自 [觀測資料查詢系統](http://e-service.cwb.gov.tw/HistoryDataQuery/) 
## Usage 使用
原資料會存在一些非數字形式(例如風向不定V，有雨跡T等)，以下開啟參數會將其簡單替換成數字：

`conv2num = True`

修改所需資料的起始時間及結束時間：

`begin_date = datetime.date(2016,1,1)`

`end_date = datetime.date(2016,12,31)`
  
## Data 資料
資料會以觀測站ID+站名儲存

資料欄位如下：
觀測時間(LST) `ObsTime`
測站氣壓(hPa) `StnPres`
海平面氣壓(hPa)SeaPres	
氣溫(℃)Temperature	
露點溫度(℃)Td dew point	
相對溼度(%)RH	
風速(m/s)WS	
風向(360degree)WD	
最大陣風(m/s)WSGust	
最大陣風風向(360degree)WDGust	
降水量(mm)Precp	
降水時數(hr)PrecpHour	
日照時數(hr)SunShine	
全天空日射量(MJ/㎡)GloblRad	
能見度(km)Visb

## Updates 更新
V2.0
加入全台觀測站

V1.0
第一版
