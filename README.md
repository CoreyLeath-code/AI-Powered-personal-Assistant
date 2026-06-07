[![Actions Status](https://img.shields.io/badge/GitHub%20Actions-View-blue?logo=github)](https://github.com/Trojan3877/AI-Powered-personal-Assistant/actions) [![Release](https://img.shields.io/github/v/release/Trojan3877/AI-Powered-personal-Assistant?include_prereleases)](https://github.com/Trojan3877/AI-Powered-personal-Assistant/releases) [![License](https://img.shields.io/github/license/Trojan3877/AI-Powered-personal-Assistant)](https://github.com/Trojan3877/AI-Powered-personal-Assistant/blob/main/LICENSE)

# 🤖 AI-Powered Personal Assistant

A modular, cloud-native AI Assistant powered by OpenAI, Snowflake, and a DevOps-first architecture. This project enables intelligent scheduling, semantic Q&A, and flexible deployment using Docker, [...]

---

## 📌 Badges
![Capstone Project](https://img.shields.io/badge/Capstone-Project-blueviolet?style=for-the-badge&logo=github)

![Status](https://img.shields.io/badge/status-active-brightgreen)
![License](https://img.shields.io/github/license/Trojan3877/AI-Powered-personal-Assistant)
![Build](https://img.shields.io/badge/build-passing-success)
![CI/CD](https://img.shields.io/badge/CI--CD-GitHub%20Actions-blue)
![OpenAI](https://img.shields.io/badge/ML%20Algo-GPT--3.5%20Turbo-blue)
![Kubernetes](https://img.shields.io/badge/Kubernetes-ready-blue)
![Snowflake](https://img.shields.io/badge/Snowflake-supported-lightblue)
🔄 [Download Superset Dashboard Config](dashboards/superset_ai_performance.json)

---

## 📘 Extended Description

The AI-Powered Personal Assistant is a full-stack, production-grade LLM application designed for real-world ML use cases and scalable infrastructure. It performs natural language scheduling, OpenA[...]

## 📊 Performance Metrics

| Query                                 | Assistant Response                                     | Latency |
|--------------------------------------|--------------------------------------------------------|---------|
| What is the capital of France?       | The capital of France is Paris.                        | 1.85s   |
| Explain Terraform in simple terms.   | Terraform lets you define and provision infra as code. | 2.14s   |
| Who is the CEO of OpenAI?            | As of 2025, the CEO of OpenAI is Sam Altman.           | 1.72s   |

### 📈 Summary Stats

- ✅ **Accuracy**: 3/3 correct responses (100%)
- ⚡ **Average Latency**: **1.90 seconds**


## 📂 Project Structure

├── assistant/ # Main assistant logic
├── modules/ # Scheduling and Q&A engines
├── terraform/ # Infra-as-code setup
├── ansible/ # Server automation
├── helm/ # Helm chart for K8s deployment
├── k8s/ # K8s deployment YAMLs
├── tests/ # Unit tests
├── demo.py # CLI E2E assistant interaction
├── Dockerfile
├── docker-compose.yaml
├── Makefile
├── .env.example
---

## 🛠️ Technologies Used

| Tool           | Purpose                                   |
|----------------|-------------------------------------------|
| Python         | Backend logic & NLP processing            |
| OpenAI         | GPT-3.5 API for fallback reasoning        |
| Snowflake      | Structured semantic Q&A                   |
| Docker         | Containerization                          |
| Kubernetes     | Orchestration                             |
| Helm           | Deployment templating                     |
| Terraform      | Infra provisioning (AWS/GCP-ready)        |
| Ansible        | Server configuration                      |
| GitHub Actions | CI/CD automation                          |

---

## 🚀 Deployment

```bash
# Local Dev
make install
make run

# Docker
make docker-build
make docker-run

# Kubernetes
kubectl apply -f k8s/deployment.yaml

# Terraform
cd terraform && terraform init && terraform apply
```
