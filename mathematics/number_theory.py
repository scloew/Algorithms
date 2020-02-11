import math


def sieve(upper_bound):
  """
    following sieve of eratosthenes return list of all primes less than upperbound
    :param upper_bound:
    :return:
    """
  nums = [False if i % 2 else True for i in range(1, upper_bound+1)]
  nums[1], nums[2] = False, True
  for i in range(3, math.ceil(math.sqrt(upper_bound)), 2):
    if nums[i]:
      for j in range(2 * i, upper_bound+1, i):
        nums[j] = False

  return nums


if __name__ == '__main__':
  n = sieve(20)
  primes = [i for i, v in enumerate(n) if v]
  print(f'primes less than or equal to 20 are {primes}')
