m = int(input('Введите сумму снятия'))
result = 0
m_i = m //100
m_os = m % 100
result += m_i
m_i = m_os // 20
result += m_i
m_os = m_os % 20
m_i = m_os // 10
result += m_i
m_os = m_os % 10
m_i = m_os // 5
result += m_i
m_os = m_os % 5
m_i = m_os // 1
result += m_i
m_os = m_os % 1
print(result)
