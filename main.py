#importing modules
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

#settting chrome options (this is the only way it will work in repl)
chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

#this is the driver for the web page that will be used 
driver = webdriver.Chrome(options=chrome_options)

#login function for sk2s
def login():
  #allows user to enter there email and password
  user = input("Enter your s2sa username: ")
  password = input("Enter your s2sa password: ")

#this gets the website
  driver.get("https://s2sacademy.com/login/")

  #id_box(2) finds the elements by whatever name the element is called in the html of the page
  #send_keys sends the variable to the page and "types it in"
  id_box = driver.find_element_by_name('email')
  id_box.send_keys(user)
  id_box2 = driver.find_element_by_name('pass')
  id_box2.send_keys(password)

  #this basically presses enter
  #unicode has to be used as the website doe not accept directed inputs
  id_box2.send_keys(u'\ue007')


#this function loads the progress page and once implemented it will gather all of the completed elements
def navigate():
  driver.get("https://s2sacademy.com/progress/")




#main function
def main():
  login()
  navigate()

main()
