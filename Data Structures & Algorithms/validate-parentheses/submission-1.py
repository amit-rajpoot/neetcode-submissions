class Solution:
    def isValid(self, s: str) -> bool:

        bucket = []

        for bracket in s:

            if bracket == "(" or bracket == "[" or bracket == "{":
                bucket.append(bracket)

            else:
                if len(bucket) == 0:
                    return False

                ch = bucket.pop()

                if (
                    (bracket == ")" and ch == "(") or
                    (bracket == "}" and ch == "{") or
                    (bracket == "]" and ch == "[")
                ):
                    continue

                else:
                    return False

        return len(bucket) == 0