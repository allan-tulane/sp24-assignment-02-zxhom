"""
CMPS 2200  Assignment 2.
See assignment-02.pdf for details.
"""
import time


class BinaryNumber:
  """ done """

  def __init__(self, n):
    self.decimal_val = n
    self.binary_vec = list('{0:b}'.format(n))

  def __repr__(self):
    return ('decimal=%d binary=%s' %
            (self.decimal_val, ''.join(self.binary_vec)))


## Implement multiplication functions here. Note that you will have to
## ensure that x, y are appropriately sized binary vectors for a
## divide and conquer approach.
def binary2int(binary_vec):
  if len(binary_vec) == 0:
    return BinaryNumber(0)
  return BinaryNumber(int(''.join(binary_vec), 2))


def split_number(vec):
  return (binary2int(vec[:len(vec) // 2]), binary2int(vec[len(vec) // 2:]))


def bit_shift(number, n):
  # append n 0s to this number's binary string
  return binary2int(number.binary_vec + ['0'] * n)


def pad(x, y):
  # pad with leading 0 if x/y have different number of bits
  # e.g., [1,0] vs [1]
  if len(x) < len(y):
    x = ['0'] * (len(y) - len(x)) + x
  elif len(y) < len(x):
    y = ['0'] * (len(x) - len(y)) + y
  # pad with leading 0 if not even number of bits
  if len(x) % 2 != 0:
    x = ['0'] + x
    y = ['0'] + y
  return x, y


def subquadratic_multiply(x, y):
  xvec = x.binary_vec
  yvec = y.binary_vec

  padded = pad(xvec, yvec)
  xvec = padded[0]
  yvec = padded[1]

  # (above) Obtain xvec and yvec, the binary_vec values of x and y

  if (x.decimal_val and y.decimal_val) <= 1:
    return BinaryNumber(x.decimal_val * y.decimal_val)

  n = len(xvec)
  # n is the length of the padded BinaryNumbers - determines coefficent 2^n

  # Split_number returns a tuple of BinaryNumbers which can be indexed
  split1 = split_number(xvec)
  split2 = split_number(yvec)

  x_left = split1[0]
  x_right = split1[1]
  y_left = split2[0]
  y_right = split2[1]

  sum1 = subquadratic_multiply(x_left, y_left)  # BinaryNumber
  sum3 = subquadratic_multiply(x_right, y_right)  # BinaryNumber

  addx = BinaryNumber(x_left.decimal_val + x_right.decimal_val)  # BinaryNumber
  addy = BinaryNumber(y_left.decimal_val + y_right.decimal_val)  # BinaryNumber

  sum2 = BinaryNumber(
      subquadratic_multiply(addx, addy).decimal_val - sum1.decimal_val -
      sum3.decimal_val)
  #print('sum1 = ', sum1)
  #print('sum2 = ', sum2)
  #print('sum3 = ', sum3)
  #sum2 = BinaryNumber(sum2.decimal_val - sum1.decimal_val - sum3.decimal_val)
  #print("tmp type is: ", type(tmp))

  return BinaryNumber(
      bit_shift(sum1, n).decimal_val + bit_shift(sum2, n // 2).decimal_val +
      sum3.decimal_val)


#print(subquadratic_multiply(BinaryNumber(11), BinaryNumber(4)).decimal_val)


def time_multiply(x, y, f):
  start = time.time()
  # multiply two numbers x, y using function f
  f(x, y)
  return (time.time() - start) * 1000


#print(time_multiply(BinaryNumber(2), BinaryNumber(2), subquadratic_multiply))
#print(time_multiply(BinaryNumber(50), BinaryNumber(60), subquadratic_multiply))
#print(time_multiply(BinaryNumber(500), BinaryNumber(600), subquadratic_multiply))
#print(time_multiply(BinaryNumber(50000), BinaryNumber(60000), subquadratic_multiply))
#print(time_multiply(BinaryNumber(100000), BinaryNumber(318837), subquadratic_multiply))
'''
def test_multiply():
  assert subquadratic_multiply(BinaryNumber(2), BinaryNumber(2)).decimal_val == 2 * 2
  assert subquadratic_multiply(BinaryNumber(3), BinaryNumber(3)).decimal_val == 3 * 3
  assert subquadratic_multiply(BinaryNumber(4), BinaryNumber(7)).decimal_val == 4 * 7
  assert subquadratic_multiply(BinaryNumber(5), BinaryNumber(6)).decimal_val == 5 * 6
  assert subquadratic_multiply(BinaryNumber(20), BinaryNumber(30)).decimal_val == 20 * 30
  assert subquadratic_multiply(BinaryNumber(20), BinaryNumber(100)).decimal_val == 20 * 100
  assert subquadratic_multiply(BinaryNumber(500), BinaryNumber(300)).decimal_val == 500 * 300
  assert subquadratic_multiply(BinaryNumber(1000), BinaryNumber(200)).decimal_val == 1000 * 200


#print(subquadratic_multiply(BinaryNumber(6), BinaryNumber(2)).decimal_val)
test_multiply()
'''
