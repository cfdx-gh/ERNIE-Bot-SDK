import os
import json
import requests
import time
import subprocess
import urllib.parse
from config_parse import get_config_elem_value

cur_path = os.getcwd()
rapid_api_result_dir = "rapid_api_result"
chinese_api_result_dir = "chinese_api_result"
config_name = os.path.join(cur_path, "config/authentication.ini")
xrapidapi_key = get_config_elem_value(config_name, "xrapidapi", "X-RapidAPI-Key")


def getCurrentWeather(location, format="摄氏度"):
    """Get the current weather in a given location"""
    weather_info = {
        "location": location,
        "temperature": "78",
        "format": format,
        "forecast": ["晴朗的", "有风"],
    }
    return json.dumps(weather_info)


def getNDayWeatherForecast(location, num_days, format="华氏度"):
    """Get forecast weather in a given location for n days in the future"""
    if num_days == 1:
        weather_info = {
            "location": location,
            "temperature": "71",
            "format": format,
            "forecast": ["大雨", "大风"],
        }
    elif num_days == 2:
        weather_info = {
            "location": location,
            "temperature": "72",
            "format": format,
            "forecast": ["小雨", "微风"],
        }
    elif num_days == 3:
        weather_info = {
            "location": location,
            "temperature": "73",
            "format": format,
            "forecast": ["多云", "比较舒服"],
        }
    else:
        weather_info = {
            "location": location,
            "temperature": "80",
            "format": format,
            "forecast": ["晴天", "有风", "舒适"],
        }

    return json.dumps(weather_info)


def getEarchQuakeInfo(latitude, longitude, radius, magnitude, count):
    """Get every earthquake and any other event that registers on the richter scale"""
    url = "https://everyearthquake.p.rapidapi.com/earthquakes"
    #querystring = {"start":"1","count":"10","type":"earthquake","latitude":"39.4","longitude":"115.7","radius":"1000","units":"miles","magnitude":"7","intensity":"1"}
    querystring = {"start":"1","count":str(count), \
            "type":"earthquake","latitude":str(latitude), \
            "longitude":str(longitude), \
            "radius":str(radius),"units":"miles", \
            "magnitude":str(magnitude),"intensity":"1"}
    headers = {
        "X-RapidAPI-Key": xrapidapi_key,
        "X-RapidAPI-Host": "everyearthquake.p.rapidapi.com"
    }
    #response = requests.get(url, headers=headers, params=querystring)
    #print(response.json())

    earchquake_list = []
    filename = "earthquake.json"
    with open(cur_path + "/" + rapid_api_result_dir + "/" + filename, 'r') as f:
        response = json.load(f)
    earchquake_num = response["count"]
    for elem in response["data"]:
        tmp_dict = {}
        tmp_dict["magnitude"] = elem["magnitude"]
        tmp_dict["title"] = elem["title"]
        tmp_dict["date"] = elem["date"]
        tmp_dict["detail_info"] = elem["detailUrl"]
        tmp_dict["country"] = elem["country"]
        tmp_dict["city"] = elem["city"]
        tmp_dict["latitude"] = elem["latitude"]
        tmp_dict["longitude"] = elem["longitude"]
        earchquake_list.append(tmp_dict)
    #print(earchquake_list)
    return json.dumps(earchquake_list)


def getMarketNews(symbol, num):
    """Get Market news of some Stock"""
    url = "https://mboum-finance.p.rapidapi.com/ne/news/"
    #querystring = {"symbol":"BIDU"}
    querystring = {"symbol":symbol}
    headers = {
        "X-RapidAPI-Key": xrapidapi_key,
        "X-RapidAPI-Host": "mboum-finance.p.rapidapi.com"
    }
    #response = requests.get(url, headers=headers, params=querystring)
    #print(response.json())

    news_list = []
    filename = "marketnews.json"
    with open(cur_path + "/" + rapid_api_result_dir + "/" + filename, 'r') as f:
        response = json.load(f)
    i = 0
    for elem in response["item"]:
        tmp_dict = {}
        tmp_dict["title"] = elem["title"]
        tmp_dict["description"] = elem["description"]
        tmp_dict["link"] = elem["link"]
        tmp_dict["pubDate"] = elem["pubDate"]
        i += 1
        news_list.append(tmp_dict)
        if i > num:
            break
    #print(news_list)
    return json.dumps(news_list)

