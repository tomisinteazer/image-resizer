def main():
  print('the python writer is alive')
  file = open('new.txt', 'a+')
  print('file opened enter text')
  new = input()
  edited = new +'\n'
  file.write(edited)
  file.close()
  print('file updated successfully')

main()