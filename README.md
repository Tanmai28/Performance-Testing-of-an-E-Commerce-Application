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
Gradually increased users beyond expected load to find breaking points.

### ✅ KPIs Analyzed
- Response Time (Avg, 90th percentile)
- Throughput (req/sec)
- Error %
- Peak Load Handling
- Server behavior on AWS EC2

### ✅ AWS EC2 Execution
- JMeter executed in non-GUI mode for high-load generation 
- Instance used: t2.medium
- Ideal for distributed testing and stable throughput

### 🏗️ Test Plan Architecture

```
Test Plan
└── Thread Group (100–500 Users)
├── HTTP Request: Homepage
├── HTTP Request: Product Listing
├── HTTP Request: Product Details API
├── HTTP Request: Add to Cart
├── CSV Data Set Config (Dynamic User Data)
├── Summary Report
├── Aggregate Report
└── View Results Tree (for debugging)

```
### ❓ Why JMeter?
- Open-source and widely used
- Easy to simulate concurrent users
- Supports API & web performance testing
- Works well with AWS for scalable load generation
- Strong reporting and listener tools
  
---

## 📁 Project Structure
```
/ecommerce_testplan.jmx
/validate_response.py
/results.csv
/README.md

```

---

## 🧪 How to Run
### 1️⃣ GUI Mode
1. Open JMeter
2. Load the ecommerce_testplan.jmx file
3. Click Start to run the test
4. Observe metrics in Summary/Aggregate reports

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

### 🔎 Performance Bottleneck Findings

1. At 400+ users, response time increased significantly
2. Throughput dropped from 120 → 85 req/sec
3. EC2 CPU usage reached ~85%
4. Indicates backend processing / DB queries may be the bottleneck

---

## 🐍 Python Validation Script
Used to validate API response status codes and JSON structure after test.

---

## 🛠 Technologies Used
- Apache JMeter  
- Python  
- AWS EC2  
- Shell scripting  

---
### 🏁 Conclusion

This project provided hands-on experience in designing performance test scenarios, executing load & stress tests, monitoring system behavior on AWS, and validating API correctness using Python.
It demonstrates a strong understanding of performance engineering, bottleneck analysis, and scalable testing workflows.
