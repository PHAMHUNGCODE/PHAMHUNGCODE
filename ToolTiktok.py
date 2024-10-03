        print("> An error occured. Trying again...", datetime.now().strftime("%H:%M:%S"))
        driver.refresh()
        loop1()

def loop2():
    global Hearts
    countdown(10)
    try:
        driver.find_element_by_xpath("/html/body/div[4]/div[1]/div[3]/div/div[2]/div/button").click()
    except:
        print("> Solve the captcha!")
        driver.refresh()
        loop2()
    try:
        countdown(2)
        driver.find_element_by_xpath('//*[@id="sid2"]/div/div/div/form/div/input').send_keys(vidUrl)
        countdown(1)
        driver.find_element_by_xpath('//*[@id="sid2"]/div/div/div/form/div/div/button').click()
        countdown(5)
        driver.find_element_by_xpath('//*[@id="c2VuZE9nb2xsb3dlcnNfdGlrdG9r"]/div[1]/div/form/button').click()
        countdown(6)
        hearts = driver.find_element_by_xpath('//*[@id="c2VuZE9nb2xsb3dlcnNfdGlrdG9r"]/span').text.split()
        Hearts += int(hearts[0])
        countdown(5)
        driver.refresh()
        countdown(640)
        loop2()
    except:
        print("> An error occured. Trying again...")
        driver.refresh()
        loop2()

def loop3():
    global Followers
    countdown(10)
    try:
        driver.find_element_by_xpath("/html/body/div[4]/div[1]/div[3]/div/div[1]/div/button").click()
        countdown(2)
        driver.find_element_by_xpath('//*[@id="sid"]/div/div/div/form/div/input').send_keys(vidUrl)
        countdown(1)
        driver.find_element_by_xpath('//*[@id="sid"]/div/div/div/form/div/div/button').click()
        countdown(5)
        folls = driver.find_element_by_xpath('//*[@id="c2VuZF9mb2xsb3dlcnNfdGlrdG9r"]/div[1]/div/form/button').text.split()
        Followers += int(folls[0])
        print(folls)
        countdown(2)
        driver.find_element_by_xpath('//*[@id="c2VuZF9mb2xsb3dlcnNfdGlrdG9r"]/div[1]/div/form/button').click()        
        countdown(6)
        driver.refresh()
        countdown(310)
        loop3()
    except:
        print("> An error occured. Now will retry again")
        driver.refresh()
        loop3()

system("cls")
print(pyfiglet.figlet_format("Successful", font="slant"))

if auto == 1:
    driver.get("https://zefoy.com/")
    a = threading.Thread(target=title1)
    b = threading.Thread(target=loop1)
    a.start()
    b.start()
elif auto == 2:
    driver.get("https://zefoy.com/")
    a = threading.Thread(target=title2)
    b = threading.Thread(target=loop2)
    a.start()
    b.start()
elif auto == 3:
    driver.get("https://zefoy.com/")
    a = threading.Thread(target=title3)
    b = threading.Thread(target=loop3)
    a.start()
    b.start()
else:
    print("Input between 1-3")
