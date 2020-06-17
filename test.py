str1 = "{[([{}])]}"



# def ww(str):
#     n = len(str1) -1
    
#     trigger = False
#     while trigger == False:
#         print("in while")
#         for i in range(0, int(len(str1)/2)):
#             print(str[i], "and", str[n-i])
#             if str[i] == str[n-i]:
#                 break
#         trigger = True
#         print(trigger)
#     print(trigger)

# ww(str1)
MACH = {
    ")" : "(",
    "}" : "{",
    "]" : "["
}

def ww(str):
    s = Stack()
    for i in text:
        if i in MATH.values():
            c.push(i)
        elif i in MACH:
            if s.is_empty():
                return False
            elif MACH[i] != s.pop():
                return False
            
        
            