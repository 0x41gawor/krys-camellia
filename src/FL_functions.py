import core.operators as o
# x1, x2 FOR TEST
# print()'s are only for test, to be deleted
x1 = b'1100'
x2 = b'1001'

def FL_function(x, k):
    XL = o.LEFT(x, 2)
    print(XL)
    XR = o.RIGHT(x, 2)
    print(XR)
    KL = o.LEFT(k, 2)
    print(KL)
    KR = o.RIGHT(k, 2)
    print(KR)
    print("---------")
    YR = o.XOR(o.ROTATE(o.AND(XL, KL), 1), XR)
    print("ROTATE")
    print(o.ROTATE(o.AND(XL, KL), 1))
    print("YR")
    print(YR)
    YL = o.XOR(o.OR(YR, KR), XL)
    print("YL")
    print(YL)
    output = o.CONCATENATE(YL, YR)
    print("output")
    print(output)
    return output

def FL1_function(y, k):
    YL = o.LEFT(y, 2)
    print(YL)
    YR = o.RIGHT(y, 2)
    print(YR)
    KL = o.LEFT(k, 2)
    print(KL)
    KR = o.RIGHT(k, 2)
    print(KR)
    print("---------------")
    XL = o.XOR(o.OR(YR, KR), YL)
    print(o.XOR(o.OR(YR, KR), YL))
    XR = o.XOR(o.ROTATE(o.AND(XL, KL), 1), YR)
    output = o.CONCATENATE(XL, XR)

    return output

# FOR TESTS
FL1_function(x1, x2)
# FL_function(x1, x2)

