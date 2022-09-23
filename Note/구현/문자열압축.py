# 2a2ba3c"(문자가 반복되지 않아 한번만 나타난 경우 1은 생략함)

s = "aabbaccc"


def solution(s):
    answer = len(s)
    # 1개 단위(step)부터 압축 단위를 늘려가며 확인
    # len(s) // 2 + 1 인 이유 : 절반이상 넘어가면 반복이 불가능
    for step in range(1, len(s) // 2 + 1):
      compressed = ""
      prev = s[0:step]
      count = 1
      # 단위(step) 크기만큼 증가시키며 이전 문자열과 비교
      for j in range(step, len(s), step):
        # 이전 상태와 동일하다면 압축 횟수(count) 증가
        if prev == s[j:j + step]:
          count += 1
        # 다른 문자열이 나왔다면(더 이상 압축하지 못하는 경우라면)
        else:
          compressed += str(count) + prev if count >= 2 else prev
          prev = s[j:j + step] # 다시 상태 초기화
          count = 1
      # 남아 있는 문자열에 대해서 처리
      compressed += str(count) + prev if count >= 2 else prev
      # 만들어지는 압축 문자열이 가장 짧은 것이 정답
      answer = min(answer, len(compressed))
    print(answer)
    return answer


solution(s)
'''
    for i in s:
        if i in memoryList:
            memoryList[i] += 1;
        else:
            memoryList[i] = 1;
    for i in memoryList:
        if memoryList[i] == 1:
            result += i
        else:
            result += str(memoryList[i]) + i
'''