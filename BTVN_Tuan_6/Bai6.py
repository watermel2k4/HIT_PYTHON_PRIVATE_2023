x = [50, 75, 80, 60, 70, 90, 100, 65, 85, 105]
y = [600, 860, 930, 700, 800, 1040, 1150, 750, 970, 1200]
n = len(x)
def calculate_loss(w,b):
    c = [w*i + b for i in  x]
    loss = sum((c[i] - y[i])**2 for i in range(len(c))) / (2 * n)
    return loss

def calculate_w_b(x, y):
    """
        y = w*x + b
        CT tính w hệ số góc = (độ lệch y / độ lệch x) nhân hệ số tương quan giữa x và y
        độ lệch y = căn((tổng xích ma từ 0 đến n (x - x(TB)**2 / n -1)
        hệ số tương quan giữa x và y = (tổng xích ma từ 0 đến n (x - x(TB)*(y - y(TB)))/ căn((tổng xích ma từ 0 đến n (x - x(TB)**2  * (y - y(TB)**2)
        b = y(TB) - w*x
    """
    average_x = sum(x) / n
    average_y = sum(y) / n

    numerator = sum((x[i] - average_x) * (y[i] - average_y) for i in range(n))
    denominator = sum((x[i] - average_x)**2 for i in range(n))

    w = numerator / denominator
    b = average_y - w * average_x
    return w, b
w, b = calculate_w_b(x, y)

print(f"w: {w}, b: {b}")

forecast_price = w * 40 + b
print(f'Ước tính giá căn nhà có diện tích 40 m2: {forecast_price}')

