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

#Tuyến: GET /tao-so
@app.route('/tao-so',methods=['GET'])
def taoSo():
    try:
        soA = random.randint(1,100)
        soB = random.randint(1,100)
        op = random.choice(['+','-','*','/'])
        return jsonify({'success':True,'soA':soA,'soB':soB,'phepToan':op}),200
    except Exception as e:
        return jsonify({'success':False,'message':str(e)}),500


#Tuyến kiểm tra Post /kiem-tra
@app.route('/kiem-tra',methods=['POST'])
def kiemTra():
    try:
        body = request.get_json()
        if not isinstance(body,dict):
            return jsonify({'success':False,'message':'Body không phải là JSON'}),400
        a = body.get('SoA')
        b = body.get('SoB')
        op = body.get('operation')
        ketqua = body.get('ketqua')
        if not isinstance(a,int) or not isinstance(b,int) :
            return jsonify({'success':False,'message':'Số a hoặc b phải là số'}),400
        sum = 0
        if op == '+':
            sum=a+b
        elif op =='-':
            sum=a-b
        elif op =='*':
            sum=a*b 
        else:
            if b==0:
                return jsonify({'success':False,'message':'Số b không được bằng 0'}),400
            else:
                sum = a/b
        a = random.randint(1,100)
        b = random.randint(1,100)
        op = random.choice(['+','-','*','/'])
        if(sum==ketqua):
            return jsonify({'success':True,'a':a,'b':b,'operation':op}),200
        else:
             return jsonify({'success':False,'a':a,'b':b,'operation':op}),400

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
    