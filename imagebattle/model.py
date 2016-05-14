from imagebattle import db

class Image(db.Model):
	image_id = db.Column(
	  db.Integer, primary_key = True)
	url = db.Column(db.Text, unique = True)
	
	def __init__(self, url):
		self.url = url

		