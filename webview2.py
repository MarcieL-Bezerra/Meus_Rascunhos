import time
import tkinter.messagebox as tkMessageBox

from selenium import webdriver

#webdriver​.setProperty("C:Windows\chromedriver.exe");
driver = webdriver.Firefox()
#driver = webdriver.Chrome()

driver.get("https://www.google.com​")
time.sleep(4)

buscas = ['teste', 'evolução', 'coronavirus']

for i in range (0,3):
    driver.execute_script("window.open('');")
    driver.switch_to.window(driver.window_handles[i])
    driver.get("https://www.google.com.br​")
    time.sleep(1)
    caixabusca = driver.find_element_by_name("q")
    caixabusca.send_keys(str(buscas[i]))
    caixabusca.submit()
time.sleep(1)
tkMessageBox.showinfo("Busca Finalizada", message= "Realizado com sucesso!") 

#manufacturer​.send_keys(Keys.CONTROL + 't')
#os​.system("tskill /A iexplore")
#os​.system("tskill /A Chrome")
