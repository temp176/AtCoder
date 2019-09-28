S = input()

head = S[:2]
tail = S[2:]

is_yymm = True
is_mmyy = True

if head == "00" or head >= "13":
    is_mmyy = False

if tail == "00" or tail >= "13":
    is_yymm = False

if is_yymm and is_mmyy:
    print("AMBIGUOUS")
elif is_yymm:
    print("YYMM")
elif is_mmyy:
    print("MMYY")
else:
    print("NA")