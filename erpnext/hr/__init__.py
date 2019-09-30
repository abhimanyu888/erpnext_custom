
from __future__ import unicode_literals
from frappe.model.document import Document

class Operation(Document):
	def validate(self):
		if not self.description:
			self.description = self.name
