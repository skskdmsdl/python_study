# 내장 함수
# https://docs.python.org/3/library/functions.html

# input : 사용자 입력을 받는 함수
# language = input("무슨 언어를 좋아하세요?")
# print(f"{language}은 아주 좋은 언어입니다.")

# dir : 어떤 객체를 넘겨줬을 때 그 객체가 어떤 변수와 함수를 가지고 있는지 표시
print(dir())
import random # 외장 함수
print(dir())
import pickle # 외장 함수
print(dir())

print(dir(random))
lst = [1, 2, 3]
print(dir(lst))

name = "Jim"
print(dir(name))