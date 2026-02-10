
# Team Number – Project Title

## 👥 Team Info
- 22471A05O6 — **T.Durga Bhavani** ( [@durgabhavani](https://www.linkedin.com/in/durgabhavani-tumma-14b29028b/) )
_Work Done: Implemented data preprocessing pipeline including data cleaning, Min-Max normalization, SMOTEENN class balancing, and Boruta feature selection. Developed and trained Autoencoder and GRU models.
- 22471A05M4 — **G.Kavya** ( [@kavya](https://www.linkedin.com/in/kavya2811) )
_Work Done:Implemented AlexNet and MiniVGGNet architectures. Performed model training, hyperparameter tuning, and accuracy optimization. _

- 22471A05O3 — **SK.Y.Khajabi** ( [@khajabi](https://www.linkedin.com/in/khajabi-shaik-yalavarthi-9436212bbutm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app) )
_Work Done: Conducted exploratory data analysis (EDA), dataset merging, feature encoding, and visualization of training/validation curves and confusion matrices._

- 23475A0513 — **A.Deepthi Priya** ( [@deepthipriya](www.linkedin.com/in/deepthipriya-andraju-3aaa7a385) )
_Work Done: Performed performance evaluation using Accuracy, Precision, Recall, F1-score, ROC analysis, and comparative study with existing models._

---

## 📌 Abstract
This project presents an adaptive Intrusion Detection System (IDS) that integrates advanced preprocessing techniques with hybrid deep learning models to improve cyberattack detection. The CICIDS2017 dataset is preprocessed using data cleaning, Min-Max normalization, SMOTEENN for class balancing, and Boruta feature selection for dimensionality reduction.

Four deep learning models—Autoencoder, GRU, AlexNet, and MiniVGGNet—are implemented and evaluated. The Autoencoder achieved the highest performance with 99.67% accuracy, demonstrating the effectiveness of hybrid feature selection and deep learning integration for intrusion detection.

---

## 📄 Paper Reference (Inspiration)
👉  Detecting Unbalanced Network Traffic Intrusion  With Deep Learning - S.Pavithra and K.Venkata vikas https://ieeexplore.ieee.org/document/10456379.

---

## 🚀Our Improvement Over Existing Paper
❌ Replaced traditional signature-based IDS with deep learning-based detection.

⚖️ Solved class imbalance using SMOTEENN instead of DSSTE.

🎯 Applied Boruta feature selection to remove redundant and irrelevant features.

🧠 Integrated both unsupervised (Autoencoder) and supervised (GRU, CNNs) models.

🔄 Improved zero-day attack detection using Autoencoder reconstruction loss.

📈 Achieved higher accuracy compared to traditional ML models like XGBoost and LSTM.

---

## 🧩 About the Project
🔍 What the Project Does

Detects malicious network traffic

Classifies attacks into multiple categories

Identifies zero-day attacks using anomaly detection

💡 Why It Is Useful

Protects networks from modern cyber threats

Handles class imbalance effectively

Reduces false positives

Suitable for real-time intrusion detection systems

🔁 Workflow

Network Traffic Dataset→ Data Cleaning → Normalization → SMOTEENN → Boruta → Deep Learning Models → Attack Classification Output

---

## 📊 Dataset Used

👉 CICIDS2017 Dataset
https://www.unb.ca/cic/datasets/ids-2017.html

🗂 Dataset Details

Developed by Canadian Institute for Cybersecurity

Contains realistic network traffic data

Includes:

DoS & DDoS attacks

Brute-force attacks

Botnet activity

Web attacks (XSS, SQL Injection)

Port scanning

Infiltration

Over 80 extracted network flow features

Highly imbalanced dataset (handled using SMOTEENN)

---

## 🧰Dependencies Used

🐍 Python 3.10

🔥 TensorFlow 2.12

🧠 Keras

📊 Scikit-learn

📈 Pandas

🔢 NumPy

📉 Matplotlib

⚖️ imbalanced-learn (SMOTEENN)

🌲 BorutaPy

---

## 🔍 EDA & Preprocessing

Merged multiple CSV files into a unified dataset

Removed unnecessary features (Flow ID, Timestamp)

Handled missing and invalid values

Applied Min-Max normalization

Encoded categorical labels

Applied SMOTEENN to balance class distribution

Applied Boruta to select important features

---

## 🧠Model Training Info

Models Implemented:

1️⃣ Autoencoder

Used for anomaly detection

Learns normal traffic pattern

Detects attacks via reconstruction error

2️⃣ GRU (Gated Recurrent Unit)

Captures temporal patterns in network traffic

Effective for time-dependent attacks

3️⃣ AlexNet

CNN-based model for spatial feature extraction

High classification capability

4️⃣ MiniVGGNet

Lightweight CNN

Efficient and suitable for real-time systems

Training Environment

Google Colab

GPU: Tesla T4 (12GB)

RAM: 12GB

OS: Linux

---

## 🧪Model Testing / Evaluation

## 📏 Metrics Used:

Accuracy

Precision

Recall

F1-score

Confusion Matrix

## 🆚 Compared With:

XGBoost

LSTM

Bidirectional LSTM

---

## 🏆 Results
| Model                      | Accuracy   | F1 Score |
| -------------------------- | ---------- | -------- |
| XGBoost                    | 93.95%     | 0.94     |
| LSTM                       | 96.74%     | 0.97     |
| AlexNet                    | 98.22%     | 0.98     |
| MiniVGGNet                 | 99.32%     | 0.98     |
| GRU (Proposed)             | 98.67%     | 0.98     |
| **Autoencoder (Proposed)** | **99.67%** | **0.98** |

✅ Best Model:

Autoencoder achieved highest accuracy: 99.67%

---

## Limitations & Future Work

## Limitations

Requires high computational resources

Performance depends on dataset quality

Not yet optimized for edge/IoT devices

## Future Enhancements

Integrate attention mechanisms

Real-time streaming intrusion detection

Edge/IoT deployment

Online learning capability

Lightweight deployment version

---

## 🌍 Deployment Info
Implemented using Python backend

Can be deployed using:

Flask

FastAPI

Suitable for:

Enterprise network monitoring

Cloud-based intrusion detection

Cybersecurity research platforms

---
## 👨‍💻 Developed By

**Durga Bhavani Tumma**  
Project Lead & Developer  
https://www.linkedin.com/in/durgabhavani-tumma-14b29028b/
