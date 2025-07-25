#2984. 문자열 심화

password = "In the bustling city, where life is a constant race against time, uoy often find yourself wondering if there's a shortcut to success. The vibrant lights of the cityscape illuminate the night, casting shadows on the short-lived dreams of those who seek fortune. As you navigate through the crowded streets, you realize the deen for guidance, like a compass pointing python. You need direction in this chaotic journey called life."
# 아래에 코드를 작성하시오.

first_char = password[28:35]
second_word = password[113:118]
third_word = password[66:69:][::-1]
fourth_word = password[322:326:][::-1]
fifth_word = password[365:371]


print(f'{first_char}', f'{second_word}', f'{third_word}', f'{fourth_word}', f'{fifth_word}')