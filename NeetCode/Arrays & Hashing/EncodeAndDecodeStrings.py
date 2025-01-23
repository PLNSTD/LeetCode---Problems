class Solution:

    def encode(self, strs: List[str]) -> str:
        if strs == [""]:
            return ""
        if strs == []:
            return "None"
        return '/'.join(strs)

    def decode(self, s: str) -> List[str]:
        if s == "":
            return [""]
        elif s == 'None':
            return []
        return s.split('/')