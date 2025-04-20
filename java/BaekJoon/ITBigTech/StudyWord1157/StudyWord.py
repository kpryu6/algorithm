def main():
   user_input = input().strip()

   if len(user_input) > 1000000:
      print("주어진 단어의 길이는 1,000,000을 넘지 말아야 한다.")
      return
   
   # input 모두 대문자로 바꿔
   user_input = user_input.upper()

   # dict 생성
   freq_dict = {}

   # key가 word, value가 빈도수
   for word in user_input:
      if word in freq_dict:
         freq_dict[word] += 1
      else:
         freq_dict[word] = 1
   
   # 최대 value 찾기
   max_freq = max(freq_dict.values())

   # 최대 value 갖는 key list
   max_words = [word for word,freq in freq_dict.items() if freq == max_freq]
   
   if len(max_words) > 1:
      print("?")
   else:
      print(max_words[0])

if __name__ == "__main__":
   main()
