## **Use 'Code' view on Github for a better visualization**



# ML_Project - Credit Score Classification (ES)

My primer trabajo personal de Machine Learning. 04/2024

Descripción del proyecto:

Mediante la información financiera de una persona, un banco es capaz de realizar un credit scoring y de esa manera clasificar a sus clientes con diferentes puntuajes para determinar si son aptos para un préstamo o no.  
- **El problema está en que actualmente este proceso está siendo realizando a través de métodos manuales en el que se destinan muchos recursos.**  
- **El objetivo es el de automatizar este proceso para aumentar la eficiencia y reducir los costes de la entidad bancaria.**    
- **Para abordar el problema de negocio, se llevará a cabo un estudio y procesado de los datos para posteriomente aplicar una serie de modelos supervisados multiclase para finalmente seleccionar aquel que obtenga mejor rendimiento.**

Directorio:

mi_proyecto_ml/
│
├── data/                      # Carpeta para los conjuntos de datos
│   ├── clean_data.csv         # Datos ya procesados y limpios para ser utilizados directamente en los modelos
│   ├── test.csv               # Datos separados para probar los modelos y evaluar su rendimiento --> sin variable 'y' por lo que no se pueden obtener las métricas al usarlos
│   ├── train.csv              # Conjunto de datos original sin procesar para entrenar los modelos 
│   ├── X_train_sample.csv     # Muestra del conjunto de entrenamiento de las variables independientes
│   └── y_train_sample.csv     # Muestra del conjunto de entrenamiento de la variable dependiente (Credit Score)
│
├── models/                    # Modelos entrenados (**se incluirán más*)
│   └── random_forest_v5.joblib   # Modelo de Random Forest seleccionado como el favorito (*por el momento*)
│
├── notebooks/                 # Jupyter Notebooks
│   ├── credit_score_classification.ipynb   # Notebook principal de clasificación de credit score --> todo el proceso de principio a fin y totalmente funcional (*versión limpia*)
│   ├── ml_project_guide.ipynb              # Guía del proyecto de ML 
│   └── model_testing.ipynb                # Notebook para probar y comparar diferentes modelos
|
| ppt/
|    └── ML_Credit_Scoring_ppt.pptx          # Presentación resumen del proyecto
│
└── scripts/                   # Scripts de Python
    └── utilities.py          # Funciones utilizadas a través del proyecto 

README.md                     # Documento que explica el proyecto y la estrctura del directorio


--> **IMPORTANTE** random_forest_v5.joblib, tiene un tamaño muy grande por lo que está en formato ZIP ya que Github no deja subirlo con más de 100 MB


-----------------------------------------------------------------

# ML Project - Credit Score Classification (EN)

My first personal Machine Learning project. 04/2024

Project Description:

Through a person's financial information, a bank is capable of performing credit scoring and thus classifying its clients with different scores to determine whether they are eligible for a loan or not.

- **The problem is that currently this process is being done manually, utilizing many resources.**
- **The goal is to automate this process to increase efficiency and reduce costs for the banking entity.**
- **To address the business problem, a study and processing of the data will be carried out, followed by the application of a series of supervised multi-class models to ultimately select the one that achieves the best performance.**


Directory:

my_ml_project/
│
├── data/                       # Folder for data sets
│   ├── clean_data.csv          # Data processed and clean, ready to be used directly in models
│   ├── test.csv                # Data separated for testing models and assessing their performance —> without 'y' variable so metrics cannot be obtained when using them
│   ├── train.csv               # Original data set, unprocessed for training models
│   ├── X_train_sample.csv      # Sample of the training set of independent variables
│   └── y_train_sample.csv      # Sample of the training set of the dependent variable (Credit Score)
│
├── models/                     # Trained models (more will be included)
│   └── random_forest_v5.joblib # Random Forest model chosen as the current favorite (for the moment)
│
├── notebooks/                  # Jupyter Notebooks
│   ├── credit_score_classification.ipynb # Main notebook of credit score classification —> the whole process from start to end and fully functional (clean version)
│   ├── ml_project_guide.ipynb           # Guide for the ML project
│   └── model_testing.ipynb              # Notebook for testing and comparing different models
|
|
|ppt/
|        └── ML_Credit_Scoring_ppt.pptx # Project overview presentation
│
└── scripts/                    # Python scripts
    └── utilities.py           # Utility functions used throughout the project for specific or repetitive tasks

README.md                      # Document that explains the project, how to run it, its basic structure and other important details
