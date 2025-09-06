import zipfile
import os
import pandas as pd

# 1. Path to your ZIP file (Windows full path)
zip_path = r"C:\Users\srira\Downloads\archive (1).zip"
extract_dir = r"C:\Users\srira\Downloads\extracted_data"

# 2. Extract ZIP if not already extracted
if not os.path.exists(extract_dir):
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_dir)
    print("✅ Zip extracted successfully!")

# 3. Path to postings.csv inside the extracted folder
csv_path = os.path.join(extract_dir, "postings.csv")

# 4. Load dataset
df = pd.read_csv(csv_path)
print("✅ Dataset loaded with shape:", df.shape)

# 5. Remove duplicates
df = df.drop_duplicates()

# 6. Fill missing values in text/categorical columns
df['company_name'] = df['company_name'].fillna("Unknown Company")
df['description'] = df['description'].fillna("No description provided")
df['location'] = df['location'].fillna("Unknown Location")
df['formatted_experience_level'] = df['formatted_experience_level'].fillna("Not Specified")
df['work_type'] = df['work_type'].fillna("Not Specified")

# 7. Fill missing numeric columns with median
num_cols = ['max_salary', 'min_salary', 'med_salary', 
            'normalized_salary', 'views', 'applies']
for col in num_cols:
    if col in df.columns:
        df[col] = df[col].fillna(df[col].median())

# 8. Fill remaining nulls with 0
df = df.fillna(0)

# 9. Save cleaned dataset
output_path = r"C:\Users\srira\Downloads\cleaned_postings.csv"
df.to_csv(output_path, index=False)
print("✅ Cleaned dataset saved at:", output_path)
print("Final shape:", df.shape)

# Show first few rows
print(df.head())
