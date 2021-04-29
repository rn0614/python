products=[]

while True:
    product = input("상품 등록 (엔터키 시 종료 ): ")

    if product=="":
        break

    products.append(product)

print("등록된 상품 : ", end=" ")

for product in products:
    print(product, end=" ")