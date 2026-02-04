def swap_case(s):
    ans=""
    for i in s:
        if i.lower()==i:
            ans+=i.upper()
        else:
            ans+=i.lower()
    return ans

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
