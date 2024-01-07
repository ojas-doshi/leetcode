class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        if endGene not in bank:
            return -1

        bank_set = set(bank)
        queue = deque([(startGene, 0)])

        while queue:
            current_gene, mutations = queue.popleft()
            if current_gene == endGene:
                return mutations

            for i in range(len(current_gene)):
                for char in 'ACGT':
                    if char != current_gene[i]:
                        next_gene = current_gene[:i] + char + current_gene[i+1:]
                        if next_gene in bank_set:
                            bank_set.remove(next_gene)
                            queue.append((next_gene, mutations + 1))

        return -1