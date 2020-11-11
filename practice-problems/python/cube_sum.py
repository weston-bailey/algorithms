def cube_sum(n):
  for a in range(n):
    for b in range(n):
      for c in range(n):
        for d in range(n):
          if a**3 + b**3 == c**3 + d**3:
            print(f'{a}^3 ({a**3}) + {b}^3 ({b**3}) = {c}^3 ({c**3}) + {d}^3 ({d**3})')
            break

cube_sum(1000)