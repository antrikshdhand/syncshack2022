class user:

	def __init__(self, SID, unikey, name, course, faculty, subjects):
		self.SID = SID
		self.unikey = unikey
		self.name = name
		self.course = course
		self.faculty = faculty
		self.subjects = subjects
		self.status = False

	#getter and setter methods

	def get_SID(self):
		return self.SID

	def get_Unikey(self):
		return self.unikey

	def get_name(self):
		return self.name

	def get_course(self):
		return self.course

	def set_course(self, course):
		self.course = course
	
	def get_faculty(self):
		return self.faculty

	def set_faculty(self, faculty):
		self.faculty = faculty

	def get_subjects(self):
		return self.subjects
	
	def set_subjects(self, subjects):
		self.subjects = subjects

	def	get_status(self):
		return self.status
	
	def change_status(self):
		self.status = not self.status

	
	



		
