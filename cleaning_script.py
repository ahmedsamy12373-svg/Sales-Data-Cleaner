import pandas as pd

# بيانات مبيعات "ملخبطة" عشان نوضح مهارة التنظيف
dirty_data = {
    'Date': ['2023-01-01', '2023-01-01', None],
    'Amount': [250, 250, 100], # لاحظ التكرار
    'Product': [' Laptop ', 'Laptop', 'Mouse'] # مسافات زيادة
}

df = pd.DataFrame(dirty_data)

# عملية التنظيف (Transformation)
df_cleaned = df.drop_duplicates() # مسح التكرار
df_cleaned['Product'] = df_cleaned['Product'].str.strip() # مسح المسافات
df_cleaned['Date'] = df_cleaned['Date'].fillna('Unknown') # معالجة القيم الناقصة

print("Data Cleaning Complete. Final Results:")
print(df_cleaned)
