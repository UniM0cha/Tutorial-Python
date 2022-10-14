kor = "Hello Python!"
print(len(kor))
print(kor[0:-1:3])
var = "12:34:56"
print(var.split(":"))
print(var.replace(":", "-"))
print(",".join(var))
print(var.count(":"))
print(var.index(":"))


my_dict = {"a": 1111, "b": 2222, "c": 3333}
print(my_dict)
key = "w"
my_dict[key] = 4444
if key in my_dict:
    print(my_dict[key])
else:
    print(f"{key} 키가 없어요.")


key, value = "w", 555
my_dict[key] = value

print(my_dict[key])


my_dict["이름"] = "이정윤"
print(my_dict)
