class Solution:
    def simplifyPath(self, path: str) -> str:
        if str == '/':
            return '/'

        list=[]
        
        for i in range(len(path)):
            if path[i] == "/":
                if i == 0:
                    list.append(path[i])
                elif not path[i-1] == "/" and not i == len(path)-1: 
                    list.append(path[i])
            elif path[i] == ".":
                if path[i-1] == "/":
                    list.pop(i-1)
                    if path
                while len(list) > 0:
                    list.pop()
                else:
                    return "/"
            else:
                list.append(path[i])

        result = ""

        for s in list:
            result = result + s

        return result
