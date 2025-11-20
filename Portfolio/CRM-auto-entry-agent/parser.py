def extract_contact(text):
parts = text.split('|')
return {
'name': parts[0].split('<')[0].strip(),
'email': parts[0].split('<')[1].replace('>', '').strip(),
'product': parts[1].split(':')[1].strip(),
'budget': int(parts[2].split(':')[1].strip())
}
