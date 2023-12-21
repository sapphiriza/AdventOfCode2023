def isdigit(c):
  return ord(c) >= ord('0') and ord(c) <= ord('9')

stringNumbers = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

def getdigit(string, i):
  if isdigit(string[i]):
    return ord(string[i]) - ord('0'),0
  for j in range(1,10):
    numlen = len(stringNumbers[j])
    if string[i:i+numlen] == stringNumbers[j]:
      return j,numlen-1

  return 0,0

if __name__ == "__main__":
  file = open("input/trebuchetCalibration.txt")
  lines = file.readlines()
  sum = 0
  for line in lines:
    number = 10 * (ord(next(i for i in line if isdigit(i))) - ord('0')) + (ord(next(i for i in reversed(line) if isdigit(i))) - ord('0'))
    sum += number
  print("The WRONG calibration sum is " + str(sum))

  sum = 0
  for line in lines:
    first = 0
    last = 0
    for i in range(0,len(line)-1):
      digit,skip = getdigit(line, i)
      if digit > 0:
        if first == 0:
          first = digit
        last = digit
      i += skip
    sum += 10 * first + last
  print("The CORRECT calibration sum is " + str(sum))
