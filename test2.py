"""
 * Project name(项目名称)：Python深拷贝和浅拷贝
 * Package(包名): 
 * File(文件名): test2
 * Author(作者）: mao
 * Author QQ：1296193245
 * GitHub：https://github.com/maomao124/
 * Date(创建日期)： 2022/3/23 
 * Time(创建时间)： 13:20
 * Version(版本): 1.0
 * Description(描述)： 浅拷贝，指的是重新分配一块内存，创建一个新的对象，但里面的元素是原对象中各个子对象的引用
 深拷贝，是指重新分配一块内存，创建一个新的对象，并且将原对象中的元素，以递归的方式，通过创建新的子对象拷贝到新对象中
 """
import copy

if __name__ == '__main__':
    # 浅拷贝
    list1 = [1, 2, 3]
    list2 = list(list1)
    print(list2)
    print("list1==list2 ?", list1 == list2)
    print("list1 is list2 ?", list1 is list2)
    set1 = set([1, 2, 3])
    set2 = set(set1)
    print(set2)
    print("set1==set2 ?", set1 == set2)
    print("set1 is set2 ?", set1 is set2)

    list1 = [1, 2, 3]
    list2 = list1[:]
    print(list2)
    print("list1 == list2 ?", list1 == list2)
    print("list1 is list2 ?", list1 is list2)

    list1 = [1, 2, 3]
    list2 = copy.copy(list1)
    print(list2)
    print("list1 == list2 ?", list1 == list2)
    print("list1 is list2 ?", list1 is list2)

    # 对于元组，使用 tuple() 或者切片操作符 ':' 不会创建一份浅拷贝，相反它会返回一个指向相同元组的引用
    tuple1 = (1, 2, 3)
    tuple2 = tuple(tuple1)
    print(tuple2)
    print("tuple1 == tuple2 ?", tuple1 == tuple2)
    print("tuple1 is tuple2 ?", tuple1 is tuple2)

    list1 = [[1, 2], (30, 40)]
    list2 = list(list1)
    list1.append(100)
    print("list1:", list1)
    print("list2:", list2)
    list1[0].append(3)
    print("list1:", list1)
    print("list2:", list2)
    list1[1] += (50, 60)
    print("list1:", list1)
    print("list2:", list2)

    # 深拷贝
    print()
    list1 = [[1, 2], (30, 40)]
    # 对任意 Python 对象的深拷贝操作。
    list2 = copy.deepcopy(list1)
    list1.append(100)
    print("list1:", list1)
    print("list2:", list2)
    list1[0].append(3)
    print("list1:", list1)
    print("list2:", list2)
    list1[1] += (50, 60)
    print("list1:", list1)
    print("list2:", list2)

    list1 = [1]
    list1.append(list1)
    print(list1)
    list2 = copy.deepcopy(list1)
    print(list2)

    input()
