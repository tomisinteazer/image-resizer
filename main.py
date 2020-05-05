def main():
  print('the python writer is alive')
  file = open('new.txt', 'a+')
  print('file opened enter text')
  new = input()
  edited = new +'\n'
  file.write(edited)
  file.close()
  print('file updated successfully')
  
  
  #the prime number generator
  
  def prime(arg):
    for i in range(0,arg):
      if arg%i!=0:
        print('it is prime')
        # TODO: write code...
      # TODO: write code...

main()