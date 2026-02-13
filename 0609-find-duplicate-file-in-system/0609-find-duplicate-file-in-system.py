class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        solution=defaultdict(list)
        a=False
        ans=[]

        for files in paths:
            path=files.split()
            directory_path=path[0]
            for k in path[1:]:
                filename,check=k.split("(")
                solution[check].append("/".join([directory_path,filename]))

        for key in solution:
            if len(solution[key])>1:
                ans.append(solution[key])
        return ans