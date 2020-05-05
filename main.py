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
    for i in range(1,num):
      if num%i!=0:
        print('it is prime')
        # TODO: write code...
      # TODO: write code...
  prime(numb)

main()