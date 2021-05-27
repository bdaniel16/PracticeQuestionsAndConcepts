class Solution:
    def __init__(self):
        self.stack = []
        self.que = []

    def pushCharacter(self, c):
        self.stack.append(c)

    def popCharacter(self):
        y = self.stack.pop()
        print("pop:{}".format(y))
        return y

    def enqueueCharacter(self, c):
        temp = [c]
        temp.extend(self.que)
        self.que = temp

    def dequeueCharacter(self):
        x = self.que.pop(len(self.que)-1)
        print('deque: {}'.format(x))
        return x


if __name__ == "__main__":
    s = "racecar"
    obj = Solution()

    l = len(s)
    # push/enqueue all the characters of string s to stack
    for i in range(l):
        obj.pushCharacter(s[i])
        obj.enqueueCharacter(s[i])

    isPalindrome = True
    '''
    pop the top character from stack
    dequeue the first character from queue
    compare both the characters
    '''
    for i in range(l // 2):
        if obj.popCharacter() != obj.dequeueCharacter():
            isPalindrome = False
            break
    # finally print whether string s is palindrome or not.
    if isPalindrome:
        print("The word, " + s + ", is a palindrome.")
    else:
        print("The word, " + s + ", is not a palindrome.")