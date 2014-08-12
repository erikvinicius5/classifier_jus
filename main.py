from splinter import Browser

category_links = {
	"Direito militar", "http://www.jusbrasil.com.br/topicos/292125/direito-militar"
	"Direito do trabalho", "http://www.jusbrasil.com.br/topicos/355654/direito-do-trabalho"
	"Direito agrario", "http://www.jusbrasil.com.br/topicos/26413195/direito-agrario"
	"Direito civil", "http://www.jusbrasil.com.br/topicos/26413196/direito-ambiental"
	"Direito constitucional", "http://www.jusbrasil.com.br/topicos/26413200/direito-civil"
	"Direito de energia", "http://www.jusbrasil.com.br/topicos/26413203/direito-constitucional"
	"Direito ", "http://www.jusbrasil.com.br/topicos/26413204/direito-de-energia"
	"Direito ", "http://www.jusbrasil.com.br/topicos/26413205/direito-de-familia"
	"Direito ", "http://www.jusbrasil.com.br/topicos/26413213/direito-do-consumidor"
	"Direito ", "http://www.jusbrasil.com.br/topicos/26413215/direito-do-turismo"
	"Direito ", "http://www.jusbrasil.com.br/topicos/26413216/direito-de-internet"
	"Direito eleitoral", "http://www.jusbrasil.com.br/topicos/26413218/direito-eleitoral"
	"Direito financeiro", "http://www.jusbrasil.com.br/topicos/26413222/direito-financeiro"
	"Direito medico", "http://www.jusbrasil.com.br/topicos/26413226/direito-medico"
	"Direito internacional", "http://www.jusbrasil.com.br/topicos/26413224/direito-internacional"
	"Direito publico", "http://www.jusbrasil.com.br/topicos/26413234/direito-publico"
	"Direitos humanos", "http://www.jusbrasil.com.br/topicos/26413243/direitos-humanos"
	"Transito ", "http://www.jusbrasil.com.br/topicos/735233/transito"
}

final_links = {}
for category in category_links:
	final_links[category] = []

class Visitor:

	def __init__(self, links):
		self.links = links
		self.browser = Browser()

	def run(self):
		for link in self.links:
			browser.visit(self.links[link])



browser = Browser()
browser.visit("http://www.jusbrasil.com.br/topicos/292125/direito-militar/noticias")

summary = browser.find_by_tag('summary')
button = browser.find_by_css('.more')
button.click()
browser.quit()
