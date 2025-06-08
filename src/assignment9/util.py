def merge_the_tools(string, k):
    for i in range(0, len(string), k):
        sub_str=string[i:i+k]
        unique_str=""
        for ch in sub_str:
            if ch not in unique_str:
                unique_str+=ch
        print(unique_str)
    

