def cilinder_calclulater(effort,table):
  list_complete = {}
  for cilinder_d, bars in table.items():
    for bar,press in bars.items():
      if effort <= press:
        list_complete[cilinder_d] = {bar:press}
        break
  return list_complete



cilinder_table = {
  'cilinder_d16': {'1bar': 1.7, '2bar': 3.5, '3bar': 5.3, '4bar': 7.1, '5bar': 8.8, '6bar': 10.6, '7bar':12.3, '8bar':14.5},
  'cilinder_d20': {'1bar': 2.7, '2bar': 5.5, '3bar': 8.3, '4bar': 10.1, '5bar': 13.8, '6bar': 16.6, '7bar':19.3, '8bar':22.5},
  'cilinder_d25': {'1bar': 4.7, '2bar': 8.5, '3bar': 13.3, '4bar': 17.1, '5bar': 21.8, '6bar': 25.6, '7bar':30.3, '8bar':34.5},
  'cilinder_d32': {'1bar': 7.7, '2bar': 14.5, '3bar': 21.3, '4bar': 28.1, '5bar': 35.8, '6bar': 42.6, '7bar':49.3, '8bar':56.5},
  'cilinder_d40': {'1bar': 11.7, '2bar': 23.5, '3bar': 35.3, '4bar': 44.1, '5bar': 55.8, '6bar': 66.6, '7bar':77.3, '8bar':88.5},
  'cilinder_d50': {'1bar': 17.7, '2bar': 34.5, '3bar': 51.3, '4bar': 70.1, '5bar': 86.8, '6bar': 103.6, '7bar':121.3, '8bar':138.5},
  'cilinder_d63': {'1bar': 27.7, '2bar': 55.5, '3bar': 82.3, '4bar': 110.1, '5bar': 137.8, '6bar': 165.6, '7bar':192.3, '8bar':220.5},
  'cilinder_d80': {'1bar': 44.7, '2bar': 88.5, '3bar': 133.3, '4bar': 177.1, '5bar': 221.8, '6bar': 266.6, '7bar':310.3, '8bar':354.5},
  'cilinder_d100': {'1bar': 69.7, '2bar': 136.5, '3bar': 207.3, '4bar': 277.1, '5bar': 346.8, '6bar': 415.6, '7bar':485.3, '8bar':554.5}
}

while True:
  print()
  number_effort = int(input("Какое усилие нужно ,кг: "))
  if number_effort > cilinder_table['cilinder_d100']["8bar"]:
    print()
    print(
        f"""Максимальное усилие из возможных: {cilinder_table['cilinder_d100']["8bar"]}кг
При диамтре цилиндра в 100мм 
И давление в 8 бар"""
    )

  else:
    table = cilinder_calclulater(number_effort,cilinder_table)
    for cilinder_str , bar_string in table.items():
      for bar,press in bar_string.items():
        print('________________________________________________________')
        print(f'\n{cilinder_str}'
              f'\nПри {bar} '
              f'\nВыдает усилие {press} кг')
