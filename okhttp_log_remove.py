# -*- coding: utf-8 -*-

import re
import sublime
import sublime_plugin


class OkhttplogremoveCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		for region in self.view.sel():
			if not region.empty():
				s = self.view.substr(region)
				self.view.replace(edit, region, OkhttplogremoveCommand.remove_log(s))

	def remove_log(str):
		startCharArray = re.findall(r"\n[\d]{4}-[\d]{2}-[\d]{2} [\d]{2}:[\d]{2}:[\d]{2}.[\d]{1,3}.*?D/OkHttp: ", str)

		for s in startCharArray:
			str = str.replace(s,"")
		return str
