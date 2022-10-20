def create_event(input_text):
    user_message = str(input_text)
    user_message = user_message[7:]
    user_message = user_message.split(" - ")
    fecha = ((user_message[1].split(" "))[0]).split("/")
    dia = fecha[0]
    mes = fecha[1]
    año = fecha[2]
    hora = (user_message[1].split(" "))[3]
    #hora_real = int(hora)-7
    #if hora_real < 10:
    #    hora = "0" + str(hora_real)
    #else:
    #    hora = str(hora_real)

    event = {
      'summary': '{}'.format(user_message[0]),
      'start': {
        'dateTime': '{}-{}-{}T{}:00:00-03:00'.format(año,mes,dia,hora),
        'timeZone': 'America/Argentina/Buenos_Aires',
      },
      'end': {
        'dateTime': '{}-{}-{}T{}:00:00-03:00'.format(año,mes,dia,hora),
        'timeZone': 'America/Argentina/Buenos_Aires',
      },
    }
    return event

#print(create_event("/evento Cumple Cami - 16/11/2022 a las 00"))