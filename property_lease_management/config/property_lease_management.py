from __future__ import unicode_literals
from frappe import _

def get_data():
	return [
		{
			"label":("Property"),
			"items":[
				{
					"type":"doctype",
					"name":"Property Units",
				},
				{
					"type":"doctype",
					"name":"Property Owner"
				},
				{
					"type":"doctype",
					"name":"Property Unit Attribute"
				},
				{
					"type":"doctype",
					"name":"Agent"
				}
			]
		},
		{
			"label": ("Inspection"),
			"items":[
				{
					"type":"doctype",
					"name":"Inspection Request"
				},
				{
					"type":"doctype",
					"name":"Inspection Details"
				},
				{
					"type":"doctype",
					"name":"Inspector Items"
				},

			]
		},
		{
			"label": ("Tenancy"),
			"items":[
				{
					"type":"doctype",
					"name":"Tenant"
				},
				{
					"type":"doctype",
					"name": "Tenancy Agreement"
				},
				{
					"type":"doctype",
					"name":"Jurisdiction"
				},
			]
		},
		{	"label": ('Periodicity'),
			"items":[
				{
					"type":"doctype",
					"name":"Periodicity"
				}
			]

		}
	]
