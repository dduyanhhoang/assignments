# Ngày 1 - Bài Tập & Phản Ánh

## Nền Tảng LLM API | Phiếu Thực Hành

**Thời lượng:** 1:30 giờ
**Cấu trúc:** Lập trình cốt lõi (60 phút) → Bài tập mở rộng (30 phút)

---

## Phần 1 - Lập Trình Cốt Lõi (0:00–1:00)

Chạy các ví dụ trong Google Colab
tại: https://colab.research.google.com/drive/172zCiXpLr1FEXMRCAbmZoqTrKiSkUERm?usp=sharing

Triển khai tất cả TODO trong `template.py`. Chạy `pytest tests/` để kiểm tra tiến độ.

**Điểm kiểm tra:** Sau khi hoàn thành 4 nhiệm vụ, chạy:

```bash
python template.py
```

Bạn sẽ thấy output so sánh phản hồi của GPT-4o và GPT-4o-mini.

---

## Phần 2 - Bài Tập Mở Rộng (1:00–1:30)

### Bài tập 2.1 - Độ Nhạy Của Temperature

Gọi `call_openai` với các giá trị temperature 0.0, 0.5, 1.0 và 1.5 sử dụng prompt **"Hãy kể cho tôi một sự thật thú vị
về Việt Nam."**

**Bạn nhận thấy quy luật gì qua bốn phản hồi?** (2–3 câu)
> Ở temperature 0.0, phản hồi luôn giống nhau qua mỗi lần gọi - nội dung mang tính factual, cấu trúc câu rõ ràng và ổn
> định. Khi tăng lên 0.5 và 1.0, câu trả lời bắt đầu đa dạng hơn về cách diễn đạt và chọn chủ đề, nhưng vẫn hợp lý. Ở
> temperature 1.5, phản hồi trở nên sáng tạo hơn đáng kể nhưng đôi khi mất mạch lạc, xuất hiện cụm từ lạ hoặc thông tin
> kém chính xác hơn.

**Bạn sẽ đặt temperature bao nhiêu cho chatbot hỗ trợ khách hàng, và tại sao?**
> Tôi sẽ đặt temperature trong khoảng 0.0 tới 0.3. Chatbot hỗ trợ khách hàng cần đưa ra câu trả lời chính xác, nhất quán
> và đáng tin cậy. Temperature thấp đảm bảo mô hình chọn token có xác suất cao nhất, giảm thiểu rủi ro đưa ra thông tin
> sai hoặc câu trả lời khác nhau cho cùng một câu hỏi, giúp trải nghiệm người dùng ổn định hơn.

Raw output

```shell
(day_01_llm_api_foundation) PS C:\Users\dduya\Work\project\vinaip\assignments\day_01_llm_api_foundation> uv run .\extra2_1.py 
2026-04-02 17:19:15.482 | INFO     | solution.solution:call_openai:62 - Starting call API                                                                               
2026-04-02 17:19:18.344 | INFO     | solution.solution:call_openai:72 - Calling finished. 2.86                                                                          
                                                                                                                                                                        
--- Temperature 0.0 (latency: 2.86s) ---                                                                                                                                
Một sự thật thú vị về Việt Nam là đất nước này có một hệ thống hang động lớn nhất thế giới, đó là hang Sơn Đoòng. Hang Sơn Đoòng nằm trong Vườn quốc gia Phong Nha-Kẻ Bàng, tỉnh Quảng Bình. Hang động này được phát hiện vào năm 1991 bởi một người dân địa phương tên là Hồ Khanh, nhưng mãi đến năm 2009, một đoàn thám hiểm người Anh mới chính thức khảo sát và công bố về kích thước khổng lồ của nó. Hang Sơn Đoòng có chiều dài hơn 5 km, cao 200 m và rộng 150 m, đủ lớn để chứa cả một tòa nhà chọc trời 40 tầng. Bên trong hang còn có hệ sinh thái riêng với rừng cây và sông ngầm, tạo nên một cảnh quan vô cùng kỳ vĩ và độc đáo.
2026-04-02 17:19:18.355 | INFO     | solution.solution:call_openai:62 - Starting call API
2026-04-02 17:19:20.961 | INFO     | solution.solution:call_openai:72 - Calling finished. 2.61

--- Temperature 0.5 (latency: 2.61s) ---
Một sự thật thú vị về Việt Nam là đất nước này có một hệ thống hang động lớn và phức tạp, nổi bật nhất là hang Sơn Đoòng. Hang Sơn Đoòng, nằm trong Vườn quốc gia Phong Nha-Kẻ Bàng ở tỉnh Quảng Bình, được coi là hang động lớn nhất thế giới. Hang này có chiều dài hơn 5 km, cao 200 m và rộng 150 m. Bên trong hang có cả một hệ sinh thái riêng với rừng rậm, sông ngầm và thậm chí là những đám mây mù. Hang Sơn Đoòng chỉ mới được phát hiện vào năm 1991 bởi một người dân địa phương và được thám hiểm đầy đủ bởi các nhà thám hiểm người Anh vào năm 2009. Sự kỳ vĩ và bí ẩn của hang động này đã thu hút rất nhiều nhà thám hiểm và du khách từ khắp nơi trên thế giới.
2026-04-02 17:19:20.972 | INFO     | solution.solution:call_openai:62 - Starting call API
2026-04-02 17:19:23.030 | INFO     | solution.solution:call_openai:72 - Calling finished. 2.06

--- Temperature 1.0 (latency: 2.06s) ---
Một sự thật thú vị về Việt Nam là nước này có hệ thống hang động lớn nhất thế giới, đó là hang Sơn Đoòng. Hang Sơn Đoòng nằm trong Vườn quốc gia Phong Nha-Kẻ Bàng, tỉnh Quảng Bình. Hang này được phát hiện vào năm 1991 bởi một người dân địa phương, nhưng mãi đến năm 2009 thì các nhà thám hiểm người Anh mới chính thức công bố và khám phá chi tiết. Hang Sơn Đoòng có kích thước khổng lồ với một số đoạn cao đến 200 mét, rộng 150 mét và dài khoảng 9 km. Hang này còn có hệ sinh thái độc đáo với rừng nhiệt đới và dòng sông ngầm bên trong.
2026-04-02 17:19:23.042 | INFO     | solution.solution:call_openai:62 - Starting call API
2026-04-02 17:19:26.627 | INFO     | solution.solution:call_openai:72 - Calling finished. 3.58

--- Temperature 1.5 (latency: 3.58s) ---
Một sự thật thú vị về Việt Nam là đất nước này là một trong những nhà sản xuất cà phê lớn nhất thế giới. Việt Nam đứng thứ hai toàn cầu về sản lượng cà phê, chỉ sau Brazil. Cà phê Việt Nam, đặc biệt là loại Robusta, được xuất khẩu rộng rãi và chiếm phần lớn trong tổng sản lượng cà phê của quốc gia. Ngoài ra, Việt Nam cũng nổi tiếng với các loại cà phê độc đáo như cà phê trứng, cà phê sữa đá và cà phê dừa, mang đậm hương vị và phong cách riêng.
```

