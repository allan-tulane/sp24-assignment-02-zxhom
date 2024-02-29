from main import *

## Feel free to add your own tests here.
def test_multiply():
  assert subquadratic_multiply(BinaryNumber(2), BinaryNumber(2)).decimal_val == 2 * 2
  assert subquadratic_multiply(BinaryNumber(3), BinaryNumber(3)).decimal_val == 3 * 3
  assert subquadratic_multiply(BinaryNumber(2), BinaryNumber(2)).decimal_val == 2 * 2
  assert subquadratic_multiply(BinaryNumber(3), BinaryNumber(3)).decimal_val == 3 * 3
  assert subquadratic_multiply(BinaryNumber(4), BinaryNumber(7)).decimal_val == 4 * 7
  assert subquadratic_multiply(BinaryNumber(5), BinaryNumber(6)).decimal_val == 5 * 6
  assert subquadratic_multiply(BinaryNumber(20), BinaryNumber(30)).decimal_val == 20 * 30
  assert subquadratic_multiply(BinaryNumber(20), BinaryNumber(100)).decimal_val == 20 * 100
  assert subquadratic_multiply(BinaryNumber(500), BinaryNumber(300)).decimal_val == 500 * 300
  assert subquadratic_multiply(BinaryNumber(1000), BinaryNumber(200)).decimal_val == 1000 * 200


#test_multiply()