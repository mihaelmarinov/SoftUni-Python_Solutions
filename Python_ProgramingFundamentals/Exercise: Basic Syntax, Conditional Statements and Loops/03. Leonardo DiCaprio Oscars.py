num = int(input())

def leo_oscar(oscar):
    if oscar == 88:
        return "Leo finally won the Oscar! Leo is happy"
    elif oscar == 86:
        return "Not even for Wolf of Wall Street?!"
    elif oscar < 88:
        if oscar != 88 or oscar != 86:
            return "When will you give Leo an Oscar?"
    elif oscar > 88:
        return "Leo got one already!"


print(leo_oscar(num))
