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
  numb = 7
  def prime(num):
    if num%i!=0:
      for i in range(1,num):
      print('it is prime')
        # TODO: write code...
      # TODO: write code...
  prime(num)

main()