class hw02 {
  public static void main(String[] args){
    //int find_primes = args.length > 1 ? Integer(String args[1]) : 1000;
    int find_primes = 1000;
    int primes = 1, counter = 1;
    double primes_sum = 0;
    while(primes < find_primes){
      counter += 2;
      if (check_prime(counter)){
        primes += 1;
        primes_sum += Math.log(counter);
      }
    }
    System.out.printf("Primes: %d\n", primes);
    System.out.printf("\nCounter: %d\n", counter);
  }
  
  static public boolean check_prime(int num){
    int count = 2;
    while (count < num){
      if ((num % count) == 0){
        return false;
      }
      count += 1;
    }
    return true;
  }
}