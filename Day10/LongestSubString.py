
def SlidingWindow(string):
    left = 0
    right = 0
    s =set()
    max_str = 0
    while right < len(string):
        if string[right] not in s:
            s.add(string[right])
            right += 1
        else:
            s.remove(string[left])
            left += 1
        
        max_str = max(max_str, right - left)
    
    print(max_str)

s="dvdf"
SlidingWindow(s)
