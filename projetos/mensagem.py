import pywhatkit
phone_number = '+5519991207669'
message = 'Salve dog,vai com que roupa hoje?'
hours = 15
minutes = 41
pywhatkit.sendwhatmsg(phone_number, message, hours, minutes)
print("Mensagem enviada")