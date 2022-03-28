/* The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ? */

function primeFactors(){
  n = 600851475143;
  const factors = [];
  let divisor = 2;

  while (n >=2) {
    if (n % divisor == 0) {
      factors.push(divisor);
      n = n / divisor;
    } else {
      divisor++;
    }
  }
  return factors;
  //output (4) [71, 839, 4171, 6857]
}
