def main():
  print('the python is alive')
  file = open('new.txt', 'a+')
  print('file opened enter new text')
  new = input()
  file.write(new)
  file.close()
  print('file written success')

main()