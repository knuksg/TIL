n, m = map(int, input().split())
n_ = list(map(int, input().split()))
m_ = list(map(int, input().split()))
print(*sorted(n_ + m_))