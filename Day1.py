def isdigit(c):
  return ord(c) >= ord('0') and ord(c) <= ord('9')

if __name__ == "__main__":
  file = open("input/trebuchetCalibration.txt")
  sum = 0
  for line in file.readlines():
    number = 10 * (ord(next(i for i in line if isdigit(i))) - ord('0')) + (ord(next(i for i in reversed(line) if isdigit(i))) - ord('0'))
    sum += number
  print("The calibration sum is " + str(sum))
