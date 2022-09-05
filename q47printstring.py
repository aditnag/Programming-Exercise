class PrintString:
    def oprstr(self):
        s = input()
        l = len(s)
        if s[l - 2] == 'e' and s[l - 1] == 'r':
            print("er")
        elif s[l - 3] == 'i' and s[l - 2] == 's' and s[l - 1] == 't':
            print("ist")


o = PrintString()
o.oprstr()
