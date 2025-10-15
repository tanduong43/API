from flask import Flask, request, jsonify
import re
import random
app = Flask(__name__)

from flask_cors import CORS
CORS(app)
#Tuyến: POST /dang-nhap
@app.route('/dang-nhap',methods=['POST'])
def danhnhap():
    try:
        body = request.get_json()
        if not isinstance(body, dict):
            return jsonify({'success': False, 'message': 'Body phải là JSON'}), 400
        
        mssv = body.get('mssv')
        hoten = body.get('hoten')
        
        if mssv == "" or hoten == "":
            return jsonify({'success':False,'message':'Thiếu mssv hoặc họ tên'}),400
        
        if not isinstance(mssv,str) or not isinstance(hoten,str):
            return jsonify({'success':False,'message':'mssv và họ tên phải là chuỗi'}),400
        if re.search(r'\d', hoten):  # \d nghĩa là “có số”
            return jsonify({'success': False, 'message': 'Họ tên không được chứa số'}), 400
        if mssv == '1' and hoten == 'aa':
            return jsonify({'success':True,'message':'Đăng nhập thành công'}),200
        else:
            return  jsonify({'success':False,'message':'MSSV hoặc họ tên bạn không chính xác'}),400

    except Exception as e:
        return jsonify({'success':False,'message':str(e)}),500


@app.route('/tao-so',methods=['GET'])
def taoSo():
    try:
        soA = random.randint(1,100)
        soB = random.randint(1,100)
        op = random.choice(['+','-','*','/'])
        return jsonify({'success':True,'soA':soA,'soB':soB,'phepToan':op}),200
    except Exception as e:
        return jsonify({'success':False,'message':str(e)}),500

# Health check
@app.route('/', methods=['GET'])
def health_check():
    return "API OK"

@app.errorhandler(404)
def not_found(e):
    return jsonify({'success': False, 'message': 'Not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)
    