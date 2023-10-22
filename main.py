import time
import pandas as pd
from selenium import webdriver

driver = webdriver.Chrome(executable_path="chromedriver.exe")
databug = open("./bug.txt", "wt", encoding="utf8")
datacpl = open("./complete.txt", "wt", encoding="utf8")


def login_github(username_git, password_git):
    driver.get("https://github.com/login")
    driver.find_element_by_id("login_field").send_keys(username_git)
    driver.find_element_by_id("password").send_keys(password_git)
    submit = driver.find_element("xpath", '//*[@id="login"]/div[4]/form/div/input[13]')
    submit.click()
    time.sleep(10)


def confirm():
    invited = driver.find_element("xpath", '/html/body/div[1]/div[6]/main/div[2]/form[2]/div[2]/div/button')
    invited.click()


def selection(name,option,fullname,lop):
    driver.find_element_by_id("org-invite-complete-input").send_keys(name)
    time.sleep(2)
    try:
        select = driver.find_element("xpath", '//*[@id="org-invite-complete-results-option-0"]')
        select.click()
        time.sleep(1)

        subb = driver.find_element("xpath", '//*[@id="invite-member-dialog"]/div[2]/div/form/div/div/button')
        subb.click()

        # Ban hoc tap
        study = driver.find_element("xpath", '//*[@id="team-8789808"]')
        study.click()

        if "Git" in option:  # Git-github
            git = driver.find_element("xpath", '//*[@id="team-8790397"]')
            git.click()

        # if "KTLT" in option: #KTLT
        #     ktlt = driver.find_element("xpath", '//*[@id="team-8790239"]')
        #     ktlt.click()

        # if "OOP" in option: #OOP
        #     oop = driver.find_element("xpath", '//*[@id="team-8790246"]')
        #     oop.click()
        #
        # if "TinDaiCuong" in option: #TDC
        #     tdc = driver.find_element("xpath", '//*[@id="team-8790372"]')
        #     tdc.click()
        #
        # if "CTDLGT" in option: #CTDL
        #     ctdl = driver.find_element("xpath", '//*[@id="team-8790241"]')
        #     ctdl.click()

        time.sleep(1)

        confirm()
        name = name + " | " + fullname + " | " + lop + " | " + option + "\n"
        datacpl.write(name)
    except:
        name = name + " | " + fullname + " | " + lop + " | " + option + "\n"
        databug.write(name)
        return


def invite(name, option, fullname, lop, check):
    driver.get("https://github.com/orgs/sfit-utc/people")
    invited = driver.find_element("xpath", '//*[@id="dialog-show-invite-member-dialog"]/span/span')
    invited.click()

    if check == "0":
        return
    else:
        selection(name,option,fullname,lop)



def main():
    username_git = "khiemhm2004@gmail.com"
    password_git = "@hmk2004"

    login_github(username_git, password_git)
    data = pd.read_json("data.json")

    lenn = len(data)
    for i in range(lenn):
        name = data.get("Username Github")[i]
        option = data.get("Bạn đang học lớp nào (Nêu không học thì chọn mục không) [LopHoc]")[i]
        option = str(option)
        fullname = data.get("Họ và Tên")[i]
        lop = data.get("Tên Lớp (Viết in hoa, không dấu cách. Ví dụ: CNTT1-K62)")[i]
        check = data.get("Check")[i]
        check = str(check)
        invite(name, option, fullname, lop, check)
        time.sleep(1)


if __name__ == '__main__':
    main()
