from splinter import Browser
from time import sleep
from threading import Semaphore
from bs4 import BeautifulSoup

import urllib

category_links = {
	"Direito militar": "http://www.jusbrasil.com.br/topicos/292125/direito-militar/artigos",
	"Direito do trabalho": "http://www.jusbrasil.com.br/topicos/355654/direito-do-trabalho/artigos",
	"Direito agrario": "http://www.jusbrasil.com.br/topicos/26413195/direito-agrario/artigos",
	"Direito ambiental": "http://www.jusbrasil.com.br/topicos/26413196/direito-ambiental/artigos",
	"Direito civil": "http://www.jusbrasil.com.br/topicos/26413200/direito-civil/artigos",
	"Direito consitucional": "http://www.jusbrasil.com.br/topicos/26413203/direito-constitucional/artigos",
	"Direito de energia": "http://www.jusbrasil.com.br/topicos/26413204/direito-de-energia/artigos",
	"Direito de familia": "http://www.jusbrasil.com.br/topicos/26413205/direito-de-familia/artigos",
	"Direito do consumidor": "http://www.jusbrasil.com.br/topicos/26413213/direito-do-consumidor/artigos",
	"Direito de turismo": "http://www.jusbrasil.com.br/topicos/26413215/direito-do-turismo/artigos",
	"Direito de internet": "http://www.jusbrasil.com.br/topicos/26413216/direito-de-internet/artigos",
	"Direito eleitoral": "http://www.jusbrasil.com.br/topicos/26413218/direito-eleitoral/artigos",
	"Direito financeiro": "http://www.jusbrasil.com.br/topicos/26413222/direito-financeiro/artigos",
	"Direito medico": "http://www.jusbrasil.com.br/topicos/26413226/direito-medico/artigos",
	"Direito internacional": "http://www.jusbrasil.com.br/topicos/26413224/direito-internacional/artigos",
	"Direito publico": "http://www.jusbrasil.com.br/topicos/26413234/direito-publico/artigos",
	"Direitos humanos": "http://www.jusbrasil.com.br/topicos/26413243/direitos-humanos/artigos",
	"Transito": "http://www.jusbrasil.com.br/topicos/735233/transito/artigos"
}

class Crawler:

	def __init__(self, base_links):
		self.base_links = base_links
		self.links = {}
		#self.browser = Browser()
		self.semaphore = Semaphore()

	def expand_page(self, page):
		self.browser.visit(page)

		for i in range(9):
			try:
				self.browser.find_by_css('.more').click()
			except:
				break
			sleep(5)

	def get_links_in_loaded_page(self):
		article_links = self.browser.find_by_css('.feed-item-title')
		
		to_return = []
		for el in article_links:
			to_return.append(el['href'])

		return to_return

	def parse_articles(self, links):
		pass

	def write_article(self, category, url):
		raw_page = urllib.urlopen(url).read()
		article = self.get_article_from_page(raw_page)
		article_id = url.split("/")[2]
		

	def get_article_from_page(self, page):
		to_return = ""

		soup = BeautifulSoup(page)
		to_return += soup.header.find_all("h1")[0].get_text()
		to_return += soup.header.find_all("h2")[0].get_text()
		soup.article.div.extract()
		to_return += soup.article.get_text()

		return to_return

	def set_links(self, category, links):
		self.semaphore.acquire()
		self.links[category] = links
		self.semaphore.release()

	def generate_links(self):
		output = file("links", "wt")
		for category in self.base_links:

			self.expand_page(self.base_links[category])
			self.set_links(category, self.get_links_in_loaded_page())

		#	output.write(category)
		#	output.write("\n"+str(len(self.links[category]))+"\n")
		#	for link in self.links[category]:
		#		output.write(link)
		#		output.write("\n")
		#	print("Category "+ category +" printed!")

	def run(self):
		self.generate_links()
		

crawler = Crawler(category_links)
#crawler.run()
crawler.get_article_from_page(urllib.urlopen("http://joaovcastello.jusbrasil.com.br/artigos/133227251/breves-consideracoes-informativas-e-juridicas-do-seguro-dpvat?ref=home").read())

#browser = Browser()
#browser.visit("http://www.jusbrasil.com.br/topicos/292125/direito-militar/noticias")

#summary = browser.find_by_tag('summary')
#button = browser.find_by_css('.more')
#button.click()
#browser.quit()
