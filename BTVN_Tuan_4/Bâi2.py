n = input()
string_in = list(map(int, input().split()))

string_out = [so for so in string_in if str(so)[-1] in ['1','3','5','7','9']]
sorted_string_out = sorted(string_out)

print(len(sorted_string_out))
print(sorted_string_out)