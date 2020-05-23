import sublime, sublime_plugin, re, string

class KdcformatCommand(sublime_plugin.TextCommand): 
	def run(self, edit): 
		for region in self.view.sel():
			if not region.empty():
				s = self.view.substr(region)
				news = s.replace('[', '[\n\t')
				news = news.replace('(','(\n\t\t')
				news = news.replace(', ',',\n\t\t')
				news = news.replace(']','\n]')
				news = news.replace(')','\n\t\t)')
				news = news.replace('),','),\n')
				self.view.replace(edit, region, news)
