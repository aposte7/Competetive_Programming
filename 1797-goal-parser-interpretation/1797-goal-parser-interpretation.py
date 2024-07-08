class Solution:
    def interpret(self, command: str) -> str:
        result = ""
        for i in range(len(command)):
            if command[i]==")" or command[i]=="a" or command[i]=="l":
                continue
            if command[i]=="G":
                result += "G"
            if command[i]=="(":
                if command[i+1]==")":
                    result += "o"
                else: result += "al"
        return result
