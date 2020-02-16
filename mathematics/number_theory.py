import math


def sieve(upper_bound):
  """
    following sieve of eratosthenes return list of all primes less than upperbound
    :param upper_bound:
    :return:
    """
  nums = [False if i % 2 else True for i in range(1, upper_bound + 1)]
  nums[1], nums[2] = False, True
  for i in range(3, math.ceil(math.sqrt(upper_bound)), 2):
    if nums[i] :
      for j in range(2 * i, upper_bound + 1, i):
        nums[j] = False

  return nums


def non_divisible_subset(ints, divisor):
  """
  Given a container of ints and a divisor return list of such that
  the sum of any two elements is not divisible by divisor
  """
  subsets = [[] for _ in range(divisor)]
  for i in ints:
    subsets[i % divisor].append(i)
  max_ = [subsets[0][0]] if subsets[0] else []
  max_ += [subsets[int(divisor / 2)][0]] if subsets[int(divisor / 2)] and not divisor % 2 else []
  for i in range(1, int(divisor / 2) + (divisor % 2)):
    max_ += subsets[i] if len(subsets[i]) >= len(subsets[divisor - i]) else subsets[divisor - i]
  return max_


if __name__ == '__main__':
  n = sieve(20)
  primes = [i for i, v in enumerate(n) if v]
  print(f'primes less than or equal to 20 are {primes}')

  arr = [1, 7, 2, 4]
  print(non_divisible_subset(arr, 3))

  # 10 4
  nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
  div = 4
  print(non_divisible_subset(nums, div))
