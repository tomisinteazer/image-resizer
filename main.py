def main():
  def writer():
    print('the python writer is alive')
    file = open('new.txt', 'a+')
    print('file opened enter text')
    new = input()
    edited = new +'\n'
    file.write(edited)
    file.close()
    print('file updated successfully')
  
  
  #the prime number generator
  num = 7
  def prime(num):
    isprime=False
    for i in range(1,num):
      if num%i!=0:
        isprime = True
      else:
        isprime = False
        break 
    print(isprime)
        # TODO: write code...
      # TODO: write code...
  prime(num)

main()