#in 50 số đầu trong dãy số fibonnaci
a = 0
b = 1
for i in range(50):
  print(a)
  sum_a_b = a + b
  a = b
  b = sum_a_b