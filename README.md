# COOKING-OIL-PURITY-DETECTION-FOR-PUBLIC-USE
![Test](C:\Users\DELL\AppData\Local\Microsoft\Windows\INetCache\IE\HFEU6J64\Screenshot_2025-12-13_133215[1].png)

## 📌 Overview
This project presents a **low-cost embedded system for real-time detection of cooking oil purity**, designed to enhance food safety in public-use environments such as **street food vendors, community kitchens, and small-scale restaurants**.

Repeated use of cooking oil causes **thermal degradation** and formation of **harmful compounds**, posing serious health risks. This system helps identify oil quality and supports timely oil replacement.

---

## 🎯 Objectives
- Detect degradation in cooking oil quality
- Classify oil as **Pure**, **Used**, or **Waste**
- Enable **real-time local and remote monitoring**
- Provide a **low-cost and scalable food safety solution**

---

## 🧠 System Description
The proposed system uses:
- **RGB Color Sensor** to measure optical clarity
- **pH Sensor** to detect acidity changes
- **Arduino / ESP32 microcontroller** to process sensor data

Oil samples are classified using **predefined threshold values** derived from experimental analysis.

### 🔄 Virtual Turbidity Estimation
In the absence of a functional turbidity sensor, the system **virtually estimates turbidity** using:
- Color sensor readings
- pH values  

This ensures **uninterrupted operation** without hardware dependency.

---

## ☁️ IoT & Cloud Integration
The system integrates **Internet of Things (IoT)** functionality by uploading sensor data to the **ThingSpeak cloud platform**.

### Uploaded Parameters:
- pH value
- Color average
- Estimated turbidity
- Oil quality classification

📊 Data can be viewed:
- Locally via **Serial Monitor**
- Remotely through **ThingSpeak dashboard**

---

## 🧪 Experimental Validation
Experiments were conducted using cooking oil samples at different stages of usage:
- Fresh oil
- Moderately used oil
- Heavily degraded oil

Results confirmed that the system **effectively distinguishes oil quality levels** based on sensor data.

---

## 🧩 System Features
- Low-cost embedded design
- Real-time monitoring
- Cloud-based visualization
- Compact and portable prototype
- Power-efficient and wireless operation

---

## 🔧 Scalability & Future Enhancements
The modular design allows easy integration of:
- Temperature sensors
- Dielectric sensors
- Advanced analytics for predictive oil replacement

Historical data can be analyzed to identify **oil degradation patterns**, supporting **predictive maintenance** and improved decision-making.

---

## 🏭 Applications
- Street food vendors
- Small restaurants
- Community kitchens
- Food safety inspections
- Academic and IoT research projects

---

## 🛠 Technologies Used
- Arduino / ESP32
- RGB Color Sensor (TCS34725)
- pH Sensor
- ThingSpeak Cloud Platform
- Embedded C / Arduino IDE

---

## 📜 Conclusion
The developed system provides a **practical, affordable, and technology-driven approach** to ensure healthier food preparation practices in decentralized and resource-limited environments. Its compact design, IoT connectivity, and scalability make it suitable for real-world deployment.

---




## 📄 License
This project is open-source.