def getGasolineDieselPrices(state):
    """Get gasoline and diesel prices in different fuel stations in different cities."""
    url = "https://gas-price.p.rapidapi.com/stateUsaPrice"
    #querystring = {"state":"NY"}
    querystring = {"state": state}
    headers = {
        "X-RapidAPI-Key": xrapidapi_key,
        "X-RapidAPI-Host": "gas-price.p.rapidapi.com"
    }
    #response = requests.get(url, headers=headers, params=querystring)
    #print(response.json())

    res_list = []
    filename = "gasoline_diesel_prices.json"
    with open(cur_path + "/" + rapid_api_result_dir + "/" + filename, 'r') as f:
        response = json.load(f)
    for elem in response["result"]["cities"]:
        tmp_dict = {}
        tmp_dict["name"] = elem["name"]
        tmp_dict["gasoline"] = elem["gasoline"]
        tmp_dict["diesel"] = elem["diesel"]
        res_list.append(tmp_dict)
    #print(res_list)
    return json.dumps(res_list)


def searchAirport(location):
    """Get gasoline and diesel prices in different fuel stations in different cities."""
    url = "https://tripadvisor16.p.rapidapi.com/api/v1/flights/searchAirport"
    #querystring = {"query":"london"}
    querystring = {"query":"location"}
    headers = {
	"X-RapidAPI-Key": xrapidapi_key,
	"X-RapidAPI-Host": "tripadvisor16.p.rapidapi.com"
    }
    #response = requests.get(url, headers=headers, params=querystring)
    #print(response.json())

    res_list = []
    filename = "search_airport.json"
    with open(cur_path + "/" + rapid_api_result_dir + "/" + filename, 'r') as f:
        response = json.load(f)
    for elem in response["data"][0]["children"]:
        tmp_dict = {}
        tmp_dict["name"] = elem["name"]
        tmp_dict["parent_name"] = elem["details"]["parent_name"]
        tmp_dict["airportCode"] = elem["airportCode"]
        tmp_dict["coords"] = elem["coords"]
        res_list.append(tmp_dict)
    #print(res_list)
    return json.dumps(res_list)


def searchFlights(sourceAirportCode, destinationAirportCode, date):
    """Get flights info between two cities """
    url = "https://tripadvisor16.p.rapidapi.com/api/v1/flights/searchFlights"
    #querystring = {"sourceAirportCode":"BOM","destinationAirportCode":"DEL","date":"2023-09-28","itineraryType":"ONE_WAY","sortOrder":"ML_BEST_VALUE","numAdults":"1","numSeniors":"0","classOfService":"ECONOMY","returnDate":"2023-09-28","nearby":"yes","nonstop":"yes","currencyCode":"USD"}
    querystring = {"sourceAirportCode": sourceAirportCode, "destinationAirportCode": destinationAirportCode, \
            "date": date, "itineraryType": "ONE_WAY", "sortOrder": "ML_BEST_VALUE", "numAdults": "1", \
            "numSeniors": "0", "classOfService": "ECONOMY", "returnDate": date, \
            "nearby": "yes", "nonstop": "yes", "currencyCode": "USD"}
    headers = {
	"X-RapidAPI-Key": xrapidapi_key,
	"X-RapidAPI-Host": "tripadvisor16.p.rapidapi.com"
    }
    #response = requests.get(url, headers=headers, params=querystring)
    #print(response.json())

    res_list = []
    filename = "search_flights.json"
    with open(cur_path + "/" + rapid_api_result_dir + "/" + filename, 'r') as f:
        response = json.load(f)
    i = 0
    for flight in response["data"]["flights"]:
        for segment in flight["segments"]:
            for leg in segment["legs"]:
                tmp_dict = {}
                tmp_dict["originStationCode"] = leg["originStationCode"]
                tmp_dict["destinationStationCode"] = leg["destinationStationCode"]
                tmp_dict["equipmentId"] = leg["equipmentId"]
                tmp_dict["flightNumber"] = leg["flightNumber"]
                tmp_dict["distanceInKM"] = leg["distanceInKM"]
                tmp_dict["departureDateTime"] = leg["departureDateTime"]
                tmp_dict["arrivalDateTime"] = leg["arrivalDateTime"]
                i += 1
                if i < 10:
                    res_list.append(tmp_dict)
                else:
                    break
    #print(res_list)
    return json.dumps(res_list)


