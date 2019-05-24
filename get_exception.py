# pegando uma excessão


try:
    raise ValueError
except ValueError:
    print("Pegamos excessão")
