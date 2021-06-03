from utils import vxMessage,openChrome
import json
import time




def punch_clock(username,password):
    try:
        driver = openChrome()
        driver.get("http://one.hfut.edu.cn" )
        time.sleep(3)
        driver.find_element_by_name('username').send_keys(username)
        driver.find_element_by_id('pwd').send_keys(password)
        driver.find_element_by_id('sb2').click()
        time.sleep(5)

        step1 = "/html/body/div[1]/div/section/div[1]/div/div[3]/div[1]/div/div[2]/div/ul/li[13]/p"
        step2 = "/html/body/main/div/div[2]/div[3]/div/div[2]/div[1]/div[1]/div"
        step3 = "/html/body/main/article/footer/a[1]"

        driver.find_element_by_xpath(step1).click()#点选按钮
        time.sleep(15)
        driver.switch_to_window(driver.window_handles[1])

        driver.find_element_by_xpath(step2).click()#点选按钮
        time.sleep(15)
        driver.switch_to_window(driver.window_handles[2])

        driver.find_element_by_xpath(step3).click()#确认打卡
        driver.quit()
        return True
    except:
        driver.quit()
        return False



if __name__ == '__main__':
    with open(file="userInfo.json",mode='r') as f:
        users = f.read()
        users = json.loads(users)

    for user in users:
        username = user["username"]
        password = user["password"]
        SCKEY = user["SCKEY"]
        if punch_clock(username,password):
            vxMessage("打卡成功！",SCKEY)
        else:
            vxMessage("打卡失败！",SCKEY)