def searchHotels(query, limit_num):
    """Get hotels in which one citie """
    url = "https://local-business-data.p.rapidapi.com/search"
    #querystring = {"query":"Hotels in  Beijing, China","limit":"10","lat":"39.56","lng":"116.2","zoom":"13","language":"en","region":"us"}
    querystring = {"query": query, "limit": limit_num, "lat": "39.56", "lng": "116.2", "zoom": "13", "language": "en", "region": "us"}
    headers = {
	"X-RapidAPI-Key": xrapidapi_key,
	"X-RapidAPI-Host": "local-business-data.p.rapidapi.com"
    }
    #response = requests.get(url, headers=headers, params=querystring)
    #print(response.json())

    res_list = []
    filename = "search_hotels.json"
    with open(cur_path + "/" + rapid_api_result_dir + "/" + filename, 'r') as f:
        response = json.load(f)
    for hotel in response["data"]:
        tmp_dict = {}
        tmp_dict["name"] = hotel["name"]
        tmp_dict["business_status"] = hotel["business_status"]
        tmp_dict["full_address"] = hotel["full_address"]
        tmp_dict["website"] = hotel["website"]
        res_list.append(tmp_dict)
    #print(res_list)
    return json.dumps(res_list)


def searchHotels(query, limit_num):
    """Get hotels in which one citie """
    url = "https://local-business-data.p.rapidapi.com/search"
    #querystring = {"query":"Hotels in  Beijing, China","limit":"10","lat":"39.56","lng":"116.2","zoom":"13","language":"en","region":"us"}
    querystring = {"query": query, "limit": limit_num, "lat": "39.56", "lng": "116.2", "zoom": "13", "language": "en", "region": "us"}
    headers = {
	"X-RapidAPI-Key": xrapidapi_key,
	"X-RapidAPI-Host": "local-business-data.p.rapidapi.com"
    }
    #response = requests.get(url, headers=headers, params=querystring)
    #print(response.json())

    res_list = []
    filename = "search_hotels.json"
    with open(cur_path + "/" + rapid_api_result_dir + "/" + filename, 'r') as f:
        response = json.load(f)
    for hotel in response["data"]:
        tmp_dict = {}
        tmp_dict["name"] = hotel["name"]
        tmp_dict["business_status"] = hotel["business_status"]
        tmp_dict["full_address"] = hotel["full_address"]
        tmp_dict["website"] = hotel["website"]
        res_list.append(tmp_dict)
    #print(res_list)
    return json.dumps(res_list)


def searchQQBindInfo(qq_num):
    """Get QQ Bind Info"""
    url = "http://thapi.top/API/qbcx2.php"
    cmd = "curl " + url + "?QQ=" + qq_num + " -s"
    status, response = subprocess.getstatusoutput(cmd)
    res =  response.replace("\n", ";").split(";")
    res_list = []
    res_dict = {}
    for elem in res:
        if elem != "":
            tmp_list = elem.split(":")
            key = tmp_list[0]
            value = tmp_list[1]
            res_dict[key] = value
    res_list.append(res_dict)
    return json.dumps(res_list)


def searchIdentityInfo(sfz_num):
    """Get Identity Info"""
    url = "http://thapi.top/API/sfzjx.php"
    cmd = "curl " + url + "?sfz=" + sfz_num + " -s"
    status, response = subprocess.getstatusoutput(cmd)
    res =  response.replace("\n", ";").split(";")
    res_list = []
    res_dict = {}
    for elem in res:
        if elem != "":
            tmp_list = elem.split("：")
            key = tmp_list[0]
            value = tmp_list[1]
            res_dict[key] = value
    res_list.append(res_dict)
    return json.dumps(res_list)


