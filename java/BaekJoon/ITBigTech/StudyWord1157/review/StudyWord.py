def main():
   # 특정 문자열 및 공백 제거
   user_input = input().strip()
   if len(user_input) > 1000000:
      print("단어의 길이는 1,000,000을 넘지 말아야 한다.")
   
   user_input = user_input.upper()
   
   freq_dict = {}

   # key = word, value = 빈도 수
   for word in user_input:
      if word in freq_dict:
         freq_dict[word] += 1
      else:
         freq_dict[word] = 1
   
   max_freq = 0
   for word in freq_dict:
      if freq_dict[word] > max_freq:
         max_freq = freq_dict[word]
   # max_freq = max(freq_dict.values())

   max_words = [word for word, freq in freq_dict.items() if freq == max_freq]

   if len(max_words) > 1:
      print("?")
   else:
      print(max_words[0])

if __name__ == "__main__":
    main()