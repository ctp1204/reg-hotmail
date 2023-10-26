from os            import environ
from time          import sleep
from datetime      import datetime
from selenium      import webdriver
import json
from random       import randint
from json         import loads, dumps, load
from os           import urandom
from names        import get_first_name, get_last_name
import threading, time, requests, random, re, os, sys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import random,os,requests,hashlib
import chromedriver_autoinstaller
from onest_captcha import OneStCaptchaClient
os.system('cls')
os.system(f"title RegHotMail By Cường TânPhú (Version 1.0)")
time.sleep(5)
class RegHotmail:
    def reg(l):
        token      = urandom(7).hex()
        tk=f"ctp1204_{token}".lower()
        mk=urandom(7).hex() + '_Ctp1204@'
        lastName = ['Trình', 'Trịnh', 'Vĩnh', 'Viên', 'Yến', 'Linh', 'Mai', 'Tuyết', 'Anh', 'Ánh', 'Nam', 'Việt', 'Đức', 'Dương', 'Ngân', 'Hoà', 'Nga', 'Hậu', 'Tú', 'Quân', 'Quốc', 'Hiển', 'Chương', 'Hà', 'Quê', 'Mùa', 'Bản', 'Liêm', 'Diệp', 'Nghĩa', 'Lợi']
        fistName = ['Nguyễn', 'Trần', 'Huỳnh', 'Phan', 'Lê', 'Đặng', 'Bùi', 'Đỗ', 'Hồ', 'Ngô', 'Dương', 'Ly', 'Cường', 'Tùng', 'Long', 'Dương', 'Duy', 'Minh', 'Hằng', 'Thảo', 'Yến']
        tendem = random.choice(fistName)
        ten = random.choice(lastName)
        timeNow = datetime.now()
        time = f'[{timeNow}] '
        os.system('cls')
        print("Đang Chạy Số Luồng: ", number)
        getnew = requests.get(f"http://proxy.tinsoftsv.com/api/changeProxy.php?key={config['tinsoft_key']}").json()
        print("Tiến Hành Lấy Proxy")
        hoanthanh = requests.get(f"http://proxy.tinsoftsv.com/api/getProxy.php?key=={config['tinsoft_key']}").json()
        proxie = hoanthanh['proxy']
        print("Lấy Thành Công Proxy:", proxie)
        chromedriver_autoinstaller.install()
        options = webdriver.ChromeOptions()
        options.add_argument(f'--proxy-server=http://{proxie}')
        options.add_argument("--app=https://httpbin.org/ip")
        driver = webdriver.Chrome(options=options)
        x = l*400
        y = 10
        driver.set_window_rect(x,y,300,420)
        driver.get("https://httpbin.org/ip")
        pre = driver.find_element(By.TAG_NAME, 'pre').text
        data = json.loads(pre)
        ip = data["origin"]
        driver.get('https://outlook.live.com/owa/?nlp=1&signup=1')
        print(f'{time} | {ip} | truy cập tới https://outlook.live.com/')
        driver.implicitly_wait(5)
        sleep(3)
        hotmail=Select(driver.find_element(By.CSS_SELECTOR, "#LiveDomainBoxList"))
        print(f'{time} | {ip} | Đổi đuôi mail css #LiveDomainBoxList')
        sleep(2)
        hotmail.select_by_value("hotmail.com")
        print(f'{time} | {ip} | Đã đổi hotmail.com')
        for x in tk:
            driver.find_element(By.CSS_SELECTOR, "#MemberName").send_keys(x)
            sleep(0.005)
        driver.find_element(By.CSS_SELECTOR, "#iSignupAction").click()
        print(f"{time} | {ip} | Click nút 'tiếp theo'")
        driver.implicitly_wait(5)
        sleep(3)
        print(f'{time} | {ip} | Nhập password tự động')
        driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/div/div[1]/div[3]/div/div[1]/div[5]/div/div/form/div[3]/div/input[2]").send_keys(mk)
        sleep(3)
        driver.find_element(By.ID, "iSignupAction").click()
        print(f"{time} | {ip} | Click nút 'tiếp theo'")
        driver.implicitly_wait(5)
        sleep(3)
        print(f'{time} | {ip} | nhập ten id FirstName')
        driver.find_element(By.ID, "FirstName").send_keys(ten)
        sleep(0.005)
        print(f'{time} | {ip} | nhập ten đệm id LastName')
        driver.find_element(By.ID, "LastName").send_keys(tendem)
        sleep(0.005)
        sleep(2)
        driver.find_element(By.ID, "iSignupAction").click()
        print(f"{time} | {ip} | Click nút 'tiếp theo'")
        driver.implicitly_wait(5)
        sleep(3)
        print(f'{time} | {ip} | Nhập tháng ngẫu nhiên')
        rd_thang=randint(1, 12)
        thang=Select(driver.find_element(By.CSS_SELECTOR, "#BirthMonth")).select_by_value(str(rd_thang))
        #list_thang=randint(1, 12)
        sleep(3)
        print(f'{time} | {ip} | Nhập ngày ngẫu nhiên')
        rd_ngay=randint(1, 28)
        day=Select(driver.find_element(By.CSS_SELECTOR, "#BirthDay")).select_by_value(str(rd_ngay))
        #list_ngay=randint(1, 28)
        sleep(3)
        print(f'{time} | {ip} | Nhập năm ngẫu nhiên')
        #list_nam= randint(1969, 2000)
        rd_nam=randint(1969, 2000)
        year=driver.find_element(By.CSS_SELECTOR, "#BirthYear").send_keys(rd_nam)
        sleep(7)
        print(f'{time} | {ip} | Click nút tiếp theo by xpath')
        driver.find_element(By.CSS_SELECTOR, "#iSignupAction").click()
        driver.switch_to.frame('enforcementFrame')
        print(f'{time} | {ip} | Đang giải captcha')
        sleep(5)
        reg=requests.post('https://api.1stcaptcha.com/createTask',headers={'Host': 'api.1stcaptcha.com','Content-Type': 'application/json',},json={"clientKey": config['captcha_key'],"task": {"type": "FunCaptchaTaskProxyless","websitePublicKey": "B7D8911C-5CC8-A9A3-35B0-554ACEE604DA","websiteURL": "signup.live.com"}}).json()
        try:
            sleep(5)
            task=reg['taskId']
        except:quit(f'{time} | {ip} | hết tiền rồi còn xài ba :3')
        sleep(5)
        while (True):
            response=requests.post('https://api.1stcaptcha.com/getTaskResult',headers={'Host': 'api.1stcaptcha.com','Content-Type': 'application/json',},json={"clientKey": config['captcha_key'],"taskId": task,}).json()
            try:
                if 'ready' in response['status']:
                    driver.execute_script('parent.postMessage(JSON.stringify ({eventId: "challenge-complete", payload: {sessionToken: "'+response['solution']['token']+'"}}), "*")')
                    break
                else:continue
            except:pass
        print(f'{time} | {ip} | Vượt captcha thành công')
        sleep(10)
        print(f'{time} | {ip} | Click nút Có by xpath')
        sleep(10)
        driver.find_element(By.XPATH, '/html/body/div/div/div[2]/button/span').click()
        sleep(5)
        driver.find_element(By.XPATH, '/html/body/div/div/div[2]/button/span').click()
        sleep(10)
        driver.find_element(By.XPATH, '/html/body/div/form/div/div/div[2]/div[1]/div/div/div/div/div/div[3]/div/div[2]/div/div[3]/div[2]/div/div/div[2]/input').click()
        sleep(5)
        tk_hotmail = f'{tk}@hotmail.com'
        print(f'')
        current_date = datetime.today().strftime('%Y-%m-%d')
        with open(f"Hotmail-{current_date}.txt", "a+", encoding="utf-8") as huhu:
            huhu.write(tk_hotmail+"|"+mk+"\n")
        driver.quit()
        print(f"Đã Lưu: {tk_hotmail}|{mk}")

if __name__ == "__main__":
    threads = []
    config  = load(open('config.json'))
    number = config['number']
    while True:
        os.system('cls')
        for l in range(number):
            threading.Thread(target=RegHotmail.reg, args=(l,)).start()
        time.sleep(150)
