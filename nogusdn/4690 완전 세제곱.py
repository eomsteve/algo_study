for a in range(2, 101):
    for b in range(2, 101):
        if a <= b:
            break
        for c in range(b+1, 101):
            if a**3 < b**3 + c**3:
                break
            for d in range(c+1,101):
                if a**3 == b**3 + c**3 + d**3:
                    print(f'Cube = {a}, Triple = ({b},{c},{d})')
                if a**3 < b**3 + c**3 + d**3:
                    break

