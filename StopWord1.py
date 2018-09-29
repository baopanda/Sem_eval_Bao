STOP_WORDS = set("""
a_lô
a_ha
ai
ai_ai
ai_nấy
ai đó
alô
amen
anh
anh ấy
ba
ba_ba
ba_bản
ba_cùng
ba_họ
ba_ngày
ba_ngôi
ba_tăng
bay_biến
biết_mình
biết_mấy
biết_trước
biết_việc
biết_được
buổi
buổi_làm
buổi_mới
buổi_ngày
buổi_sớm
bà
bà_ấy
bài
bài_bác
bài_bỏ
bài_cái
bác
bán
bán_cấp
bán_dạ
bán_thế
bây_bẩy
bây_chừ
bây_giờ
bây_nhiêu
bèn
béng
bên
bên_bị
bên_có
bên_cạnh
bông
bước
bước_khỏi
bước_tới
bước_đi
bạn
bản
bản_bộ
bản_riêng
bản_thân
bản_ý
bất_chợt
bất_cứ
bất_giác
bất_kì
bất_kể
bất_kỳ
bất_luận
bất_ngờ
bất_nhược
bất_quá
bất_thình_lình
bất_tử
bất_đồ
bấy
bấy chầy
bấy chừ
bấy_giờ
bấy_lâu
bấy lâu_nay
bấy_nay
bấy_nhiêu
bập bà bập_bõm
bập_bõm
bắt_đầu
bắt_đầu_từ
bằng
bằng_cứ
bằng không
bằng người
bằng nhau
bằng như
bằng nào
bằng nấy
bằng vào
bằng được
bằng ấy
bển
bệt
bị
bị_chú
bị vì
bỏ
bỏ_bà
bỏ_cha
bỏ_cuộc
bỏ không
bỏ lại
bỏ_mình
bỏ mất
bỏ_mẹ
bỏ_nhỏ
bỏ_quá
bỏ ra
bỏ riêng
bỏ việc
bỏ xa
bỗng
bỗng_chốc
bỗng_dưng
bỗng_không
bỗng_nhiên
bỗng nhưng
bỗng thấy
bỗng_đâu
bộ
bộ thuộc
bộ điều
bội_phần
bớ
bởi
bởi ai
bởi chưng
bởi nhưng
bởi sao
bởi_thế
bởi_thế cho_nên
bởi tại
bởi_vì
bởi_vậy
bởi đâu
bức
cao
cao lâu
cao_ráo
cao_răng
cao_sang
cao số
cao thấp
cao_thế
cao_xa
cha
cha chả
chao_ôi
chia_sẻ
chiếc
cho
cho biết
cho chắc
cho_hay
cho nhau
cho_nên
cho rằng
cho rồi
cho thấy
cho tin
cho tới
cho tới khi
cho về
cho ăn
cho đang
cho được
cho đến
cho đến khi
cho đến_nỗi
choa
chu_cha
chui_cha
chung
chung cho
chung_chung
chung_cuộc
chung cục
chung nhau
chung_qui
chung_quy
chung_quy_lại
chung_ái
chuyển
chuyển_tự
chuyển đạt
chuyện
chuẩn_bị
chành chạnh
chí_chết
chính
chính bản
chính giữa
chính là
chính_thị
chính điểm
chùn_chùn
chùn_chũn
chú
chú_dẫn
chú khách
chú_mày
chú_mình
chúng
chúng_mình
chúng_ta
chúng_tôi
chúng ông
chăn chắn
chăng
chăng chắc
chăng_nữa
chơi
chơi họ
chưa
chưa bao_giờ
chưa chắc
chưa có
chưa cần
chưa dùng
chưa dễ
chưa kể
chưa tính
chưa từng
chầm_chập
chậc
chắc
chắc_chắn
chắc_dạ
chắc_hẳn
chắc lòng
chắc người
chắc vào
chắc_ăn
chẳng_lẽ
chẳng_những
chẳng_nữa
chẳng phải
chết_nỗi
chết_thật
chết_tiệt
chỉ
chỉ chính
chỉ có
chỉ là
chỉ tên
chỉn
chị
chị bộ
chị ấy
chịu
chịu chưa
chịu lời
chịu tốt
chịu ăn
chọn
chọn bên
chọn ra
chốc_chốc
chớ
chớ_chi
chớ gì
chớ không
chớ kể
chớ như
chợt
chợt nghe
chợt nhìn
chủn
chứ
chứ ai
chứ còn
chứ gì
chứ không
chứ không phải
chứ_lại
chứ_lị
chứ như
chứ sao
coi_bộ
coi mòi
con
con_con
con_dạ
con nhà
con_tính
cu_cậu
cuối
cuối_cùng
cuối điểm
cuốn
cuộc
càng
càng càng
càng hay
cá_nhân
các
các cậu
cách
cách bức
cách không
cách nhau
cách đều
cái
cái gì
cái họ
cái đã
cái đó
cái ấy
câu hỏi
cây
cây_nước
còn
còn như
còn nữa
còn thời_gian
còn về
có
có ai
có chuyện
có_chăng
có_chăng là
có chứ
có cơ
có_dễ
có họ
có_khi
có ngày
có người
có nhiều
có nhà
có phải
có số
có tháng
có thế
có_thể
có_vẻ
có ý
có_ăn
có_điều
có điều_kiện
có đáng
có đâu
có được
cóc_khô
cô
cô_mình
cô quả
cô tăng
cô ấy
công_nhiên
cùng
cùng chung
cùng_cực
cùng nhau
cùng tuổi
cùng tột
cùng với
cùng ăn
căn
căn cái
căn_cắt
căn tính
cũng
cũng như
cũng_nên
cũng thế
cũng vậy
cũng vậy thôi
cũng được
cơ
cơ_chỉ
cơ_chừng
cơ cùng
cơ dẫn
cơ_hồ
cơ_hội
cơ_mà
cơn
cả
cả nghe
cả_nghĩ
cả ngày
cả người
cả nhà
cả năm
cả_thảy
cả_thể
cả_tin
cả ăn
cả đến
cảm_thấy
cảm_ơn
cấp
cấp số
cấp trực_tiếp
cần
cần cấp
cần gì
cần số
cật_lực
cật sức
cậu
cổ_lai
cụ_thể
cụ_thể là
cụ_thể như
của
của ngọt
của tin
cứ
cứ như
cứ_việc
cứ_điểm
cực_lực
do
do vì
do_vậy
do đó
duy
duy chỉ
duy có
dài
dài lời
dài ra
dành
dành_dành
dào
dì
dù
dù cho
dù_dì
dù gì
dù_rằng
dù_sao
dùng
dùng cho
dùng hết
dùng làm
dùng đến
dưới
dưới nước
dạ
dạ bán
dạ_con
dạ_dài
dạ_dạ
dạ khách
dần_dà
dần_dần
dầu sao
dẫn
dẫu
dẫu mà
dẫu rằng
dẫu_sao
dễ
dễ dùng
dễ gì
dễ khiến
dễ nghe
dễ ngươi
dễ như_chơi
dễ sợ
dễ sử_dụng
dễ_thường
dễ thấy
dễ ăn
dễ đâu
dở_chừng
dữ
dữ cách
em
em_em
giá_trị
giá_trị thực_tế
giảm
giảm_chính
giảm thấp
giảm_thế
giống
giống người
giống nhau
giống như
giờ
giờ_lâu
giờ này
giờ đi
giờ_đây
giờ đến
giữ
giữ lấy
giữ_ý
giữa
giữa lúc
gây
gây cho
gây giống
gây ra
gây thêm
gì
gì gì
gì đó
gần
gần bên
gần hết
gần ngày
gần như
gần_xa
gần đây
gần đến
gặp
gặp khó_khăn
gặp phải
gồm
hay
hay_biết
hay_hay
hay không
hay_là
hay làm
hay nhỉ
hay nói
hay sao
hay tin
hay đâu
hiểu
hiện_nay
hiện_tại
hoàn_toàn
hoặc
hoặc là
hãy
hãy còn
hơn
hơn cả
hơn hết
hơn là
hơn_nữa
hơn trước
hầu_hết
hết
hết chuyện
hết cả
hết của
hết nói
hết_ráo
hết rồi
hết_ý
họ
họ gần
họ xa
hỏi
hỏi lại
hỏi xem
hỏi xin
hỗ_trợ
khi
khi khác
khi không
khi nào
khi nên
khi trước
khiến
khoảng
khoảng_cách
khoảng không
khá
khá tốt
khác
khác_gì
khác khác
khác nhau
khác_nào
khác_thường
khác xa
khách
khó
khó biết
khó chơi
khó_khăn
khó làm
khó mở
khó nghe
khó nghĩ
khó nói
khó thấy
khó tránh
không
không ai
không bao_giờ
không bao_lâu
không biết
không bán
không chỉ
không còn
không có
không có gì
không cùng
không cần
không cứ
không dùng
không gì
không hay
không khỏi
không kể
không ngoài
không nhận
không_những
không phải
không phải không
không_thể
không tính
không điều_kiện
không được
không đầy
không để
khẳng_định
khỏi
khỏi nói
kể
kể_cả
kể như
kể tới
kể từ
liên_quan
loại
loại từ
luôn
luôn cả
luôn_luôn
luôn tay
là
là cùng
là là
là nhiều
là phải
là thế_nào
là vì
là ít
làm
làm_bằng
làm cho
làm dần_dần
làm gì
làm lòng
làm lại
làm lấy
làm mất
làm ngay
làm như
làm_nên
làm ra
làm riêng
làm_sao
làm theo
làm thế_nào
làm_tin
làm tôi
làm tăng
làm tại
làm tắp_lự
làm_vì
làm đúng
làm được
lâu
lâu các
lâu_lâu
lâu_nay
lâu ngày
lên
lên cao
lên_cơn
lên mạnh
lên_ngôi
lên_nước
lên số
lên xuống
lên đến
lòng
lòng không
lúc
lúc khác
lúc lâu
lúc_nào
lúc này
lúc sáng
lúc trước
lúc đi
lúc đó
lúc đến
lúc ấy
lý_do
lượng
lượng cả
lượng số
lượng từ
lại
lại bộ
lại cái
lại còn
lại_giống
lại làm
lại_người
lại nói
lại nữa
lại_quả
lại thôi
lại ăn
lại đây
lấy
lấy_có
lấy cả
lấy giống
lấy làm
lấy lý_do
lấy lại
lấy ra
lấy_ráo
lấy sau
lấy số
lấy thêm
lấy thế
lấy vào
lấy xuống
lấy_được
lấy để
lần
lần khác
lần lần
lần nào
lần này
lần sang
lần sau
lần theo
lần trước
lần tìm
lớn
lớn lên
lớn nhỏ
lời
lời chú
lời_nói
mang
mang lại
mang mang
mang nặng
mang về
muốn
mà
mà cả
mà không
mà_lại
mà thôi
mà vẫn
mình
mạnh
mất
mất còn
mọi
mọi giờ
mọi_khi
mọi lúc
mọi người
mọi nơi
mọi sự
mọi thứ
mọi việc
mối
mỗi
mỗi lúc
mỗi lần
mỗi_một
mỗi ngày
mỗi người
một
một_cách
một cơn
một_khi
một lúc
một_số
một_vài
một_ít
mới
mới hay
mới_rồi
mới_đây
mở
mở_mang
mở nước
mở ra
mợ
mức
nay
ngay
ngay bây_giờ
ngay cả
ngay khi
ngay khi đến
ngay lúc
ngay lúc này
ngay lập_tức
ngay_thật
ngay tức_khắc
ngay tức_thì
ngay từ
nghe
nghe_chừng
nghe hiểu
nghe không
nghe lại
nghe_nhìn
nghe như
nghe nói
nghe_ra
nghe rõ
nghe thấy
nghe tin
nghe trực_tiếp
nghe_đâu
nghe_đâu như
nghe được
nghen
nghiễm_nhiên
nghĩ
nghĩ_lại
nghĩ ra
nghĩ tới
nghĩ xa
nghĩ đến
nghỉm
ngoài
ngoài này
ngoài_ra
ngoài xa
ngoải
nguồn
ngày
ngày_càng
ngày cấp
ngày_giờ
ngày_ngày
ngày nào
ngày này
ngày_nọ
ngày qua
ngày_rày
ngày_tháng
ngày_xưa
ngày xửa
ngày đến
ngày ấy
ngôi
ngôi nhà
ngôi_thứ
ngõ hầu
ngăn_ngắt
ngươi
người
người hỏi
người khác
người khách
người mình
người nghe
người_người
người nhận
ngọn
ngọn_nguồn
ngọt
ngồi
ngồi_bệt
ngồi_không
ngồi sau
ngồi trệt
ngộ nhỡ
nhanh
nhanh lên
nhanh tay
nhau
nhiên hậu
nhiều
nhiều ít
nhiệt_liệt
nhung_nhăng
nhà
nhà_chung
nhà_khó
nhà làm
nhà_ngoài
nhà_ngươi
nhà tôi
nhà_việc
nhân_dịp
nhân_tiện
nhé
nhìn
nhìn_chung
nhìn lại
nhìn_nhận
nhìn theo
nhìn thấy
nhìn xuống
nhóm
nhón nhén
như
như_ai
như_chơi
như_không
như là
như nhau
như quả
như sau
như_thường
như_thế
như thế_nào
như_thể
như trên
như trước
như_tuồng
như_vậy
như_ý
nhưng
nhưng mà
nhược_bằng
nhất
nhất_loạt
nhất luật
nhất_là
nhất_mực
nhất_nhất
nhất_quyết
nhất sinh
nhất_thiết
nhất thì
nhất tâm
nhất_tề
nhất_đán
nhất_định
nhận
nhận_biết
nhận họ
nhận làm
nhận nhau
nhận ra
nhận thấy
nhận việc
nhận được
nhằm
nhằm khi
nhằm lúc
nhằm vào
nhằm để
nhỉ
nhỏ
nhỏ người
nhớ
nhớ bập_bõm
nhớ lại
nhớ lấy
nhớ ra
nhờ
nhờ chuyển
nhờ có
nhờ_nhờ
nhờ đó
nhỡ_ra
những
những_ai
những khi
những là
những lúc
những muốn
những như
nào
nào cũng
nào_hay
nào_là
nào phải
nào đâu
nào đó
này
này_nọ
nên
nên chi
nên_chăng
nên làm
nên người
nên tránh
nó
nóc
nói
nói bông
nói_chung
nói_khó
nói là
nói lên
nói lại
nói_nhỏ
nói phải
nói qua
nói ra
nói_riêng
nói rõ
nói thêm
nói thật
nói_toẹt
nói trước
nói tốt
nói với
nói xa
nói ý
nói đến
nói đủ
năm
năm_tháng
nơi
nơi_nơi
nước
nước bài
nước cùng
nước lên
nước_nặng
nước quả
nước xuống
nước_ăn
nước đến
nấy
nặng
nặng căn
nặng mình
nặng về
nếu
nếu có
nếu cần
nếu không
nếu_mà
nếu_như
nếu thế
nếu_vậy
nếu được
nền
nọ
nớ
nức_nở
nữa
nữa khi
nữa là
nữa rồi
oai_oái
oái
pho
phè
phè_phè
phía
phía bên
phía bạn
phía dưới
phía sau
phía trong
phía trên
phía trước
phóc
phót
phù_hợp
phăn phắt
phương chi
phải
phải_biết
phải_chi
phải_chăng
phải cách
phải_cái
phải giờ
phải khi
phải không
phải lại
phải lời
phải người
phải như
phải rồi
phải tay
phần
phần_lớn
phần_nhiều
phần_nào
phần sau
phần việc
phắt
phỉ_phui
phỏng
phỏng như
phỏng nước
phỏng theo
phỏng_tính
phốc
phụt
phứt
qua
qua chuyện
qua khỏi
qua_lại
qua lần
qua_ngày
qua tay
qua thì
qua đi
quan_trọng
quan_trọng vấn_đề
quan_tâm
quay
quay bước
quay lại
quay số
quay đi
quá
quá_bán
quá_bộ
quá giờ
quá_lời
quá mức
quá nhiều
quá_tay
quá thì
quá tin
quá_trình
quá tuổi
quá_đáng
quá_ư
quả
quả là
quả_thật
quả thế
quả_vậy
quận
ra
ra bài
ra_bộ
ra chơi
ra_gì
ra lại
ra lời
ra_ngôi
ra người
ra sao
ra_tay
ra vào
ra ý
ra_điều
ra đây
ren_rén
riu_ríu
riêng
riêng từng
riệt
rày
ráo
ráo cả
ráo nước
ráo_trọi
rén
rén bước
rích
rón_rén
rõ
rõ là
rõ thật
rút cục
răng
răng răng
rất
rất lâu
rằng
rằng là
rốt_cuộc
rốt cục
rồi
rồi nữa
rồi ra
rồi sao
rồi sau
rồi tay
rồi thì
rồi xem
rồi_đây
rứa
sa_sả
sang
sang_năm
sang_sáng
sang_tay
sao
sao bản
sao bằng
sao cho
sao_vậy
sao đang
sau
sau chót
sau cuối
sau_cùng
sau_hết
sau_này
sau nữa
sau sau
sau đây
sau đó
so
so với
song le
suýt
suýt_nữa
sáng
sáng ngày
sáng rõ
sáng thế
sáng_ý
sì
sì sì
sất
sắp
sắp_đặt
sẽ
sẽ biết
sẽ hay
số
số cho biết
số cụ_thể
số loại
số là
số người
số phần
số thiếu
sốt_sột
sớm
sớm ngày
sở_dĩ
sử_dụng
sự
sự thế
sự_việc
tanh
tanh tanh
tay
tay_quay
tha_hồ
tha_hồ chơi
tha_hồ_ăn
than_ôi
thanh
thanh ba
thanh_chuyển
thanh không
thanh_thanh
thanh tính
thanh điều_kiện
thanh_điểm
thay_đổi
thay_đổi tình_trạng
theo
theo bước
theo như
theo tin
thi_thoảng
thiếu
thiếu_gì
thiếu điểm
thoạt
thoạt nghe
thoạt_nhiên
thoắt
thuần
thuần_ái
thuộc
thuộc bài
thuộc cách
thuộc lại
thuộc từ
thà
thà_là
thà_rằng
thành_ra
thành_thử
thái_quá
tháng
tháng_ngày
tháng năm
tháng_tháng
thêm
thêm chuyện
thêm giờ
thêm vào
thì
thì_giờ
thì là
thì_phải
thì_ra
thì_thôi
thình_lình
thích
thích cứ
thích thuộc
thích tự
thích ý
thím
thôi
thôi_việc
thúng_thắng
thương_ôi
thường
thường bị
thường hay
thường_khi
thường số
thường sự
thường thôi
thường thường
thường tính
thường tại
thường xuất_hiện
thường đến
thảo_hèn
thảo_nào
thấp
thấp_cơ
thấp_thỏm
thấp xuống
thấy
thấy_tháng
thẩy
thậm
thậm_chí
thậm cấp
thậm từ
thật
thật chắc
thật là
thật_lực
thật quả
thật_ra
thật_sự
thật_thà
thật tốt
thật_vậy
thế
thế chuẩn_bị
thế_là
thế lại
thế_mà
thế_nào
thế nên
thế_ra
thế_sự
thế_thì
thế thôi
thế thường
thế_thế
thế à
thế đó
thếch
thỉnh_thoảng
thỏm
thốc
thốc_tháo
thốt
thốt_nhiên
thốt nói
thốt thôi
thộc
thời_gian
thời_gian sử_dụng
thời_gian tính
thời_điểm
thục_mạng
thứ
thứ bản
thứ đến
thửa
thực_hiện
thực_hiện đúng
thực_ra
thực_sự
thực_tế
thực_vậy
tin
tin thêm
tin vào
tiếp_theo
tiếp_tục
tiếp đó
tiện_thể
toà
toé_khói
toẹt
trong
trong khi
trong lúc
trong mình
trong_ngoài
trong này
trong số
trong vùng
trong đó
trong ấy
tránh
tránh khỏi
tránh ra
tránh tình_trạng
tránh xa
trên
trên bộ
trên_dưới
trước
trước_hết
trước khi
trước_kia
trước_nay
trước ngày
trước nhất
trước_sau
trước_tiên
trước tuổi
trước_đây
trước đó
trả
trả của
trả lại
trả ngay
trả trước
trếu tráo
trển
trệt
trệu_trạo
trỏng
trời_đất ơi
trở_thành
trừ_phi
trực_tiếp
trực_tiếp làm
tuy
tuy có
tuy là
tuy_nhiên
tuy_rằng
tuy_thế
tuy_vậy
tuy đã
tuyệt_nhiên
tuần_tự
tuốt_luốt
tuốt tuồn_tuột
tuốt_tuột
tuổi
tuổi cả
tuổi_tôi
tà_tà
tên
tên chính
tên cái
tên họ
tên_tự
tênh
tênh_tênh
tìm
tìm bạn
tìm cách
tìm_hiểu
tìm ra
tìm việc
tình_trạng
tính
tính_cách
tính căn
tính người
tính phỏng
tính_từ
tít_mù
tò_te
tôi
tôi con
tông_tốc
tù tì
tăm_tắp
tăng
tăng chúng
tăng cấp
tăng giảm
tăng thêm
tăng_thế
tại
tại lòng
tại nơi
tại_sao
tại tôi
tại vì
tại đâu
tại đây
tại đó
tạo
tạo cơ_hội
tạo nên
tạo ra
tạo ý
tạo điều_kiện
tấm
tấm bản
tấm các
tấn
tấn_tới
tất_cả
tất_cả bao_nhiêu
tất_thảy
tất tần_tật
tất_tật
tập_trung
tắp
tắp_lự
tắp_tắp
tọt
tỏ ra
tỏ_vẻ
tốc tả
tối_ư
tốt
tốt bạn
tốt bộ
tốt hơn
tốt mối
tốt_ngày
tột
tột_cùng
tớ
tới
tới gần
tới mức
tới nơi
tới thì
tức_thì
tức_tốc
từ
từ căn
từ giờ
từ khi
từ_loại
từ nay
từ thế
từ_tính
từ tại
từ từ
từ ái
từ điều
từ đó
từ ấy
từng
từng cái
từng giờ
từng nhà
từng phần
từng thời_gian
từng đơn_vị
từng ấy
tự
tự_cao
tự khi
tự lượng
tự tính
tự tạo
tự vì
tự_ý
tự_ăn
tựu_trung
veo
veo_veo
việc
việc_gì
vung thiên_địa
vung tàn_tán
vung tán tàn
và
vài
vài_ba
vài người
vài nhà
vài nơi
vài tên
vài điều
vào
vào gặp
vào_khoảng
vào lúc
vào vùng
vào đến
vâng
vâng chịu
vâng_dạ
vâng vâng
vâng ý
vèo
vèo_vèo
vì
vì chưng
vì rằng
vì sao
vì_thế
vì_vậy
ví bằng
ví_dù
ví_phỏng
ví_thử
vô_hình_trung
vô_kể
vô_luận
vô_vàn
vùng
vùng lên
vùng nước
văng_tê
vượt
vượt khỏi
vượt quá
vạn nhất
vả_chăng
vả_lại
vấn_đề
vấn_đề quan_trọng
vẫn
vẫn thế
vậy
vậy là
vậy_mà
vậy nên
vậy ra
vậy thì
vậy_ư
về
về không
về nước
về phần
về sau
về tay
vị_trí
vị_tất
vốn_dĩ
với
với_lại
với nhau
vở
vụt
vừa
vừa khi
vừa lúc
vừa_mới
vừa_qua
vừa_rồi
vừa vừa
xa
xa_cách
xa_gần
xa nhà
xa_tanh
xa_tắp
xa_xa
xa xả
xem
xem_lại
xem_ra
xem số
xin
xin gặp
xin vâng
xiết_bao
xon_xón
xoành_xoạch
xoét
xoẳn
xoẹt
xuất_hiện
xuất kì bất_ý
xuất_kỳ bất_ý
xuể
xuống
xăm_xúi
xăm_xăm
xăm_xắm
xảy ra
xềnh_xệch
xệp
xử_lý
yêu_cầu
à
à này
à_ơi
ào
ào vào
ào_ào
á
á_à
ái
ái_chà
ái_dà
áng
áng như
âu_là
ít
ít biết
ít có
ít hơn
ít khi
ít_lâu
ít_nhiều
ít_nhất
ít_nữa
ít quá
ít_ra
ít thôi
ít thấy
ô_hay
ô_hô
ô_kê
ô_kìa
ôi_chao
ôi_thôi
ông
ông nhỏ
ông tạo
ông từ
ông ấy
ông_ổng
úi
úi_chà
úi_dào
ý
ý_chừng
ý da
ý hoặc
ăn
ăn chung
ăn chắc
ăn_chịu
ăn cuộc
ăn hết
ăn_hỏi
ăn làm
ăn_người
ăn ngồi
ăn quá
ăn riêng
ăn sáng
ăn_tay
ăn trên
ăn về
đang
đang_tay
đang thì
điều
điều gì
điều_kiện
điểm
điểm chính
điểm gặp
điểm đầu_tiên
đành_đạch
đáng
đáng_kể
đáng_lí
đáng_lý
đáng_lẽ
đáng số
đánh_giá
đánh đùng
đáo_để
đâu
đâu có
đâu cũng
đâu như
đâu nào
đâu phải
đâu_đâu
đâu_đây
đâu_đó
đây
đây này
đây rồi
đây_đó
đã
đã hay
đã không
đã là
đã lâu
đã thế
đã vậy
đã đủ
đó
đó_đây
đúng
đúng ngày
đúng_ra
đúng tuổi
đúng với
đơn_vị
đưa
đưa cho
đưa chuyện
đưa em
đưa ra
đưa tay
đưa tin
đưa tới
đưa vào
đưa về
đưa xuống
đưa đến
được
được_cái
được lời
được nước
được tin
đại_loại
đại_nhân
đại_phàm
đại_để
đạt
đảm_bảo
đầu_tiên
đầy
đầy_năm
đầy phè
đầy tuổi
đặc_biệt
đặt
đặt làm
đặt mình
đặt mức
đặt ra
đặt trước
đặt để
đến
đến bao_giờ
đến_cùng
đến cùng_cực
đến cả
đến giờ
đến gần
đến hay
đến khi
đến lúc
đến lời
đến nay
đến ngày
đến_nơi
đến_nỗi
đến thì
đến thế
đến tuổi
đến xem
đến_điều
đến đâu
đều
đều bước
đều nhau
đều đều
để
để cho
để giống
để không
để lòng
để lại
để mà
để_phần
để được
để đến_nỗi
đối_với
đồng_thời
đủ
đủ_dùng
đủ_nơi
đủ_số
đủ_điều
đủ_điểm
ơ
ơ_hay
ơ_kìa
ơi
ơi_là
ư
ạ
ạ_ơi
ấy
ấy là
ầu_ơ
ắt
ắt_hẳn
ắt_là
ắt phải
ắt thật
ối_dào
ối giời
ối giời ơi
ồ
ồ_ồ
ổng
ớ
ớ này
ờ
ờ ờ
ở
ở lại
ở như
ở nhờ
ở năm
ở trên
ở vào
ở đây
ở đó
ở được
ủa
ứ_hự
ứ_ừ
ừ
ừ nhé
ừ thì
ừ_ào
ừ ừ
ử
“
”
u
xong
xảy
đầu
châu
đội
vòng
trẻ
toàn
văng
ngã
chạy
phường
đường
đèo
đi
tạt
hất
hải
tổ
xe
dừng
huyện
thẳng
gãy
x
xem_xét
tội
tư sở
tùng
ngụ
xã
ấp
trung
bản
san
phương
việt
yên
kỳ
thi
cận
tiếng
vụ
mưa
mậu
chôn
đất
núi
vùi
sông
>
tỉnh
chuyến
hàng
bay
trở_lại
hãng
xác_định
perth
tỷ
hiện
đâm
đông
đám
lao
song
nàng
bloom
giành
đh
trường
dân
đoàn
ob
sữa
tinh
?
hàu
phượng
xà
cháu
bé
trình
vợ
mạng
nuôi
đoạn
–
ảnh_duẩn
đứa
﻿








﻿
﻿


﻿
”
tuyên
chục
hùng
cánh
cổng
kín
chỗ
xế
quái
diễn
còi
hú
vang
phê
sắt
đón
mái
xót
bịch
hiệp
quẩy
long
tý
uống
nốt
còng
t
phá
choai_choai
lăn
má
mấy
cúi
giọt
yêng
xử
phòng
án
kẻ
đọc
nửa
gửi
hôm
ngờ
phong
hấp
rơi
bộp
cường
đích
bóng
tóe
lửa
kéo
rê
m
lái
ngon
triệu
đồng
phong
đích
tưởng
nhấn
ga
vọt
pha
ngả
ôm
cua
tuyến
phố
quanh
hồ
cường
chiếm
dậy
sóng
gầm
mặt
hồ
kia
bàn
hội
mai
bàn
lụa
câu
găm
sơn
đít
xanh
phi
kèm
gạch
đập
nắn
chân
waves
dắt
cửa
wave
dream
tết
dạo
vạn
bắt
đêm
dịp
rạng
bắt
tạm
tức
dính
tôm
sinh
đời
vốn
lận
lưng
cất
ánh
mắt
vành
tám
khóa
chặt
màu
xám
tiến
hụ
trận
cốp
hai
hai
hô
ẵm
trời
muộn
quen
cảnh
nội
thằng
mẹ
lớp
học
bố
hòm
nộp
kêu
bậc
a
b
c
d
đ
e
f
g
h
i
k
l
m
n
o
ơ
ô
p
q
r
s
t
u
ư
v
w
x
y
z
""".split('\n'))