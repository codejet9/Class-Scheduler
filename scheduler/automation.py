from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import datetime
import time
import sqlite3
from selenium.webdriver.chrome.options import Options



all=time.localtime()
day_now=str(time.strftime("%A"))





def clickme():

    opt=Options()
    opt.add_argument('--disable-blink-features=AutomationControlled')
    opt.add_argument('--start-maximized')
    opt.add_experimental_option("prefs",{
        "profile.default_content_setting_values.media_stream_mic":1,
        "profile.default_content_setting_values.media_stream_camera":1,
        "profile.default_content_setting_values.geolocation":0,
        "profile.default_content_setting_values.notifications":1
    })
    path="chromedriver.exe"
    driver=webdriver.Chrome(options=opt,executable_path=r'chromedriver.exe')


    ### CREATING/CONNECTING DATABASE TABLE ###
    myt1=sqlite3.connect("schedule.db")

    ### CREATE CURSOR ###
    myc1=myt1.cursor()
    
    ### fetching and printing ###
    myc1.execute("SELECT * FROM mytt WHERE day = '{}'".format(day_now))
    records=myc1.fetchall()

    cn=[]
    cl=[]
    ts=[]
    te=[]
    for record in records:
        cn.append(record[1])
        cl.append(record[2])
        ts.append(record[3])
        te.append(record[4])
        #print(cn)
        #print(cl)
    
    ### COMMIT CHANGES ###
    myt1.commit()

    ### CLOSE CONNECTIONS ###
    myt1.close()




    ##########################################
    ### CREATING/CONNECTING DATABASE TABLE ###
    myt1=sqlite3.connect("schedule.db")

    ### CREATE CURSOR ###
    myc1=myt1.cursor()
    
    ### fetching and printing ###
    myc1.execute("SELECT * FROM mycreds")
    records=myc1.fetchall()
    
    mail=records[0][0]
    mypassword=records[0][1]

    ### COMMIT CHANGES ###
    myt1.commit()

    ### CLOSE CONNECTIONS ###
    myt1.close()
    ###########################################



    redirect="https://accounts.google.com/signin/v2/identifier?flowName=GlifWebSignIn&flowEntry=ServiceLogin"

    def logintotal():
        driver.get(redirect)
        profile=driver.find_element_by_id("identifierId")
        profile.send_keys(mail)
        driver.implicitly_wait(5)
        profile.send_keys(Keys.RETURN)
        try:
            password1=WebDriverWait(driver,10).until(
                EC.presence_of_element_located((By.NAME,"password"))
            )
            password1.send_keys(mypassword)
            driver.implicitly_wait(5)
            password1.send_keys(Keys.RETURN)
        except:
            driver.quit()

    logintotal()

    def joining():
        datetimeinfo=datetime.datetime.now()
        nowhour=datetimeinfo.hour
        nowminute=datetimeinfo.minute
        nowtime=nowhour+(nowminute/60)
        for i in range(0,len(cn)):
            if nowtime>=ts[i] and nowtime<te[i]:
                link=cl[i]
                driver.get(link)
                driver.implicitly_wait(10)
                driver.get(link)
                driver.implicitly_wait(10)
                try:
                    mic=WebDriverWait(driver,10).until(
                        EC.presence_of_element_located((By.CLASS_NAME,"HotEze"))
                    )
                    mic.click()
                except:
                    #driver.quit()
                    pass

                driver.implicitly_wait(10)

                
                cam=driver.find_elements_by_class_name("HotEze")
                main=cam[0]
                main.click()

                driver.implicitly_wait(10)

                join=driver.find_element_by_css_selector("div.uArJ5e.UQuaGc.Y5sE8d.uyXBBb.xKiqt")
                join.click()

                running=True
                while running:
                    datetimeinfo=datetime.datetime.now()
                    nowhour1=datetimeinfo.hour
                    nowminute1=datetimeinfo.minute            
                    nowtime1=nowhour1+(nowminute1/60)
                    if nowtime1 >= te[i]:
                        last=len(cn)-1
                        if(i==last):
                            driver.close()
                        else:
                            joining() 

    joining()

            