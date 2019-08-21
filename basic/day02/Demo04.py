i = 100
id(i)   # 4390392320
i = 101
id(i)   # 4390392352
# 此方法看似容易丢失对象，会导致内存泄漏，但是Python会自动释放不再引用的对象的内存，
# 如上例中用于保存 100 的整数对象。

a = True
type(a)  # <class 'bool'>
print(True+10)  # 11
print(False+11)  # 11

c = 3.0+1.2j
print(c.real)  # 3.0
print(c.imag)  # 1.2

t = 3
type(t)  # <class 'int'>
