#coding=utf8
import os,sys
import tornado.web
import tornado.ioloop


class IndexHandler(tornado.web.RequestHandler):
	def get(self):
		self.write("Welcome to allen's resume_broken_transfer project<br/>Please access the /upload or the /download for the API")


class UploadHandler(tornado.web.RequestHandler):
	def get(self):
		self.write("hello world - upload")


class DownloadHandler(tornado.web.RequestHandler):
	def get(self):
		self.write("hello world - download")



application = tornado.web.Application([
	(r'/',IndexHandler),
	(r'/upload',UploadHandler),
	(r'/download',DownloadHandler)
	],debug=True)



if __name__ == '__main__':
	application.listen(8282)
	tornado.ioloop.IOLoop.instance().start()





