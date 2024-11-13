import time
# باز کردن فایل برای نوشتن
test_file = open(r'C:\Users\Sajedeh\OneDrive\Desktop\example.txt', 'w')
test_file.write('salam')
test_file.close()

# باز کردن فایل برای خواندن
test_file = open(r'C:\Users\Sajedeh\OneDrive\Desktop\example.txt')
print(test_file.read())
test_file.close()

import time

# زمان شروع
start_time = time.time()

# عملیات (چاپ اعداد از 1 تا 1000)
for i in range(1, 1001):
    print(i)

# زمان پایان
end_time = time.time()

# محاسبه و نمایش زمان اجرای برنامه
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")
