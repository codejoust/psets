#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#include <time.h>

short check_prime(int num){
  int count = 2;
  while (count < num){
    if ((num % count) == 0){
      return 0;
    }
    count += 1;
  }
  //printf("%i is prime.\n", num);
  return 1;
}

int main(int argc, char **argv){
  clock_t start_tm, end_tm;
  start_tm = clock() / (CLOCKS_PER_SEC / 1000);
  int find_primes = argc > 1 ? atoi(argv[1]) : 1000;
  int primes = 1, counter = 1;
  float primes_sum = 0;
  while(primes < find_primes){
    counter += 2;
    if (check_prime(counter)){
      primes += 1;
      primes_sum += log(counter);
    }
  }
  end_tm = clock() / (CLOCKS_PER_SEC / 1000);
  printf("Primes: %i", primes); // 1 extra because 2 is a prime, but not included.
  printf("\nCounter: %i\n", counter);
  if (argc > 1){
    printf("\nSum: %0.3f, Prime: %i, Ratio: %0.3f\n", primes_sum, counter, primes_sum / (float)counter);
  }
  printf("Time elapsed: %ims\n", (int)(end_tm - start_tm));
  return 0;
}