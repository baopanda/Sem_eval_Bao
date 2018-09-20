from pyvi import ViTokenizer

s = "Quán này ăn từ hồi nhỏ , giờ thì không ăn nữa do chất_lượng đi xuống quá . Xôi thơm dẻo , nhưng quá ít và quá mắc khi so_sánh chất_lượng với số tiền . Gà nướng ăn cũng ngon nhưng vẫn tập_trung một chữ mắc 1 phần xôi gà hai_mươi mấy ngàn mà có chút_ít . Chè thì dở , mua chè ngoài chợ chắc còn ngon hơn ở đây . Quán đông nên phục_vụ không tốt lắm , chậm ."
s = ViTokenizer.tokenize(s)
print(s)