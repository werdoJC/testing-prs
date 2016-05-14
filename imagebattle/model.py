from imagebattle import db

class Image(db.Model):
	image_id = db.Column(
	  db.Integer, primary_key = True)
	url = db.Column(db.Text, unique = True)
	
	def_init_(self, url):
		self.url = url
		