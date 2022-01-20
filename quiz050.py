# 1から100までの値を繰り返しで表示するが、3の倍数の時はfoo、5の倍数の時はbarと数字の代わりに表示するプログラムを作成せよ。
# なお、3と5の両方の倍数の時はfoobarと表示される。

def foo_bar(n):    
    ind_number = ""
    for i in range(1,n+1):
        if i % 3 == 0 and i % 5 == 0:
            ind_number += "foobar"
        elif i % 3 == 0:
            ind_number += "foo"
        elif i % 5 == 0:
            ind_number += "bar"
        else:
            ind_number += str(i)
    return ind_number

if __name__ == '__main__':
    print(foo_bar(100))

    


