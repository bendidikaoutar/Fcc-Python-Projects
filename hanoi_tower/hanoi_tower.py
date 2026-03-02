** start of main.py **

def hanoi_solver(n):
    source = list(range(n, 0, -1))
    auxiliary = []
    destination = []

    moves = []
    moves.append(f"{source} {auxiliary} {destination}")

    def solve(num, from_rod, aux_rod, to_rod):
        if num == 1:
            to_rod.append(from_rod.pop())
            moves.append(f"{source} {auxiliary} {destination}")
            return

        solve(num - 1, from_rod, to_rod, aux_rod)

        to_rod.append(from_rod.pop())
        moves.append(f"{source} {auxiliary} {destination}")

        solve(num - 1, aux_rod, from_rod, to_rod)

    solve(n, source, auxiliary, destination)

    return "\n".join(moves)

** end of main.py **

