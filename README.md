# sport
运动目标控制与自动追踪系统
项目描述:设计一个运动目标控制与自动追踪系统,该系统包括模拟目标运动的红色光斑位置控制系统和指示自动追踪的绿色光斑位置控制系统。
整体思路:通过OpenMV 摄像头识别并框出画板上的黑色矩形,发送矩形四角坐标,STM32将接收到坐标与期望值对比,控制1号舵机云台转动某角度,将激光笔固定在二维云台上,从而使激光笔指向期望坐标,2号舵机云台识别1号激光笔光斑并自动追踪1号云台。
团队职责:在团队中负责视觉部分,机械结构搭建及优化,摄像头与主控通信,硬件调试和故障排除。
所用知识:OpenMV颜色识别算算法和矩形检测算法(核心),STM32串口(UART)编写及数据包解析,PID算法控制PWM输出,定时中断,外部中断等。
