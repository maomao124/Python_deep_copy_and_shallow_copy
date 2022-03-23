"""
 * Project name(项目名称)：Python深拷贝和浅拷贝
 * Package(包名): 
 * File(文件名): test1
 * Author(作者）: mao
 * Author QQ：1296193245
 * GitHub：https://github.com/maomao124/
 * Date(创建日期)： 2022/3/23 
 * Time(创建时间)： 13:08
 * Version(版本): 1.0
 * Description(描述)： 
 """
# 统计时间需要用到 time 模块中的函数，了解即可
import time


def find_unique_price_using_list(products):
    unique_price_list = []
    for _, price in products:  # A
        if price not in unique_price_list:  # B
            unique_price_list.append(price)
    return len(unique_price_list)


if __name__ == '__main__':
    id = [x for x in range(0, 10000)]
    price = [x for x in range(20000, 30000)]
    products = list(zip(id, price))
    # 计算列表版本的时间
    start_using_list = time.perf_counter()
    find_unique_price_using_list(products)
    end_using_list = time.perf_counter()
    print("time elapse using list: {}".format(end_using_list - start_using_list))


# 使用集合完成同样的工作
def find_unique_price_using_set(products):
    unique_price_set = set()
    for _, price in products:
        unique_price_set.add(price)
    return len(unique_price_set)


if __name__ == '__main__':
    # 计算集合版本的时间
    start_using_set = time.perf_counter()
    find_unique_price_using_set(products)
    end_using_set = time.perf_counter()
    print("time elapse using set: {}".format(end_using_set - start_using_set))

    input()
