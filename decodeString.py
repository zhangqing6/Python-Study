class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack=[]
        current_str=""
        current_num=0
        for char in s:
            if char.isdigit():
                current_num=current_num*10+int(char)
            elif char == "[":
                stack.append((current_str,current_num))
                current_num=0
                current_str=""
            elif char == "]":
                prev_str,num=stack.pop()
                current_str=prev_str+current_str*num
            else:  # 4. 普通字母
                current_str += char
        return current_str