---

### Bài tập 2.2 - Đánh Đổi Chi Phí

Xem xét kịch bản: 10.000 người dùng hoạt động mỗi ngày, mỗi người thực hiện 3 lần gọi API, mỗi lần trung bình ~350
token.

**Ước tính xem GPT-4o đắt hơn GPT-4o-mini bao nhiêu lần cho workload này:**
> Tổng output tokens mỗi ngày: 10,000 users × 3 calls × 350 tokens = 10,500,000 tokens = 10,500 × 1K tokens.
>
> - Chi phí GPT-4o: 10,500 × $0.010 = **\$105/ngày**
> - Chi phí GPT-4o-mini: 10,500 × $0.0006 = **\$6.30/ngày**
> - Tỷ lệ: $0.010 / $0.0006 ≈ **16.67 lần**
>
> GPT-4o đắt hơn GPT-4o-mini khoảng **16.67 lần** cho workload này (\$105 so với \$6.30 mỗi ngày).

**Mô tả một trường hợp mà chi phí cao hơn của GPT-4o là xứng đáng, và một trường hợp GPT-4o-mini là lựa chọn tốt hơn:**
> **GPT-4o xứng đáng:** Trong lĩnh vực y tế hoặc pháp lý, khi cần phân tích tài liệu phức tạp, suy luận nhiều bước, hoặc
> đưa ra lời khuyên chính xác cao - sai sót có thể gây hậu quả nghiêm trọng, nên chất lượng đầu ra quan trọng hơn chi
> phí.
>
> **GPT-4o-mini phù hợp hơn:** Cho các tác vụ đơn giản như phân loại tin nhắn (spam/không spam), trả lời câu hỏi FAQ
> thường gặp, hoặc tóm tắt văn bản ngắn - những tác vụ không yêu cầu suy luận phức tạp và cần xử lý khối lượng lớn với
> chi
> phí thấp.

---

### Bài tập 2.3 - Trải Nghiệm Người Dùng với Streaming

**Streaming quan trọng nhất trong trường hợp nào, và khi nào thì non-streaming lại phù hợp hơn?** (1 đoạn văn)
> Streaming quan trọng nhất trong các ứng dụng chatbot tương tác trực tiếp với người dùng, đặc biệt khi phản hồi dài (
> giải thích, viết bài, phân tích). Người dùng thấy token xuất hiện từng chút một, giúp giảm cảm giác chờ đợi (perceived
> latency) - thay vì nhìn màn hình trống 5-10 giây, họ bắt đầu đọc ngay từ token đầu tiên. Điều này tạo trải nghiệm tự
> nhiên hơn, giống như đang trò chuyện với người thật. Ngược lại, non-streaming phù hợp hơn cho các tác vụ backend và xử
> lý hàng loạt (batch processing), ví dụ: pipeline tóm tắt hàng nghìn tài liệu, hệ thống phân loại email tự động, hoặc
> các
> API nội bộ cần toàn bộ kết quả trước khi xử lý tiếp. Trong những trường hợp này, không có người dùng đang nhìn màn
> hình,
> và việc nhận toàn bộ response cùng lúc giúp code đơn giản hơn, dễ xử lý lỗi hơn, và dễ cache kết quả hơn.

## Danh Sách Kiểm Tra Nộp Bài

- [x] Tất cả tests pass: `pytest tests/ -v`
- [x] `call_openai` đã triển khai và kiểm thử
- [x] `call_openai_mini` đã triển khai và kiểm thử
- [x] `compare_models` đã triển khai và kiểm thử
- [x] `streaming_chatbot` đã triển khai và kiểm thử
- [x] `retry_with_backoff` đã triển khai và kiểm thử
- [x] `batch_compare` đã triển khai và kiểm thử
- [x] `format_comparison_table` đã triển khai và kiểm thử
- [x] `exercises.md` đã điền đầy đủ
- [x] Sao chép bài làm vào folder `solution` và đặt tên theo quy định
