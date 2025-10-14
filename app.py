from flask import Flask, request, jsonify
# Flask → lớp dùng để tạo app web.
# request → module con của Flask (để truy cập dữ liệu người dùng gửi đến).
# jsonify → hàm con của Flask (để trả dữ liệu dạng JSON về client).
#Flask: Là một framework web nhẹ cho Python, giúp xây dựng các ứng dụng web và API một cách dễ dàng.
#request: Được sử dụng để truy cập dữ liệu từ yêu cầu HTTP mà client gửi đến server.
#jsonify được sử dụng để tạo 1 phản hồi http với nội dung JSON. Nó tự động chuyển đổi 
        # các đối tượng Python (như dictionary, list, v.v.) thành chuỗi JSON và đặt header Content-Type 
        # của phản hồi là application/json.
        #Header Content-Type: application/json đảm bảo rằng client biết phản hồi là JSON và xử lý nó đúng cách.
import random

app = Flask(__name__) # Tạo ứng dụng Flask

# app.config['JSON_AS_ASCII'] = False # Đảm bảo Flask trả về JSON với Unicode (không mã hóa ASCII)
# Bật CORS (cho phép tất cả các nguồn)
from flask_cors import CORS # Thư viện Flask-CORS để xử lý CORS trong ứng dụng Flask
CORS(app)#bật CORS cho tất cả các tuyến và tất cả các nguồn
# Tại sao cần CORS?
# Theo mặc định, trình duyệt chặn các yêu cầu từ một nguồn gốc khác (cross-origin) vì lý do bảo mật.
# Ví dụ: Nếu frontend của bạn chạy trên http://localhost:3000 và backend (API Flask) 
# chạy trên http://localhost:5000, trình duyệt sẽ chặn yêu cầu từ frontend đến backend trừ khi CORS được bật.
#Cách hoạt động:
# Khi bạn thêm CORS(app), ứng dụng Flask sẽ 
# tự động thêm các header CORS vào phản hồi HTTP, cho phép các yêu cầu từ nguồn gốc khác.





# “kho” thành ngữ
PROVERBS = [
    "Có công mài sắt, có ngày nên kim.",
    "Đi một ngày đàng, học một sàng khôn.",
    "Chậm mà chắc.",
    "Nói phải củ cải cũng nghe.",
    "Học ăn, học nói, học gói, học mở.",
    "Một cây làm chẳng nên non, ba cây chụm lại nên hòn núi cao.",
    "Biết người biết ta, trăm trận trăm thắng.",
    "Không thầy đố mày làm nên.",
    "Uống nước nhớ nguồn."
]

# Tuyến: GET /danh-ngon
@app.route('/danh-ngon', methods=['GET'])
def get_proverb():
    pick = random.choice(PROVERBS)
    return jsonify({'success': True, 'data': pick})

# Tuyến: POST /tinh-tong
@app.route('/tinh-tong', methods=['POST'])
def calculate_sum():
    try:
        body = request.get_json()  # Lấy dữ liệu JSON từ body của yêu cầu POST
        if not isinstance(body, dict):
            return jsonify({'success': False, 'message': 'Body phải là JSON'}), 400

        a = body.get('a')
        b = body.get('b')

        if a is None or b is None:
            return jsonify({'success': False, 'message': 'Thiếu tham số a hoặc b'}), 400
       

        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        # isinstance Kiểm tra đối tượng a có thuộc về 1 hoặc 1 tupe các kiểu dữ liệu hay ko
            return jsonify({'success': False, 'message': 'a và b phải là số'}), 400

        total = a + b
        return jsonify({'success': True, 'data': total})
    except Exception as e:
        return jsonify({'success': False, 'message': str(e)}), 500

# Health check
@app.route('/', methods=['GET'])
def health_check():
    return "API OK"

# 404 handler
@app.errorhandler(404)# lỗi 404 (Not Found) xảy ra khi client yêu cầu một tài nguyên không tồn tại trên server.(lỗi đường dẫn không đúng)
def not_found(e):
    return jsonify({'success': False, 'message': 'Not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)
#app.run(debug=True, port=8000)  # Chạy ứng dụng trên port 8000#
# debug=True: Chạy ứng dụng ở chế độ gỡ lỗi, giúp phát hiện lỗi nhanh hơn trong quá trình phát triển.


# Các port thường dùng:
# 80: Port mặc định cho HTTP (truy cập web không bảo mật).
# 443: Port mặc định cho HTTPS (truy cập web bảo mật).
# 3306: Port mặc định cho MySQL.
# 5432: Port mặc định cho PostgreSQL.
# 6379: Port mặc định cho Redis.
# 22: Port mặc định cho SSH (kết nối từ xa an toàn).
# 21: Port mặc định cho FTP (truyền tệp).
# 8080: Thường được sử dụng cho các ứng dụng web hoặc proxy HTTP.
# 3000: Thường được sử dụng bởi các ứng dụng frontend (React, Angular, Vue.js).
# 5000: Port mặc định cho Flask.
# 8000: Thường được sử dụng bởi Django hoặc các ứng dụng phát triển khác.