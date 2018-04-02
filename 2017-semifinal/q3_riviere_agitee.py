# https://prologin.org/train/2017/semifinal/riviere_agitee

flows = {}
for _ in range(int(input())):
    a, b, c, d = map(int, input().split())
    flows[a, b] = (c, d)

position = (0, 0)
history = set()
while True:
    if position not in flows:
        print(f"{position[0]} {position[1]}")
        break
    destination = flows[position]
    if destination in history:
        print("JAMAIS")
        break
    history.add(position)
    position = destination
