#importing modules
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains

from selenium.webdriver.common.keys import Keys
import csv

#settting chrome options (this is the only way it will work in repl)
chrome_options = Options()9
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

#this is the driver for the web page that will be used 
driver = webdriver.Chrome(options=chrome_options)


#login function for sk2s
def login():

  #allows user to enter there email and password
  user = input("Enter your s2sa username: ")
  password = input("Enter your s2sa password: ")
 
  #id_box(2) finds the elements by whatever name the element is called in the html of the page
  #send_keys sends the variable to the page and "types it in"
  id_box = driver.find_element_by_name('email')
  id_box.send_keys(user)
  id_box2 = driver.find_element_by_name('pass')
  id_box2.send_keys(password)

  #this basically presses enter
  #unicode has to be used as the website doe not accept directed inputs
  id_box2.send_keys(u'\ue007')

  if driver.find_elements_by_class_name('error'):
    ActionChains(id_box) \
      .key_down(u'\ue009') \
      .send_keys('a') \
      .key_up(u'\ue009') \
      .send_keys(u'\ue003') \
  

    print("Please rety your login was incorrect!")
 


    login()

#this function loads the progress page and once implemented it will gather all of the completed elements
def navigate():
  driver.get("https://s2sacademy.com/progress/")
  count=0
  title = ""
  for container in driver.find_elements_by_class_name("progressComponent"):  
    for card in container.find_elements_by_class_name('progressCard'):
      count+=1
      print(card)
      if card.find_elements_by_xpath("//span[@class='progress completed']"):
        for item in card.find_elements_by_xpath("//span[@class='progress completed']"):
          title = item.find_element_by_xpath("//span[@class='title']").text()
          print(title)
          print(count)
  


'''
 with open('elements.csv', 'w') as f:
    #creates the writer for the csv file
    writer = csv.writer(f)
    writer.writerows(c_list)
'''

def pro_nav():
  driver.get("https://proportal.lec.ac.uk/ProPortal/pages/dashboard.aspx?studentref=XGhas11q0aA&academicyearid=2122")
  menu = driver.find_elements_by_xpath("//span[@class'icon-bar']")
  
  ActionChains(menu) \
    .move_to_element(menu) \
    .click(menu) \
    .perform()


# This loads up the proportal login page
def proportal_login():
  # changes the driver to the current login page
  driver.get("https://proportal.lec.ac.uk/ProPortal")
  print("Please login to proportal")
  # proportal login is not a html page
  logged = input(str.lower("please type done once you have logged in: "))
  # checks if the user is done
  if logged == "done":
    pro_nav()
  else:
    print("retry")
    proportal_login()


#main function
def main():
  
   #this gets the website
  driver.get("https://s2sacademy.com/login/")
  login()
  navigate()

''' second half of program
  proportal_login()
'''

main()
