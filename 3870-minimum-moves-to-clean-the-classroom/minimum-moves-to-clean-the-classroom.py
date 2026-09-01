class Solution:
    def minMoves(self, classroom: List[str], energy: int) -> int:
        from collections import deque

        m = len(classroom)
        n = len(classroom[0])

        # Find starting position and number each litter
        start_r = start_c = 0
        litter_id = {}
        k = 0

        for r in range(m):
            for c in range(n):
                if classroom[r][c] == 'S':
                    start_r, start_c = r, c
                elif classroom[r][c] == 'L':
                    litter_id[(r, c)] = k
                    k += 1

        # No litter to collect
        if k == 0:
            return 0

        all_mask = (1 << k) - 1

        # BFS: (row, col, remaining_energy, collected_mask)
        queue = deque()
        queue.append((start_r, start_c, energy, 0))

        # visited states
        visited = set()
        visited.add((start_r, start_c, energy, 0))

        moves = 0

        while queue:
            for _ in range(len(queue)):
                r, c, e, mask = queue.popleft()

                # All litter collected
                if mask == all_mask:
                    return moves

                directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc

                    # Check boundaries
                    if nr < 0 or nr >= m or nc < 0 or nc >= n:
                        continue

                    # Cannot enter obstacle
                    if classroom[nr][nc] == 'X':
                        continue

                    # Need energy to make a move
                    if e == 0:
                        continue

                    new_energy = e - 1
                    new_mask = mask

                    # Collect litter
                    if classroom[nr][nc] == 'L':
                        idx = litter_id[(nr, nc)]
                        new_mask |= (1 << idx)

                    # Reset energy on R
                    if classroom[nr][nc] == 'R':
                        new_energy = energy

                    state = (nr, nc, new_energy, new_mask)

                    if state not in visited:
                        visited.add(state)
                        queue.append(state)

            moves += 1

        return -1
        