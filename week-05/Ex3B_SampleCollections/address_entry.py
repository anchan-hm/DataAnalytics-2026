# dictionary for contact_info
contact_info = { "name": "Alexus",
                "address": "123 Elevate",
                "city": "Charlotte",
                "state": "NC",
                "zip": "12345"}

# formatting address for mailing
print(f"""
{contact_info["name"]}
{contact_info["address"]}
{contact_info["city"]},{contact_info["state"]},{contact_info["zip"]}""")
#output: Alexus
#        123 Elevate
#        Charlotte,NC,12345

# removing key:value pair for "name"
contact_info.pop("name")
print(contact_info) #output: {'address': '123 Elevate', 'city': 'Charlotte', 'state': 'NC', 'zip': '12345'}

# creating full_name variable
full_name = {"first name": "Alexus",
             "last name": "Chanthadara"}
print(full_name) #output: {'first name': 'Alexus', 'last name': 'Chanthadara'}

# using .update() for "honorific"
full_name.update({"honorific": "Ms."})
print(full_name) #output: {'first name': 'Alexus', 'last name': 'Chanthadara', 'honorific': 'Ms.'}

# using .update() to add full_name to contact_info
contact_info.update({"full_name": full_name})
print(contact_info)
#output: 'address': '123 Elevate', 'city': 'Charlotte', 'state': 'NC', 'zip': '12345', 
# 'full_name': {'first name': 'Alexus', 'last name': 'Chanthadara', 'honorific': 'Ms.'}}

# formatting address for mailing
print(f"""
{contact_info["full_name"]["honorific"]} {contact_info["full_name"]["first name"]} {contact_info["full_name"]["last name"]}
{contact_info["address"]}
{contact_info["city"]},{contact_info["state"]} {contact_info["zip"]}
""")
#output: Ms. Alexus Chanthadara
#        123 Elevate
#        Charlotte,NC 12345