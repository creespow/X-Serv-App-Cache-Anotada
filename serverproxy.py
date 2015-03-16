#!/usr/bin/python
# -*- coding: utf-8 -*-

import webapp
import socket
import urllib

class serverproxy (webapp.webApp):

	def parse (self, request):		
		url = request.split()[1][1:].split('/')[0]		
		return url
		
	def process(self, parsedRequest):
		try:
			url = "http://" + parsedRequest
			f = urllib.urlopen (url)

		except IOError:
			code = "400"
			body = "Error"

		html = f.read()			
		posicion = html.find('<body')
		posicion = html.find('>', posicion)
		html = (html[:posicion + 1] + "hola" +
		"</br></br>" + html[(posicion + 1):])		

		return ("200 OK", html)
									

if __name__ == "__main__":
		new_serv = serverproxy (socket.gethostname(), 1234)