def getWebsiteSpeed(web_url, count):
    """Get Website Speed"""
    url = "http://thapi.top/API/wzcs.php"
    cmd = "curl -s " + url + "?url=" + web_url + "&type=text&count=" + str(count)
    status, response = subprocess.getstatusoutput(cmd)
    res =  response.replace("\n", ";").split(";")
    res_list = []
    res_dict = {}
    for elem in res:
        if elem != "":
            tmp_list = elem.split(":")
            key = tmp_list[0]
            value = tmp_list[1]
            res_dict[key] = value
    res_list.append(res_dict)
    return json.dumps(res_list)


def getTimeKeeper(hour):
    """Get TimeKeeper"""
    url = "http://thapi.top/API/zdbs.php"
    cmd = "curl -s " + url + "?time=" + hour + "&type=json"
    status, response = subprocess.getstatusoutput(cmd)
    res =  json.loads(response)
    print(res)
    res_list = []
    res_dict = {}
    res_dict["tip_msg"] = res["msg"]
    res_dict["tip_url"] = res["url"]
    res_list.append(res_dict)
    print(res_list)
    return json.dumps(res_list)


def getEncryMd5(text):
    """Get Encry Md5"""
    url = "http://thapi.top/API/md5.php"
    cmd = "curl -s " + url + "?msg=" + text
    print(cmd)
    status, response = subprocess.getstatusoutput(cmd)
    res =  response.replace("\n", ";").split(";")
    print(res)
    res_list = []
    res_dict = {}
    for elem in res:
        if elem != "":
            tmp_list = elem.split("：")
            key = tmp_list[0]
            value = tmp_list[1]
            res_dict[key] = value
    res_list.append(res_dict)
    print(res_list)
    return json.dumps(res_list)


def getTelAddress(tel_phone_num):
    """Get Tel Address"""
    url = "https://api.oioweb.cn/api/common/teladress"
    cmd = "curl -s " + url + "?mobile=" + tel_phone_num
    status, response = subprocess.getstatusoutput(cmd)
    res =  json.loads(response)
    print(res)
    res_list = []
    res_dict = {}
    res_dict["prov"] = res["result"]["prov"]
    res_dict["city"] = res["result"]["city"]
    res_dict["name"] = res["result"]["name"]
    res_dict["areaCode"] = res["result"]["areaCode"]
    res_list.append(res_dict)
    print(res_list)
    return json.dumps(res_list)


def getHistoryTodayInfo(count):
    """Get What happened in History Today"""
    url = "https://api.oioweb.cn/api/common/history"
    cmd = "curl -s " + url
    status, response = subprocess.getstatusoutput(cmd)
    res =  json.loads(response)
    #print(res)
    res_list = []
    i = 1
    for elem in res["result"]:
        if i < int(count):
            res_dict = {}
            res_dict["year"] = elem["year"]
            res_dict["title"] = elem["title"]
            res_dict["desc"] = elem["desc"]
            res_dict["link"] = elem["link"]
            #res_dict["image"] = elem["image"]
            res_list.append(res_dict)
            i += 1
            continue
        else:
            break
    print(res_list)
    return json.dumps(res_list)


def getHotList(platform_name1, platform_name2, count):
    """Get Host List"""
    url = "https://api.oioweb.cn/api/common/HotList"
    cmd = "curl -s " + url
    status, response = subprocess.getstatusoutput(cmd)
    res =  json.loads(response)
    #print(res)
    res_list = []
    res_dict_all = {}
    #get platform_name1信息
    res_list_1 = []
    i = 1
    for elem in res["result"][platform_name1]:
        if i > int(count):
            break
        else:
            res_dict = {}
            res_dict["index"] = elem["index"]
            res_dict["title"] = elem["title"]
            res_dict["hot"] = elem["hot"]
            res_dict["link"] = elem["href"]
            res_list_1.append(res_dict)
            i += 1
    res_dict_all[platform_name1] = res_list_1
    #get platform_name2信息
    res_list_2 = []
    j = 1
    for elem in res["result"][platform_name2]:
        if j > int(count):
            break
        else:
            res_dict = {}
            res_dict["index"] = elem["index"]
            res_dict["title"] = elem["title"]
            res_dict["hot"] = elem["hot"]
            res_dict["link"] = elem["href"]
            res_list_2.append(res_dict)
            j += 1
    res_dict_all[platform_name2] = res_list_2
    res_list.append(res_dict_all)
    print(res_list)
    return json.dumps(res_list)


