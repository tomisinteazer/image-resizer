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
  
  ranger= int(input ('enter the number ='))
  def prime(num):
    isprime=False
    for i in range(2,num):
      if num%i!=0:
        isprime = True
      elif i == 2:
        isprime = True
      else:
        isprime = False
        break 
    if isprime:
      print(num)
  
  for i in range(0,ranger):
    prime(i)
  #end of prime number

main()