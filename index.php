<?php
// index.php — API PHP thuần: GET /api/get-data, POST /api/tong

// Bật CORS (không bắt buộc với app native, nhưng để test từ browser cho tiện)
header('Access-Control-Allow-Origin: *');
header('Access-Control-Allow-Headers: Content-Type');
header('Access-Control-Allow-Methods: GET, POST, OPTIONS');
if ($_SERVER['REQUEST_METHOD'] === 'OPTIONS') {
    http_response_code(204);
    exit;
}

header('Content-Type: application/json; charset=UTF-8');

// Router siêu đơn giản
$method = $_SERVER['REQUEST_METHOD'];
$uri    = parse_url($_SERVER['REQUEST_URI'], PHP_URL_PATH);

// Helper trả JSON
function json_response($data, $status = 200) {
    http_response_code($status);
    echo json_encode($data, JSON_UNESCAPED_UNICODE);
    exit;
}
$OP = ['+','-','*','/'];
// // Tuyến: POST /ket-qua
if ($method === 'POST' && $uri === '/ket-qua') {
    $raw = file_get_contents('php://input');
    $body = json_decode($raw, true);

    if (!is_array($body)) {
        json_response(['success' => false, 'message' => 'Body phải là JSON'], 400);
    }

    $a = $body['a'] ?? null;
    $b = $body['b'] ?? null;
    $op = $body['operation'] ?? null;
    $ketqua = $body['ketqua'] ?? null;
    //tính toán
    $sum=0;
    if($op=='+'){
         $sum = $a + $b; 
    }else if($op=='-'){
         $sum = $a - $b; 
    }else  if($op=='*'){
         $sum = $a * $b; 
    }else if($op=='/'){
        if($b==0){
            json_response(['success'=> false,'message'=> 'Giá trị b không được bằng 0'],400 );
        }
        $sum = $a / $b; 
    } 
    $ra = random_int(1,100);
    $rb = random_int(1,100);
    $rop = $OP[random_int(0,3)];  
    if($ketqua==$sum){
        json_response(['success' => true, 'a' => $ra, 'b'=> $rb,'operation'=> $rop]);
    }else{
        json_response(['success' => false, 'a' => $ra, 'b'=> $rb,'operation'=> $rop],400);
    }
   
}
//Đăng nhập
if ($method === 'POST' && $uri === '/dang-nhap') {
    $raw = file_get_contents('php://input');
    $body = json_decode($raw, true);

    if (!is_array($body)) {
        json_response(['success' => false, 'message' => 'Body phải là JSON'], 400);
    }

    $mssv = $body['mssv'] ?? null;
    $hoten= $body['hoten'] ?? null;

    if ($mssv === "" || $hoten === "") {
        json_response(['success' => false, 'message' => 'Không được để trống ô dữ liệu'], 400);
    }
    if (is_numeric($hoten)) {
        json_response(['success' => false, 'message' => 'Họ tên phải là chữ'], 400);
    }

    if($mssv==="123" && $hoten ==="aaa") {
         json_response(['success' => true, 'message' => 'Đăng nhập thành công']);
    }else{
         json_response(['success' => false, 'message' => 'Đăng nhập thất bại'],400);
    }
}
//Tuyến: GET /phep-tinh

if ($method === 'GET' && $uri === '/phep-tinh') {
    $a = random_int(1,100);
    $b = random_int(1,100);
    $op = $OP[random_int(0,3)];  
    json_response(['success' => true, 'a' => $a, 'b'=> $b,'operation'=> $op]);
}

// Health check
if ($method === 'GET' && $uri === '/') {
    echo "API OK";
    exit;
}

// 404
json_response(['success' => false, 'message' => 'Not found'], 404);