def getDeliveryInfo(delivery_num):
    """Get Delivery Info"""
    url = "https://api.oioweb.cn/api/common/delivery"
    cmd = "curl -s " + url + "?nu=" + delivery_num
    print(cmd)
    status, response = subprocess.getstatusoutput(cmd)
    res =  json.loads(response)
    #print(res)
    res_list = []
    res_dict = {}
    res_dict["delivery_name"] = res["result"]["expTextName"]
    res_dict["delivery_mailNo"] = res["result"]["mailNo"]
    res_dict["delivery_status"] = res["result"]["StatusInfo"]
    delivery_detail_list = []
    for elem in res["result"]["data"]:
        dict_tmp = {}
        dict_tmp["context"] = elem["context"]
        dict_tmp["time"] = elem["time"]
        delivery_detail_list.append(dict_tmp)
    res_dict["delivery_detail_info"] = delivery_detail_list
    res_list.append(res_dict)
    #print(res_list)
    return json.dumps(res_list)


def getFoodHeatInfo(food_name):
    """Get Food Heat Info"""
    url = "https://api.oioweb.cn/api/search/FoodHeat"
    cmd = "curl -s " + url + "?keyword=" + food_name + "&page=1"
    print(cmd)
    status, response = subprocess.getstatusoutput(cmd)
    res =  json.loads(response)
    res_list = []
    for elem in res["result"]:
        res_dict = {}
        res_dict["name"] = elem["name"]
        res_dict["desc"] = elem["desc"]
        res_dict["heat"] = elem["heat"]
        res_dict["img_link"] = elem["img"]
        res_list.append(res_dict)
    print(res_list)
    return json.dumps(res_list)


def getOlyMedalsList(count):
    """Get Oly Medal List"""
    url = "https://api.oioweb.cn/api/search/getOlyMedals"
    cmd = "curl -s " + url
    status, response = subprocess.getstatusoutput(cmd)
    res =  json.loads(response)
    #print(res)
    res_list = []
    i = 1
    for elem in res["result"]["medalsList"]:
        if i > int(count):
            break
        else:
            res_dict = {}
            res_dict["countryname"] = elem["countryname"]
            res_dict["countryid"] = elem["countryid"]
            res_dict["medal_rank"] = elem["rank"]
            res_dict["gold_count"] = elem["gold"]
            res_dict["silver_count"] = elem["silver"]
            res_dict["bronze_count"] = elem["bronze"]
            res_dict["total_count"] = elem["count"]
            res_list.append(res_dict)
            i += 1
    print(res_list)


def isOrNotHarassPhone(tel_phone):
    """Get Whether Harass Phone"""
    url = "https://api.oioweb.cn/api/search/harassPhone"
    cmd = "curl -s " + url + "?phone=" + tel_phone
    print(cmd)
    status, response = subprocess.getstatusoutput(cmd)
    res =  json.loads(response)
    res_list = []
    res_dict = {}
    res_dict["tel_phone"] = tel_phone
    res_dict["status"] = res["result"]["status"]
    res_list.append(res_dict)
    print(res_list)
    return json.dumps(res_list)


def searchTradeMarkInfo(keyword, count):
    """search Trade Mark Info"""
    url = "https://api.oioweb.cn/api/search/trademark"
    keyword_url = urllib.parse.quote(keyword)
    cmd = "curl -s " + url + "?keyword=" + keyword_url + "&pageNo=1&pageSize=20"
    print(cmd)
    status, response = subprocess.getstatusoutput(cmd)
    res =  json.loads(response)
    res_list = []
    i = 1
    for elem in res["result"]["list"]:
        if i > int(count):
            break
        else:
            res_dict = {}
            res_dict["trademarkName"] = elem["trademarkName"]
            res_dict["agency"] = elem["agency"]
            res_dict["typeOfTrademarkName"] = elem["typeOfTrademarkName"]
            res_dict["trademarkNumber"] = elem["trademarkNumber"]
            res_dict["legalStatusName"] = elem["legalStatusName"]
            res_dict["trademarkApplicationDate"] = elem["trademarkApplicationDate"]
            res_list.append(res_dict)
    print(res_list)
    return json.dumps(res_list)


