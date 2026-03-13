class Solution:
    def simplifyPath(self, path: str) -> str:
        path_list = path.split('/')
        result = []

        for s in path_list:
            if s == '..':
                if result:
                    result.pop()
                    continue
            elif s == '' or s == '.':
                continue
            else: result.append(s)

        return "/" + "/".join(result)