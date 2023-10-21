import requests

pdfPath = "C:/Users/ALANMART/Downloads/CG_AMF_DC_Jun23 FINAL.pdf"

dashline = '-' * 50


files = [
    ('file', ('file', open(pdfPath, 'rb'), 'application/octet-stream'))
]
headers = {
    'x-api-key': 'sec_JPvnQqHhk5d651bhDesP2FxxgDmDTeBJ'
}

response = requests.post(
    'https://api.chatpdf.com/v1/sources/add-file', headers=headers, files=files)

if response.status_code == 200:
    print('Source ID:', response.json()['sourceId'])
    sourceID = response.json()['sourceId']
    pregunta = True
    while pregunta == True:
        
        print(dashline)
        content = input('Introduce una pregunta del documento: ')

        data = {
        'sourceId': sourceID,
            'messages': [
                {
                    'role': "user",
                    'content': content,
                }
            ]
        }
        response = requests.post(
        'https://api.chatpdf.com/v1/chats/message', headers=headers, json=data)

        if response.status_code == 200:
            print('\nResult:', response.json()['content'])
            nuevaPregunta = input('\nNecesitas hacer otra pregunta? Y/N: ' )
            if nuevaPregunta == 'Y':
                pregunta = True
            else:
                pregunta = False
            
        else:
            print('Status:', response.status_code)
            print('Error:', response.text)
else:
    print('Status:', response.status_code)
    print('Error:', response.text)