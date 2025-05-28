# AI-Powered Early Detection System for Neurodegenerative Disorders

## Overview
This project aims to build an AI-powered early detection system for cognitive decline in elderly individuals. The goal is to integrate automated cognitive assessments with medical report analysis to enable early diagnosis and support better clinical decision-making. A gamified Android app will make assessments accessible, intuitive, and scalable for real-world use.

---

## Research Question
**How can machine learning techniques be applied to enhance the early detection and management of neurodegenerative diseases associated with cognitive decline in elderly populations by integrating cognitive assessments and medical report analysis?**

---

## Data Sources
- **MMSE & SMMSE**: Standardized 30-question cognitive assessments. ([MMSE](https://cgatoolkit.ca/Uploads/ContentDocuments/MMSE.pdf))
- **Clock Drawing Test (CDT)**: Assesses executive and visuospatial skills. ([Dataset](https://arxiv.org/abs/1606.07163))
- **Rey Auditory Verbal Learning Test (RAVLT)**: Evaluates verbal memory. ([Dataset](https://repository.niddk.nih.gov/media/studies/look-ahead/Forms/Look_AHEAD_Cognitive_Function/CF1_Rey%20Auditory%20Verbal%20Learning%20Test%20(AVLT).pdf))
- **Geriatric Depression Scale (GDS-15/30)**: Detects depression among the elderly. ([GDS](https://hign.org/sites/default/files/2020-06/Try_This_General_Assessment_2.pdf))
- **Neuropsychiatric Inventory (NPI)**: Measures neurobehavioral symptoms in dementia. ([NPI](https://www.dementiaresearch.org.au/wp-content/uploads/2016/01/NPI.pdf))
- **Lumosity Cognitive Task Data**: Game-based assessments for memory, attention, and problem-solving. ([Lumosity Research Tools](https://www.lumosity.com/hcp/research/tools))

---

## Android App for Gamified Cognitive Testing
- Gamified interfaces for MMSE, CDT, RAVLT, GDS, NPI, and more
- Tasks include:
  - Clock drawing (touch/stylus)
  - Trail-making puzzles
  - Word recall games
  - Category naming with timers
- Data captured:
  - Time to complete, number of errors, accuracy
  - Stroke patterns, hesitation points, response times
  - Engagement metrics (retries, consistency)
- Features:
  - Large buttons, voice prompts, animated feedback
  - Logs interactions for behavioral analysis

---

## Data Collection & Processing
- Combine test scores, clinical metadata, and behavioral metrics
- Parse medical records using NLP
- Normalize test scores and impute missing data using KNN/MICE
- Unified feature set for model input

---

## Data Analysis
- Descriptive statistics (mean, SD, skewness)
- Correlation analysis (Pearson, Spearman)
- Logistic & Linear Regression for risk prediction
- Group comparison (t-tests, ANOVA)
- Feature selection via RFE, SHAP
- Longitudinal trend analysis for repeated assessments

---

## AI Model Development
- Multimodal ML pipeline integrating:
  - Structured cognitive scores
  - Behavioral app interaction data
  - Unstructured clinical text
- ML models: Random Forest, XGBoost, SVM (for baseline)
- Deep models: CNN (clock images), LSTM (sequential test data)
- LLM integration:
  - Fine-tune MedLLaMA2 for symptom summarization, entity extraction
  - Retrieval-Augmented Generation (RAG) using FAISS for contextual enhancement
- Ensemble methods at feature and decision levels

---

## Evaluation Metrics
- **Classification**: Accuracy, Precision, Recall, F1-score, AUC-ROC
- **Regression**: MSE, MAE, R²
- **Interpretability**: SHAP plots, RAG content quality analysis

---

## Visualization & Reporting
- Time-series plots for trend analysis
- Heatmaps for correlation studies
- SHAP-based variable importance
- Interactive dashboards for clinicians and caregivers
- Personalized cognitive wellness reports

---

## Expected Outcomes
- A user-friendly Android app for elderly cognitive self-assessment
- An integrated AI system for early, multimodal detection
- Enhanced prediction accuracy via clinical + behavioral + cognitive data fusion
- Contributions to scalable and accessible elder care in Canadian healthcare

---

## References
- Alzheimer Society of Canada: https://alzheimer.ca/en/about-dementia/what-dementia/dementia-numbers-canada
- CGA Toolkit Plus (MMSE): https://cgatoolkit.ca/Uploads/ContentDocuments/MMSE.pdf
- GDS: https://hign.org/sites/default/files/2020-06/Try_This_General_Assessment_2.pdf
- RAVLT: https://repository.niddk.nih.gov/media/studies/look-ahead/Forms/Look_AHEAD_Cognitive_Function/CF1_Rey%20Auditory%20Verbal%20Learning%20Test%20(AVLT).pdf
- NPI: https://www.dementiaresearch.org.au/wp-content/uploads/2016/01/NPI.pdf
- Lumosity: https://www.lumosity.com/hcp/research/tools
