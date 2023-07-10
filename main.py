# Goal is to multiply V by c

V = [3, 1, 4, 1, 5, 9]
c = 5

def fake_mult(V, c):
  # Step 1 
  # sort and eliminate duplicates
  S = V.copy()
  sorted(S)
  S = list(set(S))
  # store pointers
  P = [S.index(x)+1 for x in V]

  # Step 2
  # take the differences of S
  D = [S[0]]
  for i in range(len(S)-1):
    D.append(S[i+1] - S[i])

  # Step 3
  # Use russian-peasants mult or recursion
  def russian_peasant(a, b):
    res = 0
    while (b>0):
      if (b & 1):
        res += a
      a = a << 1
      b = b >> 1
    return res

  D_ = [russian_peasant(x, c) for x in D]

  # Step 4
  # Accumulate
  S_ = [D_[0]]
  for i in range(len(D_)-1):
    S_.append(S_[i]+D_[i+1])

  # Step 5
  # Follow pointers
  V_ = [S_[i-1] for i in P]
  
  return V_

print(fake_mult(V, c))
