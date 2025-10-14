import express from "express";
import cors from "cors";

const app = express();
const PORT = 5000;

// Middlewares
app.use(express.json());       // parse application/json
app.use(cors());               // tiện test từ browser/WebView, native Android không bị CORS

// “kho” thành ngữ/ngạn ngữ
const PROVERBS = [
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

// GET /danh-ngon → random 1 câu
app.get("/danh-ngon", (req, res) => {
  const pick = PROVERBS[Math.floor(Math.random() * PROVERBS.length)];
  return res.json({ success: true, data: pick });
});

// POST /tinh-tong → nhận {a, b} và trả về tổng
app.post("/tinh-tong", (req, res) => {
  const { a, b } = req.body ?? {};

  // validate đơn giản
  if (a === undefined || b === undefined) {
    return res.status(400).json({
      success: false,
      message: "Thiếu tham số a hoặc b"
    });
  }
  const aNum = Number(a);
  const bNum = Number(b);
  if (Number.isNaN(aNum) || Number.isNaN(bNum)) {
    return res.status(400).json({
      success: false,
      message: "a và b phải là số"
    });
  }

  const sum = aNum + bNum;
  return res.json({ success: true, data: sum });
});

// Health check nho nhỏ
app.get("/", (req, res) => res.send("API OK"));

app.listen(PORT, "127.0.0.1", () => {
  console.log(`API chạy ở http://localhost:${PORT}`);
});