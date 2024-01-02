class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(start, path, target):
            if target == 0:
                result.append(path)
                return
            if target < 0:
                return

            for i in range(start, len(candidates)):
                backtrack(i, path + [candidates[i]], target - candidates[i])

        result = []
        candidates.sort()
        backtrack(0, [], target)
        return result