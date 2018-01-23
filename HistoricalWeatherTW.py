import csv
import datetime
import pandas as pd
import urllib.request
from bs4 import BeautifulSoup

def GetWeather(date):
	conv2num = True #是否需要轉成數字
	station_id = "467490"
	station_name = "臺中"
	#兩次URL編碼
	station_name = urllib.parse.quote(urllib.parse.quote(station_name))
	url = "http://e-service.cwb.gov.tw/HistoryDataQuery/DayDataController.do?command=viewMain&station="+station_id+"&stname="+station_name+"&datepicker="+date
	req = urllib.request.Request(url)
	f = urllib.request.urlopen(req)
	soup = BeautifulSoup(f.read().decode('utf-8','ignore'), "lxml")
	data = soup.find_all('tr')
	#刪掉三個無關的
	del data[0]
	del data[0]
	del data[0]
	data_dict = {}
	for tr in data:
		td_index = 1
		data_list = []
		for td in tr.findAll('td'):
			tr_text = td.get_text().rstrip()
			if(td_index == 1):
				hour = int(tr_text)
			else:
				if(tr_text == ""):
					# print("NULL")
					data_list.append("")
				else:
					# print(tr_text)
					if conv2num:
						if(tr_text == "T"):
							data_list.append(0.05) #有雨跡，降雨量小於0.01
						elif(tr_text == "X"):
							data_list.append(0) #記錄錯誤
						elif(tr_text == "V"):
							data_list.append(0) #風向不定
						else:
							data_list.append(float(tr_text))
					else:
						try:
							tr_text = float(tr_text)
						data_list.append(tr_text)

			td_index += 1
		data_dict[hour] = data_list
		# print("--------------------")
	#print(data_dict)
	return data_dict


def main():
	#定義起始日期
	begin_date = datetime.date(2016,1,1)
	end_date = datetime.date(2016,12,31)
	#表頭
	headers = ["Date","ObsTime","StnPres","SeaPres","Temperature","Tddewpoint","RH","WS","WD","WSGust","WDGust","Precp","PrecpHour","SunShine","GloblRad","Visb"]
	df = pd.DataFrame(columns=headers)
	#日期遍历
	df_index = 0
	for i in range((end_date - begin_date).days+1):
		day = begin_date + datetime.timedelta(days=i)  
		date = str(day)
		weather_dict = GetWeather(date)
		for h in range(1,25):
			rows = weather_dict[h]
			rows.insert(0,h)
			rows.insert(0,date)
			df.loc[df_index] = rows
			df_index += 1
		print(date)
	df.to_csv ("weather.csv" , encoding = "utf-8")
   
if __name__ == '__main__':
    main()