def rata_rata(data):
    total = sum(data)
    return total / 5  # Bug: pembagi di-hardcode 5

print("Rata-rata [80, 90, 70]:", rata_rata([80, 90, 70]))