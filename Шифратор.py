def Encrypt():
  itog = ''
  x, y = 0, 0
  for i in range(len(strr)):
    if strr[i] in a1:
      y = 1
      for j in range(len(a1)):
        if strr[i] == a1[j]:
          x = j + 1
    elif strr[i] in a2:
      y = 2
      for j in range(len(a2)):
        if strr[i] == a2[j]:
          x = j + 1
    elif strr[i] in a3:
      y = 3
      for j in range(len(a3)):
        if strr[i] == a3[j]:
          x = j + 1
    elif strr[i] in a4:
      y = 4
      for j in range(len(a4)):
        if strr[i] == a4[j]:
          x = j + 1
    elif strr[i] in a5:
      y = 5
      for j in range(len(a5)):
        if strr[i] == a5[j]:
          x = j + 1
    else:
      print('Нет такого символа!')
      break
    itog = itog + (str(x) + str(y))
  return itog


def Decrypt():
  itog, result = '', ''
  x, y = 0, 0
  for i in range(0, len(strr) - 1, 2):
    result = strr[i] + strr[i + 1]
    x, y = result[0], result[1]
    if y == '1':
      itog = itog + a1[int(x) - 1]
    elif y == '2':
      itog = itog + a2[int(x) - 1]
    elif y == '3':
      itog = itog + a3[int(x) - 1]
    elif y == '4':
      itog = itog + a4[int(x) - 1]
    elif y == '5':
      itog = itog + a5[int(x) - 1]
    else:
      print('Нет такого символа!')
      break
  return itog


class Color:
  color = '\033[0m'
  red = '\033[31m'
  green = '\033[32m'
  yellow = '\033[33m'


def set_color(text, color):
  return color + text + Color.color


class Cell(object):
  start = set_color('---' * 10, Color.green)
  question = set_color('Введите действие: ', Color.yellow)
  end = set_color('---' * 10, Color.red)


a1 = 'abcde'
a2 = 'fghik'
a3 = 'lmnop'
a4 = 'qrstu'
a5 = 'vwxyz'

while True:
  try:
    print(Cell.start)
    strr = input('Введите строку: ')
    print('\nЗашифровать - 1\nРасшифровать - 2\nЗакончить - 3')
    action = int(input(f'\n{Cell.question}'))
    if action == 1:
      strr = strr.lower()
      strr = strr.replace('j', 'i')
      print(f'\nБыло: {strr}\nЗашифровка: {Encrypt()}')
      continue
    elif action == 2:
      if len(strr) % 2 == 0:
        print(f'\nБыло: {strr}\nРасшифровка: {Decrypt()}')
        continue
      else:
        print('Расшифровка не возможна!')
        continue
    elif action == 3:
      print(f'Всего хорошего!\n{Cell.end}')
      break
    else:
      print('Неверно введено!')
      continue
  except ValueError:
    print('Неверно введено!')
    continue
