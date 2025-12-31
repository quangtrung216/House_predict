# Dự đoán giá nhà
## Bài toán
Bộ dữ liệu Bengaluru House Price Data tổng hợp nhiều thông tin liên quan đến bất động sản tại thành phố Bengaluru (Ấn Độ), nhằm mục đích phân tích và dự đoán giá nhà. Bộ dữ liệu được thiết kế phục vụ cho các nghiên cứu trong lĩnh vực khoa học dữ liệu, học máy và kinh tế bất động sản, cung cấp cái nhìn chi tiết về các yếu tố ảnh hưởng đến giá nhà như vị trí, diện tích, số phòng, tiện ích và các đặc điểm khác của bất động sản.

Thông qua bộ dữ liệu này, người nghiên cứu có thể khám phá mối quan hệ giữa các đặc trưng của ngôi nhà và mức giá thị trường, từ đó hỗ trợ xây dựng các mô hình dự đoán giá nhà hiệu quả.

Mô tả bài toán 

Bài toán đặt ra là phân tích và dự đoán giá nhà tại Bengaluru dựa trên nhiều yếu tố như vị trí địa lý, diện tích sử dụng, số phòng ngủ, số phòng tắm, và các đặc điểm liên quan khác của bất động sản.

Đây là một bài toán hồi quy (Regression) trong học máy, với mục tiêu xây dựng mô hình có khả năng ước lượng chính xác giá nhà, hỗ trợ:

Tổng quan các trường dữ liệu
area_type : Loại bất động sản

availability : Tình trạng của bất động sản

location : Vị trí, khu vực của bất động sản

size : Quy mô, kích thước thường là số phòng ngủ cho 1 căn nhà

society : Tên tổ dân phố nơi toạ lạc của các căn nhà

total_sqft : Tổng diện tích tính bằng đơn vị feet vuông

bath : Số lượng phòng tắm của các căn nhà

balcony : Số lượng ban công

price : GIá bán tính bằng đơn vị Lakh

## Mục tiêu bài toán 
Xây dựng mô hình dự đoán giá nhà từ các đặc trưng trong bộ dataset
## Nguồn dữ liệu
kaggle: https://www.kaggle.com/datasets/amitabhajoy/bengaluru-house-price-data
## Pipeline
Dataset → EDA → Clean → Encode → Train → Evaluate → Inference
## Mô hình sử dụng
- Linear Regression
- Lasso Regression
## Kết quả
Linear Regression: 
- R2 Score 0.8627447700198984
- MSE score 974.0141202397293
- RMSE score 31.209199288666944

Lasso Regression:
- R2 Score 0.8553577729692834
- MSE score 1026.434996548131
- RMSE score 32.03802422978251

## Cách chạy

- B1: Tạo môi trường venv python 3.10.x
- B2: activate môi trường
- B3: chạy lệnh "pip install -r list_lib.txt"

Chạy demo : cd app
- streamlit run streamlit.py

Demo bằng fast api:
- uvicorn API:app --reload
