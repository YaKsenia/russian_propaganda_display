# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from deep_translator import GoogleTranslator
import pandas as pd

def scrape_article(url):

	#	try:

			session = requests.Session()
			req = session.get(url)
			plain_text = req.text
			html = BeautifulSoup(plain_text, "html.parser")
			#print(html)
            

			title = html.find('div', {'class': 'editor text-block active'})
			#print(title)
            
			title_text = title.text
			#print(title_text)
			list_titles = title_text.split(';')
			#print(list_titles)
			for title in list_titles:
						print(title, '\n')
			'''
			title_final = title.text
			articles = html.find('div', {'class': 'article__text article__text_free'})
			article_text = articles.text
            

		except Exception as e:
			print(e)
			title_final = ''
			article_text = ''


		return {'title' : title_final, 'text' : article_text}
    '''

def get_links(url):

	try:
        
            		#timeout = time.time() + 60*2 
            		service = Service(executable_path=GeckoDriverManager().install())
            		options = webdriver.FirefoxOptions()
            		driver = webdriver.Firefox(service=service, options=options)
            		#driver = webdriver.Firefox()
            
            		#open the link
            		driver.get(url)
            		driver.maximize_window()
            
            		#close the banner on the website
            		#driver.find_element_by_id('ensCloseBanner').click()
            		
            		#this is a page number, it will be updated after every time the scraper clicks on a page
            		
            
            				#find the button with page number and click
    
            		#driver.execute_script("window.scrollTo(0,document.documentElement.scrollHeight);")
            		driver.execute_script("window.scrollTo(0, 1700)")

		    # Wait to load page
            		#scroll_pause_time = 5
            		#time.sleep(scroll_pause_time)
            		driver.implicitly_wait(15)
            		#driver.find_element("link text", "Показать еще").click()
            		driver.find_element(By.CSS_SELECTOR, "button.itv-button:nth-child(17)").click()
            		driver.implicitly_wait(10)
            		driver.execute_script("window.scrollTo(0,document.documentElement.scrollHeight);")
            		#driver.implicitly_wait(20)
            		WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.itv-col-wrap")))
                    #button.itv-button:nth-child(17)
                    #.click()
                    #By.LINK_TEXT,
            		#driver.find_element_by_link_text(str("Показать еще")).click()
    				#print ('clicked page',  number)
    
    				#wait 10 sec so the website will not think we are robots
            		#driver.implicitly_wait(5)

				#here you should specify the range of pages you want to scrape (you can start with 1)
            		plain_text = driver.page_source
            		html = BeautifulSoup(plain_text, "html.parser")
            		#articles = html.find_all('div', {'class': 'itv-col-8 itv-col-hd-12'})
            		articles = html.find_all('h2')
            		#print(articles)
            		
            		counter = 0
            		clean_titles = []
            		for article in articles:
        		  
		            		title = article.get_text()
		            		if 'Выпуск новостей' not in title and 'Выпуск программы' not in title and 'Архив новостей' not in title and 'Все новости за' not in title:
		            		    print(title, '\n')
		            		    #clean_titles = clean_titles.join(str(title) + '*')
		            		    clean_titles.append(title + '*')
		            		    counter += 1                                                            
		            		    print(counter) 
            		print(clean_titles)
                        
						#find all links on the page
            		'''
            		            		ankor_list = article.findChildren('a')
            		            		for ankor in ankor_list:

            		            		            		link = ankor.get('href')
            		            		            		#print(link)
            		            		            		if url in link and ("vypusk_novostey" in link or "vypusk_programmy_vremya" in link):
                		            		            		#print(link)
                		            		            		counter += 1                                                            
                		            		            		#print(counter) 
                                                                '''
            		#if time.time() > timeout:
            		            		#break
                                    
                                    
						    #url = 'https://www.aljazeera.com' + url
						    #save url only if it is a news or opinion article (so we get read of social media links, advertisements etc.)
						    #if 'news' in url or 'opinion' in url:
							    #links.append(url)
							    





		#save the links as Pandas dataframe, drop duplicates and return
		
	#	links = pd.DataFrame({'links' : links })
	#	links = links.drop_duplicates(subset='links', keep='last', inplace=False)
            		str_clean_titles = ' '.join([str(elem) for i,elem in enumerate(clean_titles)])
            		f = open("new.txt", "a")
            		f.write(str_clean_titles)
            		f.close()
            		return str_clean_titles

	except Exception as e:
		print(e)

	finally:
		driver.quit()
		print('Finished.')
        
        
def translate(str_clean_titles):


# Use any translator you like, in this example GoogleTranslator
    #for title in clean_titles:
        
        #str_clean_titles = ' '.join([str(elem) for i,elem in enumerate(clean_titles)])
        if len(str_clean_titles) > 3010:
            str_clean_titles1 = str_clean_titles[:3010]
            str_clean_titles2 = str_clean_titles[3010:6020]
            #crashed at 3098
            print(len(str_clean_titles1))
            print(str_clean_titles2)
        print(len(str_clean_titles))
        translated = GoogleTranslator(source='auto', target='en').translate(str_clean_titles1) 
        translated2 = GoogleTranslator(source='auto', target='en').translate(str_clean_titles2) 
        #print(translated)
        #print(translated2)
        return translated + translated2
        
    #return translated

if __name__ == "__main__":
    url = 'https://free.1tv.ru/news/2024-04-16/'
    #'https://free.1tv.ru/news/2024-04-19/'
    
    result = get_links(url)
    #translation = translate(result)
    #print(translation)