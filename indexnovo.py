from selenium import webdriver
import time
import csv
# Se de erro... instale o geckodriver, se persistir o erro instale
# o Chrome Driver e mude de Firefox() para Chrome()
msg = "Teste mais avançado, responde para não bloquear meu numrero"
driver = webdriver.Firefox()
with open ('arquivos\lista.csv','r') as entrada:
    numero=csv.reader(entrada)
    next(numero)
    for contatos in numero:
        driver.get('https://web.whatsapp.com/send?phone=55'+str(contatos).strip('[]')+'&text=ola%20'+msg)
        time.sleep(20)
        btn = driver.find_element_by_xpath('/html/body/div/div/div/div[4]/div/footer/div[1]/div[3]/button')
        btn.click()
        #print(contatos)

        


#numero=['84994278758','84999053487']

#for linha in ler:
    #driver.get('https://web.whatsapp.com/send?phone=55'+contatos+'&text=ola%20'+msg)
    #time.sleep(20)
    #btn = driver.find_element_by_xpath('/html/body/div/div/div/div[4]/div/footer/div[1]/div[3]/button')
    #btn.click()
    #print(linha)


driver.quit()





