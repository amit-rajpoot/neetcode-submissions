class Solution:
    def calPoints(self, operations: List[str]) -> int:
        score = []

        for op in operations:
            if op == "C":
                score.pop()
            elif op == "D":
                score.append(score[-1] * 2)
            elif op == "+":
                score.append(score[-2] + score[-1])
            else:
                score.append(int(op))

        return sum(score)