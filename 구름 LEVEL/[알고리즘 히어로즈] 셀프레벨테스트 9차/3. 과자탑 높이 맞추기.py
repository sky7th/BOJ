# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
def solution():
		N, K = list(map(int, input().split()))
		heights = sorted(list(map(int, input().split())), reverse=True)
		high = heights[0]
		low = heights[-1]
		if low == high:
			print(0)
			return
		ret = 0
		idx = 0
		acc = 0
		for now_h in range(high, low-1, -1):
				if now_h == low:
						ret += 1
						break
				# 다음 높이와 높이가 같다면 같은 높이 맨 끝 idx로 이동
				while now_h == heights[idx + 1]:
						idx += 1
				# 현재 층까지 더한 값이 K 이하이면 누적
				if acc + idx + 1 <= K:
						acc += idx + 1
				# 아니면 acc 초기화하고  ret++
				else:
						acc = idx + 1
						ret += 1
		print(ret)


solution()
