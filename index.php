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

// “kho” thành ngữ
$PROVERBS = [
    "Có công mài sắt, có ngày nên kim.",
    "Đi một ngày đàng, học một sàng khôn.",
    "Chậm mà chắc.",
    "Nói phải củ cải cũng nghe.",
    "Học ăn, học nói, học gói, học mở.",
    "Một cây làm chẳng nên non, ba cây chụm lại nên hòn núi cao.",
    "Biết người biết ta, trăm trận trăm thắng.",
    "Không thầy đố mày làm nên.",
    "Uống nước nhớ nguồn."
];

// Tuyến: GET /danh-ngon
if ($method === 'GET' && $uri === '/danh-ngon') {
    $pick = $PROVERBS[array_rand($PROVERBS)];
    json_response(['success' => true, 'data' => $pick]);
}

// Tuyến: POST /tinh-tong
if ($method === 'POST' && $uri === '/tinh-tong') {
    $raw = file_get_contents('php://input');
    $body = json_decode($raw, true);

    if (!is_array($body)) {
        json_response(['success' => false, 'message' => 'Body phải là JSON'], 400);
    }

    $a = $body['a'] ?? null;
    $b = $body['b'] ?? null;

    if ($a === null || $b === null) {
        json_response(['success' => false, 'message' => 'Thiếu tham số a hoặc b'], 400);
    }

    if (!is_numeric($a) || !is_numeric($b)) {
        json_response(['success' => false, 'message' => 'a và b phải là số'], 400);
    }

    $sum = $a + $b; // PHP tự ép kiểu số
    json_response(['success' => true, 'data' => $sum]);
}

// Health check
if ($method === 'GET' && $uri === '/') {
    echo "API OK";
    exit;
}

// 404
json_response(['success' => false, 'message' => 'Not found'], 404);