def searchDomainWhoisInfo(domain):
    """search Domain Whois Info"""
    url = "https://api.oioweb.cn/api/site/whois"
    cmd = "curl -s " + url + "?domain=" + domain
    print(cmd)
    status, response = subprocess.getstatusoutput(cmd)
    res =  json.loads(response)
    res_list = []
    elem = res["result"]
    res_dict = {}
    res_dict["Registrant"] = elem["Registrant"]
    res_dict["Holder"] = elem["Holder"]
    res_dict["DomainServer"] = elem["DomainServer"]
    res_dict["DnsServer"] = elem["DnsServer"]
    res_dict["DomainStatus"] = elem["DomainStatus"]
    res_dict["RegistrationTime"] = elem["RegistrationTime"]
    res_dict["ExpirationTime"] = elem["ExpirationTime"]
    res_list.append(res_dict)
    print(res_list)
    return json.dumps(res_list)


def jianhuangPicture(pic_url):
    """jianhuang Picture"""
    url = "https://api.oioweb.cn/api/ai/jianhuang"
    cmd = "curl -s " + url + "?url=" + pic_url
    print(cmd)
    status, response = subprocess.getstatusoutput(cmd)
    res =  json.loads(response)
    res_list = []
    elem = res["result"]
    res_dict = {}
    res_dict["rating_index"] = elem["rating_index"]
    res_dict["rating_label"] = elem["rating_label"]
    res_dict["predictions"] = elem["predictions"]
    res_list.append(res_dict)
    print(res_list)
    return json.dumps(res_list)


def queryGasolinePrice(region):
    """Get Food Heat Info"""
    url = "https://api.oioweb.cn/api/common/GasolinePriceQuery"
    cmd = "curl -s " + url
    print(cmd)
    status, response = subprocess.getstatusoutput(cmd)
    res =  json.loads(response)
    #filename = "gasoline_price.json"
    #with open(cur_path + "/" + chinese_api_result_dir + "/" + filename, 'r') as f:
    #    res = json.load(f)
    res_list = []
    for elem in res["result"]:
        if elem["Region"] == region:
            res_dict = {}
            res_dict["Region"] = elem["Region"]
            res_dict["Gasoline92"] = elem["Gasoline92"]
            res_dict["Gasoline95"] = elem["Gasoline95"]
            res_dict["Gasoline98"] = elem["Gasoline98"]
            res_dict["Diesel0"] = elem["Diesel0"]
            res_dict["UpdateTime"] = elem["UpdateTime"]
            res_list.append(res_dict)
            break
    print(res_list)
    return json.dumps(res_list)


def garbageClassification(object_name):
    """Garbage Classification"""
    url = "https://api.vvhan.com/api/la.ji"
    keyword_url = urllib.parse.quote(object_name)
    cmd = "curl -s " + url + "?lj=" + keyword_url
    print(cmd)
    status, response = subprocess.getstatusoutput(cmd)
    res =  json.loads(response)
    res_list = []
    res_dict = {}
    res_dict["name"] = object_name
    res_dict["sort"] = res["sort"]
    res_list.append(res_dict)
    print(res_list)
    return json.dumps(res_list)


def queryMovieRank(count):
    """ Query Movie Rank"""
    url = "https://api.vvhan.com/api/douban"
    cmd = "curl -s " + url
    print(cmd)
    status, response = subprocess.getstatusoutput(cmd)
    res =  json.loads(response)
    res_list = []
    i = 1
    for elem in res["data"]:
        if i > int(count):
            break
        else:
            res_dict = {}
            res_dict["title"] = elem["title"]
            res_dict["movie_url"] = elem["info"]["url"]
            res_dict["movie_imgurl"] = elem["info"]["imgurl"]
            res_dict["movie_actor"] = elem["info"]["yanyuan"]
            res_dict["movie_score"] = elem["info"]["pingfen"]
            res_list.append(res_dict)
    print(res_list)
    return json.dumps(res_list)

