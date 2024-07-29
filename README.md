# Hành Trình Tạo API Module Cho Locket Camera: Những Khám Phá Đầy Bất Ngờ

## Ngày 1: Khởi Đầu Với Những Kỳ Vọng Lớn Lao

Ý tưởng về việc tạo ra một module API cho Locket Camera đến với tôi vào một buổi chiều đầy nắng. Tôi háo hức bắt tay vào việc, hy vọng sẽ nhanh chóng đạt được những kết quả đầu tiên. Mục tiêu đầu tiên của tôi là `getUserByUsername` – một API lấy thông tin tài khoản từ username. Tôi tự tin rằng chỉ cần bắt request và đưa token vào header là mọi thứ sẽ hoạt động.

Nhưng cuộc đời không như là mơ. Token trong phần authorization của Locket Camera chỉ có hiệu lực trong 15 phút. Điều này khiến tôi cảm thấy mệt mỏi và quyết định tạm dừng, để lại bài toán khó cho ngày hôm sau.

## Ngày 2: Thử Thách Và Thành Công Đầu Tiên

Sau một đêm suy nghĩ, tôi nhận ra rằng phải tìm cách lấy token authorization một cách tự động. Tôi đã tập trung vào API login và thử nghiệm với `https://www.googleapis.com/identitytoolkit/v3/relyingparty/verifyPassword?key=AIzaSyCQngaaXQIfJaH0aS2l7REgIjD7nL431So`. Payload của request bao gồm email và password. Cuối cùng, tôi nhận được token và thêm nó vào header authorization. Thật tuyệt vời! Request đến `getUserByUsername` đã thành công.

Tuy nhiên, niềm vui chưa kéo dài được bao lâu. Tôi phát hiện ra rằng cần phải có thêm một giá trị trong header là `X-Firebase-AppCheck` để thực sự hoàn tất các request khác. Tôi thử mã hóa payload dạng JWT với thuật toán HSA256 nhưng không thành công. 

## Ngày 3: Khám Phá Những Bí Mật Của API

Không nản lòng, tôi tiếp tục tìm cách khác. Tôi nhận ra rằng một số API không cần header `X-Firebase-AppCheck`. Điều này mở ra một cơ hội lớn cho tôi:

DƯỚI ĐÂY LÀ LIST API CẦN 'X-FIREBASE-CHECKAPP' Ở HEADER:

1. **API `getLastMomment`**: Chỉ cần token từ login là có thể hoạt động mà không cần `X-Firebase-AppCheck`.
    - URL: `https://api.locketcamera.com/getLatestMomentV2`
    - Payload:
    ```json
    {
        "data": {
            "excluded_users": [],
            "sync_token": "5oImx73nFjTb1FTRkBC2",
            "last_fetch": {
                "@type": "type.googleapis.com/google.protobuf.Int64Value",
                "value": "1722073779706"
            },
            "fetch_streak": false,
            "should_count_missed_moments": true
        }
    }
    ```

2. **API `changeProfileInfo`**: Thay đổi thông tin hồ sơ.
    - URL: `https://api.locketcamera.com/changeProfileInfo`
    - Payload 1: 
    ```json
    {
        "data": {
            "badge": "locket_gold"
        }
    }
    ```
    - Payload 2: 
    ```json
    {
        "data": {
            "last_name": "Nguyen",
            "first_name": "Anh"
        }
    }
    ```

3. **API `updateEmailAddress`**: Cập nhật địa chỉ email.
    - URL: `https://api.locketcamera.com/updateEmailAddress`
    - Payload:
    ```json
    {
        "data": {
            "email": "example@gmail.com"
        }
    }
    ```

4. **API `sendVerificationCode`**: Đổi số điện thoại.
    - URL: `https://api.locketcamera.com/sendVerificationCode`
    - Payload:
    ```json
    {
        "data": {
            "phone": "+84987654321",
            "operation": "change_number",
            "platform": "ios",
            "is_retry": false
        }
    }
    ```

5. **API `sendChatMessageV2`**: Gửi tin nhắn.
    - URL: `https://api.locketcamera.com/sendChatMessageV2`
    - Payload:
    ```json
    {
        "data": {
            "receiver_uid": "bmLzyn7UQTPtN7budBYirrWdDUb2",
            "client_token": "72652F96-0C4D-4CFE-9D59-B3251029B897",
            "msg": "Ê bro",
            "moment_uid": null,
            "from_memory": false
        }
    }
    ```

6. **API `createAccountWithEmailPassword`**: Tạo tài khoản mới.
    - URL: `https://api.locketcamera.com/createAccountWithEmailPassword`
    - Payload:
    ```json
    {
        "data": {
            "password": "your_password",
            "client_token": "9e4add9a8ac5b41328cff18e93aa0ff87a814c80",
            "client_email_verif": true,
            "email": "example@gmail.com",
            "platform": "ios"
        }
    }
    ```

7. **API `deleteUserAccount`**: Xóa tài khoản người dùng.
    - URL: `https://api.locketcamera.com/deleteUserAccount`
    - Chỉ cần token authorization và `X-Firebase-AppCheck`.
