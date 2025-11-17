# Performance Testing of an E-Commerce Application using JMeter

## 📌 Overview
This project demonstrates **load & stress testing** of an e‑commerce application using **Apache JMeter**.  
It includes execution on **AWS EC2**, automated KPI analysis, and Python-based response validation.

---
<img width="1536" height="1024" alt="img" src="https://github.com/user-attachments/assets/cc44de18-8456-4b31-a22d-e1557ce87c2d" />

---

## 🚀 Features Implemented
### ✅ Load Testing  
Simulated 100–500 virtual users hitting:
- Homepage
- Product listing
- Product details API

### ✅ Stress Testing  
Increased load until failure to identify breaking points.

### ✅ KPIs Analyzed
- Response Time (Avg, 90th percentile)
- Throughput (req/sec)
- Error %
- Peak Load Handling
- Server behavior on AWS EC2

### ✅ AWS EC2 Execution
- JMeter executed in non-GUI mode on t2.medium instance  
- Faster distributed load generation

---

## 📁 Project Structure
```
/ecommerce_testplan.jmx
/validate_response.py
/results/
```

---

## 🧪 How to Run
### 1️⃣ GUI Mode
Open file in JMeter → Run test

### 2️⃣ Non-GUI (AWS EC2)
```
jmeter -n -t ecommerce_testplan.jmx -l results/results.csv
```

---

## 📈 Sample Observations
| Metric | Value |
|--------|--------|
| Avg Response Time | 280ms |
| Max Response Time | 900ms |
| Throughput | 120 req/sec |
| Error Rate | 0% |

---

## 🐍 Python Validation Script
Used to validate API response status codes and JSON structure after test.

---

## 🛠 Technologies Used
- Apache JMeter  
- Python  
- AWS EC2  
- Shell scripting  
