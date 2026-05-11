# Data Science Knowledge Base for AI Chatbot

## Introduction to Data Science

### What is Data Science?
Data Science is the field of extracting useful insights, patterns, and knowledge from data using:
- Mathematics
- Statistics
- Programming
- Machine Learning
- Data Visualization

### Main Goals of Data Science
1. Analyze data
2. Predict future outcomes
3. Find hidden patterns
4. Automate decision-making
5. Build intelligent systems

### Data Science Workflow
1. Collect Data
2. Clean Data
3. Explore Data
4. Train Model
5. Evaluate Model
6. Deploy Model

---

# Python Basics for Data Science

## Variables
Variables store values.

Example:
```python
name = "JD"
age = 21
```

## Data Types
- Integer
- Float
- String
- Boolean
- List
- Tuple
- Dictionary
- Set

## Lists
Lists store multiple items.

```python
numbers = [1,2,3,4]
```

## Dictionaries
```python
student = {
    "name": "Akash",
    "age": 21
}
```

## Functions
Functions reduce repeated code.

```python
def add(a,b):
    return a+b
```

## Loops
### For Loop
```python
for i in range(5):
    print(i)
```

### While Loop
```python
count = 0
while count < 5:
    count += 1
```

---

# Linear Algebra

## Scalars
Single number.
Example:
```python
5
```

## Vectors
Collection of numbers.

Example:
```python
[1,2,3]
```

## Matrices
2D collection of numbers.

Example:
```python
[[1,2],[3,4]]
```

## Vector Addition
Add corresponding elements.

Example:
```python
[1,2] + [3,4] = [4,6]
```

## Dot Product
Measures similarity.

Formula:
genui{"math_block_widget_always_prefetch_v2":{"content":"a \cdot b = a_1b_1 + a_2b_2 + ... + a_nb_n"}}

## Matrix Multiplication
Used heavily in machine learning and neural networks.

---

# Statistics

## Mean
Average value.

Formula:
genui{"math_block_widget_always_prefetch_v2":{"content":"\mu = \frac{\sum x}{n}"}}

## Median
Middle value after sorting.

## Mode
Most repeated value.

## Range
Difference between maximum and minimum.

Formula:
```text
Range = Max - Min
```

## Variance
Measures spread of data.

## Standard Deviation
Square root of variance.

Formula:
genui{"math_block_widget_always_prefetch_v2":{"content":"\sigma = \sqrt{\frac{\sum (x-\mu)^2}{N}}"}}

## Probability
Likelihood of an event.

Formula:
```text
P(E) = Favorable Outcomes / Total Outcomes
```

---

# Data Visualization

## Why Visualization?
Visualization helps understand patterns quickly.

## Libraries
- Matplotlib
- Seaborn
- Plotly

## Types of Graphs

### Line Chart
Shows trends over time.

### Bar Chart
Compares categories.

### Histogram
Shows frequency distribution.

### Pie Chart
Shows proportions.

### Scatter Plot
Shows relationship between variables.

---

# NumPy

## What is NumPy?
NumPy is a fast numerical computing library.

## Creating Arrays
```python
import numpy as np

arr = np.array([1,2,3])
```

## Array Operations
```python
arr + 5
arr * 2
```

## Array Shape
```python
arr.shape
```

## Reshape Arrays
```python
arr.reshape(2,2)
```

---

# Pandas

## What is Pandas?
Pandas is used for data analysis and manipulation.

## DataFrame
Table-like structure.

```python
import pandas as pd
```

## Read CSV
```python
df = pd.read_csv("data.csv")
```

## Head Function
```python
df.head()
```

## Describe Function
```python
df.describe()
```

## Missing Values
```python
df.isnull().sum()
```

---

# Data Cleaning

## Remove Missing Values
```python
df.dropna()
```

## Fill Missing Values
```python
df.fillna(0)
```

## Remove Duplicates
```python
df.drop_duplicates()
```

## Convert Data Types
```python
df.astype(int)
```

---

# Machine Learning Basics

## What is Machine Learning?
Machine learning allows systems to learn patterns from data.

