=========
Tổng quan
=========

Nội dung training IoT của PTN DESLab_ sẽ hướng dẫn xây dựng hệ thống IoT đơn giản giám sát nhiệt độ phòng.
Cụ thể, hệ thống IoT sử dụng cảm biến nhiệt độ LM35_, module `Arduino ESP8266 Wifi Shield <AEWS_>`_, và nền tảng Blynk Blynk_.

Về kiến thức
------------

.. note:: 
    
    Do thời gian rất có hạn, nếu các bạn chưa có nhiều kiến thức về lập trình C, các bạn chỉ cần đọc qua 6 tài liệu tham được đề cập và **không cần tìm hiểu quá chi tiết**.

Để xây dựng một hệ thống IoT, các kiến thức cần tìm hiểu bao gồm:

1. Kiến thức tổng quan về IoT [#IoT1]_ [#IoT2]_
2. Đọc hiểu datasheet của các thiết bị điện tử [#datasheet]_.
3. Kiến thức lập trình C/C++ cơ bản [#C]_.
4. Tổng quan về Arduino Framework [#ArduinoF]_.
5. Kiến thức tổng quan về nền tảng Blynk [#BlynkDocF]_.

Về môi trường làm việc
----------------------



.. footnote
.. [#IoT1] `Các khái niệm tổng quan về IoT trên Amazon <AmazoneIoT_>`_.
.. [#IoT2] `Khái niệm cơ bản về IoT Infrastructure trên Macrometa <MacrometaIoT_>`_.
.. [#datasheet] Datasheet của cảm biến LM35_ trên TI.
.. [#C] `Khóa học lập trình C cơ bản trên Codelearn.io <CodelearnIOC_>`_.
.. [#ArduinoF] `Tổng quan về Arduino Framework <Arduino_>`_.
.. [#BlynkDocF] `Cơ bản về nền tảng Blynk <BlynkDoc_>`_.
.. Link
.. _DESLab: https://deslab.vn
.. _LM35: https://www.ti.com/product/LM35?utm_source=google&utm_medium=cpc&utm_campaign=asc-sens-null-44700045336317707_prodfolderdynamic-cpc-pf-google-soas_int&utm_content=prodfolddynamic&ds_k=DYNAMIC+SEARCH+ADS&DCM=yes&gclid=CjwKCAjw6eWnBhAKEiwADpnw9ojoX6iAxUEk_AFZ_HcGg9V-IfEd6wjS7kg2NNrGZXOVoqw8k548TxoCYKQQAvD_BwE&gclsrc=aw.ds
.. _Blynk: https://blynk.io/
.. _AEWS: https://nshopvn.com/product/arduino-esp8266-wifi-shield/
.. _AmazoneIoT: https://aws.amazon.com/what-is/iot/
.. _MacrometaIoT: https://www.macrometa.com/iot-infrastructure
.. _CodelearnIOC: https://codelearn.io/learning/c-for-beginners
.. _BlynkDoc: https://docs.blynk.io/en/
.. _Arduino: https://docs.arduino.cc/learn/starting-guide/getting-started-arduino