import requests

def download_youbike_data()->list:
    url = 'https://data.ntpc.gov.tw/api/datasets/010e5b15-3823-4b20-b401-b1cf000550c5/json?page=0&size=1000'

    response = requests.get(url)
    print(type(response))

    # if response.status_code == 200:
    #     print("下載成功")
    #     print("下載的內容如下")
    #     # print(response.text)
    #     # print(type(response.json()))
    #     for item in response.json():
    #         print(item)
    # else:
    #     print("下載失敗")

    try:
        response = requests.get(url)
        response.raise_for_status
        try:
            data = response.json()
        except requests.exceptions.JSONDecodeError as jsonError:
            raise Exception(f"發生轉換格是錯誤:jsonError")
    except requests.exceptions.HTTPError as err_http:
        # 捕捉 HTTP 狀態碼錯誤 (4xx 或 5xx)
        raise Exception(f"發生 HTTP 錯誤: {err_http}")
    except requests.exceptions.ConnectionError as err_conn:
        # 捕捉連線錯誤，如 DNS 解析失敗、拒絕連線等
        raise Exception(f"發生連線錯誤: {err_conn}")
    except requests.exceptions.Timeout as err_timeout:
        # 捕捉超時錯誤
        raise Exception(f"請求超時: {err_timeout}")
    except requests.exceptions.RequestException as err:
        # 捕捉所有 requests 相關的泛型錯誤
        raise Exception(f"發生不明錯誤: {err}")
    else:
        return data
    
def get_area(data)->list:
    areas = set()
    for item in data:
        areas.add(item["sarea"])
    return list(areas)

def get_sites_of_area(data, area)->list:
    sites = []
    for item in data:
        if item["sarea"] == area:
            sites.append(item)
    return sites