## Types of Machine Learning
1. Supervised Learning
2. Unsupervised Learning
3. Reinforcement Learning

---

# Supervised Learning

## Linear Regression
Predicts continuous values.

Formula:
genui{"math_block_widget_always_prefetch_v2":{"content":"y = mx + b"}}

### Example Use Cases
- House price prediction
- Salary prediction

## Logistic Regression
Used for classification.

Example:
- Spam detection
- Disease prediction

## Decision Trees
Tree-based model.

## Random Forest
Multiple decision trees combined.

---

# Unsupervised Learning

## Clustering
Groups similar data.

## K-Means Clustering
Popular clustering algorithm.

### Steps
1. Choose K
2. Assign clusters
3. Update centroids
4. Repeat

## Dimensionality Reduction
Reduce features while preserving information.

---

# Neural Networks

## What is a Neural Network?
Model inspired by the human brain.

## Components
- Input Layer
- Hidden Layer
- Output Layer

## Activation Functions
- ReLU
- Sigmoid
- Softmax

## Deep Learning
Deep neural networks with many layers.

---

# Natural Language Processing

## What is NLP?
Allows computers to understand human language.

## Applications
- Chatbots
- Translation
- Sentiment analysis
- Voice assistants

## Text Preprocessing
1. Tokenization
2. Stopword Removal
3. Stemming
4. Lemmatization

---

# AI Chatbot Concepts

## Rule-Based Chatbot
Uses fixed responses.

## AI Chatbot
Uses machine learning and NLP.

## Components of AI Chatbot
1. Frontend
2. Backend
3. AI Model
4. Database
5. APIs

## Chatbot Workflow
User Input → Backend → AI Model → Response

---

# APIs

## What is an API?
Allows applications to communicate.

## REST API
Uses HTTP methods.

Methods:
- GET
- POST
- PUT
- DELETE

---

# FastAPI

## What is FastAPI?
Python framework for APIs.

## Basic Example
```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message":"Hello"}
```

---

# Databases

## SQL Databases
- MySQL
- PostgreSQL

## NoSQL Databases
- MongoDB

## Why Databases?
Store:
- User data
- Chat history
- AI memory

---

# Model Evaluation

## Accuracy
Measures correct predictions.

Formula:
```text
Accuracy = Correct Predictions / Total Predictions
```

## Precision
Important when false positives matter.

## Recall
Important when false negatives matter.

## F1 Score
Balance between precision and recall.

---

# Deployment

## Frontend Deployment
- Vercel
- Netlify

## Backend Deployment
- Render
- Railway

## Cloud Platforms
- AWS
- Azure
- Google Cloud

---

# AI Agent Concepts

## What is an AI Agent?
An AI system capable of performing tasks automatically.

## Examples
- Auto email sender
- Voice assistant
- Smart scheduling bot

## Multi-Agent Systems
Multiple AI agents working together.

---

# Data Science Interview Topics

## Frequently Asked Topics
- Python
- Pandas
- NumPy
- Statistics
- Machine Learning
- SQL
- APIs
- Data Cleaning
- Visualization

---

# Recommended Learning Path

## Phase 1
- Python Basics
- Data Structures
- Functions
- OOP

## Phase 2
- NumPy
- Pandas
- Visualization

## Phase 3
- Statistics
- Linear Algebra

## Phase 4
- Machine Learning

## Phase 5
- Deep Learning
- NLP
- Chatbots

---

# How to Use This for Your Chatbot

## Idea
Convert these notes into:
- Text files
- JSON files
- Embeddings
- Vector database

Then your chatbot can answer:
- What is variance?
- Explain Pandas.
- Difference between AI and ML.
- What is clustering?

---

# Future Improvements

## Add RAG
Retrieval-Augmented Generation improves chatbot answers.

## Add Vector Database
- ChromaDB
- Pinecone

## Add Memory
Store previous conversations.

## Add Voice Assistant
Speech-to-text and text-to-speech.

---

# Final Advice

Learn by:
1. Reading
2. Coding
3. Building projects
4. Practicing daily

Projects are the fastest way to improve in data science and AI engineering.

