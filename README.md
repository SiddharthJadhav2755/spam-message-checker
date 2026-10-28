# 🛡️ Spam Message Checker (Streamlit)

A beginner-friendly web application developed in Python and Streamlit that analyzes text messages, SMS snippets, and emails to determine whether they are **Likely Spam** or **Likely Not Spam**.

This project demonstrates core cloud computing concepts, rapid Python web application development, version control with Git and GitHub, and cloud deployment using Streamlit Community Cloud (Platform as a Service).

---

## 📋 Features

- **Interactive Web Interface:** Clean, responsive UI with multiline input, real-time results, and instant sample message loaders.
- **Heuristic Spam Engine:** Rule-based detection checking for:
  - Lottery, prize, and reward claims (`winner`, `claim prize`, `jackpot`).
  - Financial bait and get-rich schemes (`free money`, `instant cash`, `earn $`).
  - High-pressure urgency phrases (`limited offer`, `urgent:`, `act now`).
  - Credential and identity phishing (`otp`, `password`, `bank account`, `cvv`).
  - Suspicious URLs and link structures (`http://`, `bit.ly`, `tinyurl`).
  - Formatting anomalies (excessive exclamation marks, currency symbols, and ALL CAPS).
- **Clear Visual Distinction:** Instant color-coded badges (`st.error` for Likely Spam, `st.success` for Likely Not Spam) with detailed breakdown of detected red flags.
- **Input Validation & Reset:** Warns users on empty input submissions and includes a one-click input clearing mechanism.
- **Lightweight & Free:** Built purely on Streamlit and Python standard libraries—no external APIs, complex ML models, or paid services required.

---

## 📁 Project Structure

```text
spam-message-checker/
├── app.py              # Complete Streamlit web application & spam engine
├── requirements.txt    # Project dependencies (Streamlit)
├── README.md           # Project documentation and deployment guide
└── .gitignore          # Git exclusion rules for virtualenvs and cache
```

---

## 🚀 Local Development Setup (Windows PowerShell)

Follow these step-by-step instructions to run the application on your local Windows machine:

### 1. Open Terminal and Navigate to Project
```powershell
cd path\to\spam-message-checker
```

### 2. Create a Virtual Environment
```powershell
python -m venv venv
```

### 3. Activate the Virtual Environment
```powershell
.\venv\Scripts\Activate.ps1
```
> *Note:* If PowerShell reports an execution policy error, run `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process` in your current PowerShell session.

### 4. Install Required Dependencies
```powershell
pip install -r requirements.txt
```

### 5. Run the Streamlit Application
```powershell
streamlit run app.py
```

### 6. Access the Application
Open your browser and navigate to:
```text
http://localhost:8501
```

---

## 🐙 GitHub Integration

To publish the project to GitHub for version control and cloud deployment:

### 1. Create a New Repository on GitHub
1. Log in to [GitHub](https://github.com).
2. Click **New** (or "+" in the top-right corner).
3. Name the repository: `spam-message-checker`.
4. Set the repository visibility to **Public**.
5. Leave "Add a README file" unchecked (since we already have one).
6. Click **Create repository**.

### 2. Initialize and Push Local Repository
Run the following commands inside the `spam-message-checker` directory:

```powershell
# Initialize git repository
git init

# Add all files to staging
git add .

# Create initial commit
git commit -m "Initial commit: Streamlit Spam Message Checker"

# Rename default branch to main
git branch -M main

# Link local repository to your remote GitHub repository
# Replace <YOUR-GITHUB-USERNAME> with your actual GitHub username
git remote add origin https://github.com/<YOUR-GITHUB-USERNAME>/spam-message-checker.git

# Push to GitHub
git push -u origin main
```

---

## ☁️ Streamlit Community Cloud Deployment

Streamlit Community Cloud is a Platform as a Service (PaaS) that runs, manages, and scales Streamlit applications directly from GitHub.

### Deployment Steps:
1. Navigate to [Streamlit Community Cloud](https://share.streamlit.io/) and sign in with your GitHub account.
2. Click **Create app** (or **New app**).
3. Under **Repository**, select your repository: `<YOUR-GITHUB-USERNAME>/spam-message-checker`.
4. Under **Branch**, select `main`.
5. Under **Main file path**, enter `app.py`.
6. Click **Deploy!**.
7. Streamlit Cloud will allocate resources, install dependencies from `requirements.txt`, and deploy the application.
8. Once built, copy your live public URL (e.g., `https://<your-app-name>.streamlit.app`).

### Continuous Deployment (CD):
Any future commits pushed to the `main` branch on GitHub will automatically trigger an incremental redeploy on Streamlit Community Cloud.

---

## ☁️ Cloud Computing Concepts: IaaS vs PaaS vs SaaS

- **IaaS (Infrastructure as a Service):** Provides virtual machines, storage, and networking while users manage the operating system and applications.
- **PaaS (Platform as a Service):** Provides a managed environment for developing and deploying applications without managing the underlying servers.
- **SaaS (Software as a Service):** Provides ready-to-use software over the internet without requiring users to manage the application infrastructure.

**Why Streamlit Community Cloud is PaaS:** Developers supply only application code and configuration via GitHub, while the platform automatically provisions computing instances, manages containers, handles networking, provisions SSL certificates, and handles application lifecycles.

---

## 📊 Free-Tier Cloud Providers Comparison

| Cloud Provider | Free Services or Offer | Important Limitations |
| :--- | :--- | :--- |
| **Amazon Web Services (AWS)** | 750 hours/month of `t2.micro`/`t3.micro` EC2 instances (12 months free); 1M free requests/month for AWS Lambda (Always Free); 5 GB standard S3 storage (12 months free). | 12-month expiration for EC2 and S3 introductory allowances; exceeding bandwidth, storage limits, or selecting non-eligible instance families incurs automated billing. |
| **Microsoft Azure** | 750 hours/month of `B1s` Linux and Windows VMs (12 months free); 1M free executions/month for Azure Functions (Always Free); 5 GB LRS Blob Storage (12 months free); $200 initial credit (30 days). | $200 promotional credit expires in 30 days; 12-month free services expire after first year; bandwidth beyond 15 GB/month is billable. |
| **Google Cloud Platform (GCP)** | 1 non-preemptible `e2-micro` VM instance per month (Always Free in eligible US regions); 2M Cloud Run requests/month (Always Free); 5 GB standard Cloud Storage (Always Free); $300 credit (90 days). | Always Free VM is restricted to specific US zones (`us-central1`, `us-west1`, `us-east1`); egress bandwidth over 1 GB/month to non-China/Australia targets is billable; $300 credit valid for 90 days only. |

---

## ⚠️ Educational Disclaimer

This project is built strictly for educational purposes, coursework demonstration, and foundational cloud computing study. It uses rule-based heuristic pattern matching and is not intended to replace machine-learning-driven enterprise email security or carrier-grade SMS spam gateways.

