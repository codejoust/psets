import time

def print_timing(func):
  def wrapper(*arg):
    t1 = time.time()
    res = func(*arg)
    t2 = time.time()
    print '%s took %0.3f ms' % (func.func_name, (t2-t1)*1000.0)
    return res
  return wrapper

@print_timing
def primes_1():
  primes = counter = 1
  while primes < 1000:
    counter += 2
    count_inner = 2
    is_prime = True
    while count_inner < counter:
      if (counter % count_inner) == 0:
        is_prime = False
        break
      count_inner += 1
    if is_prime == True:
      primes += 1
  print 'Primes:  ' + str(primes)
  print 'Counter: ' + str(counter)

@print_timing
def primes_2():  
  def check_prime(number):
    inner_count = 2
    while (inner_count < number):
      if (number % inner_count) == 0:
        return False
      inner_count += 1
    return True
  primes = counter = 1
  while primes < 1000:
    counter += 2
    if (check_prime(counter)):
      primes += 1
  print 'Primes:  ' + str(primes)
  print 'Counter: ' + str(counter)

@print_timing
def primes_3():  
  def check_prime(number):
    for i in range(2, number):
      if (number % i) == 0:
        return False
    return True
  primes = counter = 1
  while primes < 1000:
    counter += 2
    if (check_prime(counter)):
      primes += 1
  print 'Primes:  ' + str(primes)
  print 'Counter: ' + str(counter)
  
print 'primes 1'
primes_1()
print 'primes 2'
primes_2()
print 'primes 3'  
primes_3()