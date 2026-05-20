"""Chức năng 1: Cho phép thu ngân nhập vào tổng số tiền ban đầu của hóa đơn (số nguyên).
Chức năng 2: Áp dụng các kiến thức đã học để tính số tiền giảm giá:
Nếu hóa đơn từ 500,000 VND trở lên: Giảm 10% trên tổng số tiền.
Nếu hóa đơn dưới 500,000 VND: Không được giảm giá (Giảm 0%).
Chức năng 3: Tính toán số tiền thực tế khách phải trả (Tổng tiền ban đầu trừ đi số tiền giảm giá) và in kết quả ra màn hình."""

raw_money_input = float(input('Nhập số tiền ban đầu hoá đơn: '))

if raw_money_input > 500000:
    money = raw_money_input * 0.9
    deducted_money = raw_money_input - money
else:
    money = raw_money_input
    deducted_money = raw_money_input - money

print(f'\nSố tiền được giảm giá: {deducted_money} VND')
print()
print(f'Tổng tiền khách phải trả: {money} VND')