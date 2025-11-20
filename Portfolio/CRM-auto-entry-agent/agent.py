from parser import extract_contact
from crm_client import send_to_crm


email = "John Doe <john@example.com> | Product: X | Budget: 5000"
contact = extract_contact(email)
send_to_crm(contact)
